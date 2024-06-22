from PySide6 import QtWidgets as qtw
from PySide6.QtCore import Qt

from bordes_window.ui.bordes_window_ui import Ui_bordes_window


class BordesWindow(qtw.QDialog, Ui_bordes_window):

    def __init__(self, config_manager):
        # fmt: off
        super().__init__()
        self.setupUi(self)
        self.config_manager = config_manager
        self.config_name = "BOUND"

        self.pb_addpatch.clicked.connect(self.add_patch)
        self.pb_rempatch.clicked.connect(self.remove_patch)

        self.lw_bordes.currentRowChanged.connect(self.load_patch_list)
        self.lw_patchlist.currentRowChanged.connect(self.load_patch_config)
        self.lw_variables.currentRowChanged.connect(self.load_current_config)

        # Definir widgets de parches y listas de widgets
        self.patch_widgets = [
            "le_value", "le_tempamb", "chb_wall", "chb_inmass", "chb_outmass",
            "le_value_veloc_u", "le_value_veloc_v", "le_value_veloc_w",
            "le_fracmass", "le_transversal_start", "le_transversal_end",
            "le_vertical_start", "le_vertical_end", "chb_ex_veloc_u", 
            "chb_ex_veloc_v", "chb_ex_veloc_w", "chb_exclude_borders"
        ]
        self.variable_widgets = [
            "le_value", "le_tempamb", "chb_value", "chb_flux", 
            "chb_convec", "chb_ex_value", "le_k", "chb_ex_k"]
        self.widgets = self.patch_widgets + self.variable_widgets

        for chb_name in ['wall', 'inmass', 'outmass', 'value', 'flux', 'convec']:
            checkbox = getattr(self, f'chb_{chb_name}')
            checkbox.stateChanged.connect(self.handle_checkbox_state_changed)

        self.config_manager.connect_config(self)
        self.lw_bordes.setCurrentItem(self.lw_bordes.item(0))
        self.load_variables_list()
        self.initialize_patch_labels()
        # fmt: on

    def toggle_widget_list(self, widgets, toggle):
        """"""
        for widget_name in widgets:
            widget = getattr(self, widget_name, None)
            if widget:
                widget.setEnabled(toggle)
                if not toggle:
                    if isinstance(widget, qtw.QLineEdit):
                        widget.clear()
                    elif isinstance(widget, qtw.QCheckBox):
                        widget.setChecked(False)
            else:
                print(f"ERROR AL LIMPIAR: {widget_name} en {widgets}")

    def value_changed(self, value):
        """"""
        sender = self.sender()
        border = self.lw_bordes.currentItem()
        patch = self.lw_patchlist.currentItem()
        variable = self.lw_variables.currentItem()
        if value is not None and value != "":
            # Si hay un valor nuevo válido
            if border and patch and variable and sender.objectName() in self.variable_widgets:
                variable_key = variable.data(Qt.UserRole)
                self.le_tempamb.setEnabled(self.chb_convec.isChecked() or self.chb_flux.isChecked())
                if border.text() not in self.config_manager.bound:
                    self.config_manager.bound[border.text()] = {}
                if patch.text() not in self.config_manager.bound[border.text()]:
                    self.config_manager.bound[border.text()][patch.text()] = {}
                if variable_key not in self.config_manager.bound[border.text()][patch.text()]:
                    self.config_manager.bound[border.text()][patch.text()][variable_key] = {}
                self.config_manager.bound[border.text()][patch.text()][variable_key][sender.objectName()] = value
            elif border and patch and sender.objectName() in self.patch_widgets:
                if border.text() not in self.config_manager.bound:
                    self.config_manager.bound[border.text()] = {}
                if patch.text() not in self.config_manager.bound[border.text()]:
                    self.config_manager.bound[border.text()][patch.text()] = {}
                self.config_manager.bound[border.text()][patch.text()][sender.objectName()] = value
        else:
            if border and patch and variable and sender.objectName() in self.variable_widgets:
                self.config_manager.bound[border.text()][patch.text()][variable_key].pop(sender.objectName(), None)
                if not self.config_manager.bound[border.text()][patch.text()][variable_key]:
                    del self.config_manager.bound[border.text()][patch.text()][variable_key]
                if not self.config_manager.bound[border.text()][patch.text()]:
                    del self.config_manager.bound[border.text()][patch.text()]
            elif border and patch and sender.objectName() in self.patch_widgets:
                self.config_manager.bound[border.text()][patch.text()].pop(sender.objectName(), None)
                if not self.config_manager.bound[border.text()][patch.text()]:
                    del self.config_manager.bound[border.text()][patch.text()]

    def get_configured_widgets(self, border, patch, variable):
        """"""
        # Esta función busca en la configuración y recoge todos los widgets configurados
        if border and patch:
            border_text = border.text()
            patch_text = patch.text()
            if border_text not in self.config_manager.bound:
                self.config_manager.bound[border_text] = {}
            if patch_text not in self.config_manager.bound[border_text]:
                self.config_manager.bound[border_text][patch_text] = {}
            config = self.config_manager.bound[border_text][patch_text]
            configured_widgets = set()
            configured_widgets.update(key for key, value in config.items() if not isinstance(value, dict))
            if variable:
                variable_key = variable.data(Qt.UserRole)
                if variable_key not in config:
                    config[variable_key] = {}
                variable_config = config[variable_key]
                configured_widgets.update(key for key, value in variable_config.items())
            return configured_widgets
        return []

    def load_current_config(self):
        """"""
        border = self.lw_bordes.currentItem()
        patch = self.lw_patchlist.currentItem()
        variable = self.lw_variables.currentItem()
        configured_widgets = self.get_configured_widgets(border, patch, variable)
        not_configured_widgets = [widget for widget in self.widgets if widget not in configured_widgets]
        self.toggle_widget_list(not_configured_widgets, False)
        print(
            f"{border.text() if border else None}, {patch.text() if patch else None}, {variable.text() if variable else None}"
        )
        if border and patch:
            config = self.config_manager.bound[border.text()][patch.text()]
            self.toggle_widget_list(self.patch_widgets, True)
            self.config_manager.load_config(self, config)
            self.lw_variables.setEnabled(True)
            if patch.text() == "Borde base":
                self.le_transversal_start.setEnabled(False)
                self.le_transversal_end.setEnabled(False)
                self.le_vertical_start.setEnabled(False)
                self.le_vertical_end.setEnabled(False)
                if self.config_manager.is_mesh_info_complete:
                    patch_data = self.initialize_patch_data()
                    self.le_transversal_start.setText(patch_data["transversal_start"])
                    self.le_transversal_end.setText(patch_data["transversal_end"])
                    self.le_vertical_start.setText(patch_data["vertical_start"])
                    self.le_vertical_end.setText(patch_data["vertical_end"])
            if variable is not None:
                self.toggle_widget_list(self.variable_widgets, True)
                self.config_manager.load_config(self, config[variable.data(Qt.UserRole)])
                print(self.chb_convec.isChecked(), self.chb_flux.isChecked())
                self.le_tempamb.setEnabled(self.chb_convec.isChecked() or self.chb_flux.isChecked())
            else:
                self.toggle_widget_list(self.variable_widgets, False)
        else:
            self.lw_variables.setEnabled(False)

    def load_patch_list(self):
        """"""
        border = self.lw_bordes.currentItem()
        if border is not None:
            self.lw_patchlist.clear()
            config = self.config_manager.bound[border.text()]
            for key, value in config.items():
                if isinstance(value, dict):
                    self.lw_patchlist.addItem(key)
            self.load_current_config()
            self.initialize_patch_labels()

    def load_patch_config(self):
        """"""
        border = self.lw_bordes.currentItem()
        patch = self.lw_patchlist.currentItem()
        if border is not None and patch is not None:
            border_text = border.text()
            patch_text = patch.text()
            if self.config_manager.is_mesh_info_complete and patch_text != "Borde base":
                patch_data = self.initialize_patch_data()
                # Verificar si alguno de los valores ya está definido
                keys = ["le_transversal_start", "le_transversal_end", "le_vertical_start", "le_vertical_end"]
                if not any(key in self.config_manager.bound[border_text][patch_text] for key in keys):
                    self.config_manager.bound[border_text][patch_text]["le_transversal_start"] = patch_data[
                        "transversal_start"
                    ]
                    self.config_manager.bound[border_text][patch_text]["le_transversal_end"] = patch_data[
                        "transversal_end"
                    ]
                    self.config_manager.bound[border_text][patch_text]["le_vertical_start"] = patch_data[
                        "vertical_start"
                    ]
                    self.config_manager.bound[border_text][patch_text]["le_vertical_end"] = patch_data["vertical_end"]
            self.lw_variables.clearSelection()
            self.load_variables_list()

    def load_variables_list(self):
        """Carga y actualiza la lista de variables considerando el orden y permitiendo duplicados."""
        new_items = []
        for key, value in self.config_manager.variables.items():
            if key.startswith("le_var_title"):
                number = int(key[len("le_var_title") :])
                if number < 4:  # Excluir le_var_title1 a le_var_title3
                    continue
                new_items.append((number, value, key))
        new_items.sort()
        self.lw_variables.clear()
        for _, name, tech_name in new_items:
            item = qtw.QListWidgetItem(name)
            item.setData(Qt.UserRole, tech_name)
            self.lw_variables.addItem(item)
        self.load_current_config()

    def handle_checkbox_state_changed(self, state: int):
        """"""
        sender = self.sender()
        if state == 2:
            if sender in [self.chb_wall, self.chb_inmass, self.chb_outmass]:
                self.chb_wall.setChecked(sender == self.chb_wall)
                self.chb_inmass.setChecked(sender == self.chb_inmass)
                self.chb_outmass.setChecked(sender == self.chb_outmass)
            elif sender in [self.chb_value, self.chb_flux, self.chb_convec]:
                self.chb_value.setChecked(sender == self.chb_value)
                self.chb_flux.setChecked(sender == self.chb_flux)
                self.chb_convec.setChecked(sender == self.chb_convec)

    def add_patch(self):
        """"""
        border = self.lw_bordes.currentItem()
        if border:
            patch_number = self.lw_patchlist.count()
            self.lw_patchlist.addItem(f"Parche {patch_number}")
            self.config_manager.bound[border.text()][f"Parche {patch_number}"] = {"chb_wall": 2}

    def remove_patch(self):
        """"""
        border = self.lw_bordes.currentItem()
        if border:
            patch_count = self.lw_patchlist.count()
            if patch_count > 2:
                last_patch = self.lw_patchlist.item(patch_count - 1)
                self.lw_patchlist.takeItem(patch_count - 1)
                self.config_manager.bound[border.text()].pop(last_patch.text(), None)

    def initialize_patch_labels(self):
        """
        Initialize patch labels based on the selected patch.
        """
        transversal_label = ""
        vertical_label = ""
        border = self.lw_bordes.currentItem()
        if border is not None:
            border_text = border.text()
            if self.config_manager.is_cartesian:
                if border_text in {"X Max", "X Min"}:
                    transversal_label = "Y"
                    vertical_label = "Z"
                elif border_text in {"Y Max", "Y Min"}:
                    transversal_label = "X"
                    vertical_label = "Z"
                elif border_text in {"Z Max", "Z Min"}:
                    transversal_label = "X"
                    vertical_label = "Y"
            else:
                if border_text in {"X Max", "X Min"}:
                    transversal_label = "Y"
                    vertical_label = "Z"
                elif border_text in {"Y Max", "Y Min"}:
                    transversal_label = "X"
                    vertical_label = "Z"
                elif border_text in {"Z Max", "Z Min"}:
                    transversal_label = "X"
                    vertical_label = "Y"
        self.lb_transversal.setText(transversal_label)
        self.lb_vertical.setText(vertical_label)

    def initialize_patch_data(self):
        """
        Initialize patch data based on the selected patch.
        """
        patch_data = {}
        border = self.lw_bordes.currentItem()
        patch = self.lw_patchlist.currentItem()
        if border is not None and patch is not None:
            border_text = border.text()
            if self.config_manager.is_cartesian:
                if border_text in {"X Max", "X Min"}:
                    patch_data = {
                        "transversal_start": "0",
                        "transversal_end": self.config_manager.grid["le_ylon"],
                        "vertical_start": "0",
                        "vertical_end": self.config_manager.grid["le_zlon"],
                    }
                elif border_text in {"Y Max", "Y Min"}:
                    patch_data = {
                        "transversal_start": "0",
                        "transversal_end": self.config_manager.grid["le_xlon"],
                        "vertical_start": "0",
                        "vertical_end": self.config_manager.grid["le_zlon"],
                    }
                elif border_text in {"Z Max", "Z Min"}:
                    patch_data = {
                        "transversal_start": "0",
                        "transversal_end": self.config_manager.grid["le_xlon"],
                        "vertical_start": "0",
                        "vertical_end": self.config_manager.grid["le_ylon"],
                    }
            else:
                if border_text in {"X Max", "X Min"}:
                    patch_data = {
                        "transversal_start": self.config_manager.grid["le_rini"],
                        "transversal_end": self.config_manager.grid["le_rlon"],
                        "vertical_start": "0",
                        "vertical_end": self.config_manager.grid["le_zloncil"],
                    }
                elif border_text in {"Y Max", "Y Min"}:
                    patch_data = {
                        "transversal_start": "0",
                        "transversal_end": self.config_manager.grid["le_titalon"],
                        "vertical_start": "0",
                        "vertical_end": self.config_manager.grid["le_zloncil"],
                    }
                elif border_text in {"Z Max", "Z Min"}:
                    patch_data = {
                        "transversal_start": "0",
                        "transversal_end": self.config_manager.grid["le_titalon"],
                        "vertical_start": self.config_manager.grid["le_rini"],
                        "vertical_end": self.config_manager.grid["le_rlon"],
                    }
        print("patch_data", patch_data)
        print(border.text(), patch.text())
        return patch_data

    # def initialize_patch_data(self):
    #     """"""
    #     if self.config_manager.is_cartesian:
    #         volume_data = {
    #             "le_x_start": 0,
    #             "le_x_lon": self.config_manager.grid["le_xlon"],
    #             "le_y_start": 0,
    #             "le_y_lon": self.config_manager.grid["le_ylon"],
    #             "le_z_start": 0,
    #             "le_z_lon": self.config_manager.grid["le_zlon"],
    #         }
    #     else:
    #         volume_data = {
    #             "le_x_start": 0,
    #             "le_x_lon": self.config_manager.grid["le_titalon"],
    #             "le_y_start": self.config_manager.grid["le_rini"],
    #             "le_y_lon": self.config_manager.grid["le_rlon"],
    #             "le_z_start": 0,
    #             "le_z_lon": self.config_manager.grid["le_zloncil"],
    #         }
    #     return volume_data
