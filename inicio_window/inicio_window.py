from PySide6 import QtWidgets as qtw

from inicio_window.ui.inicio_window_ui import Ui_inicio_window


class InicioWindow(qtw.QDialog, Ui_inicio_window):
    def __init__(self, config_manager):
        super().__init__()
        self.setupUi(self)
        self.config_manager = config_manager

        # Conectar los widgets con los métodos para actualizar la configuración
        self.le_titulosimu.textChanged.connect(lambda text: self.update_config("HEADER", text))
        self.le_tituloimpre.textChanged.connect(lambda text: self.update_config("PRINTF", text))
        self.le_titulograf.textChanged.connect(lambda text: self.update_config("PLOTF", text))

    def update_config(self, config_key, text):
        # Actualiza el valor de la configuración en el ConfigManager
        self.config_manager.config_structure["HEADER"][config_key] = text
