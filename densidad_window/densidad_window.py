from PySide6 import QtWidgets as qtw

from densidad_window.ui.densidad_window_ui import Ui_densidad_window


class DensidadWindow(qtw.QDialog, Ui_densidad_window):
    def __init__(self, config_manager):
        super().__init__()
        self.setupUi(self)
        self.config_manager = config_manager
