import json
import glob
import sys
import os
import subprocess
import shutil

from PySide6 import QtWidgets as qtw

from main_window.ui.main_window_ui import Ui_main_window
from inicio_window.inicio_window import InicioWindow
from malla_window.malla_window import MallaWindow
from variables_window.variables_window import VariablesWindow
from valores_window.valores_window import ValoresWindow
from bordes_window.bordes_window import BordesWindow
from salida_window.salida_window import SalidaWindow

from config_manager import ConfigManager
from f90_serializer import F90Serializer


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

    def setupUi(self, *args):
        super().setupUi(self, *args)
        self.action_cargar_datos.triggered.connect(self.cargar_datos)
        self.action_guardar_datos.triggered.connect(self.guardar_datos)
        self.action_generar_rutina_fortran.triggered.connect(self.generar_rutina_fortran)
        self.action_generar_y_visualizar_resultados.triggered.connect(self.generar_y_visualizar_resultados)
        self.action_salir.triggered.connect(self.close)

        self.pb_inicio.clicked.connect(self.open_inicio)
        self.pb_malla.clicked.connect(self.open_malla)
        self.pb_variables.clicked.connect(self.open_variables)
        self.pb_valores.clicked.connect(self.open_valores)
        self.pb_bordes.clicked.connect(self.open_bordes)
        self.pb_salida.clicked.connect(self.open_salida)

    ################################################################################
    ##
    ## Funciones para abrir ventanas
    ##
    ################################################################################

    def open_inicio(self):
        if self.inicio_window is None or not self.inicio_window.isVisible():
            self.inicio_window = InicioWindow(self.config_manager)
            self.inicio_window.show()
        else:
            self.inicio_window.raise_()
            self.inicio_window.activateWindow()

    def open_malla(self):
        if self.malla_window is None or not self.malla_window.isVisible():
            self.malla_window = MallaWindow(self.config_manager)
            self.malla_window.longitudes_actualizadas_signal.connect(self.actualizar_longitudes_bordes)
            self.malla_window.show()
        else:
            self.malla_window.raise_()
            self.malla_window.activateWindow()

    def open_variables(self):
        if self.variables_window is None or not self.variables_window.isVisible():
            self.variables_window = VariablesWindow(self.config_manager)
            self.variables_window.tipo_flujo_cambio_signal.connect(self.handle_tipo_flujo_cambio)
            self.variables_window.variables_signal.connect(self.handle_variables_lista)
            self.variables_window.show()
        else:
            self.variables_window.raise_()
            self.variables_window.activateWindow()

    def open_valores(self):
        if self.valores_window is None or not self.valores_window.isVisible():
            self.valores_window = ValoresWindow(self.config_manager)
            self.valores_window.show()
        else:
            self.valores_window.raise_()
            self.valores_window.activateWindow()

    def open_bordes(self):
        if self.bordes_window is None or not self.bordes_window.isVisible():
            self.bordes_window = BordesWindow(self.config_manager)
            self.bordes_window.show()
        else:
            self.bordes_window.raise_()
            self.bordes_window.activateWindow()

    def open_salida(self):
        if self.salida_window is None or not self.salida_window.isVisible():
            self.salida_window = SalidaWindow()
            self.salida_window.show()
        else:
            self.salida_window.raise_()
            self.salida_window.activateWindow()

    ################################################################################
    ##
    ## Funciones de señales
    ##
    ################################################################################

    def handle_tipo_flujo_cambio(self, es_difusivo: bool):
        if self.bordes_window:
            # Llamar a un método que actualice el estado del campo 'Entrada de la masa'
            print(f"Recibiendo señal en MainWindow, es_difusivo: {es_difusivo}")  # Impresión de depuración
            self.bordes_window.update_entrada_masa(es_difusivo)

    def handle_variables_lista(self, variables: list):
        if self.bordes_window:
            print(f"Recibiendo señal en MainWindow, variables: {variables}")  # Impresión de depuración
            self.bordes_window.agregar_variables_lista(variables)

    def actualizar_longitudes_bordes(self, longitudes: list):
        self.bordes_window.actualizar_longitudes(longitudes)

    ################################################################################
    ##
    ## Guardado de archivos
    ##
    ################################################################################

    def cargar_datos(self):
        filename, _ = qtw.QFileDialog.getOpenFileName(self, "Seleccionar archivo", "", "Todos los archivos (*)")
        if filename:
            self.config_manager.load_from_json(filename)

    def guardar_datos(self):
        folder_name = self.config_manager.config_structure["HEADER"].get("le_titulosimu", None)
        if folder_name:
            base_dir = os.path.dirname(os.path.realpath(__file__))
            folder_path = os.path.join(base_dir, "Resultados", folder_name)
            if not os.path.exists(folder_path):
                try:
                    os.makedirs(folder_path)
                except OSError as e:
                    qtw.QMessageBox.critical(
                        self,
                        "Error al guardar configuración",
                        f"No se pudo crear la carpeta '{folder_path}': {e}",
                    )
                    return False
        else:
            qtw.QMessageBox.critical(
                self,
                "Error al guardar configuración",
                "No se indicó el nombre de la simulación",
            )
            return False
        json_path = os.path.join(folder_path, "datos.json")
        self.config_manager.save_to_json(json_path)
        qtw.QMessageBox.information(
            self,
            "Guardar Cambios",
            f"La configuración se ha guardado correctamente en '{json_path}'.",
        )
        return folder_path

    def generar_rutina_fortran(self):
        folder_path = self.guardar_datos()
        if folder_path:
            serializer = F90Serializer()
            f90_content = serializer.generate_f90(self.config_manager.config_structure)
            f90_path = os.path.join(folder_path, "datos.f90")
            with open(f90_path, "w", encoding="utf-8") as f:
                f.write(f90_content)
            qtw.QMessageBox.information(
                self,
                "Guardar Cambios",
                f"La rutina ADAPT se ha guardado correctamente en '{f90_path}'.",
            )
            return folder_path
        else:
            return False, False

    def generar_y_visualizar_resultados(self):
        folder_path = self.generar_rutina_fortran()
        if folder_path:

            # Compilando y ejecutando
            base_dir = os.path.dirname(os.path.realpath(__file__))
            exe_path = os.path.join(folder_path, "resultados.exe").replace("\\", "/")
            # Verificando si estan ubicados los archivos f90
            prodic3d_path = os.path.join(base_dir, "prodic3d.f90")
            common_path = os.path.join(base_dir, "3dcommon.f90")
            if not os.path.exists(os.path.join(folder_path, "prodic3d.f90")):
                shutil.copy(prodic3d_path, folder_path)
            if not os.path.exists(os.path.join(folder_path, "3dcommon.f90")):
                shutil.copy(common_path, folder_path)
            compile_command = "gfortran -o resultados.exe prodic3d.f90 datos.f90"
            subprocess.run(compile_command, check=True, shell=True, cwd=folder_path)
            subprocess.run(str(exe_path), check=False, shell=True, cwd=folder_path)

            # Buscando ubicación de Paraview
            try:
                with open("user_config.json", "r", encoding="utf-8") as f:
                    config = json.load(f)
                paraview_path = config.get("ruta_paraview")
                if not paraview_path:
                    raise ValueError("La ruta de ParaView no está definida en la configuración.")
            except FileNotFoundError:
                qtw.QMessageBox.critical(None, "Error de Configuración", "El archivo de configuración no se encuentra.")
                return False
            except json.JSONDecodeError:
                qtw.QMessageBox.critical(
                    None, "Error de Configuración", "Error en el formato del archivo de configuración."
                )
                return False
            except Exception as e:
                qtw.QMessageBox.critical(None, "Error de Configuración", str(e))
                return False

            # Buscando ubicacion de archivo grafico
            script_path = os.path.join(base_dir, "tecplot.py")
            search_pattern = os.path.join(folder_path, "*.000")
            tecplot_files = glob.glob(search_pattern)
            if tecplot_files:
                tecplot_path = os.path.join(folder_path, tecplot_files[0])
            else:
                qtw.QMessageBox.critical(
                    self,
                    "Error al abrir Archivo Gráfico",
                    "No se encontro el archivo de salida gráfica de la simulación",
                )
                return False
            os.environ["TECPLOT_FILE_PATH"] = tecplot_path
            subprocess.run([paraview_path, "--script=" + script_path], check=True)
            del os.environ["TECPLOT_FILE_PATH"]
            return True
        else:
            return False


if __name__ == "__main__":
    app = qtw.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
