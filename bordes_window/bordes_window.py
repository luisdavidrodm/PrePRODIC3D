import sys
from PySide6 import QtCore as qtc
from PySide6 import QtWidgets as qtw
from PySide6 import QtGui as qtg

from bordes_window.ui.bordes_window_ui import Ui_bordes_window

class BordesWindow(qtw.QDialog, Ui_bordes_window):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

if __name__ == "__main__":
    app = qtw.QApplication(sys.argv)

    form = BordesWindow()

    form.open()

    sys.exit(app.exec())