import sys
from PySide6 import QtCore as qtc
from PySide6 import QtWidgets as qtw


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

        self.inicio_window = None
        self.malla_window = None
        self.variables_window = None
        self.valores_window = None
        self.bordes_window = None
        self.salida_window = None

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
        if self.inicio_window is None or not self.inicio_window.isVisible():
            self.inicio_window = InicioWindow(self.config_manager)
            self.inicio_window.show()
        else:
            self.inicio_window.raise_()
            self.inicio_window.activateWindow()

    @qtc.Slot()
    def open_malla(self):
        if self.malla_window is None or not self.malla_window.isVisible():
            self.malla_window = MallaWindow(self.config_manager)
            self.malla_window.show()
        else:
            self.malla_window.raise_()
            self.malla_window.activateWindow()

    @qtc.Slot()
    def open_variables(self):
        if self.variables_window is None or not self.variables_window.isVisible():
            self.variables_window = VariablesWindow(self.config_manager)
            self.variables_window.tipo_flujo_cambio_signal.connect(
                self.handle_tipo_flujo_cambio
            )
            self.variables_window.show()
        else:
            self.variables_window.raise_()
            self.variables_window.activateWindow()

    @qtc.Slot()
    def open_valores(self):
        if self.valores_window is None or not self.valores_window.isVisible():
            self.valores_window = ValoresWindow(self.config_manager)
            self.valores_window.show()
        else:
            self.valores_window.raise_()
            self.valores_window.activateWindow()

    @qtc.Slot()
    def open_bordes(self):
        if self.bordes_window is None or not self.bordes_window.isVisible():
            self.bordes_window = BordesWindow(self.config_manager)
            self.bordes_window.show()
        else:
            self.bordes_window.raise_()
            self.bordes_window.activateWindow()

    @qtc.Slot()
    def open_salida(self):
        if self.salida_window is None or not self.salida_window.isVisible():
            self.salida_window = SalidaWindow()
            self.salida_window.show()
        else:
            self.salida_window.raise_()
            self.salida_window.activateWindow()

    def handle_tipo_flujo_cambio(self, es_difusivo):
        if self.bordes_window:
            # Llamar a un método que actualice el estado del campo 'Entrada de la masa'
            print(
                f"Recibiendo señal en MainWindow, es_difusivo: {es_difusivo}"
            )  # Impresión de depuración
            self.bordes_window.update_entrada_masa(es_difusivo)

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
