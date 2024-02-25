from PySide6 import QtWidgets as qtw

from valores_window.ui.valores_window_ui import Ui_valores_window


class ValoresWindow(qtw.QDialog, Ui_valores_window):
    def __init__(self, config_manager):
        super().__init__()
        self.setupUi(self)
        self.config_manager = config_manager
