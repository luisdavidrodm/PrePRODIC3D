import glob
import sys
import os
import subprocess

import shutil
import configparser

from PySide2 import QtWidgets as qtw
from PySide2 import QtCore as qtc
from PySide2.QtGui import QIcon

from main_window.ui.main_window_ui import Ui_main_window
from inicio_window.inicio_window import InicioWindow
from malla_window.malla_window import MallaWindow
from variables_window.variables_window import VariablesWindow
from values_window.values_window import ValuesWindow
from bordes_window.bordes_window import BordesWindow
from densidad_window.densidad_window import DensidadWindow
from salida_window.salida_window import SalidaWindow
from settings_window.settings_window import SettingsWindow

from config_manager import ConfigManager
from f90_translator import F90Translator


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
        self.densidad_window = None
        self.salida_window = None

    def setupUi(self, *args):
        super().setupUi(self, *args)
        self.action_load_data.triggered.connect(self.load_data)
        self.action_save_data.triggered.connect(self.save_data)
        self.action_generate_fortran_file.triggered.connect(self.generate_fortran_file)
        self.action_generate_and_view_results.triggered.connect(self.generate_and_view_results)
        self.action_generate_and_view_results_from_f90.triggered.connect(self.generate_and_view_results_from_f90)
        self.action_view_results_from_tecplot.triggered.connect(self.view_results_from_tecplot)
        self.action_manual.triggered.connect(self.open_manual)
        self.action_settings.triggered.connect(self.open_config_window)
        self.action_about.triggered.connect(self.show_about_dialog)
        self.action_exit.triggered.connect(self.close)

        self.pb_inicio.clicked.connect(self.open_inicio)
        self.pb_malla.clicked.connect(self.open_malla)
        self.pb_variables.clicked.connect(self.open_variables)
        self.pb_valores.clicked.connect(self.open_valores)
        self.pb_bordes.clicked.connect(self.open_bordes)
        self.pb_densidad.clicked.connect(self.open_densidad)
        self.pb_salida.clicked.connect(self.open_salida)

    ################################################################################
    ##
    ## Funciones para abrir ventanas
    ##
    ################################################################################

    def close_open_windows(self):
        if self.inicio_window and self.inicio_window.isVisible():
            self.inicio_window.close()
        if self.malla_window and self.malla_window.isVisible():
            self.malla_window.close()
        if self.variables_window and self.variables_window.isVisible():
            self.variables_window.close()
        if self.valores_window and self.valores_window.isVisible():
            self.valores_window.close()
        if self.bordes_window and self.bordes_window.isVisible():
            self.bordes_window.close()
        if self.densidad_window and self.densidad_window.isVisible():
            self.densidad_window.close()
        if self.salida_window and self.salida_window.isVisible():
            self.salida_window.close()

    def open_inicio(self):
        self.close_open_windows()
        if self.inicio_window is None or not self.inicio_window.isVisible():
            self.inicio_window = InicioWindow(self.config_manager)
            self.inicio_window.show()
        else:
            self.inicio_window.raise_()
            self.inicio_window.activateWindow()

    def open_malla(self):
        self.close_open_windows()
        if self.malla_window is None or not self.malla_window.isVisible():
            self.malla_window = MallaWindow(self.config_manager)
            self.malla_window.show()
        else:
            self.malla_window.raise_()
            self.malla_window.activateWindow()

    def open_variables(self):
        self.close_open_windows()
        if self.variables_window is None or not self.variables_window.isVisible():
            self.variables_window = VariablesWindow(self.config_manager)
            self.variables_window.show()
        else:
            self.variables_window.raise_()
            self.variables_window.activateWindow()

    def open_valores(self):
        self.close_open_windows()
        if self.valores_window is None or not self.valores_window.isVisible():
            self.valores_window = ValuesWindow(self.config_manager)
            self.valores_window.show()
        else:
            self.valores_window.raise_()
            self.valores_window.activateWindow()

    def open_bordes(self):
        self.close_open_windows()
        if self.bordes_window is None or not self.bordes_window.isVisible():
            self.bordes_window = BordesWindow(self.config_manager)
            self.bordes_window.show()
        else:
            self.bordes_window.raise_()
            self.bordes_window.activateWindow()

    def open_densidad(self):
        self.close_open_windows()
        if self.densidad_window is None or not self.densidad_window.isVisible():
            self.densidad_window = DensidadWindow(self.config_manager)
            self.densidad_window.show()
        else:
            self.densidad_window.raise_()
            self.densidad_window.activateWindow()

    def open_salida(self):
        self.close_open_windows()
        if self.salida_window is None or not self.salida_window.isVisible():
            self.salida_window = SalidaWindow(self.config_manager)
            self.salida_window.show()
        else:
            self.salida_window.raise_()
            self.salida_window.activateWindow()

    def open_config_window(self):
        config_window = SettingsWindow()
        config_window.exec_()

    def open_manual(self):
        try:
            current_dir = os.getcwd()
            manual_path = os.path.join(current_dir, "resources", "manual.pdf")
            if os.path.exists(manual_path):
                subprocess.run(["start", manual_path], shell=True, check=True)
            else:
                qtw.QMessageBox.warning(self, "Error", "El archivo manual.pdf no se encuentra en la ruta especificada.")
        except subprocess.CalledProcessError as e:
            qtw.QMessageBox.warning(self, "Error", f"Error al abrir el archivo manual.pdf: {e}")
        except Exception as e:
            qtw.QMessageBox.warning(self, "Error", str(e))

    def show_about_dialog(self):
        about_dialog = AboutDialog()
        about_dialog.exec_()

    ################################################################################
    ##
    ## Guardado de archivos
    ##
    ################################################################################

    def load_data(self):
        current_dir = os.getcwd()
        results_dir = os.path.join(current_dir, "RESULTADOS")
        if not os.path.exists(results_dir):
            os.makedirs(results_dir)
        filename, _ = qtw.QFileDialog.getOpenFileName(
            self, "Seleccionar archivo de datos para cargar...", results_dir, "Archivos JSON (*.json)"
        )
        if filename:
            self.config_manager.load_from_json(filename)

    def save_data(self):
        folder_name = self.config_manager.header.get("le_titulosimu", None)
        if folder_name:
            base_path = (
                os.path.dirname(sys.executable)
                if getattr(sys, "frozen", False)
                else os.path.dirname(os.path.abspath(__file__))
            )
            folder_path = os.path.join(base_path, "RESULTADOS", folder_name)
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

    def generate_fortran_file(self):
        folder_path = self.save_data()
        if folder_path:
            translator = F90Translator(self.config_manager)
            try:
                f90_content = translator.generate_f90()
            except Exception as e:
                qtw.QMessageBox.critical(
                    self,
                    "Error al guardar configuración",
                    f"No se pudo generar el archivo adapt.f90 en '{folder_path}': {e}",
                )
                return False
            f90_path = os.path.join(folder_path, "adapt.f90")
            with open(f90_path, "w", encoding="utf-8") as f:
                f.write(f90_content)
            qtw.QMessageBox.information(
                self,
                "Guardar Cambios",
                f"La rutina ADAPT se ha guardado correctamente en '{f90_path}'.",
            )
            return folder_path
        else:
            return False

    def generate_and_view_results(self):
        folder_path = self.generate_fortran_file()
        if folder_path:
            base_dir = os.path.dirname(os.path.realpath(__file__))
            gfortran_path = self.load_gfortran_and_check()
            paraview_path = self.load_paraview_config()
            script_path = os.path.join(base_dir, "tecplot.py")
            self.run_worker(folder_path, base_dir, gfortran_path, paraview_path, script_path)

    def generate_and_view_results_from_f90(self):
        current_dir = os.getcwd()
        results_dir = os.path.join(current_dir, "RESULTADOS")
        if not os.path.exists(results_dir):
            os.makedirs(results_dir)
        adapt_file, _ = qtw.QFileDialog.getOpenFileName(
            self, "Seleccionar archivo Fortran (.f90) para cargar...", results_dir, "Archivos Fortran (*.f90)"
        )
        if adapt_file:
            folder_path = os.path.dirname(adapt_file)
            base_dir = os.path.dirname(os.path.realpath(__file__))
            gfortran_path = self.load_gfortran_and_check()
            paraview_path = self.load_paraview_config()
            script_path = os.path.join(base_dir, "tecplot.py")
            self.run_worker(folder_path, base_dir, gfortran_path, paraview_path, script_path, adapt_file=adapt_file)

    def view_results_from_tecplot(self):
        current_dir = os.getcwd()
        results_dir = os.path.join(current_dir, "RESULTADOS")
        if not os.path.exists(results_dir):
            os.makedirs(results_dir)
        tecplot_file, _ = qtw.QFileDialog.getOpenFileName(
            self, "Seleccionar archivo Tecplot para cargar...", results_dir, "Todos los archivos (*)"
        )
        if tecplot_file:
            folder_path = os.path.dirname(tecplot_file)
            base_dir = os.path.dirname(os.path.realpath(__file__))
            paraview_path = self.load_paraview_config()
            if paraview_path:
                script_path = os.path.join(base_dir, "tecplot.py")
                self.run_worker(folder_path, base_dir, None, paraview_path, script_path, tecplot_file=tecplot_file)

    def load_paraview_config(self):
        try:
            base_path = (
                os.path.dirname(sys.executable)
                if getattr(sys, "frozen", False)
                else os.path.dirname(os.path.abspath(__file__))
            )
            config_path = os.path.join(base_path, "CONFIGURACION.conf")
            config = configparser.ConfigParser()
            config.read(config_path, encoding="utf-8")
            if "Rutas" not in config or "ruta_paraview" not in config["Rutas"]:
                qtw.QMessageBox.warning(
                    self,
                    "Advertencia de Configuración de paraview.exe",
                    "La ruta de ParaView no está definida en la configuración.",
                )
                return None
            paraview_path = config["Rutas"]["ruta_paraview"]
            if paraview_path == "NO":
                return None
            if not os.path.exists(paraview_path):
                qtw.QMessageBox.warning(
                    self,
                    "Advertencia de Configuración de paraview.exe",
                    f"La ruta especificada no existe: {paraview_path}",
                )
                return None
            if not os.path.isfile(paraview_path):
                qtw.QMessageBox.warning(
                    self,
                    "Advertencia de Configuración de paraview.exe",
                    f"No se encontró paraview.exe en la ruta especificada: {paraview_path}",
                )
                return None
            return paraview_path
        except FileNotFoundError:
            qtw.QMessageBox.warning(
                self, "Advertencia de Configuración de paraview.exe", "El archivo de configuración no se encuentra."
            )
        except configparser.Error:
            qtw.QMessageBox.warning(
                self,
                "Advertencia de Configuración de paraview.exe",
                "Error en el formato del archivo de configuración.",
            )
        except Exception as e:
            qtw.QMessageBox.warning(self, "Advertencia de Configuración de paraview.exe", str(e))

        return None

    def load_gfortran_config(self):
        try:
            base_path = (
                os.path.dirname(sys.executable)
                if getattr(sys, "frozen", False)
                else os.path.dirname(os.path.abspath(__file__))
            )
            config_path = os.path.join(base_path, "CONFIGURACION.conf")
            config = configparser.ConfigParser()
            config.read(config_path, encoding="utf-8")
            if "Rutas" not in config or "ruta_gfortran" not in config["Rutas"]:
                qtw.QMessageBox.warning(
                    self,
                    "Advertencia de Configuración de gfortran.exe",
                    "La ruta de gfortran.exe no está definida en la configuración.",
                )
                return None
            gfortran_path = config["Rutas"]["ruta_gfortran"]
            if gfortran_path == "NO":
                return gfortran_path
            if not os.path.exists(gfortran_path):
                qtw.QMessageBox.warning(
                    self,
                    "Advertencia de Configuración de gfortran.exe",
                    f"La ruta especificada en la configuración para gfortran.exe no existe: {gfortran_path}",
                )
                return None
            if not os.path.isfile(gfortran_path):
                qtw.QMessageBox.warning(
                    self,
                    "Advertencia de Configuración de gfortran.exe",
                    f"No se encontró gfortran.exe en la ruta especificada en la configuración: {gfortran_path}",
                )
                return None
            return gfortran_path
        except FileNotFoundError:
            qtw.QMessageBox.warning(
                self, "Advertencia de Configuración de gfortran.exe", "El archivo de configuración no se encuentra."
            )
        except configparser.Error:
            qtw.QMessageBox.warning(
                self,
                "Advertencia de Configuración de gfortran.exe",
                "Error en el formato del archivo de configuración.",
            )
        except Exception as e:
            qtw.QMessageBox.warning(self, "Advertencia de Configuración de gfortran.exe", str(e))
        return None

    def is_gfortran_available(self):
        try:
            result = subprocess.run(
                ["gfortran", "--version"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True
            )
            if result.returncode == 0:
                return True
            else:
                qtw.QMessageBox.warning(
                    self,
                    "Advertencia de Configuración de gfortran.exe",
                    "gfortran no está disponible en el PATH del sistema.",
                )
                return False
        except FileNotFoundError:
            qtw.QMessageBox.warning(
                self,
                "Advertencia de Configuración de gfortran.exe",
                "gfortran no está disponible en el PATH del sistema.",
            )
            return False
        except Exception as e:
            qtw.QMessageBox.warning(self, "Advertencia de Configuración de gfortran.exe", str(e))
            return False

    def load_gfortran_and_check(self):
        gfortran_path = self.load_gfortran_config()
        if not gfortran_path:
            if self.is_gfortran_available():
                return "gfortran"
            else:
                qtw.QMessageBox.warning(
                    self,
                    "Advertencia de Configuración de gfortran.exe",
                    "gfortran no está disponible en la ruta especificada en la configuración ni en el PATH del sistema.",
                )
                return None
        elif gfortran_path == "NO":
            return None
        return gfortran_path

    def run_worker(
        self,
        folder_path,
        base_dir,
        gfortran_path,
        paraview_path,
        script_path,
        adapt_file="adapt.f90",
        tecplot_file=None,
    ):
        terminal_dialog = TerminalOutputDialog(self)
        title = self.config_manager.header.get("le_titulosimu", None)
        terminal_dialog.setWindowTitle(f"Resultados de Simulación: {title}")

        worker = Worker(folder_path, base_dir, gfortran_path, paraview_path, script_path, adapt_file, tecplot_file)
        worker.error.connect(lambda msg: qtw.QMessageBox.critical(self, "Error", msg))
        worker.finished.connect(terminal_dialog.enable_close_button)
        worker.output.connect(terminal_dialog.append_text)

        worker.start()
        terminal_dialog.exec_()


class Worker(qtc.QThread):
    error = qtc.Signal(str)
    finished = qtc.Signal()
    output = qtc.Signal(str)

    def __init__(
        self,
        folder_path,
        base_dir,
        gfortran_path,
        paraview_path,
        script_path,
        adapt_file="adapt.f90",
        tecplot_file=None,
    ):
        super().__init__()
        self.folder_path = folder_path
        self.base_dir = base_dir
        self.gfortran_path = gfortran_path
        self.paraview_path = paraview_path
        self.script_path = script_path
        self.tecplot_file = tecplot_file
        if adapt_file == "adapt.f90":
            self.adapt_file = os.path.join(self.folder_path, adapt_file).replace("\\", "/")

    def run(self):
        try:
            if not self.tecplot_file:
                self.output.emit("Copiando archivos f90 si no existen...\n")
                exe_path = os.path.join(self.folder_path, "ejecutable.exe").replace("\\", "/")
                base_path = (
                    os.path.dirname(sys.executable)
                    if getattr(sys, "frozen", False)
                    else os.path.dirname(os.path.abspath(__file__))
                )
                prodic3d_path = os.path.join(base_path, "prodic3d.f90")
                common_path = os.path.join(base_path, "3dcommon.f90")
                if not os.path.exists(os.path.join(self.folder_path, "prodic3d.f90")):
                    shutil.copy(prodic3d_path, self.folder_path)
                if not os.path.exists(os.path.join(self.folder_path, "3dcommon.f90")):
                    shutil.copy(common_path, self.folder_path)
                if self.gfortran_path is not None:
                    self.output.emit("Compilando y ejecutando...\n")
                    cwd_prodic3d = os.path.join(self.folder_path, "prodic3d.f90").replace("\\", "/")
                    gfortran_directory = os.path.dirname(self.gfortran_path)
                    compile_command = f'gfortran -o "{exe_path}" "{cwd_prodic3d}" "{self.adapt_file}"'
                    self.output.emit(f"Carpeta de destino: {self.folder_path}")
                    rc = self.add_to_path_and_run(compile_command, gfortran_directory, self.folder_path)
                    if rc != 0:
                        self.output.emit(f"Errores durante la compilación. Código de retorno: {rc}")
                        return
                    rc = self.add_to_path_and_run(str(exe_path), gfortran_directory, self.folder_path)
                    if rc != 0:
                        self.output.emit(f"Errores durante la ejecución. Código de retorno: {rc}")
                    self.output.emit("Buscando archivo gráfico...\n")
                    search_pattern = os.path.join(self.folder_path, "*.000")
                    tecplot_files = glob.glob(search_pattern)
                    if not tecplot_files:
                        self.error.emit("No se encontró el archivo de salida gráfica de la simulación")
                        self.output.emit("Proceso finalizado.\n")
                        self.finished.emit()
                        return
                    self.tecplot_file = tecplot_files[0]
                    self.output.emit(
                        f"Los resultados numéricos se guardaron en el archivo PRINTF en {self.folder_path}\n"
                    )
                    self.output.emit(
                        f"Los resultados gráficos se guardaron en los archivos PLOTF en {self.folder_path}\n"
                    )
                else:
                    self.output.emit("Saltando la compilación porque gfortran.exe no está disponible...\n")
                    self.output.emit("Proceso finalizado.\n")
                    self.finished.emit()
                    return
            if self.paraview_path is not None:
                tecplot_path = os.path.join(self.folder_path, self.tecplot_file)
                os.environ["PREPRODIC3D_TECPLOT_FILE_PATH"] = tecplot_path
                self.output.emit("Ejecutando ParaView...\n")
                paraview_command = f'"{self.paraview_path}" --script="{self.script_path}"'
                self.run_command(paraview_command, wait=False)
                del os.environ["PREPRODIC3D_TECPLOT_FILE_PATH"]
                self.output.emit("Proceso finalizado.\n")
                self.finished.emit()
            else:
                self.output.emit("Saltando la visualización porque paraview.exe no está disponible...\n")
                self.output.emit("Proceso finalizado.\n")
                self.finished.emit()
        except Exception as e:
            self.error.emit(f"Error: {str(e)}")

    def run_command(self, command, cwd=None, env=None, wait=True):
        process = subprocess.Popen(
            command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True, cwd=cwd, env=env
        )
        if wait:
            while True:
                output = process.stdout.readline().decode()
                if output == "" and process.poll() is not None:
                    break
                if output:
                    # if output.strip():
                    #     output = output.rstrip("\r\n")
                    self.output.emit(output)
            stderr = process.stderr.read().decode()
            if stderr:
                # if stderr.strip():
                #     stderr = stderr.rstrip("\r\n")
                self.output.emit(stderr)
            rc = process.poll()
            return rc
        else:
            return None

    def add_to_path_and_run(self, command, additional_path, cwd=None, wait=True):
        env = os.environ.copy()
        env["PATH"] = additional_path + os.pathsep + env["PATH"]
        return self.run_command(command, cwd, env, wait)


class TerminalOutputDialog(qtw.QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Resultados")
        self.resize(800, 600)

        layout = qtw.QVBoxLayout(self)

        self.output_text_edit = qtw.QPlainTextEdit(self)
        self.output_text_edit.setReadOnly(True)
        layout.addWidget(self.output_text_edit)

        self.close_button = qtw.QPushButton("Cerrar", self)
        self.close_button.setEnabled(False)
        layout.addWidget(self.close_button)

        self.close_button.clicked.connect(self.accept)

    def append_text(self, text):
        # if text.strip():
        #     text = text.rstrip("\r\n")
        self.output_text_edit.appendPlainText(text)

    def enable_close_button(self):
        self.close_button.setEnabled(True)


class AboutDialog(qtw.QDialog):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Acerca de")
        self.setFixedSize(265, 345)
        icon = QIcon()
        icon.addFile(":/icon/icon/prodic_icon.png", qtc.QSize(), QIcon.Normal, QIcon.Off)
        self.setWindowIcon(icon)
        layout = qtw.QVBoxLayout()
        layout.setContentsMargins(2, 2, 2, 2)
        layout.setSpacing(2)
        about_text = (
            "<div style='text-align: center;'>"
            "<h2>PrePRODIC3D</h2>"
            "<p><b>Universidad del Zulia</b><br>"
            "Facultad de Ingeniería<br>"
            "Escuela de Ingeniería Mecánica<br>"
            "Departamento de Energía</p>"
            "<hr style='border: 1px solid #000;'>"
            "<p><b>Realizado por:</b></p>"
            "<p><b>Br. Luis David Rodríguez Muñoz</b><br>"
            "<b>Br. Diego Jesús Rojas Becerra</b></p>"
            "<hr style='border: 1px solid #000;'>"
            "<p><b>Maracaibo, Julio de 2024</b></p>"
            "<p><b>Versión: 1.0.0</b></p>"
            "<hr style='border: 1px solid #000;'>"
            "<p><a href='https://github.com/luisdavidrodm/PrePRODIC3D'>https://github.com/luisdavidrodm/PrePRODIC3D</a></p>"
            "</div>"
        )
        about_label = qtw.QLabel(about_text)
        about_label.setTextFormat(qtc.Qt.RichText)
        about_label.setAlignment(qtc.Qt.AlignCenter)
        about_label.setOpenExternalLinks(True)
        layout.addWidget(about_label)
        button_box = qtw.QDialogButtonBox(qtw.QDialogButtonBox.Ok)
        button_box.accepted.connect(self.accept)
        layout.addWidget(button_box)
        self.setLayout(layout)


def show_about_dialog(self):
    about_dialog = AboutDialog()
    about_dialog.exec_()


if __name__ == "__main__":
    app = qtw.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
