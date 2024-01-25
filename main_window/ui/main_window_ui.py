# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QMainWindow, QMenu, QMenuBar,
    QPushButton, QSizePolicy, QSpacerItem, QStatusBar,
    QVBoxLayout, QWidget)

class Ui_main_window(object):
    def setupUi(self, main_window):
        if not main_window.objectName():
            main_window.setObjectName(u"main_window")
        main_window.resize(301, 280)
        self.action_guardar = QAction(main_window)
        self.action_guardar.setObjectName(u"action_guardar")
        self.action_salir = QAction(main_window)
        self.action_salir.setObjectName(u"action_salir")
        self.action_manual = QAction(main_window)
        self.action_manual.setObjectName(u"action_manual")
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

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        main_window.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(main_window)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 301, 22))
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
        self.menu_archivo.addAction(self.action_guardar)
        self.menu_archivo.addAction(self.action_salir)
        self.menu_herramientas.addAction(self.action_manual)

        self.retranslateUi(main_window)

        QMetaObject.connectSlotsByName(main_window)
    # setupUi

    def retranslateUi(self, main_window):
        main_window.setWindowTitle(QCoreApplication.translate("main_window", u"PrePRODIC3D", None))
        self.action_guardar.setText(QCoreApplication.translate("main_window", u"Guardar como", None))
        self.action_salir.setText(QCoreApplication.translate("main_window", u"Salir", None))
        self.action_manual.setText(QCoreApplication.translate("main_window", u"Manual de usuario", None))
        self.pb_inicio.setText(QCoreApplication.translate("main_window", u"Inicio", None))
        self.pb_malla.setText(QCoreApplication.translate("main_window", u"Malla", None))
        self.pb_variables.setText(QCoreApplication.translate("main_window", u"Variables", None))
        self.pb_valores.setText(QCoreApplication.translate("main_window", u"Valores", None))
        self.menu_archivo.setTitle(QCoreApplication.translate("main_window", u"Archivo", None))
        self.menu_herramientas.setTitle(QCoreApplication.translate("main_window", u"Herramientas", None))
    # retranslateUi

