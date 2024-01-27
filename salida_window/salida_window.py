import sys
from PySide6 import QtCore as qtc
from PySide6 import QtWidgets as qtw
from PySide6 import QtGui as qtg

from salida_window.ui.salida_window_ui import Ui_salida_window

class SalidaWindow(qtw.QDialog, Ui_salida_window):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
      
if __name__ == "__main__":
    app = qtw.QApplication(sys.argv)

    form = SalidaWindow()

    form.open()

    sys.exit(app.exec())