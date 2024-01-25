# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'variables_window.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
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
    QSizePolicy, QStackedWidget, QWidget)

class Ui_variables_window(object):
    def setupUi(self, variables_window):
        if not variables_window.objectName():
            variables_window.setObjectName(u"variables_window")
        variables_window.resize(479, 573)
        self.gb_variables = QGroupBox(variables_window)
        self.gb_variables.setObjectName(u"gb_variables")
        self.gb_variables.setGeometry(QRect(10, 0, 461, 561))
        self.gb_variables1 = QGroupBox(self.gb_variables)
        self.gb_variables1.setObjectName(u"gb_variables1")
        self.gb_variables1.setGeometry(QRect(10, 20, 441, 201))
        self.formLayout_2 = QFormLayout(self.gb_variables1)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.label = QLabel(self.gb_variables1)
        self.label.setObjectName(u"label")

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.label)

        self.cb_tsimu = QComboBox(self.gb_variables1)
        self.cb_tsimu.addItem("")
        self.cb_tsimu.addItem("")
        self.cb_tsimu.setObjectName(u"cb_tsimu")

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.cb_tsimu)

        self.sw_tsimu = QStackedWidget(self.gb_variables1)
        self.sw_tsimu.setObjectName(u"sw_tsimu")
        self.sw_tsimu_perm = QWidget()
        self.sw_tsimu_perm.setObjectName(u"sw_tsimu_perm")
        self.sw_tsimu.addWidget(self.sw_tsimu_perm)
        self.sw_tsimu_trans = QWidget()
        self.sw_tsimu_trans.setObjectName(u"sw_tsimu_trans")
        self.formLayout = QFormLayout(self.sw_tsimu_trans)
        self.formLayout.setObjectName(u"formLayout")
        self.label_4 = QLabel(self.sw_tsimu_trans)
        self.label_4.setObjectName(u"label_4")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_4)

        self.lineEdit = QLineEdit(self.sw_tsimu_trans)
        self.lineEdit.setObjectName(u"lineEdit")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.lineEdit)

        self.label_5 = QLabel(self.sw_tsimu_trans)
        self.label_5.setObjectName(u"label_5")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_5)

        self.lineEdit_2 = QLineEdit(self.sw_tsimu_trans)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.lineEdit_2)

        self.sw_tsimu.addWidget(self.sw_tsimu_trans)

        self.formLayout_2.setWidget(2, QFormLayout.SpanningRole, self.sw_tsimu)

        self.label_2 = QLabel(self.gb_variables1)
        self.label_2.setObjectName(u"label_2")

        self.formLayout_2.setWidget(4, QFormLayout.LabelRole, self.label_2)

        self.comboBox_2 = QComboBox(self.gb_variables1)
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.setObjectName(u"comboBox_2")

        self.formLayout_2.setWidget(4, QFormLayout.FieldRole, self.comboBox_2)

        self.label_3 = QLabel(self.gb_variables1)
        self.label_3.setObjectName(u"label_3")

        self.formLayout_2.setWidget(5, QFormLayout.LabelRole, self.label_3)

        self.comboBox_3 = QComboBox(self.gb_variables1)
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.setObjectName(u"comboBox_3")

        self.formLayout_2.setWidget(5, QFormLayout.FieldRole, self.comboBox_3)

        self.gb_variables2 = QGroupBox(self.gb_variables)
        self.gb_variables2.setObjectName(u"gb_variables2")
        self.gb_variables2.setGeometry(QRect(0, 220, 451, 331))
        self.gridLayout = QGridLayout(self.gb_variables2)
        self.gridLayout.setObjectName(u"gridLayout")
        self.lineEdit_10 = QLineEdit(self.gb_variables2)
        self.lineEdit_10.setObjectName(u"lineEdit_10")
        self.lineEdit_10.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.lineEdit_10, 7, 2, 1, 1)

        self.lineEdit_7 = QLineEdit(self.gb_variables2)
        self.lineEdit_7.setObjectName(u"lineEdit_7")
        self.lineEdit_7.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.lineEdit_7, 4, 2, 1, 1)

        self.lineEdit_14 = QLineEdit(self.gb_variables2)
        self.lineEdit_14.setObjectName(u"lineEdit_14")
        self.lineEdit_14.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.lineEdit_14, 11, 2, 1, 1)

        self.label_15 = QLabel(self.gb_variables2)
        self.label_15.setObjectName(u"label_15")

        self.gridLayout.addWidget(self.label_15, 7, 0, 1, 1)

        self.lineEdit_11 = QLineEdit(self.gb_variables2)
        self.lineEdit_11.setObjectName(u"lineEdit_11")
        self.lineEdit_11.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.lineEdit_11, 8, 2, 1, 1)

        self.lineEdit_3 = QLineEdit(self.gb_variables2)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.lineEdit_3, 1, 2, 1, 1)

        self.label_13 = QLabel(self.gb_variables2)
        self.label_13.setObjectName(u"label_13")

        self.gridLayout.addWidget(self.label_13, 5, 0, 1, 1)

        self.lineEdit_9 = QLineEdit(self.gb_variables2)
        self.lineEdit_9.setObjectName(u"lineEdit_9")
        self.lineEdit_9.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.lineEdit_9, 6, 2, 1, 1)

        self.label_11 = QLabel(self.gb_variables2)
        self.label_11.setObjectName(u"label_11")

        self.gridLayout.addWidget(self.label_11, 4, 0, 1, 1)

        self.lineEdit_12 = QLineEdit(self.gb_variables2)
        self.lineEdit_12.setObjectName(u"lineEdit_12")
        self.lineEdit_12.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.lineEdit_12, 9, 2, 1, 1)

        self.lineEdit_5 = QLineEdit(self.gb_variables2)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        self.lineEdit_5.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.lineEdit_5, 2, 2, 1, 1)

        self.label_12 = QLabel(self.gb_variables2)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_12, 0, 5, 1, 1)

        self.lineEdit_15 = QLineEdit(self.gb_variables2)
        self.lineEdit_15.setObjectName(u"lineEdit_15")
        self.lineEdit_15.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.lineEdit_15, 12, 2, 1, 1)

        self.label_14 = QLabel(self.gb_variables2)
        self.label_14.setObjectName(u"label_14")

        self.gridLayout.addWidget(self.label_14, 6, 0, 1, 1)

        self.label_16 = QLabel(self.gb_variables2)
        self.label_16.setObjectName(u"label_16")

        self.gridLayout.addWidget(self.label_16, 8, 0, 1, 1)

        self.lineEdit_6 = QLineEdit(self.gb_variables2)
        self.lineEdit_6.setObjectName(u"lineEdit_6")
        self.lineEdit_6.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.lineEdit_6, 3, 2, 1, 1)

        self.label_18 = QLabel(self.gb_variables2)
        self.label_18.setObjectName(u"label_18")

        self.gridLayout.addWidget(self.label_18, 10, 0, 1, 1)

        self.label_9 = QLabel(self.gb_variables2)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout.addWidget(self.label_9, 2, 0, 1, 1)

        self.checkBox = QCheckBox(self.gb_variables2)
        self.checkBox.setObjectName(u"checkBox")

        self.gridLayout.addWidget(self.checkBox, 1, 3, 1, 1)

        self.label_8 = QLabel(self.gb_variables2)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout.addWidget(self.label_8, 1, 0, 1, 1)

        self.lineEdit_13 = QLineEdit(self.gb_variables2)
        self.lineEdit_13.setObjectName(u"lineEdit_13")
        self.lineEdit_13.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.lineEdit_13, 10, 2, 1, 1)

        self.label_6 = QLabel(self.gb_variables2)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout.addWidget(self.label_6, 0, 0, 1, 1)

        self.label_17 = QLabel(self.gb_variables2)
        self.label_17.setObjectName(u"label_17")

        self.gridLayout.addWidget(self.label_17, 9, 0, 1, 1)

        self.lineEdit_8 = QLineEdit(self.gb_variables2)
        self.lineEdit_8.setObjectName(u"lineEdit_8")
        self.lineEdit_8.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.lineEdit_8, 5, 2, 1, 1)

        self.label_10 = QLabel(self.gb_variables2)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout.addWidget(self.label_10, 3, 0, 1, 1)

        self.label_19 = QLabel(self.gb_variables2)
        self.label_19.setObjectName(u"label_19")

        self.gridLayout.addWidget(self.label_19, 11, 0, 1, 1)

        self.lineEdit_4 = QLineEdit(self.gb_variables2)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.lineEdit_4, 1, 5, 1, 1)

        self.label_20 = QLabel(self.gb_variables2)
        self.label_20.setObjectName(u"label_20")

        self.gridLayout.addWidget(self.label_20, 12, 0, 1, 1)

        self.checkBox_2 = QCheckBox(self.gb_variables2)
        self.checkBox_2.setObjectName(u"checkBox_2")

        self.gridLayout.addWidget(self.checkBox_2, 1, 4, 1, 1)

        self.checkBox_4 = QCheckBox(self.gb_variables2)
        self.checkBox_4.setObjectName(u"checkBox_4")

        self.gridLayout.addWidget(self.checkBox_4, 2, 3, 1, 1)

        self.checkBox_5 = QCheckBox(self.gb_variables2)
        self.checkBox_5.setObjectName(u"checkBox_5")

        self.gridLayout.addWidget(self.checkBox_5, 3, 3, 1, 1)

        self.checkBox_6 = QCheckBox(self.gb_variables2)
        self.checkBox_6.setObjectName(u"checkBox_6")

        self.gridLayout.addWidget(self.checkBox_6, 4, 3, 1, 1)

        self.checkBox_7 = QCheckBox(self.gb_variables2)
        self.checkBox_7.setObjectName(u"checkBox_7")

        self.gridLayout.addWidget(self.checkBox_7, 5, 3, 1, 1)

        self.checkBox_8 = QCheckBox(self.gb_variables2)
        self.checkBox_8.setObjectName(u"checkBox_8")

        self.gridLayout.addWidget(self.checkBox_8, 6, 3, 1, 1)

        self.checkBox_9 = QCheckBox(self.gb_variables2)
        self.checkBox_9.setObjectName(u"checkBox_9")

        self.gridLayout.addWidget(self.checkBox_9, 7, 3, 1, 1)

        self.checkBox_10 = QCheckBox(self.gb_variables2)
        self.checkBox_10.setObjectName(u"checkBox_10")

        self.gridLayout.addWidget(self.checkBox_10, 8, 3, 1, 1)

        self.checkBox_11 = QCheckBox(self.gb_variables2)
        self.checkBox_11.setObjectName(u"checkBox_11")

        self.gridLayout.addWidget(self.checkBox_11, 9, 3, 1, 1)

        self.checkBox_12 = QCheckBox(self.gb_variables2)
        self.checkBox_12.setObjectName(u"checkBox_12")

        self.gridLayout.addWidget(self.checkBox_12, 10, 3, 1, 1)

        self.checkBox_13 = QCheckBox(self.gb_variables2)
        self.checkBox_13.setObjectName(u"checkBox_13")

        self.gridLayout.addWidget(self.checkBox_13, 11, 3, 1, 1)

        self.checkBox_14 = QCheckBox(self.gb_variables2)
        self.checkBox_14.setObjectName(u"checkBox_14")

        self.gridLayout.addWidget(self.checkBox_14, 12, 3, 1, 1)

        self.checkBox_15 = QCheckBox(self.gb_variables2)
        self.checkBox_15.setObjectName(u"checkBox_15")

        self.gridLayout.addWidget(self.checkBox_15, 2, 4, 1, 1)

        self.checkBox_16 = QCheckBox(self.gb_variables2)
        self.checkBox_16.setObjectName(u"checkBox_16")

        self.gridLayout.addWidget(self.checkBox_16, 3, 4, 1, 1)

        self.checkBox_17 = QCheckBox(self.gb_variables2)
        self.checkBox_17.setObjectName(u"checkBox_17")

        self.gridLayout.addWidget(self.checkBox_17, 4, 4, 1, 1)

        self.checkBox_18 = QCheckBox(self.gb_variables2)
        self.checkBox_18.setObjectName(u"checkBox_18")

        self.gridLayout.addWidget(self.checkBox_18, 5, 4, 1, 1)

        self.checkBox_19 = QCheckBox(self.gb_variables2)
        self.checkBox_19.setObjectName(u"checkBox_19")

        self.gridLayout.addWidget(self.checkBox_19, 6, 4, 1, 1)

        self.checkBox_20 = QCheckBox(self.gb_variables2)
        self.checkBox_20.setObjectName(u"checkBox_20")

        self.gridLayout.addWidget(self.checkBox_20, 7, 4, 1, 1)

        self.checkBox_21 = QCheckBox(self.gb_variables2)
        self.checkBox_21.setObjectName(u"checkBox_21")

        self.gridLayout.addWidget(self.checkBox_21, 8, 4, 1, 1)

        self.checkBox_22 = QCheckBox(self.gb_variables2)
        self.checkBox_22.setObjectName(u"checkBox_22")

        self.gridLayout.addWidget(self.checkBox_22, 9, 4, 1, 1)

        self.checkBox_23 = QCheckBox(self.gb_variables2)
        self.checkBox_23.setObjectName(u"checkBox_23")

        self.gridLayout.addWidget(self.checkBox_23, 10, 4, 1, 1)

        self.checkBox_24 = QCheckBox(self.gb_variables2)
        self.checkBox_24.setObjectName(u"checkBox_24")

        self.gridLayout.addWidget(self.checkBox_24, 11, 4, 1, 1)

        self.checkBox_25 = QCheckBox(self.gb_variables2)
        self.checkBox_25.setObjectName(u"checkBox_25")

        self.gridLayout.addWidget(self.checkBox_25, 12, 4, 1, 1)

        self.lineEdit_16 = QLineEdit(self.gb_variables2)
        self.lineEdit_16.setObjectName(u"lineEdit_16")
        self.lineEdit_16.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.lineEdit_16, 2, 5, 1, 1)

        self.lineEdit_17 = QLineEdit(self.gb_variables2)
        self.lineEdit_17.setObjectName(u"lineEdit_17")
        self.lineEdit_17.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.lineEdit_17, 3, 5, 1, 1)

        self.lineEdit_18 = QLineEdit(self.gb_variables2)
        self.lineEdit_18.setObjectName(u"lineEdit_18")
        self.lineEdit_18.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.lineEdit_18, 4, 5, 1, 1)

        self.lineEdit_19 = QLineEdit(self.gb_variables2)
        self.lineEdit_19.setObjectName(u"lineEdit_19")
        self.lineEdit_19.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.lineEdit_19, 5, 5, 1, 1)

        self.lineEdit_20 = QLineEdit(self.gb_variables2)
        self.lineEdit_20.setObjectName(u"lineEdit_20")
        self.lineEdit_20.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.lineEdit_20, 6, 5, 1, 1)

        self.lineEdit_21 = QLineEdit(self.gb_variables2)
        self.lineEdit_21.setObjectName(u"lineEdit_21")
        self.lineEdit_21.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.lineEdit_21, 7, 5, 1, 1)

        self.lineEdit_22 = QLineEdit(self.gb_variables2)
        self.lineEdit_22.setObjectName(u"lineEdit_22")
        self.lineEdit_22.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.lineEdit_22, 8, 5, 1, 1)

        self.lineEdit_23 = QLineEdit(self.gb_variables2)
        self.lineEdit_23.setObjectName(u"lineEdit_23")
        self.lineEdit_23.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.lineEdit_23, 9, 5, 1, 1)

        self.lineEdit_24 = QLineEdit(self.gb_variables2)
        self.lineEdit_24.setObjectName(u"lineEdit_24")
        self.lineEdit_24.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.lineEdit_24, 10, 5, 1, 1)

        self.lineEdit_25 = QLineEdit(self.gb_variables2)
        self.lineEdit_25.setObjectName(u"lineEdit_25")
        self.lineEdit_25.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.lineEdit_25, 11, 5, 1, 1)

        self.lineEdit_26 = QLineEdit(self.gb_variables2)
        self.lineEdit_26.setObjectName(u"lineEdit_26")
        self.lineEdit_26.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.lineEdit_26, 12, 5, 1, 1)

        self.label_7 = QLabel(self.gb_variables2)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_7, 0, 2, 1, 1)

        self.checkBox_3 = QCheckBox(self.gb_variables2)
        self.checkBox_3.setObjectName(u"checkBox_3")

        self.gridLayout.addWidget(self.checkBox_3, 13, 2, 1, 2)


        self.retranslateUi(variables_window)

        self.sw_tsimu.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(variables_window)
    # setupUi

    def retranslateUi(self, variables_window):
        variables_window.setWindowTitle(QCoreApplication.translate("variables_window", u"Variables - PrePRODIC3D", None))
        self.gb_variables.setTitle(QCoreApplication.translate("variables_window", u"Variables", None))
        self.gb_variables1.setTitle(QCoreApplication.translate("variables_window", u"Condiciones de la simulaci\u00f3n", None))
        self.label.setText(QCoreApplication.translate("variables_window", u"Tipo de simulaci\u00f3n", None))
        self.cb_tsimu.setItemText(0, QCoreApplication.translate("variables_window", u"Permanente", None))
        self.cb_tsimu.setItemText(1, QCoreApplication.translate("variables_window", u"Transitorio", None))

        self.label_4.setText(QCoreApplication.translate("variables_window", u"Numero de pasos en el tiempo (IPTM)", None))
        self.lineEdit.setText("")
        self.label_5.setText(QCoreApplication.translate("variables_window", u"Intervalo de tiempo (DT)", None))
        self.label_2.setText(QCoreApplication.translate("variables_window", u"Tipo de flujo", None))
        self.comboBox_2.setItemText(0, QCoreApplication.translate("variables_window", u"Difusivo", None))
        self.comboBox_2.setItemText(1, QCoreApplication.translate("variables_window", u"Convectivo", None))

        self.label_3.setText(QCoreApplication.translate("variables_window", u"Condiciones de tratamiento de borde", None))
        self.comboBox_3.setItemText(0, QCoreApplication.translate("variables_window", u"Esquema de bajo orden", None))
        self.comboBox_3.setItemText(1, QCoreApplication.translate("variables_window", u"Esquema de alto orden", None))

        self.gb_variables2.setTitle(QCoreApplication.translate("variables_window", u"Variables a resolver", None))
        self.lineEdit_7.setText(QCoreApplication.translate("variables_window", u"Correcci\u00f3n de presi\u00f3n", None))
        self.label_15.setText(QCoreApplication.translate("variables_window", u"7", None))
        self.lineEdit_3.setText(QCoreApplication.translate("variables_window", u"Velocidad U", None))
        self.label_13.setText(QCoreApplication.translate("variables_window", u"5", None))
        self.label_11.setText(QCoreApplication.translate("variables_window", u"4", None))
        self.lineEdit_5.setText(QCoreApplication.translate("variables_window", u"Velocidad V", None))
        self.label_12.setText(QCoreApplication.translate("variables_window", u"Relajamiento", None))
        self.label_14.setText(QCoreApplication.translate("variables_window", u"6", None))
        self.label_16.setText(QCoreApplication.translate("variables_window", u"8", None))
        self.lineEdit_6.setText(QCoreApplication.translate("variables_window", u"Velocidad W", None))
        self.label_18.setText(QCoreApplication.translate("variables_window", u"10", None))
        self.label_9.setText(QCoreApplication.translate("variables_window", u"2", None))
        self.checkBox.setText(QCoreApplication.translate("variables_window", u"Resolver", None))
        self.label_8.setText(QCoreApplication.translate("variables_window", u"1", None))
        self.label_6.setText(QCoreApplication.translate("variables_window", u"No.", None))
        self.label_17.setText(QCoreApplication.translate("variables_window", u"9", None))
        self.lineEdit_8.setText(QCoreApplication.translate("variables_window", u"Temperatura", None))
        self.label_10.setText(QCoreApplication.translate("variables_window", u"3", None))
        self.label_19.setText(QCoreApplication.translate("variables_window", u"11", None))
        self.label_20.setText(QCoreApplication.translate("variables_window", u"12", None))
        self.checkBox_2.setText(QCoreApplication.translate("variables_window", u"Imprimir", None))
        self.checkBox_4.setText(QCoreApplication.translate("variables_window", u"Resolver", None))
        self.checkBox_5.setText(QCoreApplication.translate("variables_window", u"Resolver", None))
        self.checkBox_6.setText(QCoreApplication.translate("variables_window", u"Resolver", None))
        self.checkBox_7.setText(QCoreApplication.translate("variables_window", u"Resolver", None))
        self.checkBox_8.setText(QCoreApplication.translate("variables_window", u"Resolver", None))
        self.checkBox_9.setText(QCoreApplication.translate("variables_window", u"Resolver", None))
        self.checkBox_10.setText(QCoreApplication.translate("variables_window", u"Resolver", None))
        self.checkBox_11.setText(QCoreApplication.translate("variables_window", u"Resolver", None))
        self.checkBox_12.setText(QCoreApplication.translate("variables_window", u"Resolver", None))
        self.checkBox_13.setText(QCoreApplication.translate("variables_window", u"Resolver", None))
        self.checkBox_14.setText(QCoreApplication.translate("variables_window", u"Resolver", None))
        self.checkBox_15.setText(QCoreApplication.translate("variables_window", u"Imprimir", None))
        self.checkBox_16.setText(QCoreApplication.translate("variables_window", u"Imprimir", None))
        self.checkBox_17.setText(QCoreApplication.translate("variables_window", u"Imprimir", None))
        self.checkBox_18.setText(QCoreApplication.translate("variables_window", u"Imprimir", None))
        self.checkBox_19.setText(QCoreApplication.translate("variables_window", u"Imprimir", None))
        self.checkBox_20.setText(QCoreApplication.translate("variables_window", u"Imprimir", None))
        self.checkBox_21.setText(QCoreApplication.translate("variables_window", u"Imprimir", None))
        self.checkBox_22.setText(QCoreApplication.translate("variables_window", u"Imprimir", None))
        self.checkBox_23.setText(QCoreApplication.translate("variables_window", u"Imprimir", None))
        self.checkBox_24.setText(QCoreApplication.translate("variables_window", u"Imprimir", None))
        self.checkBox_25.setText(QCoreApplication.translate("variables_window", u"Imprimir", None))
        self.label_7.setText(QCoreApplication.translate("variables_window", u"Variables", None))
        self.checkBox_3.setText(QCoreApplication.translate("variables_window", u"Tratar variable 4 como temperatura", None))
    # retranslateUi

