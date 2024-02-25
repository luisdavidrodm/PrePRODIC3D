from PySide6 import QtWidgets as qtw

from salida_window.ui.salida_window_ui import Ui_salida_window


class SalidaWindow(qtw.QDialog, Ui_salida_window):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
