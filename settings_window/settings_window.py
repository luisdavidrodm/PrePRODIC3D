import os
import configparser
from PySide2 import QtWidgets
from PySide2.QtGui import QIcon
from PySide2.QtCore import QSize


class SettingsWindow(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Configuración")
        self.resize(500, 200)
        self.center()

        icon = QIcon()
        icon.addFile(":/icon/icon/prodic_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.setWindowIcon(icon)

        layout = QtWidgets.QVBoxLayout()
        layout.setContentsMargins(15, 15, 15, 15)
        layout.setSpacing(10)

        self.paraview_label = QtWidgets.QLabel("Ruta del ejecutable paraview.exe:")
        self.paraview_input = QtWidgets.QLineEdit(self)
        self.paraview_browse_button = QtWidgets.QPushButton("Buscar...", self)
        self.paraview_browse_button.clicked.connect(self.browse_paraview)

        paraview_layout = QtWidgets.QHBoxLayout()
        paraview_layout.addWidget(self.paraview_input)
        paraview_layout.addWidget(self.paraview_browse_button)

        layout.addWidget(self.paraview_label)
        layout.addLayout(paraview_layout)

        self.gfortran_label = QtWidgets.QLabel("Ruta del ejecutable gfortran.exe:")
        self.gfortran_input = QtWidgets.QLineEdit(self)
        self.gfortran_browse_button = QtWidgets.QPushButton("Buscar...", self)
        self.gfortran_browse_button.clicked.connect(self.browse_gfortran)

        gfortran_layout = QtWidgets.QHBoxLayout()
        gfortran_layout.addWidget(self.gfortran_input)
        gfortran_layout.addWidget(self.gfortran_browse_button)

        layout.addWidget(self.gfortran_label)
        layout.addLayout(gfortran_layout)

        self.save_button = QtWidgets.QPushButton("Guardar", self)
        self.save_button.clicked.connect(self.save_config)
        self.cancel_button = QtWidgets.QPushButton("Cancelar", self)
        self.cancel_button.clicked.connect(self.reject)

        button_layout = QtWidgets.QHBoxLayout()
        button_layout.addStretch(1)
        button_layout.addWidget(self.save_button)
        button_layout.addWidget(self.cancel_button)

        layout.addLayout(button_layout)

        self.setLayout(layout)
        self.load_config()

    def center(self):
        screen = QtWidgets.QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move((screen.width() - size.width()) / 2, (screen.height() - size.height()) / 2)

    def browse_paraview(self):
        file_name, _ = QtWidgets.QFileDialog.getOpenFileName(
            self, "Seleccionar paraview.exe", "", "paraview.exe (*.exe)"
        )
        if file_name:
            self.paraview_input.setText(file_name)

    def browse_gfortran(self):
        file_name, _ = QtWidgets.QFileDialog.getOpenFileName(
            self, "Seleccionar gfortran.exe", "", "gfortran.exe (*.exe)"
        )
        if file_name:
            self.gfortran_input.setText(file_name)

    def load_config(self):
        base_path = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
        config_path = os.path.join(base_path, "CONFIGURACION.conf")

        if os.path.exists(config_path):
            config = configparser.ConfigParser()
            config.read(config_path, encoding="utf-8")

            if "Rutas" in config:
                self.paraview_input.setText(config["Rutas"].get("ruta_paraview", ""))
                self.gfortran_input.setText(config["Rutas"].get("ruta_gfortran", ""))

    def save_config(self):
        base_path = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
        config_path = os.path.join(base_path, "CONFIGURACION.conf")

        config = configparser.ConfigParser()
        config.read(config_path, encoding="utf-8")

        if "Rutas" not in config:
            config["Rutas"] = {}

        config["Rutas"]["ruta_paraview"] = self.paraview_input.text()
        config["Rutas"]["ruta_gfortran"] = self.gfortran_input.text()

        with open(config_path, "w", encoding="utf-8") as configfile:
            config.write(configfile)

        QtWidgets.QMessageBox.information(self, "Configuración", "Configuración guardada exitosamente.")
        self.accept()
