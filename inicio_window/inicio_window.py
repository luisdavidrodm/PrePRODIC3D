from PySide6 import QtWidgets as qtw

from inicio_window.ui.inicio_window_ui import Ui_inicio_window


class InicioWindow(qtw.QDialog, Ui_inicio_window):
    def __init__(self, config_manager):
        super().__init__()
        self.setupUi(self)
        self.config_manager = config_manager

        self.widgets = ["le_titulosimu", "le_tituloimpre", "le_titulograf"]
        for widget_name in self.widgets:
            getattr(self, widget_name).textChanged.connect(self.value_changed)
        self.le_tituloimpre.setEnabled(False)
        self.le_titulograf.setEnabled(False)
        self.load_malla_config()

    def value_changed(self, value):
        sender = self.sender()
        self.config_manager.config_structure["HEADER"][sender.objectName()] = value

    def load_malla_config(self):
        config = self.config_manager.config_structure["HEADER"]
        for widget_name, value in config.items():
            getattr(self, widget_name).setText(value)
