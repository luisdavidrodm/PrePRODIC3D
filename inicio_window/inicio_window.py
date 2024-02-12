import sys
from PySide6 import QtWidgets as qtw

from config_manager import ConfigManager
from inicio_window.ui.inicio_window_ui import Ui_inicio_window


class InicioWindow(qtw.QDialog, Ui_inicio_window):
    def __init__(self, config_manager):
        super().__init__()
        self.setupUi(self)
        self.config_manager = config_manager

        # Conectar los widgets con los métodos para actualizar la configuración
        self.le_titulosimu.textChanged.connect(self.update_header)
        self.le_tituloimpre.textChanged.connect(self.update_printf)
        self.le_titulograf.textChanged.connect(self.update_plotf)

    def update_header(self, text):
        self.config_manager.set_header(
            text,
            self.config_manager.config_structure["HEADER"].get("PRINTF", ""),
            self.config_manager.config_structure["HEADER"].get("PLOTF", ""),
        )

    def update_printf(self, text):
        self.config_manager.set_header(
            self.config_manager.config_structure["HEADER"].get("HEADER", ""),
            text,
            self.config_manager.config_structure["HEADER"].get("PLOTF", ""),
        )

    def update_plotf(self, text):
        self.config_manager.set_header(
            self.config_manager.config_structure["HEADER"].get("HEADER", ""),
            self.config_manager.config_structure["HEADER"].get("PRINTF", ""),
            text,
        )


if __name__ == "__main__":
    app = qtw.QApplication(sys.argv)
    config_manager = ConfigManager()
    form = InicioWindow(config_manager)
    form.open()
    sys.exit(app.exec())
