# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_windownwBeaf.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_main_window(object):
    def setupUi(self, main_window):
        if not main_window.objectName():
            main_window.setObjectName(u"main_window")
        main_window.resize(301, 265)
        self.action_save_data = QAction(main_window)
        self.action_save_data.setObjectName(u"action_save_data")
        self.action_save_data.setCheckable(False)
        self.action_save_data.setChecked(False)
        self.action_exit = QAction(main_window)
        self.action_exit.setObjectName(u"action_exit")
        self.action_manual = QAction(main_window)
        self.action_manual.setObjectName(u"action_manual")
        self.action_generate_fortran_file = QAction(main_window)
        self.action_generate_fortran_file.setObjectName(u"action_generate_fortran_file")
        self.action_generate_and_view_results = QAction(main_window)
        self.action_generate_and_view_results.setObjectName(u"action_generate_and_view_results")
        self.action_load_data = QAction(main_window)
        self.action_load_data.setObjectName(u"action_load_data")
        self.action_generate_and_view_results_from_f90 = QAction(main_window)
        self.action_generate_and_view_results_from_f90.setObjectName(u"action_generate_and_view_results_from_f90")
        self.action_view_results_from_tecplot = QAction(main_window)
        self.action_view_results_from_tecplot.setObjectName(u"action_view_results_from_tecplot")
        self.action_about = QAction(main_window)
        self.action_about.setObjectName(u"action_about")
        self.action_settings = QAction(main_window)
        self.action_settings.setObjectName(u"action_settings")
        self.centralwidget = QWidget(main_window)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.pb_inicio = QPushButton(self.centralwidget)
        self.pb_inicio.setObjectName(u"pb_inicio")

        self.verticalLayout.addWidget(self.pb_inicio)

        self.pb_malla = QPushButton(self.centralwidget)
        self.pb_malla.setObjectName(u"pb_malla")

        self.verticalLayout.addWidget(self.pb_malla)

        self.pb_variables = QPushButton(self.centralwidget)
        self.pb_variables.setObjectName(u"pb_variables")

        self.verticalLayout.addWidget(self.pb_variables)

        self.pb_valores = QPushButton(self.centralwidget)
        self.pb_valores.setObjectName(u"pb_valores")

        self.verticalLayout.addWidget(self.pb_valores)

        self.pb_bordes = QPushButton(self.centralwidget)
        self.pb_bordes.setObjectName(u"pb_bordes")

        self.verticalLayout.addWidget(self.pb_bordes)

        self.pb_densidad = QPushButton(self.centralwidget)
        self.pb_densidad.setObjectName(u"pb_densidad")

        self.verticalLayout.addWidget(self.pb_densidad)

        self.pb_salida = QPushButton(self.centralwidget)
        self.pb_salida.setObjectName(u"pb_salida")

        self.verticalLayout.addWidget(self.pb_salida)

        main_window.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(main_window)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 301, 21))
        self.menu_archivo = QMenu(self.menubar)
        self.menu_archivo.setObjectName(u"menu_archivo")
        self.menu_herramientas = QMenu(self.menubar)
        self.menu_herramientas.setObjectName(u"menu_herramientas")
        main_window.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(main_window)
        self.statusbar.setObjectName(u"statusbar")
        main_window.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menu_archivo.menuAction())
        self.menubar.addAction(self.menu_herramientas.menuAction())
        self.menu_archivo.addAction(self.action_load_data)
        self.menu_archivo.addAction(self.action_save_data)
        self.menu_archivo.addAction(self.action_generate_fortran_file)
        self.menu_archivo.addAction(self.action_generate_and_view_results)
        self.menu_archivo.addAction(self.action_generate_and_view_results_from_f90)
        self.menu_archivo.addAction(self.action_view_results_from_tecplot)
        self.menu_archivo.addAction(self.action_exit)
        self.menu_herramientas.addAction(self.action_manual)
        self.menu_herramientas.addAction(self.action_settings)
        self.menu_herramientas.addAction(self.action_about)

        self.retranslateUi(main_window)

        QMetaObject.connectSlotsByName(main_window)
    # setupUi

    def retranslateUi(self, main_window):
        main_window.setWindowTitle(QCoreApplication.translate("main_window", u"PrePRODIC3D", None))
        self.action_save_data.setText(QCoreApplication.translate("main_window", u"Guardar datos", None))
        self.action_exit.setText(QCoreApplication.translate("main_window", u"Salir", None))
        self.action_manual.setText(QCoreApplication.translate("main_window", u"Manual de usuario", None))
        self.action_generate_fortran_file.setText(QCoreApplication.translate("main_window", u"Generar archivo Fortran", None))
        self.action_generate_and_view_results.setText(QCoreApplication.translate("main_window", u"Generar y visualizar resultados", None))
        self.action_load_data.setText(QCoreApplication.translate("main_window", u"Cargar datos", None))
        self.action_generate_and_view_results_from_f90.setText(QCoreApplication.translate("main_window", u"Generar y visualizar resultados a partir de archivo Fortran", None))
        self.action_view_results_from_tecplot.setText(QCoreApplication.translate("main_window", u"Visualizar resultados a partir de archivo Tecplot", None))
        self.action_about.setText(QCoreApplication.translate("main_window", u"Acerca de", None))
        self.action_settings.setText(QCoreApplication.translate("main_window", u"Configuraci\u00f3n", None))
        self.pb_inicio.setText(QCoreApplication.translate("main_window", u"Inicio", None))
        self.pb_malla.setText(QCoreApplication.translate("main_window", u"Malla", None))
        self.pb_variables.setText(QCoreApplication.translate("main_window", u"Variables", None))
        self.pb_valores.setText(QCoreApplication.translate("main_window", u"Valores", None))
        self.pb_bordes.setText(QCoreApplication.translate("main_window", u"Bordes", None))
        self.pb_densidad.setText(QCoreApplication.translate("main_window", u"Densidad", None))
        self.pb_salida.setText(QCoreApplication.translate("main_window", u"Salida", None))
        self.menu_archivo.setTitle(QCoreApplication.translate("main_window", u"Archivo", None))
        self.menu_herramientas.setTitle(QCoreApplication.translate("main_window", u"Herramientas", None))
    # retranslateUi

