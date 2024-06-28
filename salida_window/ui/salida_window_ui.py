# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'salida_windowjApItE.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import resources_rc

class Ui_salida_window(object):
    def setupUi(self, salida_window):
        if not salida_window.objectName():
            salida_window.setObjectName(u"salida_window")
        salida_window.resize(502, 345)
        icon = QIcon()
        icon.addFile(u":/icon/icon/prodic_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        salida_window.setWindowIcon(icon)
        self.gridLayout_3 = QGridLayout(salida_window)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.groupBox = QGroupBox(salida_window)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout = QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.groupBox_2 = QGroupBox(self.groupBox)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.horizontalLayout = QHBoxLayout(self.groupBox_2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.groupBox_3 = QGroupBox(self.groupBox_2)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.formLayout = QFormLayout(self.groupBox_3)
        self.formLayout.setObjectName(u"formLayout")
        self.lw_variables = QListWidget(self.groupBox_3)
        QListWidgetItem(self.lw_variables)
        self.lw_variables.setObjectName(u"lw_variables")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.lw_variables)


        self.horizontalLayout.addWidget(self.groupBox_3)

        self.groupBox_4 = QGroupBox(self.groupBox_2)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.gridLayout = QGridLayout(self.groupBox_4)
        self.gridLayout.setObjectName(u"gridLayout")
        self.le_y = QLineEdit(self.groupBox_4)
        self.le_y.setObjectName(u"le_y")

        self.gridLayout.addWidget(self.le_y, 1, 1, 1, 1)

        self.le_z = QLineEdit(self.groupBox_4)
        self.le_z.setObjectName(u"le_z")

        self.gridLayout.addWidget(self.le_z, 2, 1, 1, 1)

        self.lb_z = QLabel(self.groupBox_4)
        self.lb_z.setObjectName(u"lb_z")

        self.gridLayout.addWidget(self.lb_z, 2, 0, 1, 1)

        self.le_x = QLineEdit(self.groupBox_4)
        self.le_x.setObjectName(u"le_x")

        self.gridLayout.addWidget(self.le_x, 0, 1, 1, 1)

        self.lb_y = QLabel(self.groupBox_4)
        self.lb_y.setObjectName(u"lb_y")

        self.gridLayout.addWidget(self.lb_y, 1, 0, 1, 1)

        self.lb_x = QLabel(self.groupBox_4)
        self.lb_x.setObjectName(u"lb_x")

        self.gridLayout.addWidget(self.lb_x, 0, 0, 1, 1)


        self.horizontalLayout.addWidget(self.groupBox_4)


        self.verticalLayout.addWidget(self.groupBox_2)

        self.groupBox_5 = QGroupBox(self.groupBox)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.horizontalLayout_2 = QHBoxLayout(self.groupBox_5)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.groupBox_6 = QGroupBox(self.groupBox_5)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.gridLayout_2 = QGridLayout(self.groupBox_6)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.chb_corner_1 = QCheckBox(self.groupBox_6)
        self.chb_corner_1.setObjectName(u"chb_corner_1")

        self.gridLayout_2.addWidget(self.chb_corner_1, 1, 0, 1, 1)

        self.chb_corner_7 = QCheckBox(self.groupBox_6)
        self.chb_corner_7.setObjectName(u"chb_corner_7")

        self.gridLayout_2.addWidget(self.chb_corner_7, 3, 1, 1, 1)

        self.chb_corner_8 = QCheckBox(self.groupBox_6)
        self.chb_corner_8.setObjectName(u"chb_corner_8")

        self.gridLayout_2.addWidget(self.chb_corner_8, 4, 1, 1, 1)

        self.chb_corner_6 = QCheckBox(self.groupBox_6)
        self.chb_corner_6.setObjectName(u"chb_corner_6")

        self.gridLayout_2.addWidget(self.chb_corner_6, 2, 1, 1, 1)

        self.chb_corner_2 = QCheckBox(self.groupBox_6)
        self.chb_corner_2.setObjectName(u"chb_corner_2")

        self.gridLayout_2.addWidget(self.chb_corner_2, 2, 0, 1, 1)

        self.chb_corner_4 = QCheckBox(self.groupBox_6)
        self.chb_corner_4.setObjectName(u"chb_corner_4")

        self.gridLayout_2.addWidget(self.chb_corner_4, 4, 0, 1, 1)

        self.chb_corner_3 = QCheckBox(self.groupBox_6)
        self.chb_corner_3.setObjectName(u"chb_corner_3")

        self.gridLayout_2.addWidget(self.chb_corner_3, 3, 0, 1, 1)

        self.chb_all_corners = QCheckBox(self.groupBox_6)
        self.chb_all_corners.setObjectName(u"chb_all_corners")

        self.gridLayout_2.addWidget(self.chb_all_corners, 0, 0, 1, 1)

        self.chb_corner_5 = QCheckBox(self.groupBox_6)
        self.chb_corner_5.setObjectName(u"chb_corner_5")

        self.gridLayout_2.addWidget(self.chb_corner_5, 1, 1, 1, 1)


        self.horizontalLayout_2.addWidget(self.groupBox_6)

        self.groupBox_7 = QGroupBox(self.groupBox_5)
        self.groupBox_7.setObjectName(u"groupBox_7")
        self.formLayout_2 = QFormLayout(self.groupBox_7)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.label_4 = QLabel(self.groupBox_7)
        self.label_4.setObjectName(u"label_4")

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.label_4)

        self.le_last = QLineEdit(self.groupBox_7)
        self.le_last.setObjectName(u"le_last")
        self.le_last.setAlignment(Qt.AlignCenter)

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.le_last)

        self.label_6 = QLabel(self.groupBox_7)
        self.label_6.setObjectName(u"label_6")

        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.label_6)

        self.le_temp_last = QLineEdit(self.groupBox_7)
        self.le_temp_last.setObjectName(u"le_temp_last")
        self.le_temp_last.setAlignment(Qt.AlignCenter)

        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.le_temp_last)

        self.chb_dimensionless = QCheckBox(self.groupBox_7)
        self.chb_dimensionless.setObjectName(u"chb_dimensionless")

        self.formLayout_2.setWidget(3, QFormLayout.SpanningRole, self.chb_dimensionless)

        self.label_5 = QLabel(self.groupBox_7)
        self.label_5.setObjectName(u"label_5")

        self.formLayout_2.setWidget(2, QFormLayout.LabelRole, self.label_5)

        self.le_tw = QLineEdit(self.groupBox_7)
        self.le_tw.setObjectName(u"le_tw")

        self.formLayout_2.setWidget(2, QFormLayout.FieldRole, self.le_tw)


        self.horizontalLayout_2.addWidget(self.groupBox_7)


        self.verticalLayout.addWidget(self.groupBox_5)


        self.gridLayout_3.addWidget(self.groupBox, 0, 0, 1, 1)


        self.retranslateUi(salida_window)

        QMetaObject.connectSlotsByName(salida_window)
    # setupUi

    def retranslateUi(self, salida_window):
        salida_window.setWindowTitle(QCoreApplication.translate("salida_window", u"Salida - PrePRODIC3D", None))
        self.groupBox.setTitle(QCoreApplication.translate("salida_window", u"Opciones de salida", None))
        self.groupBox_2.setTitle("")
        self.groupBox_3.setTitle(QCoreApplication.translate("salida_window", u"Variables", None))

        __sortingEnabled = self.lw_variables.isSortingEnabled()
        self.lw_variables.setSortingEnabled(False)
        ___qlistwidgetitem = self.lw_variables.item(0)
        ___qlistwidgetitem.setText(QCoreApplication.translate("salida_window", u"Temperatura", None));
        self.lw_variables.setSortingEnabled(__sortingEnabled)

        self.groupBox_4.setTitle(QCoreApplication.translate("salida_window", u"Puntos de monitoreo", None))
        self.le_y.setText(QCoreApplication.translate("salida_window", u"0", None))
        self.le_z.setText(QCoreApplication.translate("salida_window", u"0", None))
        self.lb_z.setText(QCoreApplication.translate("salida_window", u"Z", None))
        self.le_x.setText(QCoreApplication.translate("salida_window", u"0", None))
        self.lb_y.setText(QCoreApplication.translate("salida_window", u"Y", None))
        self.lb_x.setText(QCoreApplication.translate("salida_window", u"X", None))
        self.groupBox_5.setTitle("")
        self.groupBox_6.setTitle(QCoreApplication.translate("salida_window", u"Promedio en las esquinas", None))
        self.chb_corner_1.setText(QCoreApplication.translate("salida_window", u"(1, 1, 1)", None))
        self.chb_corner_7.setText(QCoreApplication.translate("salida_window", u"(L1, 1, N1)", None))
        self.chb_corner_8.setText(QCoreApplication.translate("salida_window", u"(L1, M1, N1)", None))
        self.chb_corner_6.setText(QCoreApplication.translate("salida_window", u"(1, M1, N1)", None))
        self.chb_corner_2.setText(QCoreApplication.translate("salida_window", u"(L1, 1, 1)", None))
        self.chb_corner_4.setText(QCoreApplication.translate("salida_window", u"(1, 1, N1)", None))
        self.chb_corner_3.setText(QCoreApplication.translate("salida_window", u"(1, M1, 1)", None))
        self.chb_all_corners.setText(QCoreApplication.translate("salida_window", u"Todas las esquinas", None))
        self.chb_corner_5.setText(QCoreApplication.translate("salida_window", u"(L1, M1, 1)", None))
        self.groupBox_7.setTitle(QCoreApplication.translate("salida_window", u"Otras opciones", None))
        self.label_4.setText(QCoreApplication.translate("salida_window", u"Numero de iteraciones", None))
        self.le_last.setText(QCoreApplication.translate("salida_window", u"5", None))
        self.label_6.setText(QCoreApplication.translate("salida_window", u"Iteraciones de temperatura", None))
        self.chb_dimensionless.setText(QCoreApplication.translate("salida_window", u"C\u00e1lculos adimensionales", None))
        self.label_5.setText(QCoreApplication.translate("salida_window", u"TW", None))
    # retranslateUi

