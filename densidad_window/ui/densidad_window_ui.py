# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'densidad_windowleXCbn.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QFormLayout,
    QGridLayout, QGroupBox, QLabel, QLineEdit,
    QListWidget, QListWidgetItem, QPushButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

class Ui_densidad_window(object):
    def setupUi(self, densidad_window):
        if not densidad_window.objectName():
            densidad_window.setObjectName(u"densidad_window")
        densidad_window.resize(675, 583)
        self.gridLayout_2 = QGridLayout(densidad_window)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.groupBox_2 = QGroupBox(densidad_window)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.verticalLayout = QVBoxLayout(self.groupBox_2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.lw_regions = QListWidget(self.groupBox_2)
        QListWidgetItem(self.lw_regions)
        self.lw_regions.setObjectName(u"lw_regions")

        self.verticalLayout.addWidget(self.lw_regions)

        self.pb_add_region = QPushButton(self.groupBox_2)
        self.pb_add_region.setObjectName(u"pb_add_region")

        self.verticalLayout.addWidget(self.pb_add_region)

        self.pb_remove_region = QPushButton(self.groupBox_2)
        self.pb_remove_region.setObjectName(u"pb_remove_region")

        self.verticalLayout.addWidget(self.pb_remove_region)

        self.groupBox_5 = QGroupBox(self.groupBox_2)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.formLayout_2 = QFormLayout(self.groupBox_5)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.label_5 = QLabel(self.groupBox_5)
        self.label_5.setObjectName(u"label_5")

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.label_5)

        self.le_local_value = QLineEdit(self.groupBox_5)
        self.le_local_value.setObjectName(u"le_local_value")

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.le_local_value)


        self.verticalLayout.addWidget(self.groupBox_5)


        self.gridLayout_2.addWidget(self.groupBox_2, 2, 0, 1, 1)

        self.groupBox_3 = QGroupBox(densidad_window)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.verticalLayout_2 = QVBoxLayout(self.groupBox_3)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.lw_volumes = QListWidget(self.groupBox_3)
        QListWidgetItem(self.lw_volumes)
        self.lw_volumes.setObjectName(u"lw_volumes")

        self.verticalLayout_2.addWidget(self.lw_volumes)

        self.verticalSpacer = QSpacerItem(20, 220, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.pb_add_volume = QPushButton(self.groupBox_3)
        self.pb_add_volume.setObjectName(u"pb_add_volume")

        self.verticalLayout_2.addWidget(self.pb_add_volume)

        self.pb_remove_volume = QPushButton(self.groupBox_3)
        self.pb_remove_volume.setObjectName(u"pb_remove_volume")

        self.verticalLayout_2.addWidget(self.pb_remove_volume)

        self.verticalSpacer_2 = QSpacerItem(20, 250, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)


        self.gridLayout_2.addWidget(self.groupBox_3, 2, 1, 1, 1)

        self.chb_local_value = QCheckBox(densidad_window)
        self.chb_local_value.setObjectName(u"chb_local_value")
        self.chb_local_value.setContextMenuPolicy(Qt.CustomContextMenu)
        self.chb_local_value.setLayoutDirection(Qt.LeftToRight)
        self.chb_local_value.setTristate(False)

        self.gridLayout_2.addWidget(self.chb_local_value, 1, 0, 1, 2)

        self.groupBox = QGroupBox(densidad_window)
        self.groupBox.setObjectName(u"groupBox")
        self.formLayout = QFormLayout(self.groupBox)
        self.formLayout.setObjectName(u"formLayout")
        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_2)

        self.le_general_value = QLineEdit(self.groupBox)
        self.le_general_value.setObjectName(u"le_general_value")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.le_general_value)

        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.label_3)

        self.le_ref_rho = QLineEdit(self.groupBox)
        self.le_ref_rho.setObjectName(u"le_ref_rho")

        self.formLayout.setWidget(5, QFormLayout.FieldRole, self.le_ref_rho)

        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")

        self.formLayout.setWidget(6, QFormLayout.LabelRole, self.label_4)

        self.le_ref_temp = QLineEdit(self.groupBox)
        self.le_ref_temp.setObjectName(u"le_ref_temp")

        self.formLayout.setWidget(6, QFormLayout.FieldRole, self.le_ref_temp)

        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)

        self.cb_condition = QComboBox(self.groupBox)
        self.cb_condition.addItem("")
        self.cb_condition.addItem("")
        self.cb_condition.setObjectName(u"cb_condition")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.cb_condition)

        self.chb_ex_value = QCheckBox(self.groupBox)
        self.chb_ex_value.setObjectName(u"chb_ex_value")

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.chb_ex_value)


        self.gridLayout_2.addWidget(self.groupBox, 0, 0, 1, 2)

        self.groupBox_4 = QGroupBox(densidad_window)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.gridLayout = QGridLayout(self.groupBox_4)
        self.gridLayout.setObjectName(u"gridLayout")
        self.le_x_end = QLineEdit(self.groupBox_4)
        self.le_x_end.setObjectName(u"le_x_end")

        self.gridLayout.addWidget(self.le_x_end, 2, 1, 1, 1)

        self.cb_ex_z_end = QComboBox(self.groupBox_4)
        self.cb_ex_z_end.addItem("")
        self.cb_ex_z_end.addItem("")
        self.cb_ex_z_end.addItem("")
        self.cb_ex_z_end.setObjectName(u"cb_ex_z_end")

        self.gridLayout.addWidget(self.cb_ex_z_end, 2, 4, 1, 1)

        self.cb_ex_x_end = QComboBox(self.groupBox_4)
        self.cb_ex_x_end.addItem("")
        self.cb_ex_x_end.addItem("")
        self.cb_ex_x_end.addItem("")
        self.cb_ex_x_end.setObjectName(u"cb_ex_x_end")

        self.gridLayout.addWidget(self.cb_ex_x_end, 2, 0, 1, 1)

        self.cb_ex_y_start = QComboBox(self.groupBox_4)
        self.cb_ex_y_start.addItem("")
        self.cb_ex_y_start.addItem("")
        self.cb_ex_y_start.addItem("")
        self.cb_ex_y_start.setObjectName(u"cb_ex_y_start")

        self.gridLayout.addWidget(self.cb_ex_y_start, 1, 2, 1, 1)

        self.le_z_end = QLineEdit(self.groupBox_4)
        self.le_z_end.setObjectName(u"le_z_end")

        self.gridLayout.addWidget(self.le_z_end, 2, 5, 1, 1)

        self.cb_ex_y_end = QComboBox(self.groupBox_4)
        self.cb_ex_y_end.addItem("")
        self.cb_ex_y_end.addItem("")
        self.cb_ex_y_end.addItem("")
        self.cb_ex_y_end.setObjectName(u"cb_ex_y_end")

        self.gridLayout.addWidget(self.cb_ex_y_end, 2, 2, 1, 1)

        self.cb_ex_x_start = QComboBox(self.groupBox_4)
        self.cb_ex_x_start.addItem("")
        self.cb_ex_x_start.addItem("")
        self.cb_ex_x_start.addItem("")
        self.cb_ex_x_start.setObjectName(u"cb_ex_x_start")

        self.gridLayout.addWidget(self.cb_ex_x_start, 1, 0, 1, 1)

        self.label_9 = QLabel(self.groupBox_4)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_9, 0, 3, 1, 1)

        self.label_8 = QLabel(self.groupBox_4)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_8, 0, 1, 1, 1)

        self.le_x_start = QLineEdit(self.groupBox_4)
        self.le_x_start.setObjectName(u"le_x_start")

        self.gridLayout.addWidget(self.le_x_start, 1, 1, 1, 1)

        self.cb_ex_z_start = QComboBox(self.groupBox_4)
        self.cb_ex_z_start.addItem("")
        self.cb_ex_z_start.addItem("")
        self.cb_ex_z_start.addItem("")
        self.cb_ex_z_start.setObjectName(u"cb_ex_z_start")

        self.gridLayout.addWidget(self.cb_ex_z_start, 1, 4, 1, 1)

        self.le_y_end = QLineEdit(self.groupBox_4)
        self.le_y_end.setObjectName(u"le_y_end")

        self.gridLayout.addWidget(self.le_y_end, 2, 3, 1, 1)

        self.label_10 = QLabel(self.groupBox_4)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_10, 0, 5, 1, 1)

        self.le_z_start = QLineEdit(self.groupBox_4)
        self.le_z_start.setObjectName(u"le_z_start")

        self.gridLayout.addWidget(self.le_z_start, 1, 5, 1, 1)

        self.le_y_start = QLineEdit(self.groupBox_4)
        self.le_y_start.setObjectName(u"le_y_start")

        self.gridLayout.addWidget(self.le_y_start, 1, 3, 1, 1)


        self.gridLayout_2.addWidget(self.groupBox_4, 3, 0, 1, 2)

        self.chb_exclude_borders = QCheckBox(densidad_window)
        self.chb_exclude_borders.setObjectName(u"chb_exclude_borders")

        self.gridLayout_2.addWidget(self.chb_exclude_borders, 4, 0, 1, 1)


        self.retranslateUi(densidad_window)

        QMetaObject.connectSlotsByName(densidad_window)
    # setupUi

    def retranslateUi(self, densidad_window):
        densidad_window.setWindowTitle(QCoreApplication.translate("densidad_window", u"Densidad - PrePRODIC3D", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("densidad_window", u"Regiones", None))

        __sortingEnabled = self.lw_regions.isSortingEnabled()
        self.lw_regions.setSortingEnabled(False)
        ___qlistwidgetitem = self.lw_regions.item(0)
        ___qlistwidgetitem.setText(QCoreApplication.translate("densidad_window", u"Region 1", None));
        self.lw_regions.setSortingEnabled(__sortingEnabled)

        self.pb_add_region.setText(QCoreApplication.translate("densidad_window", u"Agregar una regi\u00f3n", None))
        self.pb_remove_region.setText(QCoreApplication.translate("densidad_window", u"Eliminar \u00faltima regi\u00f3n", None))
        self.groupBox_5.setTitle("")
        self.label_5.setText(QCoreApplication.translate("densidad_window", u"Densidad local", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("densidad_window", u"Conformaci\u00f3n de la regi\u00f3n", None))

        __sortingEnabled1 = self.lw_volumes.isSortingEnabled()
        self.lw_volumes.setSortingEnabled(False)
        ___qlistwidgetitem1 = self.lw_volumes.item(0)
        ___qlistwidgetitem1.setText(QCoreApplication.translate("densidad_window", u"Volumen 1", None));
        self.lw_volumes.setSortingEnabled(__sortingEnabled1)

        self.pb_add_volume.setText(QCoreApplication.translate("densidad_window", u"Agregar un volumen", None))
        self.pb_remove_volume.setText(QCoreApplication.translate("densidad_window", u"Eliminar \u00faltimo volumen", None))
        self.chb_local_value.setText(QCoreApplication.translate("densidad_window", u"Activar variables locales:", None))
        self.groupBox.setTitle(QCoreApplication.translate("densidad_window", u"Densidad general del dominio", None))
        self.label_2.setText(QCoreApplication.translate("densidad_window", u"Valor de densidad", None))
        self.label_3.setText(QCoreApplication.translate("densidad_window", u"Densidad de referencia", None))
        self.label_4.setText(QCoreApplication.translate("densidad_window", u"Temperatura de referencia", None))
        self.label.setText(QCoreApplication.translate("densidad_window", u"Condici\u00f3n", None))
        self.cb_condition.setItemText(0, QCoreApplication.translate("densidad_window", u"Valor constante", None))
        self.cb_condition.setItemText(1, QCoreApplication.translate("densidad_window", u"Dependiente de la temperatura", None))

        self.chb_ex_value.setText("")
        self.groupBox_4.setTitle("")
        self.cb_ex_z_end.setItemText(0, "")
        self.cb_ex_z_end.setItemText(1, QCoreApplication.translate("densidad_window", u"Mayor a", None))
        self.cb_ex_z_end.setItemText(2, QCoreApplication.translate("densidad_window", u"Menor a", None))

        self.cb_ex_x_end.setItemText(0, "")
        self.cb_ex_x_end.setItemText(1, QCoreApplication.translate("densidad_window", u"<", None))
        self.cb_ex_x_end.setItemText(2, QCoreApplication.translate("densidad_window", u"\u2264", None))

        self.cb_ex_y_start.setItemText(0, "")
        self.cb_ex_y_start.setItemText(1, QCoreApplication.translate("densidad_window", u">", None))
        self.cb_ex_y_start.setItemText(2, QCoreApplication.translate("densidad_window", u"\u2265", None))

        self.cb_ex_y_end.setItemText(0, "")
        self.cb_ex_y_end.setItemText(1, QCoreApplication.translate("densidad_window", u"Mayor a", None))
        self.cb_ex_y_end.setItemText(2, QCoreApplication.translate("densidad_window", u"Menor a", None))

        self.cb_ex_x_start.setItemText(0, "")
        self.cb_ex_x_start.setItemText(1, QCoreApplication.translate("densidad_window", u">", None))
        self.cb_ex_x_start.setItemText(2, QCoreApplication.translate("densidad_window", u"\u2265", None))

        self.label_9.setText(QCoreApplication.translate("densidad_window", u"Y", None))
        self.label_8.setText(QCoreApplication.translate("densidad_window", u"X", None))
        self.cb_ex_z_start.setItemText(0, "")
        self.cb_ex_z_start.setItemText(1, QCoreApplication.translate("densidad_window", u"Mayor a", None))
        self.cb_ex_z_start.setItemText(2, QCoreApplication.translate("densidad_window", u"Menor a", None))

        self.label_10.setText(QCoreApplication.translate("densidad_window", u"Z", None))
        self.chb_exclude_borders.setText(QCoreApplication.translate("densidad_window", u"V.C Excluir Bordes", None))
    # retranslateUi

