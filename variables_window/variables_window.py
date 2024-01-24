import sys
from PySide6 import QtCore as qtc
from PySide6 import QtWidgets as qtw
from PySide6 import QtGui as qtg

from variables_window.ui.variables_window_ui import Ui_variables_window

class VariablesWindow(qtw.QDialog, Ui_variables_window):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.cb_tsimu.currentTextChanged.connect(self.changeTipoSimu)

    def changeTipoSimu(self):
        current_text_simu = self.cb_tsimu.currentText()

        if current_text_simu == "Permanente":
            self.sw_tsimu.setCurrentIndex(0)
        elif current_text_simu == "Transitorio":
            self.sw_tsimu.setCurrentIndex(1)
        
if __name__ == "__main__":
    app = qtw.QApplication(sys.argv)

    form = VariablesWindow()

    form.open()

    sys.exit(app.exec())