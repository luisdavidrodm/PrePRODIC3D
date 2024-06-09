# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'inicio_window.ui'
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
from PySide6.QtWidgets import QApplication, QDialog, QGroupBox, QLineEdit, QSizePolicy, QVBoxLayout, QWidget
from Recursos import recursos_rc


class Ui_inicio_window(object):
    def setupUi(self, inicio_window):
        if not inicio_window.objectName():
            inicio_window.setObjectName("inicio_window")
        inicio_window.resize(402, 317)
        icon = QIcon()
        icon.addFile(":/Icon/icon/prodic_icon.jpg", QSize(), QIcon.Normal, QIcon.Off)
        inicio_window.setWindowIcon(icon)
        self.verticalLayout_5 = QVBoxLayout(inicio_window)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.gb_inicio = QGroupBox(inicio_window)
        self.gb_inicio.setObjectName("gb_inicio")
        self.verticalLayout_4 = QVBoxLayout(self.gb_inicio)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.gb_inicio_titulosimu = QGroupBox(self.gb_inicio)
        self.gb_inicio_titulosimu.setObjectName("gb_inicio_titulosimu")
        self.verticalLayout = QVBoxLayout(self.gb_inicio_titulosimu)
        self.verticalLayout.setObjectName("verticalLayout")
        self.le_titulosimu = QLineEdit(self.gb_inicio_titulosimu)
        self.le_titulosimu.setObjectName("le_titulosimu")

        self.verticalLayout.addWidget(self.le_titulosimu)

        self.verticalLayout_4.addWidget(self.gb_inicio_titulosimu)

        self.gb_inicio_tituloimpre = QGroupBox(self.gb_inicio)
        self.gb_inicio_tituloimpre.setObjectName("gb_inicio_tituloimpre")
        self.verticalLayout_2 = QVBoxLayout(self.gb_inicio_tituloimpre)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.le_tituloimpre = QLineEdit(self.gb_inicio_tituloimpre)
        self.le_tituloimpre.setObjectName("le_tituloimpre")

        self.verticalLayout_2.addWidget(self.le_tituloimpre)

        self.verticalLayout_4.addWidget(self.gb_inicio_tituloimpre)

        self.gb_inicio_titulograf = QGroupBox(self.gb_inicio)
        self.gb_inicio_titulograf.setObjectName("gb_inicio_titulograf")
        self.verticalLayout_3 = QVBoxLayout(self.gb_inicio_titulograf)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.le_titulograf = QLineEdit(self.gb_inicio_titulograf)
        self.le_titulograf.setObjectName("le_titulograf")

        self.verticalLayout_3.addWidget(self.le_titulograf)

        self.verticalLayout_4.addWidget(self.gb_inicio_titulograf)

        self.verticalLayout_5.addWidget(self.gb_inicio)

        self.retranslateUi(inicio_window)

        QMetaObject.connectSlotsByName(inicio_window)

    # setupUi

    def retranslateUi(self, inicio_window):
        inicio_window.setWindowTitle(QCoreApplication.translate("inicio_window", "Inicio - PrePRODIC3D", None))
        self.gb_inicio.setTitle(QCoreApplication.translate("inicio_window", "Inicio", None))
        self.gb_inicio_titulosimu.setTitle(
            QCoreApplication.translate("inicio_window", "Titulo de la simulaci\u00f3n", None)
        )
        self.le_titulosimu.setInputMask("")
        self.le_titulosimu.setText(QCoreApplication.translate("inicio_window", "Sin t\u00edtulo", None))
        self.gb_inicio_tituloimpre.setTitle(
            QCoreApplication.translate(
                "inicio_window", "Nombre del archivo de impresi\u00f3n (m\u00e1x. 8 caracteres)", None
            )
        )
        self.le_tituloimpre.setText(QCoreApplication.translate("inicio_window", "Print1", None))
        self.gb_inicio_titulograf.setTitle(
            QCoreApplication.translate(
                "inicio_window", "Nombre del archivo gr\u00e1fico (m\u00e1x. 8 caracteres)", None
            )
        )
        self.le_titulograf.setText(QCoreApplication.translate("inicio_window", "Plot1", None))

    # retranslateUi
