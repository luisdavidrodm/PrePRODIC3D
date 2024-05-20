from PySide6 import QtWidgets as qtw

from salida_window.ui.salida_window_ui import Ui_salida_window


class SalidaWindow(qtw.QDialog, Ui_salida_window):
    def __init__(self, config_manager):
        super().__init__()
        self.setupUi(self)
        self.config_manager = config_manager
        self.config_name = "OUTPUT"

        self.widgets = ["le_last"]
        for widget_name in self.widgets:
            getattr(self, widget_name).textChanged.connect(self.value_changed)
        self.load_malla_config()

    def value_changed(self, value):
        sender = self.sender()
        if value is None or value == "":
            self.config_manager.config_structure[self.config_name].pop(sender.objectName(), None)
        else:
            self.config_manager.config_structure[self.config_name][sender.objectName()] = value

    def load_malla_config(self):
        config = self.config_manager.config_structure[self.config_name]
        for widget_name, value in config.items():
            getattr(self, widget_name).setText(value)
