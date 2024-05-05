from collections import OrderedDict

from PySide6 import QtWidgets as qtw
from PySide6.QtWidgets import QLineEdit, QCheckBox

from values_window.ui.values_window_ui import Ui_valores_window


class ValuesWindow(qtw.QDialog, Ui_valores_window):

    def __init__(self, config_manager):
        # fmt: off
        super().__init__()
        self.setupUi(self)
        self.config_manager = config_manager
        self.config_name = "VALUES"

        self.pb_add_region.clicked.connect(self.add_region)
        self.pb_remove_region.clicked.connect(self.remove_region)
        self.pb_add_volume.clicked.connect(self.add_volume)
        self.pb_remove_volume.clicked.connect(self.remove_volume)

        self.lw_variables.currentRowChanged.connect(self.load_region_config)
        self.lw_regions.currentRowChanged.connect(self.load_volume_config)
        self.lw_volumes.currentRowChanged.connect(self.load_current_config)

        self.variable_widgets = ["le_general_value", "le_k", "chb_local_value"]
        self.region_widgets = ["chb_fixed_value", "chb_linear_source", "le_local_value", "le_local_k"]
        self.volume_widgets = ["le_x_start", "le_x_lon", "le_y_start", "le_y_lon", "le_z_start", "le_z_lon"]
        self.widgets = self.variable_widgets + self.region_widgets + self.volume_widgets

        self.config_manager.connect_config(self)
        self.chb_local_value.stateChanged.connect(self.load_current_config)
        self.load_current_config()
        # fmt: on

    def get_configured_widgets(self, variable, region, volume):
        """"""
        # Esta función busca en la configuración y recoge todos los widgets configurados
        if variable:
            config = self.config_manager.config_structure[self.config_name][variable.text()]
            configured_widgets = set()
            configured_widgets.update(k for k, v in config.items() if not isinstance(v, OrderedDict))
            if region:
                region_config = config[region.text()]
                configured_widgets.update(k for k, v in region_config.items() if not isinstance(v, OrderedDict))
                if volume:
                    volume_config = region_config[volume.text()]
                    configured_widgets.update(k for k, v in volume_config.items())
            return configured_widgets
        return []

    def load_current_config(self):
        """"""
        variable = self.lw_variables.currentItem()
        region = self.lw_regions.currentItem()
        volume = self.lw_volumes.currentItem()
        configured_widgets = self.get_configured_widgets(variable, region, volume)
        not_configured_widgets = [widget for widget in self.widgets if widget not in configured_widgets]
        self.toggle_widget_list(not_configured_widgets, False)
        # Seleccionada una variable
        if variable is not None:
            config = self.config_manager.config_structure[self.config_name][variable.text()]
            self.toggle_widget_list(self.variable_widgets, True)
            self.config_manager.load_config(self, config)
            self.chb_local_value.setEnabled(True)
            if config.get("chb_local_value") == 2:
                self.lw_regions.setEnabled(True)
                self.pb_add_region.setEnabled(True)
                self.pb_remove_region.setEnabled(True)
                # Seleccionada una region
                if region is not None:
                    self.toggle_widget_list(self.region_widgets, True)
                    self.config_manager.load_config(self, config[region.text()])
                    self.lw_volumes.setEnabled(True)
                    self.pb_add_volume.setEnabled(True)
                    self.pb_remove_volume.setEnabled(True)
                    # Seleccionado un volumen
                    if volume is not None:
                        self.toggle_widget_list(self.volume_widgets, True)
                        self.config_manager.load_config(self, config[region.text()][volume.text()])
                    else:
                        self.toggle_widget_list(self.volume_widgets, False)
                else:
                    self.toggle_widget_list(self.region_widgets + self.volume_widgets, False)
                    self.lw_volumes.setEnabled(False)
            else:
                self.lw_regions.setEnabled(False)
                self.pb_add_region.setEnabled(False)
                self.pb_remove_region.setEnabled(False)
                self.lw_volumes.setEnabled(False)
                self.pb_add_volume.setEnabled(False)
                self.pb_remove_volume.setEnabled(False)
        else:
            self.lw_regions.setEnabled(False)
            self.pb_add_region.setEnabled(False)
            self.pb_remove_region.setEnabled(False)
            self.lw_volumes.setEnabled(False)
            self.pb_add_volume.setEnabled(False)
            self.pb_remove_volume.setEnabled(False)
            self.chb_local_value.setEnabled(False)

    def load_region_config(self):
        variable = self.lw_variables.currentItem()
        # self.print_ordereddict(self.config_manager.config_structure, show_markers=True)
        if variable is not None:
            self.lw_regions.clear()
            config = self.config_manager.config_structure[self.config_name][variable.text()]
            for key, value in config.items():
                if isinstance(value, OrderedDict):
                    self.lw_regions.addItem(key)
            self.load_current_config()

    def load_volume_config(self):
        variable = self.lw_variables.currentItem()
        region = self.lw_regions.currentItem()
        # self.print_ordereddict(self.config_manager.config_structure, show_markers=True)
        if region is not None:
            self.lw_volumes.clear()
            config = self.config_manager.config_structure[self.config_name][variable.text()][region.text()]
            for key, value in config.items():
                if isinstance(value, OrderedDict):
                    self.lw_volumes.addItem(key)
            self.load_current_config()

    def toggle_widget_list(self, widgets, toggle):
        """"""
        for widget_name in widgets:
            try:
                widget = getattr(self, widget_name)
                widget.setEnabled(toggle)
                if not toggle and isinstance(widget, QLineEdit):
                    if widget.text():
                        widget.clear()
                elif not toggle and isinstance(widget, QCheckBox):
                    widget.setChecked(toggle)
                else:
                    continue
            except Exception as e:
                print(f"ERROR AL LIMPIAR: {e}")

    def value_changed(self, value):
        """"""
        # fmt: off
        sender = self.sender()
        variable = self.lw_variables.currentItem()
        region = self.lw_regions.currentItem()
        volume = self.lw_volumes.currentItem()
        if value is not None:
            if volume and sender.objectName() in self.volume_widgets:
                if variable.text() not in self.config_manager.config_structure[self.config_name]:
                    self.config_manager.config_structure[self.config_name][variable.text()] = OrderedDict()
                if region.text() not in self.config_manager.config_structure[self.config_name][variable.text()]:
                    self.config_manager.config_structure[self.config_name][variable.text()][region.text()] = OrderedDict()
                if volume.text() not in self.config_manager.config_structure[self.config_name][variable.text()][region.text()]:
                    self.config_manager.config_structure[self.config_name][variable.text()][region.text()][[volume.text()]] = OrderedDict()
                self.config_manager.config_structure[self.config_name][variable.text()][region.text()][volume.text()][sender.objectName()] = value
            elif region and sender.objectName() in self.region_widgets:
                if variable.text() not in self.config_manager.config_structure[self.config_name]:
                    self.config_manager.config_structure[self.config_name][variable.text()] = OrderedDict()
                if region.text() not in self.config_manager.config_structure[self.config_name][variable.text()]:
                    self.config_manager.config_structure[self.config_name][variable.text()][region.text()] = OrderedDict()
                self.config_manager.config_structure[self.config_name][variable.text()][region.text()][sender.objectName()] = value
            elif variable and sender.objectName() in self.variable_widgets:
                if variable.text() not in self.config_manager.config_structure[self.config_name]:
                    self.config_manager.config_structure[self.config_name][variable.text()] = OrderedDict()
                self.config_manager.config_structure[self.config_name][variable.text()][sender.objectName()] = value
            else:
                return None
        else:
            if volume:
                self.config_manager.config_structure[self.config_name][variable.text()][region.text()][volume.text()].pop(sender.objectName(), None)
                # if len(self.config_manager.config_structure[self.config_name][variable.text()][region.text()][volume.text()]) == 0 and volume.text() != "Volumen 1":
                #     self.config_manager.config_structure[self.config_name][variable.text()][region.text()].pop(volume.text(), None)
                    # if len(self.config_manager.config_structure[self.config_name][variable.text()][region.text()]) == 0 and volume.text() != "Region 1":
                    #     self.config_manager.config_structure[self.config_name][variable.text()].pop(region.text(), None)
            elif region:
                self.config_manager.config_structure[self.config_name][variable.text()][region.text()].pop(sender.objectName(), None)
                # if len(self.config_manager.config_structure[self.config_name][variable.text()][region.text()]) == 0 and volume.text() != "Region 1":
                #     self.config_manager.config_structure[self.config_name][variable.text()].pop(region.text(), None)
            elif variable:
                self.config_manager.config_structure[self.config_name][variable.text()].pop(sender.objectName(), None)
            else:
                return None
        # fmt: on

    def add_region(self):
        """"""
        region_number = self.lw_regions.count() + 1
        self.lw_regions.addItem(f"Region {region_number}")
        variable = self.lw_variables.currentItem()
        if variable is not None:
            self.config_manager.config_structure[self.config_name][variable.text()][
                f"Region {region_number}"
            ] = OrderedDict()

    def remove_region(self):
        """"""
        region_count = self.lw_regions.count()
        if region_count > 1:
            self.lw_regions.takeItem(region_count - 1)
            last_region = self.lw_regions.item(region_count - 1)
            variable = self.lw_variables.currentItem()
            if variable is not None:
                self.config_manager.config_structure[self.config_name][variable.text()].pop(last_region.text(), None)

    def add_volume(self):
        """"""
        volume_number = self.lw_volumes.count() + 1
        self.lw_volumes.addItem(f"Volumen {volume_number}")
        variable = self.lw_variables.currentItem()
        region = self.lw_regions.currentItem()
        if variable is not None and region is not None:
            self.config_manager.config_structure[self.config_name][variable.text()][region.text()][
                f"Volumen {volume_number}"
            ] = OrderedDict()

    def remove_volume(self):
        """"""
        volume_count = self.lw_volumes.count()
        if volume_count > 1:
            self.lw_volumes.takeItem(volume_count - 1)
            last_volume = self.lw_regions.item(volume_count - 1)
            variable = self.lw_variables.currentItem()
            region = self.lw_regions.currentItem()
            if variable is not None and region is not None:
                self.config_manager.config_structure[self.config_name][variable.text()][region.text()].pop(
                    last_volume.text(), None
                )

    def print_ordereddict(self, od, indent=0, show_markers=False):
        # Create an indentation space based on the current level
        indent_space = "    " * indent
        if show_markers:
            print(f"{indent_space}INICIO ######################")
        for key, value in od.items():
            if isinstance(value, dict):  # If the value is a dictionary, print the key and then the nested dictionary
                print(f"{indent_space}{key}:")
                self.print_ordereddict(value, indent + 1, show_markers=False)
            else:  # If the value is not a dictionary, print key-value pair
                print(f"{indent_space}{key}: {value}")
        if show_markers:
            print(f"{indent_space}FINAL ######################")
