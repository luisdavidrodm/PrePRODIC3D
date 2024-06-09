# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'variables_window.ui'
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
from PySide6.QtWidgets import (
    QApplication,
    QCheckBox,
    QComboBox,
    QFormLayout,
    QGridLayout,
    QGroupBox,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QSizePolicy,
    QStackedWidget,
    QVBoxLayout,
    QWidget,
)
from Recursos import recursos_rc


class Ui_variables_window(object):
    def setupUi(self, variables_window):
        if not variables_window.objectName():
            variables_window.setObjectName("variables_window")
        variables_window.resize(487, 674)
        icon = QIcon()
        icon.addFile(":/Icon/icon/prodic_icon.jpg", QSize(), QIcon.Normal, QIcon.Off)
        variables_window.setWindowIcon(icon)
        self.horizontalLayout = QHBoxLayout(variables_window)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.gb_variables = QGroupBox(variables_window)
        self.gb_variables.setObjectName("gb_variables")
        self.verticalLayout = QVBoxLayout(self.gb_variables)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gb_variables1 = QGroupBox(self.gb_variables)
        self.gb_variables1.setObjectName("gb_variables1")
        self.formLayout_2 = QFormLayout(self.gb_variables1)
        self.formLayout_2.setObjectName("formLayout_2")
        self.label = QLabel(self.gb_variables1)
        self.label.setObjectName("label")

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.label)

        self.cb_tsimu = QComboBox(self.gb_variables1)
        self.cb_tsimu.addItem("")
        self.cb_tsimu.addItem("")
        self.cb_tsimu.setObjectName("cb_tsimu")

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.cb_tsimu)

        self.sw_tsimu = QStackedWidget(self.gb_variables1)
        self.sw_tsimu.setObjectName("sw_tsimu")
        self.sw_tsimu_perm = QWidget()
        self.sw_tsimu_perm.setObjectName("sw_tsimu_perm")
        self.sw_tsimu.addWidget(self.sw_tsimu_perm)
        self.sw_tsimu_trans = QWidget()
        self.sw_tsimu_trans.setObjectName("sw_tsimu_trans")
        self.formLayout = QFormLayout(self.sw_tsimu_trans)
        self.formLayout.setObjectName("formLayout")
        self.label_4 = QLabel(self.sw_tsimu_trans)
        self.label_4.setObjectName("label_4")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_4)

        self.le_iptm = QLineEdit(self.sw_tsimu_trans)
        self.le_iptm.setObjectName("le_iptm")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.le_iptm)

        self.label_5 = QLabel(self.sw_tsimu_trans)
        self.label_5.setObjectName("label_5")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_5)

        self.le_dt = QLineEdit(self.sw_tsimu_trans)
        self.le_dt.setObjectName("le_dt")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.le_dt)

        self.sw_tsimu.addWidget(self.sw_tsimu_trans)

        self.formLayout_2.setWidget(2, QFormLayout.SpanningRole, self.sw_tsimu)

        self.label_2 = QLabel(self.gb_variables1)
        self.label_2.setObjectName("label_2")

        self.formLayout_2.setWidget(4, QFormLayout.LabelRole, self.label_2)

        self.cb_tipoflujo = QComboBox(self.gb_variables1)
        self.cb_tipoflujo.addItem("")
        self.cb_tipoflujo.addItem("")
        self.cb_tipoflujo.setObjectName("cb_tipoflujo")

        self.formLayout_2.setWidget(4, QFormLayout.FieldRole, self.cb_tipoflujo)

        self.label_3 = QLabel(self.gb_variables1)
        self.label_3.setObjectName("label_3")

        self.formLayout_2.setWidget(5, QFormLayout.LabelRole, self.label_3)

        self.cb_trataborde = QComboBox(self.gb_variables1)
        self.cb_trataborde.addItem("")
        self.cb_trataborde.addItem("")
        self.cb_trataborde.setObjectName("cb_trataborde")

        self.formLayout_2.setWidget(5, QFormLayout.FieldRole, self.cb_trataborde)

        self.verticalLayout.addWidget(self.gb_variables1)

        self.gb_variables2 = QGroupBox(self.gb_variables)
        self.gb_variables2.setObjectName("gb_variables2")
        self.gridLayout = QGridLayout(self.gb_variables2)
        self.gridLayout.setObjectName("gridLayout")
        self.chb_kprint1 = QCheckBox(self.gb_variables2)
        self.chb_kprint1.setObjectName("chb_kprint1")

        self.gridLayout.addWidget(self.chb_kprint1, 1, 4, 1, 1)

        self.chb_kprint9 = QCheckBox(self.gb_variables2)
        self.chb_kprint9.setObjectName("chb_kprint9")
        self.chb_kprint9.setEnabled(False)

        self.gridLayout.addWidget(self.chb_kprint9, 9, 4, 1, 1)

        self.le_relax8 = QLineEdit(self.gb_variables2)
        self.le_relax8.setObjectName("le_relax8")
        self.le_relax8.setEnabled(False)
        self.le_relax8.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.le_relax8, 8, 5, 1, 1)

        self.label_20 = QLabel(self.gb_variables2)
        self.label_20.setObjectName("label_20")

        self.gridLayout.addWidget(self.label_20, 12, 0, 1, 1)

        self.le_var_title2 = QLineEdit(self.gb_variables2)
        self.le_var_title2.setObjectName("le_var_title2")
        self.le_var_title2.setEnabled(False)
        self.le_var_title2.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.le_var_title2, 2, 2, 1, 1)

        self.chb_kprint10 = QCheckBox(self.gb_variables2)
        self.chb_kprint10.setObjectName("chb_kprint10")
        self.chb_kprint10.setEnabled(False)

        self.gridLayout.addWidget(self.chb_kprint10, 10, 4, 1, 1)

        self.label_17 = QLabel(self.gb_variables2)
        self.label_17.setObjectName("label_17")

        self.gridLayout.addWidget(self.label_17, 9, 0, 1, 1)

        self.chb_kprint12 = QCheckBox(self.gb_variables2)
        self.chb_kprint12.setObjectName("chb_kprint12")
        self.chb_kprint12.setEnabled(True)

        self.gridLayout.addWidget(self.chb_kprint12, 12, 3, 1, 1)

        self.chb_kprint4 = QCheckBox(self.gb_variables2)
        self.chb_kprint4.setObjectName("chb_kprint4")
        self.chb_kprint4.setEnabled(True)

        self.gridLayout.addWidget(self.chb_kprint4, 4, 4, 1, 1)

        self.label_12 = QLabel(self.gb_variables2)
        self.label_12.setObjectName("label_12")
        self.label_12.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_12, 0, 5, 1, 1)

        self.le_var_title10 = QLineEdit(self.gb_variables2)
        self.le_var_title10.setObjectName("le_var_title10")
        self.le_var_title10.setEnabled(False)
        self.le_var_title10.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.le_var_title10, 10, 2, 1, 1)

        self.le_var_title7 = QLineEdit(self.gb_variables2)
        self.le_var_title7.setObjectName("le_var_title7")
        self.le_var_title7.setEnabled(False)
        self.le_var_title7.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.le_var_title7, 7, 2, 1, 1)

        self.le_relax6 = QLineEdit(self.gb_variables2)
        self.le_relax6.setObjectName("le_relax6")
        self.le_relax6.setEnabled(False)
        self.le_relax6.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.le_relax6, 6, 5, 1, 1)

        self.le_var_title9 = QLineEdit(self.gb_variables2)
        self.le_var_title9.setObjectName("le_var_title9")
        self.le_var_title9.setEnabled(False)
        self.le_var_title9.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.le_var_title9, 9, 2, 1, 1)

        self.chb_ksolve3 = QCheckBox(self.gb_variables2)
        self.chb_ksolve3.setObjectName("chb_ksolve3")
        self.chb_ksolve3.setEnabled(True)

        self.gridLayout.addWidget(self.chb_ksolve3, 3, 3, 1, 1)

        self.le_var_title6 = QLineEdit(self.gb_variables2)
        self.le_var_title6.setObjectName("le_var_title6")
        self.le_var_title6.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.le_var_title6, 6, 2, 1, 1)

        self.label_18 = QLabel(self.gb_variables2)
        self.label_18.setObjectName("label_18")

        self.gridLayout.addWidget(self.label_18, 10, 0, 1, 1)

        self.label_14 = QLabel(self.gb_variables2)
        self.label_14.setObjectName("label_14")

        self.gridLayout.addWidget(self.label_14, 6, 0, 1, 1)

        self.label_19 = QLabel(self.gb_variables2)
        self.label_19.setObjectName("label_19")

        self.gridLayout.addWidget(self.label_19, 11, 0, 1, 1)

        self.le_var_title3 = QLineEdit(self.gb_variables2)
        self.le_var_title3.setObjectName("le_var_title3")
        self.le_var_title3.setEnabled(False)
        self.le_var_title3.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.le_var_title3, 3, 2, 1, 1)

        self.chb_kprint5 = QCheckBox(self.gb_variables2)
        self.chb_kprint5.setObjectName("chb_kprint5")
        self.chb_kprint5.setChecked(True)

        self.gridLayout.addWidget(self.chb_kprint5, 5, 4, 1, 1)

        self.chb_kprint7 = QCheckBox(self.gb_variables2)
        self.chb_kprint7.setObjectName("chb_kprint7")
        self.chb_kprint7.setEnabled(False)

        self.gridLayout.addWidget(self.chb_kprint7, 7, 4, 1, 1)

        self.label_11 = QLabel(self.gb_variables2)
        self.label_11.setObjectName("label_11")

        self.gridLayout.addWidget(self.label_11, 4, 0, 1, 1)

        self.le_relax11 = QLineEdit(self.gb_variables2)
        self.le_relax11.setObjectName("le_relax11")
        self.le_relax11.setEnabled(True)
        self.le_relax11.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.le_relax11, 11, 5, 1, 1)

        self.le_var_title4 = QLineEdit(self.gb_variables2)
        self.le_var_title4.setObjectName("le_var_title4")
        self.le_var_title4.setEnabled(False)
        self.le_var_title4.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.le_var_title4, 4, 2, 1, 1)

        self.label_8 = QLabel(self.gb_variables2)
        self.label_8.setObjectName("label_8")

        self.gridLayout.addWidget(self.label_8, 1, 0, 1, 1)

        self.chb_kprint3 = QCheckBox(self.gb_variables2)
        self.chb_kprint3.setObjectName("chb_kprint3")

        self.gridLayout.addWidget(self.chb_kprint3, 3, 4, 1, 1)

        self.le_relax7 = QLineEdit(self.gb_variables2)
        self.le_relax7.setObjectName("le_relax7")
        self.le_relax7.setEnabled(False)
        self.le_relax7.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.le_relax7, 7, 5, 1, 1)

        self.chb_ksolve4 = QCheckBox(self.gb_variables2)
        self.chb_ksolve4.setObjectName("chb_ksolve4")
        self.chb_ksolve4.setEnabled(True)

        self.gridLayout.addWidget(self.chb_ksolve4, 4, 3, 1, 1)

        self.chb_ksolve8 = QCheckBox(self.gb_variables2)
        self.chb_ksolve8.setObjectName("chb_ksolve8")
        self.chb_ksolve8.setEnabled(False)

        self.gridLayout.addWidget(self.chb_ksolve8, 8, 3, 1, 1)

        self.chb_ksolve10 = QCheckBox(self.gb_variables2)
        self.chb_ksolve10.setObjectName("chb_ksolve10")
        self.chb_ksolve10.setEnabled(False)

        self.gridLayout.addWidget(self.chb_ksolve10, 10, 3, 1, 1)

        self.label_9 = QLabel(self.gb_variables2)
        self.label_9.setObjectName("label_9")

        self.gridLayout.addWidget(self.label_9, 2, 0, 1, 1)

        self.le_var_title11 = QLineEdit(self.gb_variables2)
        self.le_var_title11.setObjectName("le_var_title11")
        self.le_var_title11.setEnabled(False)
        self.le_var_title11.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.le_var_title11, 11, 2, 1, 1)

        self.label_13 = QLabel(self.gb_variables2)
        self.label_13.setObjectName("label_13")

        self.gridLayout.addWidget(self.label_13, 5, 0, 1, 1)

        self.chb_ksolve6 = QCheckBox(self.gb_variables2)
        self.chb_ksolve6.setObjectName("chb_ksolve6")
        self.chb_ksolve6.setEnabled(False)

        self.gridLayout.addWidget(self.chb_ksolve6, 6, 3, 1, 1)

        self.chb_ksolve1 = QCheckBox(self.gb_variables2)
        self.chb_ksolve1.setObjectName("chb_ksolve1")
        self.chb_ksolve1.setEnabled(True)

        self.gridLayout.addWidget(self.chb_ksolve1, 1, 3, 1, 1)

        self.chb_ksolve2 = QCheckBox(self.gb_variables2)
        self.chb_ksolve2.setObjectName("chb_ksolve2")
        self.chb_ksolve2.setEnabled(True)

        self.gridLayout.addWidget(self.chb_ksolve2, 2, 3, 1, 1)

        self.chb_ksolve5 = QCheckBox(self.gb_variables2)
        self.chb_ksolve5.setObjectName("chb_ksolve5")
        self.chb_ksolve5.setEnabled(True)
        self.chb_ksolve5.setChecked(True)

        self.gridLayout.addWidget(self.chb_ksolve5, 5, 3, 1, 1)

        self.label_15 = QLabel(self.gb_variables2)
        self.label_15.setObjectName("label_15")

        self.gridLayout.addWidget(self.label_15, 7, 0, 1, 1)

        self.chb_ksolve11 = QCheckBox(self.gb_variables2)
        self.chb_ksolve11.setObjectName("chb_ksolve11")
        self.chb_ksolve11.setEnabled(True)

        self.gridLayout.addWidget(self.chb_ksolve11, 11, 3, 1, 1)

        self.le_relax1 = QLineEdit(self.gb_variables2)
        self.le_relax1.setObjectName("le_relax1")
        self.le_relax1.setEnabled(False)
        self.le_relax1.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.le_relax1, 1, 5, 1, 1)

        self.label_10 = QLabel(self.gb_variables2)
        self.label_10.setObjectName("label_10")

        self.gridLayout.addWidget(self.label_10, 3, 0, 1, 1)

        self.le_var_title12 = QLineEdit(self.gb_variables2)
        self.le_var_title12.setObjectName("le_var_title12")
        self.le_var_title12.setEnabled(False)
        self.le_var_title12.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.le_var_title12, 12, 2, 1, 1)

        self.chb_kprint8 = QCheckBox(self.gb_variables2)
        self.chb_kprint8.setObjectName("chb_kprint8")
        self.chb_kprint8.setEnabled(False)

        self.gridLayout.addWidget(self.chb_kprint8, 8, 4, 1, 1)

        self.le_relax2 = QLineEdit(self.gb_variables2)
        self.le_relax2.setObjectName("le_relax2")
        self.le_relax2.setEnabled(False)
        self.le_relax2.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.le_relax2, 2, 5, 1, 1)

        self.label_7 = QLabel(self.gb_variables2)
        self.label_7.setObjectName("label_7")
        self.label_7.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_7, 0, 2, 1, 1)

        self.label_16 = QLabel(self.gb_variables2)
        self.label_16.setObjectName("label_16")

        self.gridLayout.addWidget(self.label_16, 8, 0, 1, 1)

        self.label_6 = QLabel(self.gb_variables2)
        self.label_6.setObjectName("label_6")

        self.gridLayout.addWidget(self.label_6, 0, 0, 1, 1)

        self.chb_kprint6 = QCheckBox(self.gb_variables2)
        self.chb_kprint6.setObjectName("chb_kprint6")
        self.chb_kprint6.setEnabled(False)

        self.gridLayout.addWidget(self.chb_kprint6, 6, 4, 1, 1)

        self.le_relax10 = QLineEdit(self.gb_variables2)
        self.le_relax10.setObjectName("le_relax10")
        self.le_relax10.setEnabled(False)
        self.le_relax10.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.le_relax10, 10, 5, 1, 1)

        self.le_relax3 = QLineEdit(self.gb_variables2)
        self.le_relax3.setObjectName("le_relax3")
        self.le_relax3.setEnabled(False)
        self.le_relax3.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.le_relax3, 3, 5, 1, 1)

        self.le_var_title8 = QLineEdit(self.gb_variables2)
        self.le_var_title8.setObjectName("le_var_title8")
        self.le_var_title8.setEnabled(False)
        self.le_var_title8.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.le_var_title8, 8, 2, 1, 1)

        self.chb_ksolve7 = QCheckBox(self.gb_variables2)
        self.chb_ksolve7.setObjectName("chb_ksolve7")
        self.chb_ksolve7.setEnabled(False)

        self.gridLayout.addWidget(self.chb_ksolve7, 7, 3, 1, 1)

        self.chb_kprint11 = QCheckBox(self.gb_variables2)
        self.chb_kprint11.setObjectName("chb_kprint11")
        self.chb_kprint11.setEnabled(True)

        self.gridLayout.addWidget(self.chb_kprint11, 11, 4, 1, 1)

        self.le_var_title5 = QLineEdit(self.gb_variables2)
        self.le_var_title5.setObjectName("le_var_title5")
        self.le_var_title5.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.le_var_title5, 5, 2, 1, 1)

        self.chb_kprint2 = QCheckBox(self.gb_variables2)
        self.chb_kprint2.setObjectName("chb_kprint2")

        self.gridLayout.addWidget(self.chb_kprint2, 2, 4, 1, 1)

        self.le_relax9 = QLineEdit(self.gb_variables2)
        self.le_relax9.setObjectName("le_relax9")
        self.le_relax9.setEnabled(False)
        self.le_relax9.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.le_relax9, 9, 5, 1, 1)

        self.chb_ksolve9 = QCheckBox(self.gb_variables2)
        self.chb_ksolve9.setObjectName("chb_ksolve9")
        self.chb_ksolve9.setEnabled(False)

        self.gridLayout.addWidget(self.chb_ksolve9, 9, 3, 1, 1)

        self.le_relax4 = QLineEdit(self.gb_variables2)
        self.le_relax4.setObjectName("le_relax4")
        self.le_relax4.setEnabled(False)
        self.le_relax4.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.le_relax4, 4, 5, 1, 1)

        self.le_relax5 = QLineEdit(self.gb_variables2)
        self.le_relax5.setObjectName("le_relax5")
        self.le_relax5.setEnabled(True)
        self.le_relax5.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.le_relax5, 5, 5, 1, 1)

        self.le_var_title1 = QLineEdit(self.gb_variables2)
        self.le_var_title1.setObjectName("le_var_title1")
        self.le_var_title1.setEnabled(False)
        self.le_var_title1.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.le_var_title1, 1, 2, 1, 1)

        self.checkBox = QCheckBox(self.gb_variables2)
        self.checkBox.setObjectName("checkBox")
        self.checkBox.setLayoutDirection(Qt.RightToLeft)
        self.checkBox.setChecked(True)

        self.gridLayout.addWidget(self.checkBox, 13, 2, 1, 2)

        self.label_21 = QLabel(self.gb_variables2)
        self.label_21.setObjectName("label_21")

        self.gridLayout.addWidget(self.label_21, 12, 4, 1, 1)

        self.le_tol = QLineEdit(self.gb_variables2)
        self.le_tol.setObjectName("le_tol")

        self.gridLayout.addWidget(self.le_tol, 12, 5, 1, 1)

        self.verticalLayout.addWidget(self.gb_variables2)

        self.horizontalLayout.addWidget(self.gb_variables)

        self.retranslateUi(variables_window)

        self.sw_tsimu.setCurrentIndex(0)

        QMetaObject.connectSlotsByName(variables_window)

    # setupUi

    def retranslateUi(self, variables_window):
        variables_window.setWindowTitle(QCoreApplication.translate("variables_window", "Variables - PrePRODIC3D", None))
        self.gb_variables.setTitle(QCoreApplication.translate("variables_window", "Variables", None))
        self.gb_variables1.setTitle(
            QCoreApplication.translate("variables_window", "Condiciones de la simulaci\u00f3n", None)
        )
        self.label.setText(QCoreApplication.translate("variables_window", "Tipo de simulaci\u00f3n", None))
        self.cb_tsimu.setItemText(0, QCoreApplication.translate("variables_window", "Permanente", None))
        self.cb_tsimu.setItemText(1, QCoreApplication.translate("variables_window", "Transitorio", None))

        self.label_4.setText(
            QCoreApplication.translate("variables_window", "Numero de pasos en el tiempo (IPTM)", None)
        )
        self.le_iptm.setText("")
        self.label_5.setText(QCoreApplication.translate("variables_window", "Intervalo de tiempo (DT)", None))
        self.label_2.setText(QCoreApplication.translate("variables_window", "Tipo de flujo", None))
        self.cb_tipoflujo.setItemText(0, QCoreApplication.translate("variables_window", "Difusivo", None))
        self.cb_tipoflujo.setItemText(1, QCoreApplication.translate("variables_window", "Flujo Laminar", None))

        self.label_3.setText(
            QCoreApplication.translate("variables_window", "Condiciones de tratamiento de borde", None)
        )
        self.cb_trataborde.setItemText(0, QCoreApplication.translate("variables_window", "Esquema de bajo orden", None))
        self.cb_trataborde.setItemText(1, QCoreApplication.translate("variables_window", "Esquema de alto orden", None))

        self.gb_variables2.setTitle(QCoreApplication.translate("variables_window", "Variables a resolver", None))
        self.chb_kprint1.setText(QCoreApplication.translate("variables_window", "Imprimir", None))
        self.chb_kprint9.setText(QCoreApplication.translate("variables_window", "Imprimir", None))
        self.label_20.setText(QCoreApplication.translate("variables_window", "12", None))
        self.le_var_title2.setText(QCoreApplication.translate("variables_window", "Velocidad V", None))
        self.chb_kprint10.setText(QCoreApplication.translate("variables_window", "Imprimir", None))
        self.label_17.setText(QCoreApplication.translate("variables_window", "9", None))
        self.chb_kprint12.setText(QCoreApplication.translate("variables_window", "Imprimir", None))
        self.chb_kprint4.setText(QCoreApplication.translate("variables_window", "Imprimir", None))
        self.label_12.setText(QCoreApplication.translate("variables_window", "Relajamiento", None))
        self.chb_ksolve3.setText(QCoreApplication.translate("variables_window", "Resolver", None))
        self.label_18.setText(QCoreApplication.translate("variables_window", "10", None))
        self.label_14.setText(QCoreApplication.translate("variables_window", "6", None))
        self.label_19.setText(QCoreApplication.translate("variables_window", "11", None))
        self.le_var_title3.setText(QCoreApplication.translate("variables_window", "Velocidad W", None))
        self.chb_kprint5.setText(QCoreApplication.translate("variables_window", "Imprimir", None))
        self.chb_kprint7.setText(QCoreApplication.translate("variables_window", "Imprimir", None))
        self.label_11.setText(QCoreApplication.translate("variables_window", "4", None))
        self.le_var_title4.setText(
            QCoreApplication.translate("variables_window", "Correcci\u00f3n de presi\u00f3n", None)
        )
        self.label_8.setText(QCoreApplication.translate("variables_window", "1", None))
        self.chb_kprint3.setText(QCoreApplication.translate("variables_window", "Imprimir", None))
        self.chb_ksolve4.setText(QCoreApplication.translate("variables_window", "Resolver", None))
        self.chb_ksolve8.setText(QCoreApplication.translate("variables_window", "Resolver", None))
        self.chb_ksolve10.setText(QCoreApplication.translate("variables_window", "Resolver", None))
        self.label_9.setText(QCoreApplication.translate("variables_window", "2", None))
        self.le_var_title11.setText(QCoreApplication.translate("variables_window", "Presi\u00f3n", None))
        self.label_13.setText(QCoreApplication.translate("variables_window", "5", None))
        self.chb_ksolve6.setText(QCoreApplication.translate("variables_window", "Resolver", None))
        self.chb_ksolve1.setText(QCoreApplication.translate("variables_window", "Resolver", None))
        self.chb_ksolve2.setText(QCoreApplication.translate("variables_window", "Resolver", None))
        self.chb_ksolve5.setText(QCoreApplication.translate("variables_window", "Resolver", None))
        self.label_15.setText(QCoreApplication.translate("variables_window", "7", None))
        self.chb_ksolve11.setText(QCoreApplication.translate("variables_window", "Resolver", None))
        self.label_10.setText(QCoreApplication.translate("variables_window", "3", None))
        self.le_var_title12.setText(QCoreApplication.translate("variables_window", "Funci\u00f3n de corriente", None))
        self.chb_kprint8.setText(QCoreApplication.translate("variables_window", "Imprimir", None))
        self.label_7.setText(QCoreApplication.translate("variables_window", "Variables", None))
        self.label_16.setText(QCoreApplication.translate("variables_window", "8", None))
        self.label_6.setText(QCoreApplication.translate("variables_window", "No.", None))
        self.chb_kprint6.setText(QCoreApplication.translate("variables_window", "Imprimir", None))
        self.chb_ksolve7.setText(QCoreApplication.translate("variables_window", "Resolver", None))
        self.chb_kprint11.setText(QCoreApplication.translate("variables_window", "Imprimir", None))
        self.le_var_title5.setText(QCoreApplication.translate("variables_window", "Temperatura", None))
        self.chb_kprint2.setText(QCoreApplication.translate("variables_window", "Imprimir", None))
        self.chb_ksolve9.setText(QCoreApplication.translate("variables_window", "Resolver", None))
        self.le_relax5.setText(QCoreApplication.translate("variables_window", "1", None))
        self.le_var_title1.setText(QCoreApplication.translate("variables_window", "Velocidad U", None))
        self.checkBox.setText(
            QCoreApplication.translate("variables_window", "Tratar variable 5 como temperatura:", None)
        )
        self.label_21.setText(QCoreApplication.translate("variables_window", "Tolerancia", None))

    # retranslateUi
