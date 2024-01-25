import sys
from PySide6 import QtCore as qtc
from PySide6 import QtWidgets as qtw
from PySide6 import QtGui as qtg

from valores_window.ui.valores_window_ui import Ui_valores_window

class ValoresWindow(qtw.QDialog, Ui_valores_window):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
      
if __name__ == "__main__":
    app = qtw.QApplication(sys.argv)

    form = ValoresWindow()

    form.open()

    sys.exit(app.exec())