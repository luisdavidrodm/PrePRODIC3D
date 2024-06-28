# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'values_windoweFtrXB.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import resources_rc

class Ui_valores_window(object):
    def setupUi(self, valores_window):
        if not valores_window.objectName():
            valores_window.setObjectName(u"valores_window")
        valores_window.resize(630, 788)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(valores_window.sizePolicy().hasHeightForWidth())
        valores_window.setSizePolicy(sizePolicy)
        icon = QIcon()
        icon.addFile(u":/icon/icon/prodic_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        valores_window.setWindowIcon(icon)
        self.verticalLayout_2 = QVBoxLayout(valores_window)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.scrollArea = QScrollArea(valores_window)
        self.scrollArea.setObjectName(u"scrollArea")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy1)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 610, 768))
        self.verticalLayout_3 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.groupBox = QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox.setObjectName(u"groupBox")
        self.formLayout_3 = QFormLayout(self.groupBox)
        self.formLayout_3.setObjectName(u"formLayout_3")
        self.groupBox_2 = QGroupBox(self.groupBox)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.gridLayout_7 = QGridLayout(self.groupBox_2)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.groupBox_3 = QGroupBox(self.groupBox_2)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.gridLayout_2 = QGridLayout(self.groupBox_3)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.lw_variables = QListWidget(self.groupBox_3)
        QListWidgetItem(self.lw_variables)
        self.lw_variables.setObjectName(u"lw_variables")

        self.gridLayout_2.addWidget(self.lw_variables, 0, 0, 1, 1)


        self.gridLayout_7.addWidget(self.groupBox_3, 0, 0, 1, 1)

        self.groupBox_5 = QGroupBox(self.groupBox_2)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.formLayout = QFormLayout(self.groupBox_5)
        self.formLayout.setObjectName(u"formLayout")
        self.chb_buoyancy = QCheckBox(self.groupBox_5)
        self.chb_buoyancy.setObjectName(u"chb_buoyancy")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.chb_buoyancy)

        self.label_3 = QLabel(self.groupBox_5)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_3)

        self.le_therm_exp_coef = QLineEdit(self.groupBox_5)
        self.le_therm_exp_coef.setObjectName(u"le_therm_exp_coef")
        self.le_therm_exp_coef.setEnabled(False)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.le_therm_exp_coef)

        self.label_4 = QLabel(self.groupBox_5)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setAlignment(Qt.AlignCenter)

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_4)

        self.le_gravity = QLineEdit(self.groupBox_5)
        self.le_gravity.setObjectName(u"le_gravity")
        self.le_gravity.setEnabled(False)

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.le_gravity)

        self.label_5 = QLabel(self.groupBox_5)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setAlignment(Qt.AlignCenter)

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_5)

        self.le_angle = QLineEdit(self.groupBox_5)
        self.le_angle.setObjectName(u"le_angle")
        self.le_angle.setEnabled(False)

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.le_angle)

        self.label_10 = QLabel(self.groupBox_5)
        self.label_10.setObjectName(u"label_10")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.label_10)

        self.cb_plane = QComboBox(self.groupBox_5)
        self.cb_plane.addItem("")
        self.cb_plane.addItem("")
        self.cb_plane.addItem("")
        self.cb_plane.setObjectName(u"cb_plane")
        self.cb_plane.setEnabled(False)

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.cb_plane)


        self.gridLayout_7.addWidget(self.groupBox_5, 0, 2, 1, 1)

        self.groupBox_4 = QGroupBox(self.groupBox_2)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.gridLayout_8 = QGridLayout(self.groupBox_4)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.groupBox_10 = QGroupBox(self.groupBox_4)
        self.groupBox_10.setObjectName(u"groupBox_10")
        self.gridLayout_4 = QGridLayout(self.groupBox_10)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.chb_iborx = QCheckBox(self.groupBox_10)
        self.chb_iborx.setObjectName(u"chb_iborx")
        self.chb_iborx.setLayoutDirection(Qt.RightToLeft)

        self.gridLayout_4.addWidget(self.chb_iborx, 1, 0, 1, 1)

        self.chb_iborz = QCheckBox(self.groupBox_10)
        self.chb_iborz.setObjectName(u"chb_iborz")
        self.chb_iborz.setLayoutDirection(Qt.RightToLeft)

        self.gridLayout_4.addWidget(self.chb_iborz, 1, 2, 1, 1)

        self.chb_ibory = QCheckBox(self.groupBox_10)
        self.chb_ibory.setObjectName(u"chb_ibory")
        self.chb_ibory.setLayoutDirection(Qt.RightToLeft)

        self.gridLayout_4.addWidget(self.chb_ibory, 1, 1, 1, 1)


        self.gridLayout_8.addWidget(self.groupBox_10, 5, 1, 1, 2)

        self.le_k = QLineEdit(self.groupBox_4)
        self.le_k.setObjectName(u"le_k")

        self.gridLayout_8.addWidget(self.le_k, 1, 1, 1, 1)

        self.groupBox_11 = QGroupBox(self.groupBox_4)
        self.groupBox_11.setObjectName(u"groupBox_11")
        self.horizontalLayout_3 = QHBoxLayout(self.groupBox_11)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.chb_ipun = QCheckBox(self.groupBox_11)
        self.chb_ipun.setObjectName(u"chb_ipun")
        self.chb_ipun.setLayoutDirection(Qt.RightToLeft)

        self.horizontalLayout_3.addWidget(self.chb_ipun)


        self.gridLayout_8.addWidget(self.groupBox_11, 5, 0, 1, 1)

        self.le_ixyz = QLineEdit(self.groupBox_4)
        self.le_ixyz.setObjectName(u"le_ixyz")

        self.gridLayout_8.addWidget(self.le_ixyz, 6, 1, 1, 2)

        self.chb_ex_k = QCheckBox(self.groupBox_4)
        self.chb_ex_k.setObjectName(u"chb_ex_k")

        self.gridLayout_8.addWidget(self.chb_ex_k, 1, 2, 1, 1)

        self.label_17 = QLabel(self.groupBox_4)
        self.label_17.setObjectName(u"label_17")

        self.gridLayout_8.addWidget(self.label_17, 7, 0, 1, 1)

        self.le_kblock = QLineEdit(self.groupBox_4)
        self.le_kblock.setObjectName(u"le_kblock")

        self.gridLayout_8.addWidget(self.le_kblock, 7, 1, 1, 2)

        self.label_15 = QLabel(self.groupBox_4)
        self.label_15.setObjectName(u"label_15")

        self.gridLayout_8.addWidget(self.label_15, 4, 0, 1, 1)

        self.le_general_value = QLineEdit(self.groupBox_4)
        self.le_general_value.setObjectName(u"le_general_value")

        self.gridLayout_8.addWidget(self.le_general_value, 0, 1, 1, 1)

        self.label = QLabel(self.groupBox_4)
        self.label.setObjectName(u"label")

        self.gridLayout_8.addWidget(self.label, 0, 0, 1, 1)

        self.label_2 = QLabel(self.groupBox_4)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_8.addWidget(self.label_2, 1, 0, 1, 1)

        self.label_16 = QLabel(self.groupBox_4)
        self.label_16.setObjectName(u"label_16")

        self.gridLayout_8.addWidget(self.label_16, 6, 0, 1, 1)

        self.chb_ex_value = QCheckBox(self.groupBox_4)
        self.chb_ex_value.setObjectName(u"chb_ex_value")

        self.gridLayout_8.addWidget(self.chb_ex_value, 0, 2, 1, 1)


        self.gridLayout_7.addWidget(self.groupBox_4, 0, 1, 1, 1)


        self.formLayout_3.setWidget(0, QFormLayout.SpanningRole, self.groupBox_2)

        self.chb_local_value = QCheckBox(self.groupBox)
        self.chb_local_value.setObjectName(u"chb_local_value")

        self.formLayout_3.setWidget(2, QFormLayout.SpanningRole, self.chb_local_value)

        self.chb_exclude_borders = QCheckBox(self.groupBox)
        self.chb_exclude_borders.setObjectName(u"chb_exclude_borders")

        self.formLayout_3.setWidget(5, QFormLayout.LabelRole, self.chb_exclude_borders)

        self.groupBox_9 = QGroupBox(self.groupBox)
        self.groupBox_9.setObjectName(u"groupBox_9")
        self.gridLayout = QGridLayout(self.groupBox_9)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_14 = QLabel(self.groupBox_9)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_14, 0, 5, 1, 1)

        self.cb_ex_y_start = QComboBox(self.groupBox_9)
        self.cb_ex_y_start.addItem("")
        self.cb_ex_y_start.addItem("")
        self.cb_ex_y_start.addItem("")
        self.cb_ex_y_start.setObjectName(u"cb_ex_y_start")

        self.gridLayout.addWidget(self.cb_ex_y_start, 1, 2, 1, 1)

        self.cb_ex_x_start = QComboBox(self.groupBox_9)
        self.cb_ex_x_start.addItem("")
        self.cb_ex_x_start.addItem("")
        self.cb_ex_x_start.addItem("")
        self.cb_ex_x_start.setObjectName(u"cb_ex_x_start")

        self.gridLayout.addWidget(self.cb_ex_x_start, 1, 0, 1, 1)

        self.cb_ex_x_end = QComboBox(self.groupBox_9)
        self.cb_ex_x_end.addItem("")
        self.cb_ex_x_end.addItem("")
        self.cb_ex_x_end.addItem("")
        self.cb_ex_x_end.setObjectName(u"cb_ex_x_end")

        self.gridLayout.addWidget(self.cb_ex_x_end, 2, 0, 1, 1)

        self.label_12 = QLabel(self.groupBox_9)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_12, 0, 1, 1, 1)

        self.cb_ex_y_end = QComboBox(self.groupBox_9)
        self.cb_ex_y_end.addItem("")
        self.cb_ex_y_end.addItem("")
        self.cb_ex_y_end.addItem("")
        self.cb_ex_y_end.setObjectName(u"cb_ex_y_end")

        self.gridLayout.addWidget(self.cb_ex_y_end, 2, 2, 1, 1)

        self.label_13 = QLabel(self.groupBox_9)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_13, 0, 3, 1, 1)

        self.le_z_end = QLineEdit(self.groupBox_9)
        self.le_z_end.setObjectName(u"le_z_end")
        sizePolicy2 = QSizePolicy(QSizePolicy.Ignored, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.le_z_end.sizePolicy().hasHeightForWidth())
        self.le_z_end.setSizePolicy(sizePolicy2)

        self.gridLayout.addWidget(self.le_z_end, 2, 5, 1, 1)

        self.le_x_end = QLineEdit(self.groupBox_9)
        self.le_x_end.setObjectName(u"le_x_end")
        sizePolicy2.setHeightForWidth(self.le_x_end.sizePolicy().hasHeightForWidth())
        self.le_x_end.setSizePolicy(sizePolicy2)

        self.gridLayout.addWidget(self.le_x_end, 2, 1, 1, 1)

        self.le_z_start = QLineEdit(self.groupBox_9)
        self.le_z_start.setObjectName(u"le_z_start")
        sizePolicy2.setHeightForWidth(self.le_z_start.sizePolicy().hasHeightForWidth())
        self.le_z_start.setSizePolicy(sizePolicy2)

        self.gridLayout.addWidget(self.le_z_start, 1, 5, 1, 1)

        self.le_x_start = QLineEdit(self.groupBox_9)
        self.le_x_start.setObjectName(u"le_x_start")
        sizePolicy2.setHeightForWidth(self.le_x_start.sizePolicy().hasHeightForWidth())
        self.le_x_start.setSizePolicy(sizePolicy2)

        self.gridLayout.addWidget(self.le_x_start, 1, 1, 1, 1)

        self.le_y_end = QLineEdit(self.groupBox_9)
        self.le_y_end.setObjectName(u"le_y_end")
        sizePolicy2.setHeightForWidth(self.le_y_end.sizePolicy().hasHeightForWidth())
        self.le_y_end.setSizePolicy(sizePolicy2)

        self.gridLayout.addWidget(self.le_y_end, 2, 3, 1, 1)

        self.le_y_start = QLineEdit(self.groupBox_9)
        self.le_y_start.setObjectName(u"le_y_start")
        sizePolicy2.setHeightForWidth(self.le_y_start.sizePolicy().hasHeightForWidth())
        self.le_y_start.setSizePolicy(sizePolicy2)

        self.gridLayout.addWidget(self.le_y_start, 1, 3, 1, 1)

        self.cb_ex_z_start = QComboBox(self.groupBox_9)
        self.cb_ex_z_start.setObjectName(u"cb_ex_z_start")

        self.gridLayout.addWidget(self.cb_ex_z_start, 1, 4, 1, 1)

        self.cb_ex_z_end = QComboBox(self.groupBox_9)
        self.cb_ex_z_end.setObjectName(u"cb_ex_z_end")

        self.gridLayout.addWidget(self.cb_ex_z_end, 2, 4, 1, 1)


        self.formLayout_3.setWidget(6, QFormLayout.SpanningRole, self.groupBox_9)

        self.groupBox_6 = QGroupBox(self.groupBox)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.horizontalLayout_2 = QHBoxLayout(self.groupBox_6)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.groupBox_7 = QGroupBox(self.groupBox_6)
        self.groupBox_7.setObjectName(u"groupBox_7")
        self.groupBox_7.setLayoutDirection(Qt.LeftToRight)
        self.gridLayout_6 = QGridLayout(self.groupBox_7)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.label_7 = QLabel(self.groupBox_7)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setAlignment(Qt.AlignCenter)

        self.gridLayout_6.addWidget(self.label_7, 5, 0, 1, 1)

        self.le_local_sp = QLineEdit(self.groupBox_7)
        self.le_local_sp.setObjectName(u"le_local_sp")

        self.gridLayout_6.addWidget(self.le_local_sp, 7, 1, 1, 1)

        self.pb_remove_region = QPushButton(self.groupBox_7)
        self.pb_remove_region.setObjectName(u"pb_remove_region")

        self.gridLayout_6.addWidget(self.pb_remove_region, 2, 0, 1, 2)

        self.label_6 = QLabel(self.groupBox_7)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setAlignment(Qt.AlignCenter)

        self.gridLayout_6.addWidget(self.label_6, 3, 0, 1, 1)

        self.le_local_value = QLineEdit(self.groupBox_7)
        self.le_local_value.setObjectName(u"le_local_value")

        self.gridLayout_6.addWidget(self.le_local_value, 3, 1, 1, 1)

        self.le_local_k = QLineEdit(self.groupBox_7)
        self.le_local_k.setObjectName(u"le_local_k")

        self.gridLayout_6.addWidget(self.le_local_k, 9, 1, 1, 1)

        self.le_local_sc = QLineEdit(self.groupBox_7)
        self.le_local_sc.setObjectName(u"le_local_sc")

        self.gridLayout_6.addWidget(self.le_local_sc, 5, 1, 1, 1)

        self.pb_add_region = QPushButton(self.groupBox_7)
        self.pb_add_region.setObjectName(u"pb_add_region")

        self.gridLayout_6.addWidget(self.pb_add_region, 1, 0, 1, 2)

        self.label_9 = QLabel(self.groupBox_7)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setAlignment(Qt.AlignCenter)

        self.gridLayout_6.addWidget(self.label_9, 9, 0, 1, 1)

        self.label_8 = QLabel(self.groupBox_7)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setAlignment(Qt.AlignCenter)

        self.gridLayout_6.addWidget(self.label_8, 7, 0, 1, 1)

        self.lw_regions = QListWidget(self.groupBox_7)
        QListWidgetItem(self.lw_regions)
        self.lw_regions.setObjectName(u"lw_regions")
        self.lw_regions.setLayoutDirection(Qt.LeftToRight)

        self.gridLayout_6.addWidget(self.lw_regions, 0, 0, 1, 2)


        self.horizontalLayout_2.addWidget(self.groupBox_7)

        self.groupBox_8 = QGroupBox(self.groupBox_6)
        self.groupBox_8.setObjectName(u"groupBox_8")
        self.verticalLayout = QVBoxLayout(self.groupBox_8)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.lw_volumes = QListWidget(self.groupBox_8)
        QListWidgetItem(self.lw_volumes)
        self.lw_volumes.setObjectName(u"lw_volumes")

        self.verticalLayout.addWidget(self.lw_volumes)

        self.pb_add_volume = QPushButton(self.groupBox_8)
        self.pb_add_volume.setObjectName(u"pb_add_volume")

        self.verticalLayout.addWidget(self.pb_add_volume)

        self.pb_remove_volume = QPushButton(self.groupBox_8)
        self.pb_remove_volume.setObjectName(u"pb_remove_volume")

        self.verticalLayout.addWidget(self.pb_remove_volume)

        self.verticalSpacer = QSpacerItem(20, 167, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.horizontalLayout_2.addWidget(self.groupBox_8)


        self.formLayout_3.setWidget(3, QFormLayout.SpanningRole, self.groupBox_6)


        self.verticalLayout_3.addWidget(self.groupBox)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_2.addWidget(self.scrollArea)


        self.retranslateUi(valores_window)

        QMetaObject.connectSlotsByName(valores_window)
    # setupUi

    def retranslateUi(self, valores_window):
        valores_window.setWindowTitle(QCoreApplication.translate("valores_window", u"Valores - PrePRODIC3D", None))
        self.groupBox.setTitle(QCoreApplication.translate("valores_window", u"Valores", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("valores_window", u"Valores generales del dominio por variable", None))
        self.groupBox_3.setTitle("")

        __sortingEnabled = self.lw_variables.isSortingEnabled()
        self.lw_variables.setSortingEnabled(False)
        ___qlistwidgetitem = self.lw_variables.item(0)
        ___qlistwidgetitem.setText(QCoreApplication.translate("valores_window", u"Temperatura", None));
        self.lw_variables.setSortingEnabled(__sortingEnabled)

        self.groupBox_5.setTitle(QCoreApplication.translate("valores_window", u"Flotabilidad", None))
        self.chb_buoyancy.setText(QCoreApplication.translate("valores_window", u"Activar flotabilidad", None))
        self.label_3.setText(QCoreApplication.translate("valores_window", u"Coef. exp. term.", None))
        self.label_4.setText(QCoreApplication.translate("valores_window", u"Gravedad", None))
        self.label_5.setText(QCoreApplication.translate("valores_window", u"\u00c1ngulo", None))
        self.label_10.setText(QCoreApplication.translate("valores_window", u"Plano", None))
        self.cb_plane.setItemText(0, QCoreApplication.translate("valores_window", u"XY", None))
        self.cb_plane.setItemText(1, QCoreApplication.translate("valores_window", u"YZ", None))
        self.cb_plane.setItemText(2, QCoreApplication.translate("valores_window", u"XZ", None))

        self.groupBox_4.setTitle("")
        self.groupBox_10.setTitle("")
        self.chb_iborx.setText(QCoreApplication.translate("valores_window", u"X", None))
        self.chb_iborz.setText(QCoreApplication.translate("valores_window", u"Z", None))
        self.chb_ibory.setText(QCoreApplication.translate("valores_window", u"Y", None))
        self.groupBox_11.setTitle("")
        self.chb_ipun.setText(QCoreApplication.translate("valores_window", u"Esquinas", None))
#if QT_CONFIG(tooltip)
        self.chb_ex_k.setToolTip(QCoreApplication.translate("valores_window", u"<html><head/><body><p>Activa esta opci\u00f3n para excluir los <br/>bordes inicial y final del dominio al <br/>iterar este valor.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.chb_ex_k.setWhatsThis(QCoreApplication.translate("valores_window", u"Activa esta opci\u00f3n para excluir los bordes inicial y final del dominio al iterar este valor.", None))
#endif // QT_CONFIG(whatsthis)
        self.chb_ex_k.setText("")
        self.label_17.setText(QCoreApplication.translate("valores_window", u"Ind. correc. bloque", None))
        self.label_15.setText(QCoreApplication.translate("valores_window", u"Extrapola excepto:", None))
        self.label.setText(QCoreApplication.translate("valores_window", u"Valor general", None))
        self.label_2.setText(QCoreApplication.translate("valores_window", u"Conductividad", None))
        self.label_16.setText(QCoreApplication.translate("valores_window", u"Ind. Impresi\u00f3n", None))
#if QT_CONFIG(tooltip)
        self.chb_ex_value.setToolTip(QCoreApplication.translate("valores_window", u"<html><head/><body><p>Activa esta opci\u00f3n para excluir los <br/>bordes inicial y final del dominio al <br/>iterar este valor.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.chb_ex_value.setWhatsThis(QCoreApplication.translate("valores_window", u"Activa esta opci\u00f3n para excluir los bordes inicial y final del dominio al iterar este valor.", None))
#endif // QT_CONFIG(whatsthis)
        self.chb_ex_value.setText("")
        self.chb_local_value.setText(QCoreApplication.translate("valores_window", u"Para aplicar valores locales para alguna variable, active la siguiente casilla", None))
#if QT_CONFIG(tooltip)
        self.chb_exclude_borders.setToolTip(QCoreApplication.translate("valores_window", u"<html><head/><body><p>Activa esta opci\u00f3n para excluir<br/>los bordes inicial y final del dominio<br/>para cada iteraci\u00f3n en el volumen<br/>seleccionado, independientemente<br/>de las limitantes por coordenadas.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.chb_exclude_borders.setWhatsThis(QCoreApplication.translate("valores_window", u"Activa esta opci\u00f3n para excluir los bordes inicial y final del dominio para cada iteraci\u00f3n en el volumen seleccionado, independientemente de las limitantes por coordenadas.", None))
#endif // QT_CONFIG(whatsthis)
        self.chb_exclude_borders.setText(QCoreApplication.translate("valores_window", u"V.C. Excluir bordes", None))
        self.groupBox_9.setTitle("")
        self.label_14.setText(QCoreApplication.translate("valores_window", u"Z", None))
        self.cb_ex_y_start.setItemText(0, "")
        self.cb_ex_y_start.setItemText(1, QCoreApplication.translate("valores_window", u">", None))
        self.cb_ex_y_start.setItemText(2, QCoreApplication.translate("valores_window", u"\u2265", None))

        self.cb_ex_x_start.setItemText(0, "")
        self.cb_ex_x_start.setItemText(1, QCoreApplication.translate("valores_window", u">", None))
        self.cb_ex_x_start.setItemText(2, QCoreApplication.translate("valores_window", u"\u2265", None))

        self.cb_ex_x_end.setItemText(0, "")
        self.cb_ex_x_end.setItemText(1, QCoreApplication.translate("valores_window", u"<", None))
        self.cb_ex_x_end.setItemText(2, QCoreApplication.translate("valores_window", u"\u2264", None))

        self.label_12.setText(QCoreApplication.translate("valores_window", u"X", None))
        self.cb_ex_y_end.setItemText(0, "")
        self.cb_ex_y_end.setItemText(1, QCoreApplication.translate("valores_window", u"<", None))
        self.cb_ex_y_end.setItemText(2, QCoreApplication.translate("valores_window", u"\u2264", None))

        self.label_13.setText(QCoreApplication.translate("valores_window", u"Y", None))
        self.groupBox_6.setTitle(QCoreApplication.translate("valores_window", u"Valores locales por variable", None))
        self.groupBox_7.setTitle(QCoreApplication.translate("valores_window", u"Regiones", None))
        self.label_7.setText(QCoreApplication.translate("valores_window", u"Sc", None))
        self.pb_remove_region.setText(QCoreApplication.translate("valores_window", u"Eliminar \u00faltima regi\u00f3n", None))
        self.label_6.setText(QCoreApplication.translate("valores_window", u"Valor local", None))
        self.pb_add_region.setText(QCoreApplication.translate("valores_window", u"Agregar una regi\u00f3n", None))
        self.label_9.setText(QCoreApplication.translate("valores_window", u"k local", None))
        self.label_8.setText(QCoreApplication.translate("valores_window", u"Sp", None))

        __sortingEnabled1 = self.lw_regions.isSortingEnabled()
        self.lw_regions.setSortingEnabled(False)
        ___qlistwidgetitem1 = self.lw_regions.item(0)
        ___qlistwidgetitem1.setText(QCoreApplication.translate("valores_window", u"Regi\u00f3n 1", None));
        self.lw_regions.setSortingEnabled(__sortingEnabled1)

        self.groupBox_8.setTitle(QCoreApplication.translate("valores_window", u"Conformaci\u00f3n de la regi\u00f3n", None))

        __sortingEnabled2 = self.lw_volumes.isSortingEnabled()
        self.lw_volumes.setSortingEnabled(False)
        ___qlistwidgetitem2 = self.lw_volumes.item(0)
        ___qlistwidgetitem2.setText(QCoreApplication.translate("valores_window", u"Volumen 1", None));
        self.lw_volumes.setSortingEnabled(__sortingEnabled2)

        self.pb_add_volume.setText(QCoreApplication.translate("valores_window", u"Agregar un volumen", None))
        self.pb_remove_volume.setText(QCoreApplication.translate("valores_window", u"Eliminar \u00faltimo volumen", None))
    # retranslateUi

