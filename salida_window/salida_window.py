from PySide6 import QtWidgets as qtw
from PySide6.QtCore import Qt

from salida_window.ui.salida_window_ui import Ui_salida_window


class SalidaWindow(qtw.QDialog, Ui_salida_window):
    def __init__(self, config_manager):
        super().__init__()
        self.setupUi(self)
        self.config_manager = config_manager
        self.config_name = "OUTPUT"

        self.general_widgets = ["le_last", "chb_dimensionless"]
        self.variable_widgets = ["le_x", "le_y", "le_z", "chb_common_node", "chb_different_nodes"]
        self.widgets = self.general_widgets + self.variable_widgets

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
                self.config_manager.output[variable_key].pop(sender.objectName(), None)
            else:
                self.config_manager.output.pop(sender.objectName(), None)
            # Limpieza adicional para asegurar que no queden diccionarios vacíos
            if variable and not self.config_manager.output[variable_key]:
                del self.config_manager.output[variable_key]
        self.print_dict(self.config_manager.output)
        print()

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
            config = self.config_manager.values[variable.data(Qt.UserRole)]
            configured_widgets = set()
            configured_widgets.update(key for key, value in config.items() if not isinstance(value, dict))
            return configured_widgets
        return []

    def load_current_config(self):
        """"""
        variable = self.lw_variables.currentItem()
        configured_widgets = self.get_configured_widgets(variable)
        not_configured_widgets = [widget for widget in self.variable_widgets if widget not in configured_widgets]
        self.toggle_widget_list(not_configured_widgets, False)
        # Seleccionada una variable
        if variable is not None:
            config = self.config_manager.output[variable.data(Qt.UserRole)]
            self.toggle_widget_list(self.variable_widgets, True)
            self.config_manager.load_config(self, config)
        self.config_manager.load_config(self, self.config_manager.output)

    def load_variables_list(self):
        """Carga y actualiza la lista de variables considerando el orden y permitiendo duplicados."""
        current_items = [
            (self.lw_variables.item(i).text(), self.lw_variables.item(i).data(Qt.UserRole))
            for i in range(self.lw_variables.count())
        ]
        new_items = [(data["name"], key) for key, data in self.config_manager.values.items() if "name" in data]
        print("CURRENT VS NEW:", current_items, new_items)
        if new_items != current_items:
            self.lw_variables.clear()
            for name, tech_name in new_items:
                item = qtw.QListWidgetItem(name)
                item.setData(Qt.UserRole, tech_name)
                self.lw_variables.addItem(item)
        self.load_current_config()

    def print_dict(self, od, indent=0, show_markers=False):
        # Create an indentation space based on the current level
        indent_space = "    " * indent
        if show_markers:
            print(f"{indent_space}INICIO ######################")
        for key, value in od.items():
            if isinstance(value, dict):  # If the value is a dictionary, print the key and then the nested dictionary
                print(f"{indent_space}{key}:")
                self.print_dict(value, indent + 1, show_markers=False)
            else:  # If the value is not a dictionary, print key-value pair
                print(f"{indent_space}{key}: {value}")
        if show_markers:
            print(f"{indent_space}FINAL ######################")
