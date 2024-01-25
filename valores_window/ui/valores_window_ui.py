# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'valores_window.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QFormLayout, QGridLayout,
    QGroupBox, QHBoxLayout, QLabel, QLineEdit,
    QListWidget, QListWidgetItem, QPushButton, QScrollArea,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

class Ui_valores_window(object):
    def setupUi(self, valores_window):
        if not valores_window.objectName():
            valores_window.setObjectName(u"valores_window")
        valores_window.resize(585, 414)
        self.gridLayout_3 = QGridLayout(valores_window)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.scrollArea = QScrollArea(valores_window)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 548, 741))
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
        self.listWidget = QListWidget(self.groupBox_3)
        QListWidgetItem(self.listWidget)
        self.listWidget.setObjectName(u"listWidget")

        self.gridLayout_2.addWidget(self.listWidget, 0, 0, 1, 1)


        self.horizontalLayout.addWidget(self.groupBox_3)

        self.groupBox_4 = QGroupBox(self.groupBox_2)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.formLayout_2 = QFormLayout(self.groupBox_4)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.label = QLabel(self.groupBox_4)
        self.label.setObjectName(u"label")

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.label)

        self.lineEdit = QLineEdit(self.groupBox_4)
        self.lineEdit.setObjectName(u"lineEdit")

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.lineEdit)

        self.label_2 = QLabel(self.groupBox_4)
        self.label_2.setObjectName(u"label_2")

        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.label_2)

        self.lineEdit_2 = QLineEdit(self.groupBox_4)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.lineEdit_2)

        self.checkBox = QCheckBox(self.groupBox_4)
        self.checkBox.setObjectName(u"checkBox")

        self.formLayout_2.setWidget(2, QFormLayout.SpanningRole, self.checkBox)

        self.groupBox_5 = QGroupBox(self.groupBox_4)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.formLayout = QFormLayout(self.groupBox_5)
        self.formLayout.setObjectName(u"formLayout")
        self.label_3 = QLabel(self.groupBox_5)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_3)

        self.lineEdit_3 = QLineEdit(self.groupBox_5)
        self.lineEdit_3.setObjectName(u"lineEdit_3")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.lineEdit_3)

        self.label_4 = QLabel(self.groupBox_5)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setAlignment(Qt.AlignCenter)

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_4)

        self.lineEdit_4 = QLineEdit(self.groupBox_5)
        self.lineEdit_4.setObjectName(u"lineEdit_4")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.lineEdit_4)

        self.label_5 = QLabel(self.groupBox_5)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setAlignment(Qt.AlignCenter)

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_5)

        self.lineEdit_5 = QLineEdit(self.groupBox_5)
        self.lineEdit_5.setObjectName(u"lineEdit_5")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.lineEdit_5)


        self.formLayout_2.setWidget(3, QFormLayout.SpanningRole, self.groupBox_5)


        self.horizontalLayout.addWidget(self.groupBox_4)


        self.verticalLayout_2.addWidget(self.groupBox_2)

        self.checkBox_2 = QCheckBox(self.groupBox)
        self.checkBox_2.setObjectName(u"checkBox_2")

        self.verticalLayout_2.addWidget(self.checkBox_2)

        self.groupBox_6 = QGroupBox(self.groupBox)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.horizontalLayout_2 = QHBoxLayout(self.groupBox_6)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.groupBox_7 = QGroupBox(self.groupBox_6)
        self.groupBox_7.setObjectName(u"groupBox_7")
        self.groupBox_7.setLayoutDirection(Qt.RightToLeft)
        self.formLayout_3 = QFormLayout(self.groupBox_7)
        self.formLayout_3.setObjectName(u"formLayout_3")
        self.pushButton = QPushButton(self.groupBox_7)
        self.pushButton.setObjectName(u"pushButton")

        self.formLayout_3.setWidget(2, QFormLayout.SpanningRole, self.pushButton)

        self.pushButton_2 = QPushButton(self.groupBox_7)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.formLayout_3.setWidget(4, QFormLayout.SpanningRole, self.pushButton_2)

        self.listWidget_2 = QListWidget(self.groupBox_7)
        self.listWidget_2.setObjectName(u"listWidget_2")

        self.formLayout_3.setWidget(0, QFormLayout.SpanningRole, self.listWidget_2)

        self.lineEdit_6 = QLineEdit(self.groupBox_7)
        self.lineEdit_6.setObjectName(u"lineEdit_6")

        self.formLayout_3.setWidget(10, QFormLayout.LabelRole, self.lineEdit_6)

        self.label_6 = QLabel(self.groupBox_7)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setAlignment(Qt.AlignCenter)

        self.formLayout_3.setWidget(10, QFormLayout.FieldRole, self.label_6)

        self.lineEdit_7 = QLineEdit(self.groupBox_7)
        self.lineEdit_7.setObjectName(u"lineEdit_7")

        self.formLayout_3.setWidget(11, QFormLayout.LabelRole, self.lineEdit_7)

        self.label_7 = QLabel(self.groupBox_7)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setAlignment(Qt.AlignCenter)

        self.formLayout_3.setWidget(11, QFormLayout.FieldRole, self.label_7)

        self.lineEdit_8 = QLineEdit(self.groupBox_7)
        self.lineEdit_8.setObjectName(u"lineEdit_8")

        self.formLayout_3.setWidget(14, QFormLayout.LabelRole, self.lineEdit_8)

        self.label_8 = QLabel(self.groupBox_7)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setAlignment(Qt.AlignCenter)

        self.formLayout_3.setWidget(14, QFormLayout.FieldRole, self.label_8)

        self.lineEdit_9 = QLineEdit(self.groupBox_7)
        self.lineEdit_9.setObjectName(u"lineEdit_9")

        self.formLayout_3.setWidget(17, QFormLayout.LabelRole, self.lineEdit_9)

        self.label_9 = QLabel(self.groupBox_7)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setAlignment(Qt.AlignCenter)

        self.formLayout_3.setWidget(17, QFormLayout.FieldRole, self.label_9)

        self.checkBox_4 = QCheckBox(self.groupBox_7)
        self.checkBox_4.setObjectName(u"checkBox_4")

        self.formLayout_3.setWidget(8, QFormLayout.FieldRole, self.checkBox_4)

        self.checkBox_3 = QCheckBox(self.groupBox_7)
        self.checkBox_3.setObjectName(u"checkBox_3")

        self.formLayout_3.setWidget(8, QFormLayout.LabelRole, self.checkBox_3)


        self.horizontalLayout_2.addWidget(self.groupBox_7)

        self.groupBox_8 = QGroupBox(self.groupBox_6)
        self.groupBox_8.setObjectName(u"groupBox_8")
        self.verticalLayout = QVBoxLayout(self.groupBox_8)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.listWidget_3 = QListWidget(self.groupBox_8)
        self.listWidget_3.setObjectName(u"listWidget_3")

        self.verticalLayout.addWidget(self.listWidget_3)

        self.pushButton_4 = QPushButton(self.groupBox_8)
        self.pushButton_4.setObjectName(u"pushButton_4")

        self.verticalLayout.addWidget(self.pushButton_4)

        self.pushButton_3 = QPushButton(self.groupBox_8)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.verticalLayout.addWidget(self.pushButton_3)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.groupBox_9 = QGroupBox(self.groupBox_8)
        self.groupBox_9.setObjectName(u"groupBox_9")
        self.gridLayout = QGridLayout(self.groupBox_9)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_10 = QLabel(self.groupBox_9)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout.addWidget(self.label_10, 2, 0, 1, 1)

        self.lineEdit_13 = QLineEdit(self.groupBox_9)
        self.lineEdit_13.setObjectName(u"lineEdit_13")
        sizePolicy = QSizePolicy(QSizePolicy.Ignored, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_13.sizePolicy().hasHeightForWidth())
        self.lineEdit_13.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.lineEdit_13, 2, 2, 1, 1)

        self.lineEdit_10 = QLineEdit(self.groupBox_9)
        self.lineEdit_10.setObjectName(u"lineEdit_10")
        sizePolicy.setHeightForWidth(self.lineEdit_10.sizePolicy().hasHeightForWidth())
        self.lineEdit_10.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.lineEdit_10, 1, 1, 1, 1)

        self.lineEdit_11 = QLineEdit(self.groupBox_9)
        self.lineEdit_11.setObjectName(u"lineEdit_11")
        sizePolicy.setHeightForWidth(self.lineEdit_11.sizePolicy().hasHeightForWidth())
        self.lineEdit_11.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.lineEdit_11, 1, 2, 1, 1)

        self.lineEdit_12 = QLineEdit(self.groupBox_9)
        self.lineEdit_12.setObjectName(u"lineEdit_12")
        sizePolicy.setHeightForWidth(self.lineEdit_12.sizePolicy().hasHeightForWidth())
        self.lineEdit_12.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.lineEdit_12, 2, 1, 1, 1)

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

        self.lineEdit_14 = QLineEdit(self.groupBox_9)
        self.lineEdit_14.setObjectName(u"lineEdit_14")
        sizePolicy.setHeightForWidth(self.lineEdit_14.sizePolicy().hasHeightForWidth())
        self.lineEdit_14.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.lineEdit_14, 1, 3, 1, 1)

        self.lineEdit_15 = QLineEdit(self.groupBox_9)
        self.lineEdit_15.setObjectName(u"lineEdit_15")
        sizePolicy.setHeightForWidth(self.lineEdit_15.sizePolicy().hasHeightForWidth())
        self.lineEdit_15.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.lineEdit_15, 2, 3, 1, 1)


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

        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        ___qlistwidgetitem = self.listWidget.item(0)
        ___qlistwidgetitem.setText(QCoreApplication.translate("valores_window", u"Temperatura", None));
        self.listWidget.setSortingEnabled(__sortingEnabled)

        self.groupBox_4.setTitle("")
        self.label.setText(QCoreApplication.translate("valores_window", u"Valor general", None))
        self.label_2.setText(QCoreApplication.translate("valores_window", u"k", None))
        self.checkBox.setText(QCoreApplication.translate("valores_window", u"Activar flotabilidad", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("valores_window", u"Flotabilidad", None))
        self.label_3.setText(QCoreApplication.translate("valores_window", u"Coef. exp. term.", None))
        self.label_4.setText(QCoreApplication.translate("valores_window", u"Gravedad", None))
        self.label_5.setText(QCoreApplication.translate("valores_window", u"\u00c1ngulo", None))
        self.checkBox_2.setText(QCoreApplication.translate("valores_window", u"Para aplicar valores locales para alguna variable, active la siguiente casilla", None))
        self.groupBox_6.setTitle(QCoreApplication.translate("valores_window", u"Valores locales por variable", None))
        self.groupBox_7.setTitle(QCoreApplication.translate("valores_window", u"Regiones", None))
        self.pushButton.setText(QCoreApplication.translate("valores_window", u"Agregar una regi\u00f3n", None))
        self.pushButton_2.setText(QCoreApplication.translate("valores_window", u"Eliminar \u00faltima regi\u00f3n", None))
        self.label_6.setText(QCoreApplication.translate("valores_window", u"Valor local", None))
        self.label_7.setText(QCoreApplication.translate("valores_window", u"Sc", None))
        self.label_8.setText(QCoreApplication.translate("valores_window", u"Sp", None))
        self.label_9.setText(QCoreApplication.translate("valores_window", u"k local", None))
        self.checkBox_4.setText(QCoreApplication.translate("valores_window", u"Valor fijo", None))
        self.checkBox_3.setText(QCoreApplication.translate("valores_window", u"Fuente lineal", None))
        self.groupBox_8.setTitle(QCoreApplication.translate("valores_window", u"Conformaci\u00f3n de la regi\u00f3n", None))
        self.pushButton_4.setText(QCoreApplication.translate("valores_window", u"Agregar un \u00e1rea", None))
        self.pushButton_3.setText(QCoreApplication.translate("valores_window", u"Eliminar \u00faltima \u00e1rea", None))
        self.groupBox_9.setTitle("")
        self.label_10.setText(QCoreApplication.translate("valores_window", u"Longitud", None))
        self.label_12.setText(QCoreApplication.translate("valores_window", u"X", None))
        self.label_13.setText(QCoreApplication.translate("valores_window", u"Y", None))
        self.label_11.setText(QCoreApplication.translate("valores_window", u"Inicio", None))
        self.label_14.setText(QCoreApplication.translate("valores_window", u"Z", None))
    # retranslateUi

