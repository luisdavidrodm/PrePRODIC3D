import sys
from PySide6 import QtCore as qtc
from PySide6 import QtWidgets as qtw
from PySide6 import QtGui as qtg

from main_window.ui.main_window_ui import Ui_main_window
from inicio_window.inicio_window import InicioWindow
from malla_window.malla_window import MallaWindow
from variables_window.variables_window import VariablesWindow
from valores_window.valores_window import ValoresWindow
from bordes_window.bordes_window import BordesWindow
from salida_window.salida_window import SalidaWindow

class MainWindow(qtw.QMainWindow, Ui_main_window):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.action_salir.triggered.connect(self.close)

        self.pb_inicio.clicked.connect(self.open_inicio)

        self.pb_malla.clicked.connect(self.open_malla)

        self.pb_variables.clicked.connect(self.open_variables)

        self.pb_valores.clicked.connect(self.open_valores)

        self.pb_bordes.clicked.connect(self.open_bordes)
        
        self.pb_salida.clicked.connect(self.open_salida)

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
    
    @qtc.Slot()
    def open_valores(self):
        self.form = ValoresWindow()
        self.form.exec()

    @qtc.Slot()
    def open_bordes(self):
        self.form = BordesWindow()
        self.form.exec()

    @qtc.Slot()
    def open_salida(self):
        self.form = SalidaWindow()
        self.form.exec()

if __name__ == "__main__":
    app = qtw.QApplication(sys.argv)

    window = MainWindow()

    window.show()

    sys.exit(app.exec())