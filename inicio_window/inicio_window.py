import sys
from PySide6 import QtCore as qtc
from PySide6 import QtWidgets as qtw
from PySide6 import QtGui as qtg

from inicio_window.ui.inicio_window_ui import Ui_inicio_window

class InicioWindow(qtw.QDialog, Ui_inicio_window):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

if __name__ == "__main__":
    app = qtw.QApplication(sys.argv)

    form = InicioWindow()

    form.open()

    sys.exit(app.exec())