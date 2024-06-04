# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'values_windowuIrvBK.ui'
##
## Created by: Qt User Interface Compiler version 6.4.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QFormLayout, QGridLayout,
    QGroupBox, QHBoxLayout, QLabel, QLineEdit,
    QListWidget, QListWidgetItem, QPushButton, QScrollArea,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

class Ui_valores_window(object):
    def setupUi(self, valores_window):
        if not valores_window.objectName():
            valores_window.setObjectName(u"valores_window")
        valores_window.resize(664, 762)
        self.gridLayout_3 = QGridLayout(valores_window)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.scrollArea = QScrollArea(valores_window)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 644, 742))
        self.verticalLayout_3 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.groupBox = QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout_2 = QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.groupBox_2 = QGroupBox(self.groupBox)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.horizontalLayout = QHBoxLayout(self.groupBox_2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.groupBox_3 = QGroupBox(self.groupBox_2)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.gridLayout_2 = QGridLayout(self.groupBox_3)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.lw_variables = QListWidget(self.groupBox_3)
        QListWidgetItem(self.lw_variables)
        self.lw_variables.setObjectName(u"lw_variables")

        self.gridLayout_2.addWidget(self.lw_variables, 0, 0, 1, 1)


        self.horizontalLayout.addWidget(self.groupBox_3)

        self.groupBox_4 = QGroupBox(self.groupBox_2)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.formLayout_2 = QFormLayout(self.groupBox_4)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.le_general_value = QLineEdit(self.groupBox_4)
        self.le_general_value.setObjectName(u"le_general_value")

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.le_general_value)

        self.label_2 = QLabel(self.groupBox_4)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.label_2)

        self.le_k = QLineEdit(self.groupBox_4)
        self.le_k.setObjectName(u"le_k")

        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.le_k)

        self.label_15 = QLabel(self.groupBox_4)
        self.label_15.setObjectName(u"label_15")

        self.formLayout_2.setWidget(5, QFormLayout.LabelRole, self.label_15)

        self.groupBox_11 = QGroupBox(self.groupBox_4)
        self.groupBox_11.setObjectName(u"groupBox_11")
        self.horizontalLayout_3 = QHBoxLayout(self.groupBox_11)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.chb_ipun = QCheckBox(self.groupBox_11)
        self.chb_ipun.setObjectName(u"chb_ipun")
        self.chb_ipun.setLayoutDirection(Qt.RightToLeft)

        self.horizontalLayout_3.addWidget(self.chb_ipun)


        self.formLayout_2.setWidget(6, QFormLayout.LabelRole, self.groupBox_11)

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


        self.formLayout_2.setWidget(6, QFormLayout.FieldRole, self.groupBox_10)

        self.label = QLabel(self.groupBox_4)
        self.label.setObjectName(u"label")

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.label)

        self.label_16 = QLabel(self.groupBox_4)
        self.label_16.setObjectName(u"label_16")

        self.formLayout_2.setWidget(7, QFormLayout.LabelRole, self.label_16)

        self.le_ixyz = QLineEdit(self.groupBox_4)
        self.le_ixyz.setObjectName(u"le_ixyz")

        self.formLayout_2.setWidget(7, QFormLayout.FieldRole, self.le_ixyz)

        self.label_17 = QLabel(self.groupBox_4)
        self.label_17.setObjectName(u"label_17")

        self.formLayout_2.setWidget(8, QFormLayout.LabelRole, self.label_17)

        self.le_kblock = QLineEdit(self.groupBox_4)
        self.le_kblock.setObjectName(u"le_kblock")

        self.formLayout_2.setWidget(8, QFormLayout.FieldRole, self.le_kblock)


        self.horizontalLayout.addWidget(self.groupBox_4)

        self.groupBox_5 = QGroupBox(self.groupBox_2)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.formLayout = QFormLayout(self.groupBox_5)
        self.formLayout.setObjectName(u"formLayout")
        self.label_3 = QLabel(self.groupBox_5)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_3)

        self.lineEdit_3 = QLineEdit(self.groupBox_5)
        self.lineEdit_3.setObjectName(u"lineEdit_3")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.lineEdit_3)

        self.label_4 = QLabel(self.groupBox_5)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setAlignment(Qt.AlignCenter)

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_4)

        self.lineEdit_4 = QLineEdit(self.groupBox_5)
        self.lineEdit_4.setObjectName(u"lineEdit_4")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.lineEdit_4)

        self.label_5 = QLabel(self.groupBox_5)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setAlignment(Qt.AlignCenter)

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_5)

        self.lineEdit_5 = QLineEdit(self.groupBox_5)
        self.lineEdit_5.setObjectName(u"lineEdit_5")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.lineEdit_5)

        self.checkBox = QCheckBox(self.groupBox_5)
        self.checkBox.setObjectName(u"checkBox")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.checkBox)


        self.horizontalLayout.addWidget(self.groupBox_5)


        self.verticalLayout_2.addWidget(self.groupBox_2)

        self.chb_local_value = QCheckBox(self.groupBox)
        self.chb_local_value.setObjectName(u"chb_local_value")

        self.verticalLayout_2.addWidget(self.chb_local_value)

        self.groupBox_6 = QGroupBox(self.groupBox)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.horizontalLayout_2 = QHBoxLayout(self.groupBox_6)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.groupBox_7 = QGroupBox(self.groupBox_6)
        self.groupBox_7.setObjectName(u"groupBox_7")
        self.groupBox_7.setLayoutDirection(Qt.LeftToRight)
        self.formLayout_3 = QFormLayout(self.groupBox_7)
        self.formLayout_3.setObjectName(u"formLayout_3")
        self.pb_add_region = QPushButton(self.groupBox_7)
        self.pb_add_region.setObjectName(u"pb_add_region")

        self.formLayout_3.setWidget(2, QFormLayout.SpanningRole, self.pb_add_region)

        self.pb_remove_region = QPushButton(self.groupBox_7)
        self.pb_remove_region.setObjectName(u"pb_remove_region")

        self.formLayout_3.setWidget(4, QFormLayout.SpanningRole, self.pb_remove_region)

        self.lw_regions = QListWidget(self.groupBox_7)
        QListWidgetItem(self.lw_regions)
        self.lw_regions.setObjectName(u"lw_regions")
        self.lw_regions.setLayoutDirection(Qt.LeftToRight)

        self.formLayout_3.setWidget(0, QFormLayout.SpanningRole, self.lw_regions)

        self.le_local_value = QLineEdit(self.groupBox_7)
        self.le_local_value.setObjectName(u"le_local_value")

        self.formLayout_3.setWidget(10, QFormLayout.LabelRole, self.le_local_value)

        self.label_6 = QLabel(self.groupBox_7)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setAlignment(Qt.AlignCenter)

        self.formLayout_3.setWidget(10, QFormLayout.FieldRole, self.label_6)

        self.label_7 = QLabel(self.groupBox_7)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setAlignment(Qt.AlignCenter)

        self.formLayout_3.setWidget(11, QFormLayout.FieldRole, self.label_7)

        self.le_local_sp = QLineEdit(self.groupBox_7)
        self.le_local_sp.setObjectName(u"le_local_sp")

        self.formLayout_3.setWidget(14, QFormLayout.LabelRole, self.le_local_sp)

        self.label_8 = QLabel(self.groupBox_7)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setAlignment(Qt.AlignCenter)

        self.formLayout_3.setWidget(14, QFormLayout.FieldRole, self.label_8)

        self.le_local_k = QLineEdit(self.groupBox_7)
        self.le_local_k.setObjectName(u"le_local_k")

        self.formLayout_3.setWidget(17, QFormLayout.LabelRole, self.le_local_k)

        self.label_9 = QLabel(self.groupBox_7)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setAlignment(Qt.AlignCenter)

        self.formLayout_3.setWidget(17, QFormLayout.FieldRole, self.label_9)

        self.chb_fixed_value = QCheckBox(self.groupBox_7)
        self.chb_fixed_value.setObjectName(u"chb_fixed_value")

        self.formLayout_3.setWidget(8, QFormLayout.FieldRole, self.chb_fixed_value)

        self.chb_linear_source = QCheckBox(self.groupBox_7)
        self.chb_linear_source.setObjectName(u"chb_linear_source")

        self.formLayout_3.setWidget(8, QFormLayout.LabelRole, self.chb_linear_source)

        self.le_local_sc = QLineEdit(self.groupBox_7)
        self.le_local_sc.setObjectName(u"le_local_sc")

        self.formLayout_3.setWidget(11, QFormLayout.LabelRole, self.le_local_sc)


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

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.groupBox_9 = QGroupBox(self.groupBox_8)
        self.groupBox_9.setObjectName(u"groupBox_9")
        self.gridLayout = QGridLayout(self.groupBox_9)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_10 = QLabel(self.groupBox_9)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout.addWidget(self.label_10, 2, 0, 1, 1)

        self.le_y_lon = QLineEdit(self.groupBox_9)
        self.le_y_lon.setObjectName(u"le_y_lon")
        sizePolicy = QSizePolicy(QSizePolicy.Ignored, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.le_y_lon.sizePolicy().hasHeightForWidth())
        self.le_y_lon.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.le_y_lon, 2, 2, 1, 1)

        self.le_x_start = QLineEdit(self.groupBox_9)
        self.le_x_start.setObjectName(u"le_x_start")
        sizePolicy.setHeightForWidth(self.le_x_start.sizePolicy().hasHeightForWidth())
        self.le_x_start.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.le_x_start, 1, 1, 1, 1)

        self.le_y_start = QLineEdit(self.groupBox_9)
        self.le_y_start.setObjectName(u"le_y_start")
        sizePolicy.setHeightForWidth(self.le_y_start.sizePolicy().hasHeightForWidth())
        self.le_y_start.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.le_y_start, 1, 2, 1, 1)

        self.le_x_lon = QLineEdit(self.groupBox_9)
        self.le_x_lon.setObjectName(u"le_x_lon")
        sizePolicy.setHeightForWidth(self.le_x_lon.sizePolicy().hasHeightForWidth())
        self.le_x_lon.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.le_x_lon, 2, 1, 1, 1)

        self.label_12 = QLabel(self.groupBox_9)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_12, 0, 1, 1, 1)

        self.label_13 = QLabel(self.groupBox_9)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_13, 0, 2, 1, 1)

        self.label_11 = QLabel(self.groupBox_9)
        self.label_11.setObjectName(u"label_11")

        self.gridLayout.addWidget(self.label_11, 1, 0, 1, 1)

        self.label_14 = QLabel(self.groupBox_9)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_14, 0, 3, 1, 1)

        self.le_z_start = QLineEdit(self.groupBox_9)
        self.le_z_start.setObjectName(u"le_z_start")
        sizePolicy.setHeightForWidth(self.le_z_start.sizePolicy().hasHeightForWidth())
        self.le_z_start.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.le_z_start, 1, 3, 1, 1)

        self.le_z_lon = QLineEdit(self.groupBox_9)
        self.le_z_lon.setObjectName(u"le_z_lon")
        sizePolicy.setHeightForWidth(self.le_z_lon.sizePolicy().hasHeightForWidth())
        self.le_z_lon.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.le_z_lon, 2, 3, 1, 1)


        self.verticalLayout.addWidget(self.groupBox_9)


        self.horizontalLayout_2.addWidget(self.groupBox_8)


        self.verticalLayout_2.addWidget(self.groupBox_6)


        self.verticalLayout_3.addWidget(self.groupBox)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout_3.addWidget(self.scrollArea, 0, 0, 1, 1)


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

        self.groupBox_4.setTitle("")
        self.label_2.setText(QCoreApplication.translate("valores_window", u"Conductividad", None))
        self.label_15.setText(QCoreApplication.translate("valores_window", u"Extrapola excepto", None))
        self.groupBox_11.setTitle("")
        self.chb_ipun.setText(QCoreApplication.translate("valores_window", u"Esquinas", None))
        self.groupBox_10.setTitle("")
        self.chb_iborx.setText(QCoreApplication.translate("valores_window", u"X", None))
        self.chb_iborz.setText(QCoreApplication.translate("valores_window", u"Z", None))
        self.chb_ibory.setText(QCoreApplication.translate("valores_window", u"Y", None))
        self.label.setText(QCoreApplication.translate("valores_window", u"Valor general", None))
        self.label_16.setText(QCoreApplication.translate("valores_window", u"Ind. Impresi\u00f3n", None))
        self.label_17.setText(QCoreApplication.translate("valores_window", u"Ind. correc. bloque", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("valores_window", u"Flotabilidad", None))
        self.label_3.setText(QCoreApplication.translate("valores_window", u"Coef. exp. term.", None))
        self.label_4.setText(QCoreApplication.translate("valores_window", u"Gravedad", None))
        self.label_5.setText(QCoreApplication.translate("valores_window", u"\u00c1ngulo", None))
        self.checkBox.setText(QCoreApplication.translate("valores_window", u"Activar flotabilidad", None))
        self.chb_local_value.setText(QCoreApplication.translate("valores_window", u"Para aplicar valores locales para alguna variable, active la siguiente casilla", None))
        self.groupBox_6.setTitle(QCoreApplication.translate("valores_window", u"Valores locales por variable", None))
        self.groupBox_7.setTitle(QCoreApplication.translate("valores_window", u"Regiones", None))
        self.pb_add_region.setText(QCoreApplication.translate("valores_window", u"Agregar una regi\u00f3n", None))
        self.pb_remove_region.setText(QCoreApplication.translate("valores_window", u"Eliminar \u00faltima regi\u00f3n", None))

        __sortingEnabled1 = self.lw_regions.isSortingEnabled()
        self.lw_regions.setSortingEnabled(False)
        ___qlistwidgetitem1 = self.lw_regions.item(0)
        ___qlistwidgetitem1.setText(QCoreApplication.translate("valores_window", u"Region 1", None));
        self.lw_regions.setSortingEnabled(__sortingEnabled1)

        self.label_6.setText(QCoreApplication.translate("valores_window", u"Valor local", None))
        self.label_7.setText(QCoreApplication.translate("valores_window", u"Sc", None))
        self.label_8.setText(QCoreApplication.translate("valores_window", u"Sp", None))
        self.label_9.setText(QCoreApplication.translate("valores_window", u"k local", None))
        self.chb_fixed_value.setText(QCoreApplication.translate("valores_window", u"Valor fijo", None))
        self.chb_linear_source.setText(QCoreApplication.translate("valores_window", u"Fuente lineal", None))
        self.groupBox_8.setTitle(QCoreApplication.translate("valores_window", u"Conformaci\u00f3n de la regi\u00f3n", None))

        __sortingEnabled2 = self.lw_volumes.isSortingEnabled()
        self.lw_volumes.setSortingEnabled(False)
        ___qlistwidgetitem2 = self.lw_volumes.item(0)
        ___qlistwidgetitem2.setText(QCoreApplication.translate("valores_window", u"Volumen 1", None));
        self.lw_volumes.setSortingEnabled(__sortingEnabled2)

        self.pb_add_volume.setText(QCoreApplication.translate("valores_window", u"Agregar un volumen", None))
        self.pb_remove_volume.setText(QCoreApplication.translate("valores_window", u"Eliminar \u00faltimo volumen", None))
        self.groupBox_9.setTitle("")
        self.label_10.setText(QCoreApplication.translate("valores_window", u"Longitud", None))
        self.label_12.setText(QCoreApplication.translate("valores_window", u"X", None))
        self.label_13.setText(QCoreApplication.translate("valores_window", u"Y", None))
        self.label_11.setText(QCoreApplication.translate("valores_window", u"Inicio", None))
        self.label_14.setText(QCoreApplication.translate("valores_window", u"Z", None))
    # retranslateUi

