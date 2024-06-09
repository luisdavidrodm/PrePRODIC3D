# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (
    QCoreApplication,
    QDate,
    QDateTime,
    QLocale,
    QMetaObject,
    QObject,
    QPoint,
    QRect,
    QSize,
    QTime,
    QUrl,
    Qt,
)
from PySide6.QtGui import (
    QAction,
    QBrush,
    QColor,
    QConicalGradient,
    QCursor,
    QFont,
    QFontDatabase,
    QGradient,
    QIcon,
    QImage,
    QKeySequence,
    QLinearGradient,
    QPainter,
    QPalette,
    QPixmap,
    QRadialGradient,
    QTransform,
)
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QMenu,
    QMenuBar,
    QPushButton,
    QSizePolicy,
    QStatusBar,
    QVBoxLayout,
    QWidget,
)
from Recursos import recursos_rc


class Ui_main_window(object):
    def setupUi(self, main_window):
        if not main_window.objectName():
            main_window.setObjectName("main_window")
        main_window.resize(301, 265)
        main_window.setContextMenuPolicy(Qt.NoContextMenu)
        icon = QIcon()
        icon.addFile(":/Icon/icon/prodic_icon.jpg", QSize(), QIcon.Normal, QIcon.Off)
        main_window.setWindowIcon(icon)
        self.action_guardar_datos = QAction(main_window)
        self.action_guardar_datos.setObjectName("action_guardar_datos")
        self.action_guardar_datos.setCheckable(False)
        self.action_guardar_datos.setChecked(False)
        self.action_salir = QAction(main_window)
        self.action_salir.setObjectName("action_salir")
        self.action_manual = QAction(main_window)
        self.action_manual.setObjectName("action_manual")
        self.action_generar_rutina_fortran = QAction(main_window)
        self.action_generar_rutina_fortran.setObjectName("action_generar_rutina_fortran")
        self.action_generar_y_visualizar_resultados = QAction(main_window)
        self.action_generar_y_visualizar_resultados.setObjectName("action_generar_y_visualizar_resultados")
        self.action_cargar_datos = QAction(main_window)
        self.action_cargar_datos.setObjectName("action_cargar_datos")
        self.centralwidget = QWidget(main_window)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pb_inicio = QPushButton(self.centralwidget)
        self.pb_inicio.setObjectName("pb_inicio")

        self.verticalLayout.addWidget(self.pb_inicio)

        self.pb_malla = QPushButton(self.centralwidget)
        self.pb_malla.setObjectName("pb_malla")

        self.verticalLayout.addWidget(self.pb_malla)

        self.pb_variables = QPushButton(self.centralwidget)
        self.pb_variables.setObjectName("pb_variables")

        self.verticalLayout.addWidget(self.pb_variables)

        self.pb_valores = QPushButton(self.centralwidget)
        self.pb_valores.setObjectName("pb_valores")

        self.verticalLayout.addWidget(self.pb_valores)

        self.pb_bordes = QPushButton(self.centralwidget)
        self.pb_bordes.setObjectName("pb_bordes")

        self.verticalLayout.addWidget(self.pb_bordes)

        self.pb_densidad = QPushButton(self.centralwidget)
        self.pb_densidad.setObjectName("pb_densidad")

        self.verticalLayout.addWidget(self.pb_densidad)

        self.pb_salida = QPushButton(self.centralwidget)
        self.pb_salida.setObjectName("pb_salida")

        self.verticalLayout.addWidget(self.pb_salida)

        main_window.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(main_window)
        self.menubar.setObjectName("menubar")
        self.menubar.setGeometry(QRect(0, 0, 301, 22))
        self.menu_archivo = QMenu(self.menubar)
        self.menu_archivo.setObjectName("menu_archivo")
        self.menu_herramientas = QMenu(self.menubar)
        self.menu_herramientas.setObjectName("menu_herramientas")
        main_window.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(main_window)
        self.statusbar.setObjectName("statusbar")
        main_window.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menu_archivo.menuAction())
        self.menubar.addAction(self.menu_herramientas.menuAction())
        self.menu_archivo.addAction(self.action_guardar_datos)
        self.menu_archivo.addAction(self.action_cargar_datos)
        self.menu_archivo.addAction(self.action_generar_rutina_fortran)
        self.menu_archivo.addAction(self.action_generar_y_visualizar_resultados)
        self.menu_archivo.addAction(self.action_salir)
        self.menu_herramientas.addAction(self.action_manual)

        self.retranslateUi(main_window)

        QMetaObject.connectSlotsByName(main_window)

    # setupUi

    def retranslateUi(self, main_window):
        main_window.setWindowTitle(QCoreApplication.translate("main_window", "PrePRODIC3D", None))
        self.action_guardar_datos.setText(QCoreApplication.translate("main_window", "Guardar datos", None))
        self.action_salir.setText(QCoreApplication.translate("main_window", "Salir", None))
        self.action_manual.setText(QCoreApplication.translate("main_window", "Manual de usuario", None))
        self.action_generar_rutina_fortran.setText(
            QCoreApplication.translate("main_window", "Generar rutina FORTRAN", None)
        )
        self.action_generar_y_visualizar_resultados.setText(
            QCoreApplication.translate("main_window", "Generar y visualiza resultados", None)
        )
        self.action_cargar_datos.setText(QCoreApplication.translate("main_window", "Cargar datos", None))
        self.pb_inicio.setText(QCoreApplication.translate("main_window", "Inicio", None))
        self.pb_malla.setText(QCoreApplication.translate("main_window", "Malla", None))
        self.pb_variables.setText(QCoreApplication.translate("main_window", "Variables", None))
        self.pb_valores.setText(QCoreApplication.translate("main_window", "Valores", None))
        self.pb_bordes.setText(QCoreApplication.translate("main_window", "Bordes", None))
        self.pb_densidad.setText(QCoreApplication.translate("main_window", "Densidad", None))
        self.pb_salida.setText(QCoreApplication.translate("main_window", "Salida", None))
        self.menu_archivo.setTitle(QCoreApplication.translate("main_window", "Archivo", None))
        self.menu_herramientas.setTitle(QCoreApplication.translate("main_window", "Herramientas", None))

    # retranslateUi
