import sys
from PySide6 import QtCore as qtc
from PySide6 import QtWidgets as qtw
from PySide6 import QtGui as qtg
from PySide6.QtGui import QAction


from main_window.ui.main_window_ui import Ui_main_window
from inicio_window.inicio_window import InicioWindow
from malla_window.malla_window import MallaWindow
from variables_window.variables_window import VariablesWindow
from valores_window.valores_window import ValoresWindow
from bordes_window.bordes_window import BordesWindow
from salida_window.salida_window import SalidaWindow


from config_manager import ConfigManager
from f90_serializer import generate_f90


class MainWindow(qtw.QMainWindow, Ui_main_window):
    def __init__(self):
        super().__init__()
        self.config_manager = ConfigManager()
        self.setupUi()

    def setupUi(self):
        super().setupUi(self)
        self.action_guardar.triggered.connect(self.guardar_configuracion)
        self.action_salir.triggered.connect(self.close)

        self.pb_inicio.clicked.connect(self.open_inicio)
        self.pb_malla.clicked.connect(self.open_malla)
        self.pb_variables.clicked.connect(self.open_variables)
        self.pb_valores.clicked.connect(self.open_valores)
        self.pb_bordes.clicked.connect(self.open_bordes)
        self.pb_salida.clicked.connect(self.open_salida)

    @qtc.Slot()
    def open_inicio(self):
        self.form = InicioWindow(self.config_manager)
        self.form.exec()

    @qtc.Slot()
    def open_malla(self):
        self.form = MallaWindow(self.config_manager)
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

    def guardar_configuracion(self):
        # Primero, guardar la configuración en un archivo JSON
        nombre_archivo_json = "configuracion.json"
        self.config_manager.save_to_json(nombre_archivo_json)
        qtw.QMessageBox.information(
            self,
            "Guardar Configuración",
            f"La configuración se ha guardado correctamente en '{nombre_archivo_json}'.",
        )

        # Luego, generar y guardar el contenido .f90
        contenido_f90 = generate_f90(self.config_manager.config_structure)
        nombre_archivo_f90 = "configuracion.adapt.f90"
        with open(nombre_archivo_f90, "w") as archivo:
            archivo.write(contenido_f90)
        qtw.QMessageBox.information(
            self,
            "Guardar Configuración",
            f"La configuración se ha guardado correctamente en '{nombre_archivo_f90}'.",
        )


if __name__ == "__main__":
    app = qtw.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
