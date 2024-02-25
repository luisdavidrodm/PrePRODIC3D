import sys
from PySide6 import QtWidgets as qtw

from valores_window.ui.valores_window_ui import Ui_valores_window
from config_manager import ConfigManager


class ValoresWindow(qtw.QDialog, Ui_valores_window):
    def __init__(self, config_manager):
        super().__init__()
        self.setupUi(self)
        self.config_manager = config_manager


if __name__ == "__main__":
    app = qtw.QApplication(sys.argv)
    config_manager = ConfigManager()
    form = ValoresWindow(config_manager)
    form.open()
    sys.exit(app.exec())
