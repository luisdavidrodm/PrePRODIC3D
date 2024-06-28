# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'inicio_windowIdOVmC.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_inicio_window(object):
    def setupUi(self, inicio_window):
        if not inicio_window.objectName():
            inicio_window.setObjectName(u"inicio_window")
        inicio_window.resize(402, 317)
        self.verticalLayout_5 = QVBoxLayout(inicio_window)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.gb_inicio = QGroupBox(inicio_window)
        self.gb_inicio.setObjectName(u"gb_inicio")
        self.verticalLayout_4 = QVBoxLayout(self.gb_inicio)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.gb_inicio_titulosimu = QGroupBox(self.gb_inicio)
        self.gb_inicio_titulosimu.setObjectName(u"gb_inicio_titulosimu")
        self.verticalLayout = QVBoxLayout(self.gb_inicio_titulosimu)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.le_titulosimu = QLineEdit(self.gb_inicio_titulosimu)
        self.le_titulosimu.setObjectName(u"le_titulosimu")

        self.verticalLayout.addWidget(self.le_titulosimu)


        self.verticalLayout_4.addWidget(self.gb_inicio_titulosimu)

        self.gb_inicio_tituloimpre = QGroupBox(self.gb_inicio)
        self.gb_inicio_tituloimpre.setObjectName(u"gb_inicio_tituloimpre")
        self.verticalLayout_2 = QVBoxLayout(self.gb_inicio_tituloimpre)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.le_tituloimpre = QLineEdit(self.gb_inicio_tituloimpre)
        self.le_tituloimpre.setObjectName(u"le_tituloimpre")

        self.verticalLayout_2.addWidget(self.le_tituloimpre)


        self.verticalLayout_4.addWidget(self.gb_inicio_tituloimpre)

        self.gb_inicio_titulograf = QGroupBox(self.gb_inicio)
        self.gb_inicio_titulograf.setObjectName(u"gb_inicio_titulograf")
        self.verticalLayout_3 = QVBoxLayout(self.gb_inicio_titulograf)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.le_titulograf = QLineEdit(self.gb_inicio_titulograf)
        self.le_titulograf.setObjectName(u"le_titulograf")

        self.verticalLayout_3.addWidget(self.le_titulograf)


        self.verticalLayout_4.addWidget(self.gb_inicio_titulograf)


        self.verticalLayout_5.addWidget(self.gb_inicio)


        self.retranslateUi(inicio_window)

        QMetaObject.connectSlotsByName(inicio_window)
    # setupUi

    def retranslateUi(self, inicio_window):
        inicio_window.setWindowTitle(QCoreApplication.translate("inicio_window", u"Inicio - PrePRODIC3D", None))
        self.gb_inicio.setTitle(QCoreApplication.translate("inicio_window", u"Inicio", None))
        self.gb_inicio_titulosimu.setTitle(QCoreApplication.translate("inicio_window", u"Titulo de la simulaci\u00f3n", None))
        self.le_titulosimu.setInputMask("")
        self.le_titulosimu.setText(QCoreApplication.translate("inicio_window", u"Sin t\u00edtulo", None))
        self.gb_inicio_tituloimpre.setTitle(QCoreApplication.translate("inicio_window", u"Nombre del archivo de impresi\u00f3n (m\u00e1x. 8 caracteres)", None))
        self.le_tituloimpre.setText(QCoreApplication.translate("inicio_window", u"Print1", None))
        self.gb_inicio_titulograf.setTitle(QCoreApplication.translate("inicio_window", u"Nombre del archivo gr\u00e1fico (m\u00e1x. 8 caracteres)", None))
        self.le_titulograf.setText(QCoreApplication.translate("inicio_window", u"Plot1", None))
    # retranslateUi

