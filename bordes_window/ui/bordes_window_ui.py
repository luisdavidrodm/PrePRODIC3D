# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'bordes_window.ui'
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
    QListWidget, QListWidgetItem, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_bordes_window(object):
    def setupUi(self, bordes_window):
        if not bordes_window.objectName():
            bordes_window.setObjectName(u"bordes_window")
        bordes_window.resize(445, 490)
        self.gridLayout_3 = QGridLayout(bordes_window)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.groupBox = QGroupBox(bordes_window)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout = QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.listWidget_2 = QListWidget(self.groupBox)
        QListWidgetItem(self.listWidget_2)
        self.listWidget_2.setObjectName(u"listWidget_2")

        self.gridLayout.addWidget(self.listWidget_2, 2, 3, 1, 1, Qt.AlignHCenter)

        self.listWidget = QListWidget(self.groupBox)
        QListWidgetItem(self.listWidget)
        QListWidgetItem(self.listWidget)
        QListWidgetItem(self.listWidget)
        QListWidgetItem(self.listWidget)
        QListWidgetItem(self.listWidget)
        QListWidgetItem(self.listWidget)
        self.listWidget.setObjectName(u"listWidget")

        self.gridLayout.addWidget(self.listWidget, 2, 0, 1, 3)

        self.lineEdit = QLineEdit(self.groupBox)
        self.lineEdit.setObjectName(u"lineEdit")

        self.gridLayout.addWidget(self.lineEdit, 0, 3, 1, 1)

        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 2)

        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 1, 3, 1, 1)

        self.pushButton = QPushButton(self.groupBox)
        self.pushButton.setObjectName(u"pushButton")

        self.gridLayout.addWidget(self.pushButton, 4, 0, 1, 4)

        self.pushButton_2 = QPushButton(self.groupBox)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.gridLayout.addWidget(self.pushButton_2, 3, 0, 1, 4)


        self.gridLayout_3.addWidget(self.groupBox, 0, 0, 1, 1)

        self.groupBox_2 = QGroupBox(bordes_window)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.verticalLayout = QVBoxLayout(self.groupBox_2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.checkBox = QCheckBox(self.groupBox_2)
        self.checkBox.setObjectName(u"checkBox")

        self.verticalLayout.addWidget(self.checkBox)

        self.checkBox_3 = QCheckBox(self.groupBox_2)
        self.checkBox_3.setObjectName(u"checkBox_3")

        self.verticalLayout.addWidget(self.checkBox_3)

        self.checkBox_4 = QCheckBox(self.groupBox_2)
        self.checkBox_4.setObjectName(u"checkBox_4")

        self.verticalLayout.addWidget(self.checkBox_4)

        self.checkBox_5 = QCheckBox(self.groupBox_2)
        self.checkBox_5.setObjectName(u"checkBox_5")

        self.verticalLayout.addWidget(self.checkBox_5)


        self.gridLayout_3.addWidget(self.groupBox_2, 0, 1, 1, 1)

        self.groupBox_3 = QGroupBox(bordes_window)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.horizontalLayout = QHBoxLayout(self.groupBox_3)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.groupBox_6 = QGroupBox(self.groupBox_3)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.gridLayout_2 = QGridLayout(self.groupBox_6)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.listWidget_3 = QListWidget(self.groupBox_6)
        QListWidgetItem(self.listWidget_3)
        self.listWidget_3.setObjectName(u"listWidget_3")

        self.gridLayout_2.addWidget(self.listWidget_3, 0, 0, 1, 1)


        self.horizontalLayout.addWidget(self.groupBox_6)

        self.groupBox_7 = QGroupBox(self.groupBox_3)
        self.groupBox_7.setObjectName(u"groupBox_7")
        self.verticalLayout_2 = QVBoxLayout(self.groupBox_7)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.checkBox_6 = QCheckBox(self.groupBox_7)
        self.checkBox_6.setObjectName(u"checkBox_6")

        self.verticalLayout_2.addWidget(self.checkBox_6)

        self.checkBox_7 = QCheckBox(self.groupBox_7)
        self.checkBox_7.setObjectName(u"checkBox_7")

        self.verticalLayout_2.addWidget(self.checkBox_7)

        self.checkBox_8 = QCheckBox(self.groupBox_7)
        self.checkBox_8.setObjectName(u"checkBox_8")

        self.verticalLayout_2.addWidget(self.checkBox_8)


        self.horizontalLayout.addWidget(self.groupBox_7)

        self.groupBox_8 = QGroupBox(self.groupBox_3)
        self.groupBox_8.setObjectName(u"groupBox_8")
        self.verticalLayout_3 = QVBoxLayout(self.groupBox_8)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_7 = QLabel(self.groupBox_8)
        self.label_7.setObjectName(u"label_7")

        self.verticalLayout_3.addWidget(self.label_7)

        self.lineEdit_5 = QLineEdit(self.groupBox_8)
        self.lineEdit_5.setObjectName(u"lineEdit_5")

        self.verticalLayout_3.addWidget(self.lineEdit_5)

        self.label_8 = QLabel(self.groupBox_8)
        self.label_8.setObjectName(u"label_8")

        self.verticalLayout_3.addWidget(self.label_8)

        self.lineEdit_6 = QLineEdit(self.groupBox_8)
        self.lineEdit_6.setObjectName(u"lineEdit_6")

        self.verticalLayout_3.addWidget(self.lineEdit_6)


        self.horizontalLayout.addWidget(self.groupBox_8)


        self.gridLayout_3.addWidget(self.groupBox_3, 1, 0, 1, 2)

        self.groupBox_4 = QGroupBox(bordes_window)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.gridLayout_4 = QGridLayout(self.groupBox_4)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.label_4 = QLabel(self.groupBox_4)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_4.addWidget(self.label_4, 0, 0, 1, 1)

        self.lineEdit_2 = QLineEdit(self.groupBox_4)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.gridLayout_4.addWidget(self.lineEdit_2, 0, 1, 1, 1)

        self.label_5 = QLabel(self.groupBox_4)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_4.addWidget(self.label_5, 1, 0, 1, 1)

        self.lineEdit_3 = QLineEdit(self.groupBox_4)
        self.lineEdit_3.setObjectName(u"lineEdit_3")

        self.gridLayout_4.addWidget(self.lineEdit_3, 1, 1, 1, 1)


        self.gridLayout_3.addWidget(self.groupBox_4, 2, 0, 1, 1)

        self.groupBox_5 = QGroupBox(bordes_window)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.formLayout_2 = QFormLayout(self.groupBox_5)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.label_6 = QLabel(self.groupBox_5)
        self.label_6.setObjectName(u"label_6")

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.label_6)

        self.lineEdit_4 = QLineEdit(self.groupBox_5)
        self.lineEdit_4.setObjectName(u"lineEdit_4")

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.lineEdit_4)


        self.gridLayout_3.addWidget(self.groupBox_5, 2, 1, 1, 1)


        self.retranslateUi(bordes_window)

        QMetaObject.connectSlotsByName(bordes_window)
    # setupUi

    def retranslateUi(self, bordes_window):
        bordes_window.setWindowTitle(QCoreApplication.translate("bordes_window", u"Bordes - PrePRODIC3D", None))
        self.groupBox.setTitle(QCoreApplication.translate("bordes_window", u"Divisi\u00f3n de bordes", None))
        self.label.setText(QCoreApplication.translate("bordes_window", u"Longitud", None))

        __sortingEnabled = self.listWidget_2.isSortingEnabled()
        self.listWidget_2.setSortingEnabled(False)
        ___qlistwidgetitem = self.listWidget_2.item(0)
        ___qlistwidgetitem.setText(QCoreApplication.translate("bordes_window", u"Segmento 1", None));
        self.listWidget_2.setSortingEnabled(__sortingEnabled)


        __sortingEnabled1 = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        ___qlistwidgetitem1 = self.listWidget.item(0)
        ___qlistwidgetitem1.setText(QCoreApplication.translate("bordes_window", u"X Max", None));
        ___qlistwidgetitem2 = self.listWidget.item(1)
        ___qlistwidgetitem2.setText(QCoreApplication.translate("bordes_window", u"X Min", None));
        ___qlistwidgetitem3 = self.listWidget.item(2)
        ___qlistwidgetitem3.setText(QCoreApplication.translate("bordes_window", u"Y Max", None));
        ___qlistwidgetitem4 = self.listWidget.item(3)
        ___qlistwidgetitem4.setText(QCoreApplication.translate("bordes_window", u"Y Min", None));
        ___qlistwidgetitem5 = self.listWidget.item(4)
        ___qlistwidgetitem5.setText(QCoreApplication.translate("bordes_window", u"Z Max", None));
        ___qlistwidgetitem6 = self.listWidget.item(5)
        ___qlistwidgetitem6.setText(QCoreApplication.translate("bordes_window", u"Z Min", None));
        self.listWidget.setSortingEnabled(__sortingEnabled1)

        self.label_2.setText(QCoreApplication.translate("bordes_window", u"Borde", None))
        self.label_3.setText(QCoreApplication.translate("bordes_window", u"Segmento", None))
        self.pushButton.setText(QCoreApplication.translate("bordes_window", u"Eliminar \u00faltimo segmento", None))
        self.pushButton_2.setText(QCoreApplication.translate("bordes_window", u"Agregar un segmento", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("bordes_window", u"Tipo de segmento", None))
        self.checkBox.setText(QCoreApplication.translate("bordes_window", u"Pared", None))
        self.checkBox_3.setText(QCoreApplication.translate("bordes_window", u"Entrada de la masa", None))
        self.checkBox_4.setText(QCoreApplication.translate("bordes_window", u"Salida de la masa", None))
        self.checkBox_5.setText(QCoreApplication.translate("bordes_window", u"Nodos internos", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("bordes_window", u"Variables escalares", None))
        self.groupBox_6.setTitle("")

        __sortingEnabled2 = self.listWidget_3.isSortingEnabled()
        self.listWidget_3.setSortingEnabled(False)
        ___qlistwidgetitem7 = self.listWidget_3.item(0)
        ___qlistwidgetitem7.setText(QCoreApplication.translate("bordes_window", u"Temperatura", None));
        self.listWidget_3.setSortingEnabled(__sortingEnabled2)

        self.groupBox_7.setTitle("")
        self.checkBox_6.setText(QCoreApplication.translate("bordes_window", u"Valor", None))
        self.checkBox_7.setText(QCoreApplication.translate("bordes_window", u"Flujo", None))
        self.checkBox_8.setText(QCoreApplication.translate("bordes_window", u"Convecci\u00f3n", None))
        self.groupBox_8.setTitle("")
        self.label_7.setText(QCoreApplication.translate("bordes_window", u"Valor", None))
        self.label_8.setText(QCoreApplication.translate("bordes_window", u"Temp. ambiente", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("bordes_window", u"Velocidad", None))
        self.label_4.setText(QCoreApplication.translate("bordes_window", u"Normal", None))
        self.label_5.setText(QCoreApplication.translate("bordes_window", u"Tangencial", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("bordes_window", u"Salida de la masa", None))
        self.label_6.setText(QCoreApplication.translate("bordes_window", u"Fracci\u00f3n", None))
    # retranslateUi

