import sys
from PySide6 import QtCore as qtc
from PySide6 import QtWidgets as qtw
from PySide6 import QtGui as qtg

from main_window.ui.main_window_ui import Ui_main_window
from inicio_window.inicio_window import InicioWindow
from malla_window.malla_window import MallaWindow
from variables_window.variables_window import VariablesWindow

class MainWindow(qtw.QMainWindow, Ui_main_window):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.action_salir.triggered.connect(self.close)

        self.pb_inicio.clicked.connect(self.open_inicio)

        self.pb_malla.clicked.connect(self.open_malla)

        self.pb_variables.clicked.connect(self.open_variables)

    @qtc.Slot()
    def open_inicio(self):
        self.form = InicioWindow()
        self.form.exec()
    
    @qtc.Slot()
    def open_malla(self):
        self.form = MallaWindow()
        self.form.exec()

    @qtc.Slot()
    def open_variables(self):
        self.form = VariablesWindow()
        self.form.exec()

if __name__ == "__main__":
    app = qtw.QApplication(sys.argv)

    window = MainWindow()

    window.show()

    sys.exit(app.exec())