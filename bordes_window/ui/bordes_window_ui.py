# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'bordes_window.ui'
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
    QGridLayout,
    QGroupBox,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QListWidget,
    QListWidgetItem,
    QPushButton,
    QSizePolicy,
    QVBoxLayout,
    QWidget,
)
from Recursos import recursos_rc


class Ui_bordes_window(object):
    def setupUi(self, bordes_window):
        if not bordes_window.objectName():
            bordes_window.setObjectName("bordes_window")
        bordes_window.resize(445, 603)
        icon = QIcon()
        icon.addFile(":/Icon/icon/prodic_icon.jpg", QSize(), QIcon.Normal, QIcon.Off)
        bordes_window.setWindowIcon(icon)
        self.gridLayout_3 = QGridLayout(bordes_window)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.groupBox_4 = QGroupBox(bordes_window)
        self.groupBox_4.setObjectName("groupBox_4")
        self.gridLayout_4 = QGridLayout(self.groupBox_4)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.le_value_veloc_v = QLineEdit(self.groupBox_4)
        self.le_value_veloc_v.setObjectName("le_value_veloc_v")
        self.le_value_veloc_v.setEnabled(True)

        self.gridLayout_4.addWidget(self.le_value_veloc_v, 1, 2, 1, 1)

        self.label_4 = QLabel(self.groupBox_4)
        self.label_4.setObjectName("label_4")

        self.gridLayout_4.addWidget(self.label_4, 0, 1, 1, 1)

        self.label_5 = QLabel(self.groupBox_4)
        self.label_5.setObjectName("label_5")

        self.gridLayout_4.addWidget(self.label_5, 1, 1, 1, 1)

        self.le_value_veloc_w = QLineEdit(self.groupBox_4)
        self.le_value_veloc_w.setObjectName("le_value_veloc_w")
        self.le_value_veloc_w.setEnabled(True)

        self.gridLayout_4.addWidget(self.le_value_veloc_w, 2, 2, 1, 1)

        self.le_value_veloc_u = QLineEdit(self.groupBox_4)
        self.le_value_veloc_u.setObjectName("le_value_veloc_u")
        self.le_value_veloc_u.setEnabled(True)

        self.gridLayout_4.addWidget(self.le_value_veloc_u, 0, 2, 1, 1)

        self.label_9 = QLabel(self.groupBox_4)
        self.label_9.setObjectName("label_9")

        self.gridLayout_4.addWidget(self.label_9, 2, 1, 1, 1)

        self.chb_ex_veloc_u = QCheckBox(self.groupBox_4)
        self.chb_ex_veloc_u.setObjectName("chb_ex_veloc_u")

        self.gridLayout_4.addWidget(self.chb_ex_veloc_u, 0, 3, 1, 1)

        self.chb_ex_veloc_v = QCheckBox(self.groupBox_4)
        self.chb_ex_veloc_v.setObjectName("chb_ex_veloc_v")

        self.gridLayout_4.addWidget(self.chb_ex_veloc_v, 1, 3, 1, 1)

        self.chb_ex_veloc_w = QCheckBox(self.groupBox_4)
        self.chb_ex_veloc_w.setObjectName("chb_ex_veloc_w")

        self.gridLayout_4.addWidget(self.chb_ex_veloc_w, 2, 3, 1, 1)

        self.gridLayout_3.addWidget(self.groupBox_4, 2, 0, 1, 1)

        self.groupBox_3 = QGroupBox(bordes_window)
        self.groupBox_3.setObjectName("groupBox_3")
        self.horizontalLayout = QHBoxLayout(self.groupBox_3)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.groupBox_6 = QGroupBox(self.groupBox_3)
        self.groupBox_6.setObjectName("groupBox_6")
        self.gridLayout_2 = QGridLayout(self.groupBox_6)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.lw_variables = QListWidget(self.groupBox_6)
        QListWidgetItem(self.lw_variables)
        self.lw_variables.setObjectName("lw_variables")

        self.gridLayout_2.addWidget(self.lw_variables, 0, 0, 1, 1)

        self.horizontalLayout.addWidget(self.groupBox_6)

        self.gb_chbvalues = QGroupBox(self.groupBox_3)
        self.gb_chbvalues.setObjectName("gb_chbvalues")
        self.verticalLayout_2 = QVBoxLayout(self.gb_chbvalues)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.chb_value = QCheckBox(self.gb_chbvalues)
        self.chb_value.setObjectName("chb_value")
        self.chb_value.setChecked(True)
        self.chb_value.setTristate(False)

        self.verticalLayout_2.addWidget(self.chb_value)

        self.chb_flux = QCheckBox(self.gb_chbvalues)
        self.chb_flux.setObjectName("chb_flux")

        self.verticalLayout_2.addWidget(self.chb_flux)

        self.chb_convec = QCheckBox(self.gb_chbvalues)
        self.chb_convec.setObjectName("chb_convec")

        self.verticalLayout_2.addWidget(self.chb_convec)

        self.horizontalLayout.addWidget(self.gb_chbvalues)

        self.groupBox_8 = QGroupBox(self.groupBox_3)
        self.groupBox_8.setObjectName("groupBox_8")
        self.gridLayout_6 = QGridLayout(self.groupBox_8)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.le_tempamb = QLineEdit(self.groupBox_8)
        self.le_tempamb.setObjectName("le_tempamb")
        self.le_tempamb.setEnabled(False)

        self.gridLayout_6.addWidget(self.le_tempamb, 4, 0, 1, 1)

        self.lb_variable = QLabel(self.groupBox_8)
        self.lb_variable.setObjectName("lb_variable")

        self.gridLayout_6.addWidget(self.lb_variable, 3, 0, 1, 1)

        self.le_value = QLineEdit(self.groupBox_8)
        self.le_value.setObjectName("le_value")

        self.gridLayout_6.addWidget(self.le_value, 2, 0, 1, 1)

        self.lb_value = QLabel(self.groupBox_8)
        self.lb_value.setObjectName("lb_value")

        self.gridLayout_6.addWidget(self.lb_value, 0, 0, 1, 1)

        self.chb_ex_value = QCheckBox(self.groupBox_8)
        self.chb_ex_value.setObjectName("chb_ex_value")

        self.gridLayout_6.addWidget(self.chb_ex_value, 2, 1, 1, 1)

        self.chb_ex_tempamb = QCheckBox(self.groupBox_8)
        self.chb_ex_tempamb.setObjectName("chb_ex_tempamb")

        self.gridLayout_6.addWidget(self.chb_ex_tempamb, 4, 1, 1, 1)

        self.horizontalLayout.addWidget(self.groupBox_8)

        self.gridLayout_3.addWidget(self.groupBox_3, 1, 0, 1, 2)

        self.gb_tipo_segment = QGroupBox(bordes_window)
        self.gb_tipo_segment.setObjectName("gb_tipo_segment")
        self.verticalLayout = QVBoxLayout(self.gb_tipo_segment)
        self.verticalLayout.setObjectName("verticalLayout")
        self.chb_wall = QCheckBox(self.gb_tipo_segment)
        self.chb_wall.setObjectName("chb_wall")
        self.chb_wall.setChecked(True)
        self.chb_wall.setTristate(False)

        self.verticalLayout.addWidget(self.chb_wall)

        self.chb_inmass = QCheckBox(self.gb_tipo_segment)
        self.chb_inmass.setObjectName("chb_inmass")
        self.chb_inmass.setEnabled(False)

        self.verticalLayout.addWidget(self.chb_inmass)

        self.chb_outmass = QCheckBox(self.gb_tipo_segment)
        self.chb_outmass.setObjectName("chb_outmass")
        self.chb_outmass.setEnabled(False)

        self.verticalLayout.addWidget(self.chb_outmass)

        self.gridLayout_3.addWidget(self.gb_tipo_segment, 0, 1, 1, 1)

        self.groupBox_5 = QGroupBox(bordes_window)
        self.groupBox_5.setObjectName("groupBox_5")
        self.horizontalLayout_34 = QHBoxLayout(self.groupBox_5)
        self.horizontalLayout_34.setObjectName("horizontalLayout_34")
        self.label_6 = QLabel(self.groupBox_5)
        self.label_6.setObjectName("label_6")

        self.horizontalLayout_34.addWidget(self.label_6)

        self.le_fracmass = QLineEdit(self.groupBox_5)
        self.le_fracmass.setObjectName("le_fracmass")
        self.le_fracmass.setEnabled(False)

        self.horizontalLayout_34.addWidget(self.le_fracmass)

        self.gridLayout_3.addWidget(self.groupBox_5, 2, 1, 1, 1)

        self.groupBox = QGroupBox(bordes_window)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout = QGridLayout(self.groupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.lw_bordes = QListWidget(self.groupBox)
        QListWidgetItem(self.lw_bordes)
        QListWidgetItem(self.lw_bordes)
        QListWidgetItem(self.lw_bordes)
        QListWidgetItem(self.lw_bordes)
        QListWidgetItem(self.lw_bordes)
        QListWidgetItem(self.lw_bordes)
        self.lw_bordes.setObjectName("lw_bordes")

        self.gridLayout.addWidget(self.lw_bordes, 3, 0, 1, 3)

        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName("label_3")

        self.gridLayout.addWidget(self.label_3, 2, 3, 1, 1)

        self.groupBox_2 = QGroupBox(self.groupBox)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_5 = QGridLayout(self.groupBox_2)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.le_vertical_lon = QLineEdit(self.groupBox_2)
        self.le_vertical_lon.setObjectName("le_vertical_lon")

        self.gridLayout_5.addWidget(self.le_vertical_lon, 1, 2, 1, 1)

        self.le_transversal_start = QLineEdit(self.groupBox_2)
        self.le_transversal_start.setObjectName("le_transversal_start")

        self.gridLayout_5.addWidget(self.le_transversal_start, 3, 1, 1, 1)

        self.label = QLabel(self.groupBox_2)
        self.label.setObjectName("label")

        self.gridLayout_5.addWidget(self.label, 1, 0, 1, 1)

        self.label_10 = QLabel(self.groupBox_2)
        self.label_10.setObjectName("label_10")

        self.gridLayout_5.addWidget(self.label_10, 3, 0, 1, 1)

        self.le_transversal_lon = QLineEdit(self.groupBox_2)
        self.le_transversal_lon.setObjectName("le_transversal_lon")

        self.gridLayout_5.addWidget(self.le_transversal_lon, 1, 1, 1, 1)

        self.le_vertical_start = QLineEdit(self.groupBox_2)
        self.le_vertical_start.setObjectName("le_vertical_start")

        self.gridLayout_5.addWidget(self.le_vertical_start, 3, 2, 1, 1)

        self.lb_transversal = QLabel(self.groupBox_2)
        self.lb_transversal.setObjectName("lb_transversal")
        self.lb_transversal.setLayoutDirection(Qt.LeftToRight)
        self.lb_transversal.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.lb_transversal, 0, 1, 1, 1)

        self.lb_vertical = QLabel(self.groupBox_2)
        self.lb_vertical.setObjectName("lb_vertical")
        self.lb_vertical.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.lb_vertical, 0, 2, 1, 1)

        self.gridLayout.addWidget(self.groupBox_2, 1, 0, 1, 4)

        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName("label_2")

        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 2)

        self.groupBox_7 = QGroupBox(self.groupBox)
        self.groupBox_7.setObjectName("groupBox_7")
        self.verticalLayout_5 = QVBoxLayout(self.groupBox_7)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.pb_addpatch = QPushButton(self.groupBox_7)
        self.pb_addpatch.setObjectName("pb_addpatch")

        self.verticalLayout_5.addWidget(self.pb_addpatch)

        self.pb_rempatch = QPushButton(self.groupBox_7)
        self.pb_rempatch.setObjectName("pb_rempatch")

        self.verticalLayout_5.addWidget(self.pb_rempatch)

        self.gridLayout.addWidget(self.groupBox_7, 4, 0, 1, 4)

        self.lw_patchlist = QListWidget(self.groupBox)
        QListWidgetItem(self.lw_patchlist)
        self.lw_patchlist.setObjectName("lw_patchlist")

        self.gridLayout.addWidget(self.lw_patchlist, 3, 3, 1, 1)

        self.gridLayout_3.addWidget(self.groupBox, 0, 0, 1, 1)

        self.retranslateUi(bordes_window)

        QMetaObject.connectSlotsByName(bordes_window)

    # setupUi

    def retranslateUi(self, bordes_window):
        bordes_window.setWindowTitle(QCoreApplication.translate("bordes_window", "Bordes - PrePRODIC3D", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("bordes_window", "Velocidad", None))
        self.label_4.setText(QCoreApplication.translate("bordes_window", "Velocidad U", None))
        self.label_5.setText(QCoreApplication.translate("bordes_window", "Velocidad V", None))
        self.label_9.setText(QCoreApplication.translate("bordes_window", "Velocidad W", None))
        self.chb_ex_veloc_u.setText("")
        self.chb_ex_veloc_v.setText("")
        self.chb_ex_veloc_w.setText("")
        self.groupBox_3.setTitle(QCoreApplication.translate("bordes_window", "Variables escalares", None))
        self.groupBox_6.setTitle("")

        __sortingEnabled = self.lw_variables.isSortingEnabled()
        self.lw_variables.setSortingEnabled(False)
        ___qlistwidgetitem = self.lw_variables.item(0)
        ___qlistwidgetitem.setText(QCoreApplication.translate("bordes_window", "Temperatura", None))
        self.lw_variables.setSortingEnabled(__sortingEnabled)

        self.gb_chbvalues.setTitle("")
        self.chb_value.setText(QCoreApplication.translate("bordes_window", "Valor", None))
        self.chb_flux.setText(QCoreApplication.translate("bordes_window", "Flujo", None))
        self.chb_convec.setText(QCoreApplication.translate("bordes_window", "Convecci\u00f3n", None))
        self.groupBox_8.setTitle("")
        self.lb_variable.setText(QCoreApplication.translate("bordes_window", "Temp. ambiente", None))
        self.lb_value.setText(QCoreApplication.translate("bordes_window", "Valor", None))
        self.chb_ex_value.setText("")
        self.chb_ex_tempamb.setText("")
        self.gb_tipo_segment.setTitle(QCoreApplication.translate("bordes_window", "Tipo de segmento", None))
        self.chb_wall.setText(QCoreApplication.translate("bordes_window", "Pared", None))
        self.chb_inmass.setText(QCoreApplication.translate("bordes_window", "Entrada de la masa", None))
        self.chb_outmass.setText(QCoreApplication.translate("bordes_window", "Salida de la masa", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("bordes_window", "Salida de la masa", None))
        self.label_6.setText(QCoreApplication.translate("bordes_window", "Fracci\u00f3n", None))
        self.groupBox.setTitle(QCoreApplication.translate("bordes_window", "Divisi\u00f3n de bordes", None))

        __sortingEnabled1 = self.lw_bordes.isSortingEnabled()
        self.lw_bordes.setSortingEnabled(False)
        ___qlistwidgetitem1 = self.lw_bordes.item(0)
        ___qlistwidgetitem1.setText(QCoreApplication.translate("bordes_window", "X Max", None))
        ___qlistwidgetitem2 = self.lw_bordes.item(1)
        ___qlistwidgetitem2.setText(QCoreApplication.translate("bordes_window", "X Min", None))
        ___qlistwidgetitem3 = self.lw_bordes.item(2)
        ___qlistwidgetitem3.setText(QCoreApplication.translate("bordes_window", "Y Max", None))
        ___qlistwidgetitem4 = self.lw_bordes.item(3)
        ___qlistwidgetitem4.setText(QCoreApplication.translate("bordes_window", "Y Min", None))
        ___qlistwidgetitem5 = self.lw_bordes.item(4)
        ___qlistwidgetitem5.setText(QCoreApplication.translate("bordes_window", "Z Max", None))
        ___qlistwidgetitem6 = self.lw_bordes.item(5)
        ___qlistwidgetitem6.setText(QCoreApplication.translate("bordes_window", "Z Min", None))
        self.lw_bordes.setSortingEnabled(__sortingEnabled1)

        self.label_3.setText(QCoreApplication.translate("bordes_window", "Segmento", None))
        self.groupBox_2.setTitle("")
        self.label.setText(QCoreApplication.translate("bordes_window", "Longitud", None))
        self.label_10.setText(QCoreApplication.translate("bordes_window", "Empieza", None))
        self.lb_transversal.setText(QCoreApplication.translate("bordes_window", "Y", None))
        self.lb_vertical.setText(QCoreApplication.translate("bordes_window", "Z", None))
        self.label_2.setText(QCoreApplication.translate("bordes_window", "Borde", None))
        self.groupBox_7.setTitle("")
        self.pb_addpatch.setText(QCoreApplication.translate("bordes_window", "Agregar un segmento", None))
        self.pb_rempatch.setText(QCoreApplication.translate("bordes_window", "Eliminar un segmento", None))

        __sortingEnabled2 = self.lw_patchlist.isSortingEnabled()
        self.lw_patchlist.setSortingEnabled(False)
        ___qlistwidgetitem7 = self.lw_patchlist.item(0)
        ___qlistwidgetitem7.setText(QCoreApplication.translate("bordes_window", "Borde base", None))
        self.lw_patchlist.setSortingEnabled(__sortingEnabled2)

    # retranslateUi
