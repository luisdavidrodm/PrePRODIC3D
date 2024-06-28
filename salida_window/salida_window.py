from PySide2 import QtWidgets as qtw
from PySide2.QtCore import Qt

from salida_window.ui.salida_window_ui import Ui_salida_window


class SalidaWindow(qtw.QDialog, Ui_salida_window):
    def __init__(self, config_manager):
        super().__init__()
        self.setupUi(self)
        self.config_manager = config_manager
        self.config_name = "OUTPUT"

        self.general_widgets = ["le_last", "le_temp_last", "le_tw", "chb_dimensionless"]
        self.variable_widgets = ["le_x", "le_y", "le_z", "chb_all_corners"]
        for i in range(1, 9):
            self.variable_widgets.extend([f"chb_corner_{i}"])
            getattr(self, f"chb_corner_{i}").stateChanged.connect(self.handle_chb_corners_changed)

        self.widgets = self.general_widgets + self.variable_widgets

        self.chb_all_corners.stateChanged.connect(self.handle_chb_all_corners_changed)
        self.lw_variables.currentRowChanged.connect(self.load_current_config)

        self.config_manager.connect_config(self)
        self.load_variables_list()
        self.lw_variables.setCurrentItem(self.lw_variables.item(0))

    def value_changed(self, value):
        """
        Maneja cambios en los valores de los widgets y actualiza el diccionario de configuraciones.

        Parameters:
        value: El nuevo valor del widget que ha cambiado.
        """
        # fmt: off
        sender = self.sender()
        variable = self.lw_variables.currentItem()
        if value is not None and value != "":
            # Si hay un valor nuevo válido
            if variable and sender.objectName() in self.variable_widgets:
                # Si el cambio es en un widget de variable
                variable_key = variable.data(Qt.UserRole)
                if variable_key not in self.config_manager.output:
                    self.config_manager.output[variable_key] = {}
                self.config_manager.output[variable_key][sender.objectName()] = value
            else:
                self.config_manager.output[sender.objectName()] = value
        else:
            if variable and sender.objectName() in self.variable_widgets:
                # Eliminar valor del widget de variable
                variable_key = variable.data(Qt.UserRole)
                if variable_key in self.config_manager.output:
                    self.config_manager.output[variable_key].pop(sender.objectName(), None)
            else:
                self.config_manager.output.pop(sender.objectName(), None)
            # Limpieza adicional para asegurar que no queden diccionarios vacíos
            if variable:
                variable_key = variable.data(Qt.UserRole)
                if variable_key in self.config_manager.output and not self.config_manager.output[variable_key]:
                    del self.config_manager.output[variable_key]

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
                        widget.setChecked(toggle)
            else:
                print(f"ERROR AL LIMPIAR: {widget_name} en {widgets}")

    def get_configured_widgets(self, variable):
        """"""
        # Esta función busca en la configuración y recoge todos los widgets configurados
        if variable:
            variable_key = variable.data(Qt.UserRole)
            if variable_key in self.config_manager.output:
                config = self.config_manager.output[variable.data(Qt.UserRole)]
                configured_widgets = set()
                configured_widgets.update(key for key in config.keys())
                return configured_widgets
        return []

    def load_current_config(self):
        """"""
        variable = self.lw_variables.currentItem()
        configured_widgets = self.get_configured_widgets(variable)
        not_configured_widgets = [widget for widget in self.variable_widgets if widget not in configured_widgets]
        self.toggle_widget_list(not_configured_widgets, False)
        # Seleccionada una variable
        if variable:
            self.toggle_widget_list(self.variable_widgets, True)
            variable_key = variable.data(Qt.UserRole)
            if variable_key in self.config_manager.output:
                config = self.config_manager.output[variable_key]
                self.config_manager.load_config(self, config)
        self.config_manager.load_config(self, self.config_manager.output)

    def load_variables_list(self):
        """Carga y actualiza la lista de variables considerando el orden y permitiendo duplicados."""
        current_items = [
            (self.lw_variables.item(i).text(), self.lw_variables.item(i).data(Qt.UserRole))
            for i in range(self.lw_variables.count())
        ]
        new_items = [
            (data["name"], key) for key, data in self.config_manager.output.items() if key.startswith("le_var_title")
        ]
        if new_items != current_items:
            self.lw_variables.clear()
            for name, tech_name in new_items:
                item = qtw.QListWidgetItem(name)
                item.setData(Qt.UserRole, tech_name)
                self.lw_variables.addItem(item)
        self.load_current_config()

    def handle_chb_all_corners_changed(self, state):
        if state == 2:
            for i in range(1, 9):
                getattr(self, f"chb_corner_{i}").setChecked(True)

    def handle_chb_corners_changed(self, _):
        if all([getattr(self, f"chb_corner_{i}").isChecked() for i in range(1, 9)]):
            if not self.chb_all_corners.isChecked():
                self.chb_all_corners.setChecked(True)
        else:
            if self.chb_all_corners.isChecked():
                self.chb_all_corners.setChecked(False)
