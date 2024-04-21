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
from PySide6.QtWidgets import (QApplication, QCheckBox, QGridLayout, QGroupBox,
    QHBoxLayout, QLabel, QLineEdit, QListWidget,
    QListWidgetItem, QPushButton, QSizePolicy, QStackedWidget,
    QVBoxLayout, QWidget)

class Ui_bordes_window(object):
    def setupUi(self, bordes_window):
        if not bordes_window.objectName():
            bordes_window.setObjectName(u"bordes_window")
        bordes_window.resize(445, 637)
        self.gridLayout_3 = QGridLayout(bordes_window)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.groupBox_4 = QGroupBox(bordes_window)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.gridLayout_4 = QGridLayout(self.groupBox_4)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.le_value_veloc_u = QLineEdit(self.groupBox_4)
        self.le_value_veloc_u.setObjectName(u"le_value_veloc_u")
        self.le_value_veloc_u.setEnabled(False)

        self.gridLayout_4.addWidget(self.le_value_veloc_u, 0, 1, 1, 1)

        self.label_4 = QLabel(self.groupBox_4)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_4.addWidget(self.label_4, 0, 0, 1, 1)

        self.label_5 = QLabel(self.groupBox_4)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_4.addWidget(self.label_5, 1, 0, 1, 1)

        self.le_value_veloc_v = QLineEdit(self.groupBox_4)
        self.le_value_veloc_v.setObjectName(u"le_value_veloc_v")
        self.le_value_veloc_v.setEnabled(False)

        self.gridLayout_4.addWidget(self.le_value_veloc_v, 1, 1, 1, 1)

        self.le_value_veloc_w = QLineEdit(self.groupBox_4)
        self.le_value_veloc_w.setObjectName(u"le_value_veloc_w")
        self.le_value_veloc_w.setEnabled(False)

        self.gridLayout_4.addWidget(self.le_value_veloc_w, 2, 1, 1, 1)

        self.label_9 = QLabel(self.groupBox_4)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout_4.addWidget(self.label_9, 2, 0, 1, 1)


        self.gridLayout_3.addWidget(self.groupBox_4, 2, 0, 1, 1)

        self.groupBox_3 = QGroupBox(bordes_window)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.horizontalLayout = QHBoxLayout(self.groupBox_3)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.groupBox_6 = QGroupBox(self.groupBox_3)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.gridLayout_2 = QGridLayout(self.groupBox_6)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.lw_variables = QListWidget(self.groupBox_6)
        QListWidgetItem(self.lw_variables)
        self.lw_variables.setObjectName(u"lw_variables")

        self.gridLayout_2.addWidget(self.lw_variables, 0, 0, 1, 1)


        self.horizontalLayout.addWidget(self.groupBox_6)

        self.gb_chbvalues = QGroupBox(self.groupBox_3)
        self.gb_chbvalues.setObjectName(u"gb_chbvalues")
        self.verticalLayout_2 = QVBoxLayout(self.gb_chbvalues)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.chb_value = QCheckBox(self.gb_chbvalues)
        self.chb_value.setObjectName(u"chb_value")
        self.chb_value.setChecked(True)
        self.chb_value.setTristate(False)

        self.verticalLayout_2.addWidget(self.chb_value)

        self.chb_flux = QCheckBox(self.gb_chbvalues)
        self.chb_flux.setObjectName(u"chb_flux")

        self.verticalLayout_2.addWidget(self.chb_flux)

        self.chb_convec = QCheckBox(self.gb_chbvalues)
        self.chb_convec.setObjectName(u"chb_convec")

        self.verticalLayout_2.addWidget(self.chb_convec)


        self.horizontalLayout.addWidget(self.gb_chbvalues)

        self.groupBox_8 = QGroupBox(self.groupBox_3)
        self.groupBox_8.setObjectName(u"groupBox_8")
        self.verticalLayout_3 = QVBoxLayout(self.groupBox_8)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_7 = QLabel(self.groupBox_8)
        self.label_7.setObjectName(u"label_7")

        self.verticalLayout_3.addWidget(self.label_7)

        self.le_value = QLineEdit(self.groupBox_8)
        self.le_value.setObjectName(u"le_value")

        self.verticalLayout_3.addWidget(self.le_value)

        self.label_8 = QLabel(self.groupBox_8)
        self.label_8.setObjectName(u"label_8")

        self.verticalLayout_3.addWidget(self.label_8)

        self.le_tempamb = QLineEdit(self.groupBox_8)
        self.le_tempamb.setObjectName(u"le_tempamb")
        self.le_tempamb.setEnabled(False)

        self.verticalLayout_3.addWidget(self.le_tempamb)


        self.horizontalLayout.addWidget(self.groupBox_8)


        self.gridLayout_3.addWidget(self.groupBox_3, 1, 0, 1, 2)

        self.gb_tipo_segment = QGroupBox(bordes_window)
        self.gb_tipo_segment.setObjectName(u"gb_tipo_segment")
        self.verticalLayout = QVBoxLayout(self.gb_tipo_segment)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.chb_wall = QCheckBox(self.gb_tipo_segment)
        self.chb_wall.setObjectName(u"chb_wall")
        self.chb_wall.setChecked(True)
        self.chb_wall.setTristate(False)

        self.verticalLayout.addWidget(self.chb_wall)

        self.chb_inmass = QCheckBox(self.gb_tipo_segment)
        self.chb_inmass.setObjectName(u"chb_inmass")
        self.chb_inmass.setEnabled(False)

        self.verticalLayout.addWidget(self.chb_inmass)

        self.chb_outmass = QCheckBox(self.gb_tipo_segment)
        self.chb_outmass.setObjectName(u"chb_outmass")
        self.chb_outmass.setEnabled(False)

        self.verticalLayout.addWidget(self.chb_outmass)


        self.gridLayout_3.addWidget(self.gb_tipo_segment, 0, 1, 1, 1)

        self.groupBox_5 = QGroupBox(bordes_window)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.horizontalLayout_34 = QHBoxLayout(self.groupBox_5)
        self.horizontalLayout_34.setObjectName(u"horizontalLayout_34")
        self.label_6 = QLabel(self.groupBox_5)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_34.addWidget(self.label_6)

        self.le_fracmass = QLineEdit(self.groupBox_5)
        self.le_fracmass.setObjectName(u"le_fracmass")
        self.le_fracmass.setEnabled(False)

        self.horizontalLayout_34.addWidget(self.le_fracmass)


        self.gridLayout_3.addWidget(self.groupBox_5, 2, 1, 1, 1)

        self.groupBox = QGroupBox(bordes_window)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout = QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 2, 3, 1, 1)

        self.sw_patchlist = QStackedWidget(self.groupBox)
        self.sw_patchlist.setObjectName(u"sw_patchlist")
        self.sw_patchlist_xmax = QWidget()
        self.sw_patchlist_xmax.setObjectName(u"sw_patchlist_xmax")
        self.verticalLayout_4 = QVBoxLayout(self.sw_patchlist_xmax)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.lw_patchlist_xmax = QListWidget(self.sw_patchlist_xmax)
        QListWidgetItem(self.lw_patchlist_xmax)
        self.lw_patchlist_xmax.setObjectName(u"lw_patchlist_xmax")

        self.verticalLayout_4.addWidget(self.lw_patchlist_xmax)

        self.sw_patchlist.addWidget(self.sw_patchlist_xmax)
        self.sw_patchlist_xmin = QWidget()
        self.sw_patchlist_xmin.setObjectName(u"sw_patchlist_xmin")
        self.horizontalLayout_2 = QHBoxLayout(self.sw_patchlist_xmin)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.lw_patchlist_xmin = QListWidget(self.sw_patchlist_xmin)
        QListWidgetItem(self.lw_patchlist_xmin)
        self.lw_patchlist_xmin.setObjectName(u"lw_patchlist_xmin")

        self.horizontalLayout_2.addWidget(self.lw_patchlist_xmin)

        self.sw_patchlist.addWidget(self.sw_patchlist_xmin)
        self.sw_patchlist_ymax = QWidget()
        self.sw_patchlist_ymax.setObjectName(u"sw_patchlist_ymax")
        self.horizontalLayout_3 = QHBoxLayout(self.sw_patchlist_ymax)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.lw_patchlist_ymax = QListWidget(self.sw_patchlist_ymax)
        QListWidgetItem(self.lw_patchlist_ymax)
        self.lw_patchlist_ymax.setObjectName(u"lw_patchlist_ymax")

        self.horizontalLayout_3.addWidget(self.lw_patchlist_ymax)

        self.sw_patchlist.addWidget(self.sw_patchlist_ymax)
        self.sw_patchlist_ymin = QWidget()
        self.sw_patchlist_ymin.setObjectName(u"sw_patchlist_ymin")
        self.verticalLayout_11 = QVBoxLayout(self.sw_patchlist_ymin)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.lw_patchlist_ymin = QListWidget(self.sw_patchlist_ymin)
        QListWidgetItem(self.lw_patchlist_ymin)
        self.lw_patchlist_ymin.setObjectName(u"lw_patchlist_ymin")

        self.verticalLayout_11.addWidget(self.lw_patchlist_ymin)

        self.sw_patchlist.addWidget(self.sw_patchlist_ymin)
        self.sw_patchlist_zmax = QWidget()
        self.sw_patchlist_zmax.setObjectName(u"sw_patchlist_zmax")
        self.horizontalLayout_4 = QHBoxLayout(self.sw_patchlist_zmax)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.lw_patchlist_zmax = QListWidget(self.sw_patchlist_zmax)
        QListWidgetItem(self.lw_patchlist_zmax)
        self.lw_patchlist_zmax.setObjectName(u"lw_patchlist_zmax")

        self.horizontalLayout_4.addWidget(self.lw_patchlist_zmax)

        self.sw_patchlist.addWidget(self.sw_patchlist_zmax)
        self.sw_patchlist_zmin = QWidget()
        self.sw_patchlist_zmin.setObjectName(u"sw_patchlist_zmin")
        self.verticalLayout_12 = QVBoxLayout(self.sw_patchlist_zmin)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.lw_patchlist_zmin = QListWidget(self.sw_patchlist_zmin)
        QListWidgetItem(self.lw_patchlist_zmin)
        self.lw_patchlist_zmin.setObjectName(u"lw_patchlist_zmin")

        self.verticalLayout_12.addWidget(self.lw_patchlist_zmin)

        self.sw_patchlist.addWidget(self.sw_patchlist_zmin)

        self.gridLayout.addWidget(self.sw_patchlist, 3, 3, 1, 1)

        self.lw_bordes = QListWidget(self.groupBox)
        QListWidgetItem(self.lw_bordes)
        QListWidgetItem(self.lw_bordes)
        QListWidgetItem(self.lw_bordes)
        QListWidgetItem(self.lw_bordes)
        QListWidgetItem(self.lw_bordes)
        QListWidgetItem(self.lw_bordes)
        self.lw_bordes.setObjectName(u"lw_bordes")

        self.gridLayout.addWidget(self.lw_bordes, 3, 0, 1, 3)

        self.sw_patch_addremove = QStackedWidget(self.groupBox)
        self.sw_patch_addremove.setObjectName(u"sw_patch_addremove")
        self.sw_patch_addremove_xmax = QWidget()
        self.sw_patch_addremove_xmax.setObjectName(u"sw_patch_addremove_xmax")
        self.verticalLayout_5 = QVBoxLayout(self.sw_patch_addremove_xmax)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.pb_addpatch_xmax = QPushButton(self.sw_patch_addremove_xmax)
        self.pb_addpatch_xmax.setObjectName(u"pb_addpatch_xmax")

        self.verticalLayout_5.addWidget(self.pb_addpatch_xmax)

        self.pb_rempatch_xmax = QPushButton(self.sw_patch_addremove_xmax)
        self.pb_rempatch_xmax.setObjectName(u"pb_rempatch_xmax")

        self.verticalLayout_5.addWidget(self.pb_rempatch_xmax)

        self.sw_patch_addremove.addWidget(self.sw_patch_addremove_xmax)
        self.sw_patch_addremove_xmin = QWidget()
        self.sw_patch_addremove_xmin.setObjectName(u"sw_patch_addremove_xmin")
        self.verticalLayout_6 = QVBoxLayout(self.sw_patch_addremove_xmin)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.pb_addpatch_xmin = QPushButton(self.sw_patch_addremove_xmin)
        self.pb_addpatch_xmin.setObjectName(u"pb_addpatch_xmin")

        self.verticalLayout_6.addWidget(self.pb_addpatch_xmin)

        self.pb_rempatch_xmin = QPushButton(self.sw_patch_addremove_xmin)
        self.pb_rempatch_xmin.setObjectName(u"pb_rempatch_xmin")

        self.verticalLayout_6.addWidget(self.pb_rempatch_xmin)

        self.sw_patch_addremove.addWidget(self.sw_patch_addremove_xmin)
        self.sw_patch_addremove_ymax = QWidget()
        self.sw_patch_addremove_ymax.setObjectName(u"sw_patch_addremove_ymax")
        self.verticalLayout_7 = QVBoxLayout(self.sw_patch_addremove_ymax)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.pb_addpatch_ymax = QPushButton(self.sw_patch_addremove_ymax)
        self.pb_addpatch_ymax.setObjectName(u"pb_addpatch_ymax")

        self.verticalLayout_7.addWidget(self.pb_addpatch_ymax)

        self.pb_rempatch_ymax = QPushButton(self.sw_patch_addremove_ymax)
        self.pb_rempatch_ymax.setObjectName(u"pb_rempatch_ymax")

        self.verticalLayout_7.addWidget(self.pb_rempatch_ymax)

        self.sw_patch_addremove.addWidget(self.sw_patch_addremove_ymax)
        self.sw_patch_addremove_ymin = QWidget()
        self.sw_patch_addremove_ymin.setObjectName(u"sw_patch_addremove_ymin")
        self.verticalLayout_8 = QVBoxLayout(self.sw_patch_addremove_ymin)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.pb_addpatch_ymin = QPushButton(self.sw_patch_addremove_ymin)
        self.pb_addpatch_ymin.setObjectName(u"pb_addpatch_ymin")

        self.verticalLayout_8.addWidget(self.pb_addpatch_ymin)

        self.pb_rempatch_ymin = QPushButton(self.sw_patch_addremove_ymin)
        self.pb_rempatch_ymin.setObjectName(u"pb_rempatch_ymin")

        self.verticalLayout_8.addWidget(self.pb_rempatch_ymin)

        self.sw_patch_addremove.addWidget(self.sw_patch_addremove_ymin)
        self.sw_patch_addremove_zmax = QWidget()
        self.sw_patch_addremove_zmax.setObjectName(u"sw_patch_addremove_zmax")
        self.verticalLayout_9 = QVBoxLayout(self.sw_patch_addremove_zmax)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.pb_addpatch_zmax = QPushButton(self.sw_patch_addremove_zmax)
        self.pb_addpatch_zmax.setObjectName(u"pb_addpatch_zmax")

        self.verticalLayout_9.addWidget(self.pb_addpatch_zmax)

        self.pb_rempatch_zmax = QPushButton(self.sw_patch_addremove_zmax)
        self.pb_rempatch_zmax.setObjectName(u"pb_rempatch_zmax")

        self.verticalLayout_9.addWidget(self.pb_rempatch_zmax)

        self.sw_patch_addremove.addWidget(self.sw_patch_addremove_zmax)
        self.sw_patch_addremove_zmin = QWidget()
        self.sw_patch_addremove_zmin.setObjectName(u"sw_patch_addremove_zmin")
        self.verticalLayout_10 = QVBoxLayout(self.sw_patch_addremove_zmin)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.pb_addpatch_zmin = QPushButton(self.sw_patch_addremove_zmin)
        self.pb_addpatch_zmin.setObjectName(u"pb_addpatch_zmin")

        self.verticalLayout_10.addWidget(self.pb_addpatch_zmin)

        self.pb_rempatch_zmin = QPushButton(self.sw_patch_addremove_zmin)
        self.pb_rempatch_zmin.setObjectName(u"pb_rempatch_zmin")

        self.verticalLayout_10.addWidget(self.pb_rempatch_zmin)

        self.sw_patch_addremove.addWidget(self.sw_patch_addremove_zmin)

        self.gridLayout.addWidget(self.sw_patch_addremove, 5, 0, 1, 4)

        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 2)

        self.groupBox_2 = QGroupBox(self.groupBox)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.gridLayout_5 = QGridLayout(self.groupBox_2)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.le_vertical_lon = QLineEdit(self.groupBox_2)
        self.le_vertical_lon.setObjectName(u"le_vertical_lon")

        self.gridLayout_5.addWidget(self.le_vertical_lon, 1, 2, 1, 1)

        self.le_transversal_start = QLineEdit(self.groupBox_2)
        self.le_transversal_start.setObjectName(u"le_transversal_start")

        self.gridLayout_5.addWidget(self.le_transversal_start, 3, 1, 1, 1)

        self.label = QLabel(self.groupBox_2)
        self.label.setObjectName(u"label")

        self.gridLayout_5.addWidget(self.label, 1, 0, 1, 1)

        self.label_10 = QLabel(self.groupBox_2)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout_5.addWidget(self.label_10, 3, 0, 1, 1)

        self.le_transversal_lon = QLineEdit(self.groupBox_2)
        self.le_transversal_lon.setObjectName(u"le_transversal_lon")

        self.gridLayout_5.addWidget(self.le_transversal_lon, 1, 1, 1, 1)

        self.le_vertical_start = QLineEdit(self.groupBox_2)
        self.le_vertical_start.setObjectName(u"le_vertical_start")

        self.gridLayout_5.addWidget(self.le_vertical_start, 3, 2, 1, 1)

        self.lb_transversal = QLabel(self.groupBox_2)
        self.lb_transversal.setObjectName(u"lb_transversal")
        self.lb_transversal.setLayoutDirection(Qt.LeftToRight)
        self.lb_transversal.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.lb_transversal, 0, 1, 1, 1)

        self.lb_vertical = QLabel(self.groupBox_2)
        self.lb_vertical.setObjectName(u"lb_vertical")
        self.lb_vertical.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.lb_vertical, 0, 2, 1, 1)


        self.gridLayout.addWidget(self.groupBox_2, 1, 0, 1, 4)


        self.gridLayout_3.addWidget(self.groupBox, 0, 0, 1, 1)


        self.retranslateUi(bordes_window)

        self.sw_patchlist.setCurrentIndex(0)
        self.sw_patch_addremove.setCurrentIndex(5)


        QMetaObject.connectSlotsByName(bordes_window)
    # setupUi

    def retranslateUi(self, bordes_window):
        bordes_window.setWindowTitle(QCoreApplication.translate("bordes_window", u"Bordes - PrePRODIC3D", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("bordes_window", u"Velocidad", None))
        self.label_4.setText(QCoreApplication.translate("bordes_window", u"Velocidad U", None))
        self.label_5.setText(QCoreApplication.translate("bordes_window", u"Velocidad V", None))
        self.label_9.setText(QCoreApplication.translate("bordes_window", u"Velocidad W", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("bordes_window", u"Variables escalares", None))
        self.groupBox_6.setTitle("")

        __sortingEnabled = self.lw_variables.isSortingEnabled()
        self.lw_variables.setSortingEnabled(False)
        ___qlistwidgetitem = self.lw_variables.item(0)
        ___qlistwidgetitem.setText(QCoreApplication.translate("bordes_window", u"Temperatura", None));
        self.lw_variables.setSortingEnabled(__sortingEnabled)

        self.gb_chbvalues.setTitle("")
        self.chb_value.setText(QCoreApplication.translate("bordes_window", u"Valor", None))
        self.chb_flux.setText(QCoreApplication.translate("bordes_window", u"Flujo", None))
        self.chb_convec.setText(QCoreApplication.translate("bordes_window", u"Convecci\u00f3n", None))
        self.groupBox_8.setTitle("")
        self.label_7.setText(QCoreApplication.translate("bordes_window", u"Valor", None))
        self.label_8.setText(QCoreApplication.translate("bordes_window", u"Temp. ambiente", None))
        self.gb_tipo_segment.setTitle(QCoreApplication.translate("bordes_window", u"Tipo de segmento", None))
        self.chb_wall.setText(QCoreApplication.translate("bordes_window", u"Pared", None))
        self.chb_inmass.setText(QCoreApplication.translate("bordes_window", u"Entrada de la masa", None))
        self.chb_outmass.setText(QCoreApplication.translate("bordes_window", u"Salida de la masa", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("bordes_window", u"Salida de la masa", None))
        self.label_6.setText(QCoreApplication.translate("bordes_window", u"Fracci\u00f3n", None))
        self.groupBox.setTitle(QCoreApplication.translate("bordes_window", u"Divisi\u00f3n de bordes", None))
        self.label_3.setText(QCoreApplication.translate("bordes_window", u"Segmento", None))

        __sortingEnabled1 = self.lw_patchlist_xmax.isSortingEnabled()
        self.lw_patchlist_xmax.setSortingEnabled(False)
        ___qlistwidgetitem1 = self.lw_patchlist_xmax.item(0)
        ___qlistwidgetitem1.setText(QCoreApplication.translate("bordes_window", u"Borde base", None));
        self.lw_patchlist_xmax.setSortingEnabled(__sortingEnabled1)


        __sortingEnabled2 = self.lw_patchlist_xmin.isSortingEnabled()
        self.lw_patchlist_xmin.setSortingEnabled(False)
        ___qlistwidgetitem2 = self.lw_patchlist_xmin.item(0)
        ___qlistwidgetitem2.setText(QCoreApplication.translate("bordes_window", u"Borde base", None));
        self.lw_patchlist_xmin.setSortingEnabled(__sortingEnabled2)


        __sortingEnabled3 = self.lw_patchlist_ymax.isSortingEnabled()
        self.lw_patchlist_ymax.setSortingEnabled(False)
        ___qlistwidgetitem3 = self.lw_patchlist_ymax.item(0)
        ___qlistwidgetitem3.setText(QCoreApplication.translate("bordes_window", u"Borde base", None));
        self.lw_patchlist_ymax.setSortingEnabled(__sortingEnabled3)


        __sortingEnabled4 = self.lw_patchlist_ymin.isSortingEnabled()
        self.lw_patchlist_ymin.setSortingEnabled(False)
        ___qlistwidgetitem4 = self.lw_patchlist_ymin.item(0)
        ___qlistwidgetitem4.setText(QCoreApplication.translate("bordes_window", u"Borde base", None));
        self.lw_patchlist_ymin.setSortingEnabled(__sortingEnabled4)


        __sortingEnabled5 = self.lw_patchlist_zmax.isSortingEnabled()
        self.lw_patchlist_zmax.setSortingEnabled(False)
        ___qlistwidgetitem5 = self.lw_patchlist_zmax.item(0)
        ___qlistwidgetitem5.setText(QCoreApplication.translate("bordes_window", u"Borde base", None));
        self.lw_patchlist_zmax.setSortingEnabled(__sortingEnabled5)


        __sortingEnabled6 = self.lw_patchlist_zmin.isSortingEnabled()
        self.lw_patchlist_zmin.setSortingEnabled(False)
        ___qlistwidgetitem6 = self.lw_patchlist_zmin.item(0)
        ___qlistwidgetitem6.setText(QCoreApplication.translate("bordes_window", u"Borde base", None));
        self.lw_patchlist_zmin.setSortingEnabled(__sortingEnabled6)


        __sortingEnabled7 = self.lw_bordes.isSortingEnabled()
        self.lw_bordes.setSortingEnabled(False)
        ___qlistwidgetitem7 = self.lw_bordes.item(0)
        ___qlistwidgetitem7.setText(QCoreApplication.translate("bordes_window", u"X Max", None));
        ___qlistwidgetitem8 = self.lw_bordes.item(1)
        ___qlistwidgetitem8.setText(QCoreApplication.translate("bordes_window", u"X Min", None));
        ___qlistwidgetitem9 = self.lw_bordes.item(2)
        ___qlistwidgetitem9.setText(QCoreApplication.translate("bordes_window", u"Y Max", None));
        ___qlistwidgetitem10 = self.lw_bordes.item(3)
        ___qlistwidgetitem10.setText(QCoreApplication.translate("bordes_window", u"Y Min", None));
        ___qlistwidgetitem11 = self.lw_bordes.item(4)
        ___qlistwidgetitem11.setText(QCoreApplication.translate("bordes_window", u"Z Max", None));
        ___qlistwidgetitem12 = self.lw_bordes.item(5)
        ___qlistwidgetitem12.setText(QCoreApplication.translate("bordes_window", u"Z Min", None));
        self.lw_bordes.setSortingEnabled(__sortingEnabled7)

        self.pb_addpatch_xmax.setText(QCoreApplication.translate("bordes_window", u"Agregar un segmento", None))
        self.pb_rempatch_xmax.setText(QCoreApplication.translate("bordes_window", u"Eliminar un segmento", None))
        self.pb_addpatch_xmin.setText(QCoreApplication.translate("bordes_window", u"Agregar un segmento", None))
        self.pb_rempatch_xmin.setText(QCoreApplication.translate("bordes_window", u"Eliminar un segmento", None))
        self.pb_addpatch_ymax.setText(QCoreApplication.translate("bordes_window", u"Agregar un segmento", None))
        self.pb_rempatch_ymax.setText(QCoreApplication.translate("bordes_window", u"Eliminar un segmento", None))
        self.pb_addpatch_ymin.setText(QCoreApplication.translate("bordes_window", u"Agregar un segmento", None))
        self.pb_rempatch_ymin.setText(QCoreApplication.translate("bordes_window", u"Eliminar un segmento", None))
        self.pb_addpatch_zmax.setText(QCoreApplication.translate("bordes_window", u"Agregar un segmento", None))
        self.pb_rempatch_zmax.setText(QCoreApplication.translate("bordes_window", u"Eliminar un segmento", None))
        self.pb_addpatch_zmin.setText(QCoreApplication.translate("bordes_window", u"Agregar un segmento", None))
        self.pb_rempatch_zmin.setText(QCoreApplication.translate("bordes_window", u"Eliminar un segmento", None))
        self.label_2.setText(QCoreApplication.translate("bordes_window", u"Borde", None))
        self.groupBox_2.setTitle("")
        self.label.setText(QCoreApplication.translate("bordes_window", u"Longitud", None))
        self.label_10.setText(QCoreApplication.translate("bordes_window", u"Empieza", None))
        self.lb_transversal.setText(QCoreApplication.translate("bordes_window", u"Y", None))
        self.lb_vertical.setText(QCoreApplication.translate("bordes_window", u"Z", None))
    # retranslateUi

