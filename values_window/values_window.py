from PySide6 import QtWidgets as qtw
from PySide6.QtCore import Qt

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

        self.variable_widgets = [
            "le_general_value", "le_k", "le_kblock", "chb_iborx", "chb_ibory",
            "chb_iborz", "chb_ipun", "chb_local_value", "le_ixyz", "chb_ex_value", "chb_ex_k"
        ]
        self.region_widgets = [
            "le_local_value", "le_local_sc", "le_local_sp", "le_local_k",
        ]
        self.volume_widgets = [
            "le_x_start", "le_x_end", "le_y_start", "le_y_end", "le_z_start", "le_z_end", 
            "chb_exclude_borders", "cb_ex_x_start", "cb_ex_x_end", "cb_ex_y_start", "cb_ex_y_end",
            "cb_ex_z_start", "cb_ex_z_end"]
        self.widgets = self.variable_widgets + self.region_widgets + self.volume_widgets

        self.config_manager.connect_config(self)
        self.chb_local_value.stateChanged.connect(self.load_region_config)
        self.load_variables_list()
        # fmt: on

    def get_configured_widgets(self, variable, region, volume):
        """"""
        # Esta función busca en la configuración y recoge todos los widgets configurados
        if variable:
            config = self.config_manager.values[variable.data(Qt.UserRole)]
            configured_widgets = set()
            configured_widgets.update(key for key, value in config.items() if not isinstance(value, dict))
            if region:
                region_config = config[region.text()]
                configured_widgets.update(key for key, value in region_config.items() if not isinstance(value, dict))
                if volume:
                    volume_config = region_config[volume.text()]
                    configured_widgets.update(key for key in volume_config.keys())
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
            config = self.config_manager.values[variable.data(Qt.UserRole)]
            self.toggle_widget_list(self.variable_widgets, True)
            self.config_manager.load_config(self, config)
            self.chb_local_value.setEnabled(True)
            if config.get("chb_local_value") == 2:
                self.lw_regions.setEnabled(True)
                self.pb_add_region.setEnabled(True)
                self.pb_remove_region.setEnabled(True)
                # Seleccionada una region
                if region is not None:
                    # self.toggle_widget_list(self.region_widgets, True)
                    # self.config_manager.load_config(self, config[region.text()])
                    self.lw_volumes.setEnabled(True)
                    self.pb_add_volume.setEnabled(True)
                    self.pb_remove_volume.setEnabled(True)
                    # Seleccionado un volumen
                    if volume is not None:
                        self.toggle_widget_list(self.region_widgets, True)
                        self.config_manager.load_config(self, config[region.text()])
                        self.toggle_widget_list(self.volume_widgets, True)
                        self.config_manager.load_config(self, config[region.text()][volume.text()])
                        if self.config_manager.is_mesh_info_complete:
                            volume_data = self.initialize_volume_data()
                            # Verificar si alguno de los valores ya está definido
                            keys = ["le_x_start", "le_x_end", "le_y_start", "le_y_end", "le_z_start", "le_z_end"]
                            if not any(key in config[region.text()][volume.text()] for key in keys):
                                self.le_x_start.setText(volume_data["le_x_start"])
                                self.le_x_end.setText(volume_data["le_x_end"])
                                self.le_y_start.setText(volume_data["le_y_start"])
                                self.le_y_end.setText(volume_data["le_y_end"])
                                self.le_z_start.setText(volume_data["le_z_start"])
                                self.le_z_end.setText(volume_data["le_z_end"])
                    else:
                        self.toggle_widget_list(self.volume_widgets, False)
                else:
                    self.toggle_widget_list(self.region_widgets + self.volume_widgets, False)
                    self.lw_volumes.setEnabled(False)
                    self.lw_volumes.clear()
            else:
                self.lw_regions.setEnabled(False)
                self.lw_regions.clear()
                self.pb_add_region.setEnabled(False)
                self.pb_remove_region.setEnabled(False)
                self.lw_volumes.setEnabled(False)
                self.lw_volumes.clear()
                self.pb_add_volume.setEnabled(False)
                self.pb_remove_volume.setEnabled(False)
        else:
            self.lw_regions.setEnabled(False)
            self.lw_regions.clear()
            self.pb_add_region.setEnabled(False)
            self.pb_remove_region.setEnabled(False)
            self.lw_volumes.setEnabled(False)
            self.lw_volumes.clear()
            self.pb_add_volume.setEnabled(False)
            self.pb_remove_volume.setEnabled(False)
            self.chb_local_value.setEnabled(False)

    def load_variables_list(self):
        """Carga y actualiza la lista de variables considerando el orden y permitiendo duplicados."""
        current_items = [
            (self.lw_variables.item(i).text(), self.lw_variables.item(i).data(Qt.UserRole))
            for i in range(self.lw_variables.count())
        ]
        new_items = []
        for key, data in self.config_manager.values.items():
            if "name" in data:
                number = int(key[len("le_var_title") :]) if key.startswith("le_var_title") else float("inf")
                new_items.append((number, data["name"], key))
        new_items.sort()
        if [(name, tech_name) for _, name, tech_name in new_items] != current_items:
            self.lw_variables.clear()
            for _, name, tech_name in new_items:
                item = qtw.QListWidgetItem(name)
                item.setData(Qt.UserRole, tech_name)
                self.lw_variables.addItem(item)
        self.load_current_config()

    def load_region_config(self):
        """Carga la configuración de la región basada en la variable seleccionada."""
        variable = self.lw_variables.currentItem()
        if variable is not None:
            self.lw_regions.clear()
            config = self.config_manager.values[variable.data(Qt.UserRole)]
            for key, value in config.items():
                if isinstance(value, dict):
                    self.lw_regions.addItem(key)
            self.load_current_config()

    def load_volume_config(self):
        """"""
        variable = self.lw_variables.currentItem()
        region = self.lw_regions.currentItem()
        if region is not None:
            self.lw_volumes.clear()
            config = self.config_manager.values[variable.data(Qt.UserRole)][region.text()]
            for key, value in config.items():
                if isinstance(value, dict):
                    self.lw_volumes.addItem(key)
            self.load_current_config()

    def toggle_widget_list(self, widgets, toggle):
        """"""
        for widget_name in widgets:
            widget = getattr(self, widget_name, None)
            if widget:
                widget.setEnabled(toggle)
                if not toggle:
                    if isinstance(widget, qtw.QLineEdit):
                        widget.clear()
                    elif isinstance(widget, qtw.QComboBox):
                        widget.setCurrentText(None)
                    elif isinstance(widget, qtw.QCheckBox):
                        widget.setChecked(toggle)
            else:
                print(f"ERROR AL LIMPIAR: {widget_name} en {widgets}")

    def value_changed(self, value):
        """
        Maneja cambios en los valores de los widgets y actualiza el diccionario de configuraciones.

        Parameters:
        value: El nuevo valor del widget que ha cambiado.
        """
        # fmt: off
        sender = self.sender()
        variable = self.lw_variables.currentItem()
        region = self.lw_regions.currentItem()
        volume = self.lw_volumes.currentItem()
        variable_key = variable.data(Qt.UserRole)
        if value is not None and value != "":
            # Si hay un valor nuevo válido
            if region and volume and sender.objectName() in self.volume_widgets:
                # Si el cambio es en un widget de volumen
                if variable_key not in self.config_manager.values:
                    self.config_manager.values[variable_key] = {}
                if region.text() not in self.config_manager.values[variable_key]:
                    self.config_manager.values[variable_key][region.text()] = {}
                if volume.text() not in self.config_manager.values[variable_key][region.text()]:
                    self.config_manager.values[variable_key][region.text()][volume.text()] = {}
                self.config_manager.values[variable_key][region.text()][volume.text()][sender.objectName()] = value
            elif region and sender.objectName() in self.region_widgets:
                # Si el cambio es en un widget de región
                if variable_key not in self.config_manager.values:
                    self.config_manager.values[variable_key] = {}
                if region.text() not in self.config_manager.values[variable_key]:
                    self.config_manager.values[variable_key][region.text()] = {}
                self.config_manager.values[variable_key][region.text()][sender.objectName()] = value
            elif variable and sender.objectName() in self.variable_widgets:
                # Si el cambio es en un widget de variable
                if variable_key not in self.config_manager.values:
                    self.config_manager.values[variable_key] = {}
                self.config_manager.values[variable_key][sender.objectName()] = value
        else:
            # Si el valor es None o vacío, eliminar el valor del diccionario
            if region and volume and sender.objectName() in self.volume_widgets:
                # Eliminar valor del widget de volumen
                self.config_manager.values[variable_key][region.text()][volume.text()].pop(sender.objectName(), None)
                # Limpiar diccionarios vacíos
                if not self.config_manager.values[variable_key][region.text()]:
                    del self.config_manager.values[variable_key][region.text()]
            elif region and sender.objectName() in self.region_widgets:
                # Eliminar valor del widget de región
                self.config_manager.values[variable_key][region.text()].pop(sender.objectName(), None)
                # Limpiar diccionarios vacíos
                if not self.config_manager.values[variable_key][region.text()]:
                    del self.config_manager.values[variable_key][region.text()]
            elif variable and sender.objectName() in self.variable_widgets:
                # Eliminar valor del widget de variable
                self.config_manager.values[variable_key].pop(sender.objectName(), None)
            # Limpieza adicional para asegurar que no queden diccionarios vacíos
            if variable and not self.config_manager.values[variable_key]:
                del self.config_manager.values[variable_key]

    def add_region(self):
        """"""
        region_number = self.lw_regions.count() + 1
        self.lw_regions.addItem(f"Region {region_number}")
        variable = self.lw_variables.currentItem()
        if variable is not None:
            if f"Region {region_number}" not in self.config_manager.values[variable.data(Qt.UserRole)]:
                self.config_manager.values[variable.data(Qt.UserRole)][f"Region {region_number}"] = {}
            self.config_manager.values[variable.data(Qt.UserRole)][f"Region {region_number}"]["Volumen 1"] = {}

    def remove_region(self):
        """"""
        region_count = self.lw_regions.count()
        if region_count > 1:
            last_region = self.lw_regions.item(region_count - 1)
            self.lw_regions.takeItem(region_count - 1)
            variable = self.lw_variables.currentItem()
            if variable is not None:
                self.config_manager.values[variable.data(Qt.UserRole)].pop(last_region.text(), None)

    def add_volume(self):
        volume_number = self.lw_volumes.count() + 1
        self.lw_volumes.addItem(f"Volumen {volume_number}")
        variable = self.lw_variables.currentItem()
        region = self.lw_regions.currentItem()
        if variable is not None and region is not None:
            volume_key = f"Volumen {volume_number}"
            self.config_manager.values[variable.data(Qt.UserRole)][region.text()][volume_key] = {}

    def remove_volume(self):
        """"""
        volume_count = self.lw_volumes.count()
        if volume_count > 1:
            last_volume = self.lw_regions.item(volume_count - 1)
            self.lw_volumes.takeItem(volume_count - 1)
            variable = self.lw_variables.currentItem()
            region = self.lw_regions.currentItem()
            if variable is not None and region is not None:
                self.config_manager.values[variable.data(Qt.UserRole)][region.text()].pop(last_volume.text(), None)

    def initialize_volume_data(self):
        """Inicializa los valores de malla para un volumen nuevo"""
        if self.config_manager.is_cartesian and self.config_manager.is_ezgrid:
            volume_data = {
                "le_x_start": "0",
                "le_x_end": self.config_manager.grid["le_xlon"],
                "le_y_start": "0",
                "le_y_end": self.config_manager.grid["le_ylon"],
                "le_z_start": "0",
                "le_z_end": self.config_manager.grid["le_zlon"],
            }
        elif not self.config_manager.is_cartesian and self.config_manager.is_ezgrid:
            volume_data = {
                "le_x_start": "0",
                "le_x_end": self.config_manager.grid["le_titalon"],
                "le_y_start": self.config_manager.grid["le_rini"],
                "le_y_end": self.config_manager.grid["le_rlon"],
                "le_z_start": "0",
                "le_z_end": self.config_manager.grid["le_zloncil"],
            }
        elif self.config_manager.is_cartesian and not self.config_manager.is_ezgrid:
            x_end = sum(
                float(self.config_manager.grid.get(f"le_dirx_lon_zon{i}", 0))
                for i in range(1, self.config_manager.grid["sb_dirx_numz"] + 1)
            )
            y_end = sum(
                float(self.config_manager.grid.get(f"le_diry_lon_zon{i}", 0))
                for i in range(1, self.config_manager.grid["sb_diry_numz"] + 1)
            )
            z_end = sum(
                float(self.config_manager.grid.get(f"le_dirz_lon_zon{i}", 0))
                for i in range(1, self.config_manager.grid["sb_dirz_numz"] + 1)
            )
            volume_data = {
                "le_x_start": "0",
                "le_x_end": str(x_end),
                "le_y_start": "0",
                "le_y_end": str(y_end),
                "le_z_start": "0",
                "le_z_end": str(z_end),
            }
        else:  # if not self.config_manager.is_cartesian and not self.config_manager.is_ezgrid
            x_end = sum(
                float(self.config_manager.grid.get(f"le_dirtita_lon_zon{i}", 0))
                for i in range(1, self.config_manager.grid["sb_dirtita_numz"] + 1)
            )
            y_end = sum(
                float(self.config_manager.grid.get(f"le_dirr_lon_zon{i}", 0))
                for i in range(1, self.config_manager.grid["sb_dirr_numz"] + 1)
            )
            z_end = sum(
                float(self.config_manager.grid.get(f"le_dirzcil_lon_zon{i}", 0))
                for i in range(1, self.config_manager.grid["sb_dirzcil_numz"] + 1)
            )
            y_start = self.config_manager.grid.get("le_dirr_inidom", 0)
            volume_data = {
                "le_x_start": "0",
                "le_x_end": str(x_end),
                "le_y_start": str(y_start),
                "le_y_end": str(y_end),
                "le_z_start": "0",
                "le_z_end": str(z_end),
            }
        return volume_data

    def print_dict(self, od, indent=0, show_markers=False):
        # Create an indentation space based on the current level
        indent_space = "    " * indent
        if show_markers:
            print(f"{indent_space}INICIO ######################")
        for key, value in od.items():
            if isinstance(value, dict):
                print(f"{indent_space}{key}:")
                self.print_dict(value, indent + 1, show_markers=False)
            else:
                print(f"{indent_space}{key}: {value}")
        if show_markers:
            print(f"{indent_space}FINAL ######################")
