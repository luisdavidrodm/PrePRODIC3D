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
        self.horizontalLayout_35 = QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_35.setObjectName(u"horizontalLayout_35")
        self.sw_lon_patch = QStackedWidget(self.groupBox_2)
        self.sw_lon_patch.setObjectName(u"sw_lon_patch")
        self.sw_lon_patch_xmax_1 = QWidget()
        self.sw_lon_patch_xmax_1.setObjectName(u"sw_lon_patch_xmax_1")
        self.gridLayout_5 = QGridLayout(self.sw_lon_patch_xmax_1)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.label_11 = QLabel(self.sw_lon_patch_xmax_1)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.label_11, 0, 2, 1, 1)

        self.le_xmax_bb_zstart = QLineEdit(self.sw_lon_patch_xmax_1)
        self.le_xmax_bb_zstart.setObjectName(u"le_xmax_bb_zstart")

        self.gridLayout_5.addWidget(self.le_xmax_bb_zstart, 1, 2, 1, 1)

        self.le_xmax_bb_ystart = QLineEdit(self.sw_lon_patch_xmax_1)
        self.le_xmax_bb_ystart.setObjectName(u"le_xmax_bb_ystart")

        self.gridLayout_5.addWidget(self.le_xmax_bb_ystart, 1, 1, 1, 1)

        self.le_xmax_bb_zlon = QLineEdit(self.sw_lon_patch_xmax_1)
        self.le_xmax_bb_zlon.setObjectName(u"le_xmax_bb_zlon")

        self.gridLayout_5.addWidget(self.le_xmax_bb_zlon, 2, 2, 1, 1)

        self.le_xmax_bb_ylon = QLineEdit(self.sw_lon_patch_xmax_1)
        self.le_xmax_bb_ylon.setObjectName(u"le_xmax_bb_ylon")

        self.gridLayout_5.addWidget(self.le_xmax_bb_ylon, 2, 1, 1, 1)

        self.label_10 = QLabel(self.sw_lon_patch_xmax_1)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.label_10, 0, 1, 1, 1)

        self.label_12 = QLabel(self.sw_lon_patch_xmax_1)
        self.label_12.setObjectName(u"label_12")

        self.gridLayout_5.addWidget(self.label_12, 1, 0, 1, 1)

        self.label_13 = QLabel(self.sw_lon_patch_xmax_1)
        self.label_13.setObjectName(u"label_13")

        self.gridLayout_5.addWidget(self.label_13, 2, 0, 1, 1)

        self.sw_lon_patch.addWidget(self.sw_lon_patch_xmax_1)
        self.sw_lon_patch_xmax_2 = QWidget()
        self.sw_lon_patch_xmax_2.setObjectName(u"sw_lon_patch_xmax_2")
        self.gridLayout_6 = QGridLayout(self.sw_lon_patch_xmax_2)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.label_16 = QLabel(self.sw_lon_patch_xmax_2)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setAlignment(Qt.AlignCenter)

        self.gridLayout_6.addWidget(self.label_16, 0, 1, 1, 1)

        self.label_17 = QLabel(self.sw_lon_patch_xmax_2)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setAlignment(Qt.AlignCenter)

        self.gridLayout_6.addWidget(self.label_17, 0, 2, 1, 1)

        self.label_14 = QLabel(self.sw_lon_patch_xmax_2)
        self.label_14.setObjectName(u"label_14")

        self.gridLayout_6.addWidget(self.label_14, 1, 0, 1, 1)

        self.lineEdit_4 = QLineEdit(self.sw_lon_patch_xmax_2)
        self.lineEdit_4.setObjectName(u"lineEdit_4")

        self.gridLayout_6.addWidget(self.lineEdit_4, 1, 1, 1, 1)

        self.le_lon_segment_xmax_2 = QLineEdit(self.sw_lon_patch_xmax_2)
        self.le_lon_segment_xmax_2.setObjectName(u"le_lon_segment_xmax_2")

        self.gridLayout_6.addWidget(self.le_lon_segment_xmax_2, 1, 2, 1, 1)

        self.label_15 = QLabel(self.sw_lon_patch_xmax_2)
        self.label_15.setObjectName(u"label_15")

        self.gridLayout_6.addWidget(self.label_15, 2, 0, 1, 1)

        self.lineEdit_5 = QLineEdit(self.sw_lon_patch_xmax_2)
        self.lineEdit_5.setObjectName(u"lineEdit_5")

        self.gridLayout_6.addWidget(self.lineEdit_5, 2, 1, 1, 1)

        self.lineEdit_6 = QLineEdit(self.sw_lon_patch_xmax_2)
        self.lineEdit_6.setObjectName(u"lineEdit_6")

        self.gridLayout_6.addWidget(self.lineEdit_6, 2, 2, 1, 1)

        self.sw_lon_patch.addWidget(self.sw_lon_patch_xmax_2)
        self.sw_lon_patch_xmax_3 = QWidget()
        self.sw_lon_patch_xmax_3.setObjectName(u"sw_lon_patch_xmax_3")
        self.gridLayout_7 = QGridLayout(self.sw_lon_patch_xmax_3)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.label_19 = QLabel(self.sw_lon_patch_xmax_3)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setAlignment(Qt.AlignCenter)

        self.gridLayout_7.addWidget(self.label_19, 0, 1, 1, 1)

        self.label_21 = QLabel(self.sw_lon_patch_xmax_3)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setAlignment(Qt.AlignCenter)

        self.gridLayout_7.addWidget(self.label_21, 0, 2, 1, 1)

        self.label_20 = QLabel(self.sw_lon_patch_xmax_3)
        self.label_20.setObjectName(u"label_20")

        self.gridLayout_7.addWidget(self.label_20, 1, 0, 1, 1)

        self.lineEdit_8 = QLineEdit(self.sw_lon_patch_xmax_3)
        self.lineEdit_8.setObjectName(u"lineEdit_8")

        self.gridLayout_7.addWidget(self.lineEdit_8, 1, 1, 1, 1)

        self.le_lon_segment_xmax_3 = QLineEdit(self.sw_lon_patch_xmax_3)
        self.le_lon_segment_xmax_3.setObjectName(u"le_lon_segment_xmax_3")

        self.gridLayout_7.addWidget(self.le_lon_segment_xmax_3, 1, 2, 1, 1)

        self.label_18 = QLabel(self.sw_lon_patch_xmax_3)
        self.label_18.setObjectName(u"label_18")

        self.gridLayout_7.addWidget(self.label_18, 2, 0, 1, 1)

        self.lineEdit_9 = QLineEdit(self.sw_lon_patch_xmax_3)
        self.lineEdit_9.setObjectName(u"lineEdit_9")

        self.gridLayout_7.addWidget(self.lineEdit_9, 2, 1, 1, 1)

        self.lineEdit_7 = QLineEdit(self.sw_lon_patch_xmax_3)
        self.lineEdit_7.setObjectName(u"lineEdit_7")

        self.gridLayout_7.addWidget(self.lineEdit_7, 2, 2, 1, 1)

        self.sw_lon_patch.addWidget(self.sw_lon_patch_xmax_3)
        self.sw_lon_patch_xmax_4 = QWidget()
        self.sw_lon_patch_xmax_4.setObjectName(u"sw_lon_patch_xmax_4")
        self.gridLayout_8 = QGridLayout(self.sw_lon_patch_xmax_4)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.label_23 = QLabel(self.sw_lon_patch_xmax_4)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setAlignment(Qt.AlignCenter)

        self.gridLayout_8.addWidget(self.label_23, 0, 1, 1, 1)

        self.label_25 = QLabel(self.sw_lon_patch_xmax_4)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setAlignment(Qt.AlignCenter)

        self.gridLayout_8.addWidget(self.label_25, 0, 2, 1, 1)

        self.label_24 = QLabel(self.sw_lon_patch_xmax_4)
        self.label_24.setObjectName(u"label_24")

        self.gridLayout_8.addWidget(self.label_24, 1, 0, 1, 1)

        self.lineEdit_11 = QLineEdit(self.sw_lon_patch_xmax_4)
        self.lineEdit_11.setObjectName(u"lineEdit_11")

        self.gridLayout_8.addWidget(self.lineEdit_11, 1, 1, 1, 1)

        self.le_lon_segment_xmax_4 = QLineEdit(self.sw_lon_patch_xmax_4)
        self.le_lon_segment_xmax_4.setObjectName(u"le_lon_segment_xmax_4")

        self.gridLayout_8.addWidget(self.le_lon_segment_xmax_4, 1, 2, 1, 1)

        self.label_22 = QLabel(self.sw_lon_patch_xmax_4)
        self.label_22.setObjectName(u"label_22")

        self.gridLayout_8.addWidget(self.label_22, 2, 0, 1, 1)

        self.lineEdit_12 = QLineEdit(self.sw_lon_patch_xmax_4)
        self.lineEdit_12.setObjectName(u"lineEdit_12")

        self.gridLayout_8.addWidget(self.lineEdit_12, 2, 1, 1, 1)

        self.lineEdit_10 = QLineEdit(self.sw_lon_patch_xmax_4)
        self.lineEdit_10.setObjectName(u"lineEdit_10")

        self.gridLayout_8.addWidget(self.lineEdit_10, 2, 2, 1, 1)

        self.sw_lon_patch.addWidget(self.sw_lon_patch_xmax_4)
        self.sw_lon_patch_xmax_5 = QWidget()
        self.sw_lon_patch_xmax_5.setObjectName(u"sw_lon_patch_xmax_5")
        self.gridLayout_9 = QGridLayout(self.sw_lon_patch_xmax_5)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.label_27 = QLabel(self.sw_lon_patch_xmax_5)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setAlignment(Qt.AlignCenter)

        self.gridLayout_9.addWidget(self.label_27, 0, 1, 1, 1)

        self.label_29 = QLabel(self.sw_lon_patch_xmax_5)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setAlignment(Qt.AlignCenter)

        self.gridLayout_9.addWidget(self.label_29, 0, 2, 1, 1)

        self.label_28 = QLabel(self.sw_lon_patch_xmax_5)
        self.label_28.setObjectName(u"label_28")

        self.gridLayout_9.addWidget(self.label_28, 1, 0, 1, 1)

        self.lineEdit_14 = QLineEdit(self.sw_lon_patch_xmax_5)
        self.lineEdit_14.setObjectName(u"lineEdit_14")

        self.gridLayout_9.addWidget(self.lineEdit_14, 1, 1, 1, 1)

        self.le_lon_segment_xmax_5 = QLineEdit(self.sw_lon_patch_xmax_5)
        self.le_lon_segment_xmax_5.setObjectName(u"le_lon_segment_xmax_5")

        self.gridLayout_9.addWidget(self.le_lon_segment_xmax_5, 1, 2, 1, 1)

        self.label_26 = QLabel(self.sw_lon_patch_xmax_5)
        self.label_26.setObjectName(u"label_26")

        self.gridLayout_9.addWidget(self.label_26, 2, 0, 1, 1)

        self.lineEdit_15 = QLineEdit(self.sw_lon_patch_xmax_5)
        self.lineEdit_15.setObjectName(u"lineEdit_15")

        self.gridLayout_9.addWidget(self.lineEdit_15, 2, 1, 1, 1)

        self.lineEdit_13 = QLineEdit(self.sw_lon_patch_xmax_5)
        self.lineEdit_13.setObjectName(u"lineEdit_13")

        self.gridLayout_9.addWidget(self.lineEdit_13, 2, 2, 1, 1)

        self.sw_lon_patch.addWidget(self.sw_lon_patch_xmax_5)
        self.sw_lon_patch_xmin_1 = QWidget()
        self.sw_lon_patch_xmin_1.setObjectName(u"sw_lon_patch_xmin_1")
        self.gridLayout_10 = QGridLayout(self.sw_lon_patch_xmin_1)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.label_31 = QLabel(self.sw_lon_patch_xmin_1)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setAlignment(Qt.AlignCenter)

        self.gridLayout_10.addWidget(self.label_31, 0, 1, 1, 1)

        self.label_33 = QLabel(self.sw_lon_patch_xmin_1)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setAlignment(Qt.AlignCenter)

        self.gridLayout_10.addWidget(self.label_33, 0, 2, 1, 1)

        self.label_32 = QLabel(self.sw_lon_patch_xmin_1)
        self.label_32.setObjectName(u"label_32")

        self.gridLayout_10.addWidget(self.label_32, 1, 0, 1, 1)

        self.le_xmin_bb_ystart = QLineEdit(self.sw_lon_patch_xmin_1)
        self.le_xmin_bb_ystart.setObjectName(u"le_xmin_bb_ystart")

        self.gridLayout_10.addWidget(self.le_xmin_bb_ystart, 1, 1, 1, 1)

        self.le_xmin_bb_zstart = QLineEdit(self.sw_lon_patch_xmin_1)
        self.le_xmin_bb_zstart.setObjectName(u"le_xmin_bb_zstart")

        self.gridLayout_10.addWidget(self.le_xmin_bb_zstart, 1, 2, 1, 1)

        self.label_30 = QLabel(self.sw_lon_patch_xmin_1)
        self.label_30.setObjectName(u"label_30")

        self.gridLayout_10.addWidget(self.label_30, 2, 0, 1, 1)

        self.le_xmin_bb_ylon = QLineEdit(self.sw_lon_patch_xmin_1)
        self.le_xmin_bb_ylon.setObjectName(u"le_xmin_bb_ylon")

        self.gridLayout_10.addWidget(self.le_xmin_bb_ylon, 2, 1, 1, 1)

        self.le_xmin_bb_zlon = QLineEdit(self.sw_lon_patch_xmin_1)
        self.le_xmin_bb_zlon.setObjectName(u"le_xmin_bb_zlon")

        self.gridLayout_10.addWidget(self.le_xmin_bb_zlon, 2, 2, 1, 1)

        self.sw_lon_patch.addWidget(self.sw_lon_patch_xmin_1)
        self.sw_lon_patch_xmin_2 = QWidget()
        self.sw_lon_patch_xmin_2.setObjectName(u"sw_lon_patch_xmin_2")
        self.gridLayout_11 = QGridLayout(self.sw_lon_patch_xmin_2)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.label_35 = QLabel(self.sw_lon_patch_xmin_2)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setAlignment(Qt.AlignCenter)

        self.gridLayout_11.addWidget(self.label_35, 0, 1, 1, 1)

        self.label_37 = QLabel(self.sw_lon_patch_xmin_2)
        self.label_37.setObjectName(u"label_37")
        self.label_37.setAlignment(Qt.AlignCenter)

        self.gridLayout_11.addWidget(self.label_37, 0, 2, 1, 1)

        self.label_36 = QLabel(self.sw_lon_patch_xmin_2)
        self.label_36.setObjectName(u"label_36")

        self.gridLayout_11.addWidget(self.label_36, 1, 0, 1, 1)

        self.lineEdit_20 = QLineEdit(self.sw_lon_patch_xmin_2)
        self.lineEdit_20.setObjectName(u"lineEdit_20")

        self.gridLayout_11.addWidget(self.lineEdit_20, 1, 1, 1, 1)

        self.le_lon_segment_xmax_7 = QLineEdit(self.sw_lon_patch_xmin_2)
        self.le_lon_segment_xmax_7.setObjectName(u"le_lon_segment_xmax_7")

        self.gridLayout_11.addWidget(self.le_lon_segment_xmax_7, 1, 2, 1, 1)

        self.label_34 = QLabel(self.sw_lon_patch_xmin_2)
        self.label_34.setObjectName(u"label_34")

        self.gridLayout_11.addWidget(self.label_34, 2, 0, 1, 1)

        self.lineEdit_21 = QLineEdit(self.sw_lon_patch_xmin_2)
        self.lineEdit_21.setObjectName(u"lineEdit_21")

        self.gridLayout_11.addWidget(self.lineEdit_21, 2, 1, 1, 1)

        self.lineEdit_19 = QLineEdit(self.sw_lon_patch_xmin_2)
        self.lineEdit_19.setObjectName(u"lineEdit_19")

        self.gridLayout_11.addWidget(self.lineEdit_19, 2, 2, 1, 1)

        self.sw_lon_patch.addWidget(self.sw_lon_patch_xmin_2)
        self.sw_lon_patch_xmin_3 = QWidget()
        self.sw_lon_patch_xmin_3.setObjectName(u"sw_lon_patch_xmin_3")
        self.gridLayout_12 = QGridLayout(self.sw_lon_patch_xmin_3)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.label_39 = QLabel(self.sw_lon_patch_xmin_3)
        self.label_39.setObjectName(u"label_39")
        self.label_39.setAlignment(Qt.AlignCenter)

        self.gridLayout_12.addWidget(self.label_39, 0, 1, 1, 1)

        self.label_41 = QLabel(self.sw_lon_patch_xmin_3)
        self.label_41.setObjectName(u"label_41")
        self.label_41.setAlignment(Qt.AlignCenter)

        self.gridLayout_12.addWidget(self.label_41, 0, 2, 1, 1)

        self.label_40 = QLabel(self.sw_lon_patch_xmin_3)
        self.label_40.setObjectName(u"label_40")

        self.gridLayout_12.addWidget(self.label_40, 1, 0, 1, 1)

        self.lineEdit_23 = QLineEdit(self.sw_lon_patch_xmin_3)
        self.lineEdit_23.setObjectName(u"lineEdit_23")

        self.gridLayout_12.addWidget(self.lineEdit_23, 1, 1, 1, 1)

        self.le_lon_segment_xmax_8 = QLineEdit(self.sw_lon_patch_xmin_3)
        self.le_lon_segment_xmax_8.setObjectName(u"le_lon_segment_xmax_8")

        self.gridLayout_12.addWidget(self.le_lon_segment_xmax_8, 1, 2, 1, 1)

        self.label_38 = QLabel(self.sw_lon_patch_xmin_3)
        self.label_38.setObjectName(u"label_38")

        self.gridLayout_12.addWidget(self.label_38, 2, 0, 1, 1)

        self.lineEdit_24 = QLineEdit(self.sw_lon_patch_xmin_3)
        self.lineEdit_24.setObjectName(u"lineEdit_24")

        self.gridLayout_12.addWidget(self.lineEdit_24, 2, 1, 1, 1)

        self.lineEdit_22 = QLineEdit(self.sw_lon_patch_xmin_3)
        self.lineEdit_22.setObjectName(u"lineEdit_22")

        self.gridLayout_12.addWidget(self.lineEdit_22, 2, 2, 1, 1)

        self.sw_lon_patch.addWidget(self.sw_lon_patch_xmin_3)
        self.sw_lon_patch_xmin_4 = QWidget()
        self.sw_lon_patch_xmin_4.setObjectName(u"sw_lon_patch_xmin_4")
        self.gridLayout_13 = QGridLayout(self.sw_lon_patch_xmin_4)
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.label_43 = QLabel(self.sw_lon_patch_xmin_4)
        self.label_43.setObjectName(u"label_43")
        self.label_43.setAlignment(Qt.AlignCenter)

        self.gridLayout_13.addWidget(self.label_43, 0, 1, 1, 1)

        self.label_45 = QLabel(self.sw_lon_patch_xmin_4)
        self.label_45.setObjectName(u"label_45")
        self.label_45.setAlignment(Qt.AlignCenter)

        self.gridLayout_13.addWidget(self.label_45, 0, 2, 1, 1)

        self.label_44 = QLabel(self.sw_lon_patch_xmin_4)
        self.label_44.setObjectName(u"label_44")

        self.gridLayout_13.addWidget(self.label_44, 1, 0, 1, 1)

        self.lineEdit_26 = QLineEdit(self.sw_lon_patch_xmin_4)
        self.lineEdit_26.setObjectName(u"lineEdit_26")

        self.gridLayout_13.addWidget(self.lineEdit_26, 1, 1, 1, 1)

        self.le_lon_segment_xmax_9 = QLineEdit(self.sw_lon_patch_xmin_4)
        self.le_lon_segment_xmax_9.setObjectName(u"le_lon_segment_xmax_9")

        self.gridLayout_13.addWidget(self.le_lon_segment_xmax_9, 1, 2, 1, 1)

        self.label_42 = QLabel(self.sw_lon_patch_xmin_4)
        self.label_42.setObjectName(u"label_42")

        self.gridLayout_13.addWidget(self.label_42, 2, 0, 1, 1)

        self.lineEdit_27 = QLineEdit(self.sw_lon_patch_xmin_4)
        self.lineEdit_27.setObjectName(u"lineEdit_27")

        self.gridLayout_13.addWidget(self.lineEdit_27, 2, 1, 1, 1)

        self.lineEdit_25 = QLineEdit(self.sw_lon_patch_xmin_4)
        self.lineEdit_25.setObjectName(u"lineEdit_25")

        self.gridLayout_13.addWidget(self.lineEdit_25, 2, 2, 1, 1)

        self.sw_lon_patch.addWidget(self.sw_lon_patch_xmin_4)
        self.sw_lon_patch_xmin_5 = QWidget()
        self.sw_lon_patch_xmin_5.setObjectName(u"sw_lon_patch_xmin_5")
        self.gridLayout_14 = QGridLayout(self.sw_lon_patch_xmin_5)
        self.gridLayout_14.setObjectName(u"gridLayout_14")
        self.label_47 = QLabel(self.sw_lon_patch_xmin_5)
        self.label_47.setObjectName(u"label_47")
        self.label_47.setAlignment(Qt.AlignCenter)

        self.gridLayout_14.addWidget(self.label_47, 0, 1, 1, 1)

        self.label_49 = QLabel(self.sw_lon_patch_xmin_5)
        self.label_49.setObjectName(u"label_49")
        self.label_49.setAlignment(Qt.AlignCenter)

        self.gridLayout_14.addWidget(self.label_49, 0, 2, 1, 1)

        self.label_48 = QLabel(self.sw_lon_patch_xmin_5)
        self.label_48.setObjectName(u"label_48")

        self.gridLayout_14.addWidget(self.label_48, 1, 0, 1, 1)

        self.lineEdit_29 = QLineEdit(self.sw_lon_patch_xmin_5)
        self.lineEdit_29.setObjectName(u"lineEdit_29")

        self.gridLayout_14.addWidget(self.lineEdit_29, 1, 1, 1, 1)

        self.le_lon_segment_xmax_10 = QLineEdit(self.sw_lon_patch_xmin_5)
        self.le_lon_segment_xmax_10.setObjectName(u"le_lon_segment_xmax_10")

        self.gridLayout_14.addWidget(self.le_lon_segment_xmax_10, 1, 2, 1, 1)

        self.label_46 = QLabel(self.sw_lon_patch_xmin_5)
        self.label_46.setObjectName(u"label_46")

        self.gridLayout_14.addWidget(self.label_46, 2, 0, 1, 1)

        self.lineEdit_30 = QLineEdit(self.sw_lon_patch_xmin_5)
        self.lineEdit_30.setObjectName(u"lineEdit_30")

        self.gridLayout_14.addWidget(self.lineEdit_30, 2, 1, 1, 1)

        self.lineEdit_28 = QLineEdit(self.sw_lon_patch_xmin_5)
        self.lineEdit_28.setObjectName(u"lineEdit_28")

        self.gridLayout_14.addWidget(self.lineEdit_28, 2, 2, 1, 1)

        self.sw_lon_patch.addWidget(self.sw_lon_patch_xmin_5)
        self.sw_lon_patch_ymax_1 = QWidget()
        self.sw_lon_patch_ymax_1.setObjectName(u"sw_lon_patch_ymax_1")
        self.gridLayout_15 = QGridLayout(self.sw_lon_patch_ymax_1)
        self.gridLayout_15.setObjectName(u"gridLayout_15")
        self.label_51 = QLabel(self.sw_lon_patch_ymax_1)
        self.label_51.setObjectName(u"label_51")
        self.label_51.setAlignment(Qt.AlignCenter)

        self.gridLayout_15.addWidget(self.label_51, 0, 1, 1, 1)

        self.label_53 = QLabel(self.sw_lon_patch_ymax_1)
        self.label_53.setObjectName(u"label_53")
        self.label_53.setAlignment(Qt.AlignCenter)

        self.gridLayout_15.addWidget(self.label_53, 0, 2, 1, 1)

        self.label_52 = QLabel(self.sw_lon_patch_ymax_1)
        self.label_52.setObjectName(u"label_52")

        self.gridLayout_15.addWidget(self.label_52, 1, 0, 1, 1)

        self.le_ymax_bb_xstart = QLineEdit(self.sw_lon_patch_ymax_1)
        self.le_ymax_bb_xstart.setObjectName(u"le_ymax_bb_xstart")

        self.gridLayout_15.addWidget(self.le_ymax_bb_xstart, 1, 1, 1, 1)

        self.le_ymax_bb_zstart = QLineEdit(self.sw_lon_patch_ymax_1)
        self.le_ymax_bb_zstart.setObjectName(u"le_ymax_bb_zstart")

        self.gridLayout_15.addWidget(self.le_ymax_bb_zstart, 1, 2, 1, 1)

        self.label_50 = QLabel(self.sw_lon_patch_ymax_1)
        self.label_50.setObjectName(u"label_50")

        self.gridLayout_15.addWidget(self.label_50, 2, 0, 1, 1)

        self.le_ymax_bb_xlon = QLineEdit(self.sw_lon_patch_ymax_1)
        self.le_ymax_bb_xlon.setObjectName(u"le_ymax_bb_xlon")

        self.gridLayout_15.addWidget(self.le_ymax_bb_xlon, 2, 1, 1, 1)

        self.le_ymax_bb_zlon = QLineEdit(self.sw_lon_patch_ymax_1)
        self.le_ymax_bb_zlon.setObjectName(u"le_ymax_bb_zlon")

        self.gridLayout_15.addWidget(self.le_ymax_bb_zlon, 2, 2, 1, 1)

        self.sw_lon_patch.addWidget(self.sw_lon_patch_ymax_1)
        self.sw_lon_patch_ymax_2 = QWidget()
        self.sw_lon_patch_ymax_2.setObjectName(u"sw_lon_patch_ymax_2")
        self.gridLayout_16 = QGridLayout(self.sw_lon_patch_ymax_2)
        self.gridLayout_16.setObjectName(u"gridLayout_16")
        self.label_54 = QLabel(self.sw_lon_patch_ymax_2)
        self.label_54.setObjectName(u"label_54")
        self.label_54.setAlignment(Qt.AlignCenter)

        self.gridLayout_16.addWidget(self.label_54, 0, 1, 1, 1)

        self.label_55 = QLabel(self.sw_lon_patch_ymax_2)
        self.label_55.setObjectName(u"label_55")
        self.label_55.setAlignment(Qt.AlignCenter)

        self.gridLayout_16.addWidget(self.label_55, 0, 2, 1, 1)

        self.label_56 = QLabel(self.sw_lon_patch_ymax_2)
        self.label_56.setObjectName(u"label_56")

        self.gridLayout_16.addWidget(self.label_56, 1, 0, 1, 1)

        self.lineEdit_34 = QLineEdit(self.sw_lon_patch_ymax_2)
        self.lineEdit_34.setObjectName(u"lineEdit_34")

        self.gridLayout_16.addWidget(self.lineEdit_34, 1, 1, 1, 1)

        self.le_lon_segment_xmax_12 = QLineEdit(self.sw_lon_patch_ymax_2)
        self.le_lon_segment_xmax_12.setObjectName(u"le_lon_segment_xmax_12")

        self.gridLayout_16.addWidget(self.le_lon_segment_xmax_12, 1, 2, 1, 1)

        self.label_57 = QLabel(self.sw_lon_patch_ymax_2)
        self.label_57.setObjectName(u"label_57")

        self.gridLayout_16.addWidget(self.label_57, 2, 0, 1, 1)

        self.lineEdit_36 = QLineEdit(self.sw_lon_patch_ymax_2)
        self.lineEdit_36.setObjectName(u"lineEdit_36")

        self.gridLayout_16.addWidget(self.lineEdit_36, 2, 1, 1, 1)

        self.lineEdit_35 = QLineEdit(self.sw_lon_patch_ymax_2)
        self.lineEdit_35.setObjectName(u"lineEdit_35")

        self.gridLayout_16.addWidget(self.lineEdit_35, 2, 2, 1, 1)

        self.sw_lon_patch.addWidget(self.sw_lon_patch_ymax_2)
        self.sw_lon_patch_ymax_3 = QWidget()
        self.sw_lon_patch_ymax_3.setObjectName(u"sw_lon_patch_ymax_3")
        self.gridLayout_17 = QGridLayout(self.sw_lon_patch_ymax_3)
        self.gridLayout_17.setObjectName(u"gridLayout_17")
        self.label_58 = QLabel(self.sw_lon_patch_ymax_3)
        self.label_58.setObjectName(u"label_58")
        self.label_58.setAlignment(Qt.AlignCenter)

        self.gridLayout_17.addWidget(self.label_58, 0, 1, 1, 1)

        self.label_59 = QLabel(self.sw_lon_patch_ymax_3)
        self.label_59.setObjectName(u"label_59")
        self.label_59.setAlignment(Qt.AlignCenter)

        self.gridLayout_17.addWidget(self.label_59, 0, 2, 1, 1)

        self.label_60 = QLabel(self.sw_lon_patch_ymax_3)
        self.label_60.setObjectName(u"label_60")

        self.gridLayout_17.addWidget(self.label_60, 1, 0, 1, 1)

        self.lineEdit_37 = QLineEdit(self.sw_lon_patch_ymax_3)
        self.lineEdit_37.setObjectName(u"lineEdit_37")

        self.gridLayout_17.addWidget(self.lineEdit_37, 1, 1, 1, 1)

        self.le_lon_segment_xmax_13 = QLineEdit(self.sw_lon_patch_ymax_3)
        self.le_lon_segment_xmax_13.setObjectName(u"le_lon_segment_xmax_13")

        self.gridLayout_17.addWidget(self.le_lon_segment_xmax_13, 1, 2, 1, 1)

        self.label_61 = QLabel(self.sw_lon_patch_ymax_3)
        self.label_61.setObjectName(u"label_61")

        self.gridLayout_17.addWidget(self.label_61, 2, 0, 1, 1)

        self.lineEdit_39 = QLineEdit(self.sw_lon_patch_ymax_3)
        self.lineEdit_39.setObjectName(u"lineEdit_39")

        self.gridLayout_17.addWidget(self.lineEdit_39, 2, 1, 1, 1)

        self.lineEdit_38 = QLineEdit(self.sw_lon_patch_ymax_3)
        self.lineEdit_38.setObjectName(u"lineEdit_38")

        self.gridLayout_17.addWidget(self.lineEdit_38, 2, 2, 1, 1)

        self.sw_lon_patch.addWidget(self.sw_lon_patch_ymax_3)
        self.sw_lon_patch_ymax_4 = QWidget()
        self.sw_lon_patch_ymax_4.setObjectName(u"sw_lon_patch_ymax_4")
        self.gridLayout_18 = QGridLayout(self.sw_lon_patch_ymax_4)
        self.gridLayout_18.setObjectName(u"gridLayout_18")
        self.label_62 = QLabel(self.sw_lon_patch_ymax_4)
        self.label_62.setObjectName(u"label_62")
        self.label_62.setAlignment(Qt.AlignCenter)

        self.gridLayout_18.addWidget(self.label_62, 0, 1, 1, 1)

        self.label_63 = QLabel(self.sw_lon_patch_ymax_4)
        self.label_63.setObjectName(u"label_63")
        self.label_63.setAlignment(Qt.AlignCenter)

        self.gridLayout_18.addWidget(self.label_63, 0, 2, 1, 1)

        self.label_64 = QLabel(self.sw_lon_patch_ymax_4)
        self.label_64.setObjectName(u"label_64")

        self.gridLayout_18.addWidget(self.label_64, 1, 0, 1, 1)

        self.lineEdit_40 = QLineEdit(self.sw_lon_patch_ymax_4)
        self.lineEdit_40.setObjectName(u"lineEdit_40")

        self.gridLayout_18.addWidget(self.lineEdit_40, 1, 1, 1, 1)

        self.le_lon_segment_xmax_14 = QLineEdit(self.sw_lon_patch_ymax_4)
        self.le_lon_segment_xmax_14.setObjectName(u"le_lon_segment_xmax_14")

        self.gridLayout_18.addWidget(self.le_lon_segment_xmax_14, 1, 2, 1, 1)

        self.label_65 = QLabel(self.sw_lon_patch_ymax_4)
        self.label_65.setObjectName(u"label_65")

        self.gridLayout_18.addWidget(self.label_65, 2, 0, 1, 1)

        self.lineEdit_42 = QLineEdit(self.sw_lon_patch_ymax_4)
        self.lineEdit_42.setObjectName(u"lineEdit_42")

        self.gridLayout_18.addWidget(self.lineEdit_42, 2, 1, 1, 1)

        self.lineEdit_41 = QLineEdit(self.sw_lon_patch_ymax_4)
        self.lineEdit_41.setObjectName(u"lineEdit_41")

        self.gridLayout_18.addWidget(self.lineEdit_41, 2, 2, 1, 1)

        self.sw_lon_patch.addWidget(self.sw_lon_patch_ymax_4)
        self.sw_lon_patch_ymax_5 = QWidget()
        self.sw_lon_patch_ymax_5.setObjectName(u"sw_lon_patch_ymax_5")
        self.gridLayout_19 = QGridLayout(self.sw_lon_patch_ymax_5)
        self.gridLayout_19.setObjectName(u"gridLayout_19")
        self.label_66 = QLabel(self.sw_lon_patch_ymax_5)
        self.label_66.setObjectName(u"label_66")
        self.label_66.setAlignment(Qt.AlignCenter)

        self.gridLayout_19.addWidget(self.label_66, 0, 1, 1, 1)

        self.label_67 = QLabel(self.sw_lon_patch_ymax_5)
        self.label_67.setObjectName(u"label_67")
        self.label_67.setAlignment(Qt.AlignCenter)

        self.gridLayout_19.addWidget(self.label_67, 0, 2, 1, 1)

        self.label_68 = QLabel(self.sw_lon_patch_ymax_5)
        self.label_68.setObjectName(u"label_68")

        self.gridLayout_19.addWidget(self.label_68, 1, 0, 1, 1)

        self.lineEdit_43 = QLineEdit(self.sw_lon_patch_ymax_5)
        self.lineEdit_43.setObjectName(u"lineEdit_43")

        self.gridLayout_19.addWidget(self.lineEdit_43, 1, 1, 1, 1)

        self.le_lon_segment_xmax_15 = QLineEdit(self.sw_lon_patch_ymax_5)
        self.le_lon_segment_xmax_15.setObjectName(u"le_lon_segment_xmax_15")

        self.gridLayout_19.addWidget(self.le_lon_segment_xmax_15, 1, 2, 1, 1)

        self.label_69 = QLabel(self.sw_lon_patch_ymax_5)
        self.label_69.setObjectName(u"label_69")

        self.gridLayout_19.addWidget(self.label_69, 2, 0, 1, 1)

        self.lineEdit_45 = QLineEdit(self.sw_lon_patch_ymax_5)
        self.lineEdit_45.setObjectName(u"lineEdit_45")

        self.gridLayout_19.addWidget(self.lineEdit_45, 2, 1, 1, 1)

        self.lineEdit_44 = QLineEdit(self.sw_lon_patch_ymax_5)
        self.lineEdit_44.setObjectName(u"lineEdit_44")

        self.gridLayout_19.addWidget(self.lineEdit_44, 2, 2, 1, 1)

        self.sw_lon_patch.addWidget(self.sw_lon_patch_ymax_5)
        self.sw_lon_patch_ymin_1 = QWidget()
        self.sw_lon_patch_ymin_1.setObjectName(u"sw_lon_patch_ymin_1")
        self.gridLayout_20 = QGridLayout(self.sw_lon_patch_ymin_1)
        self.gridLayout_20.setObjectName(u"gridLayout_20")
        self.label_70 = QLabel(self.sw_lon_patch_ymin_1)
        self.label_70.setObjectName(u"label_70")
        self.label_70.setAlignment(Qt.AlignCenter)

        self.gridLayout_20.addWidget(self.label_70, 0, 1, 1, 1)

        self.label_71 = QLabel(self.sw_lon_patch_ymin_1)
        self.label_71.setObjectName(u"label_71")
        self.label_71.setAlignment(Qt.AlignCenter)

        self.gridLayout_20.addWidget(self.label_71, 0, 2, 1, 1)

        self.label_72 = QLabel(self.sw_lon_patch_ymin_1)
        self.label_72.setObjectName(u"label_72")

        self.gridLayout_20.addWidget(self.label_72, 1, 0, 1, 1)

        self.le_ymin_bb_xstart = QLineEdit(self.sw_lon_patch_ymin_1)
        self.le_ymin_bb_xstart.setObjectName(u"le_ymin_bb_xstart")

        self.gridLayout_20.addWidget(self.le_ymin_bb_xstart, 1, 1, 1, 1)

        self.le_ymin_bb_zstart = QLineEdit(self.sw_lon_patch_ymin_1)
        self.le_ymin_bb_zstart.setObjectName(u"le_ymin_bb_zstart")

        self.gridLayout_20.addWidget(self.le_ymin_bb_zstart, 1, 2, 1, 1)

        self.label_73 = QLabel(self.sw_lon_patch_ymin_1)
        self.label_73.setObjectName(u"label_73")

        self.gridLayout_20.addWidget(self.label_73, 2, 0, 1, 1)

        self.le_ymin_bb_xlon = QLineEdit(self.sw_lon_patch_ymin_1)
        self.le_ymin_bb_xlon.setObjectName(u"le_ymin_bb_xlon")

        self.gridLayout_20.addWidget(self.le_ymin_bb_xlon, 2, 1, 1, 1)

        self.le_ymin_bb_zlon = QLineEdit(self.sw_lon_patch_ymin_1)
        self.le_ymin_bb_zlon.setObjectName(u"le_ymin_bb_zlon")

        self.gridLayout_20.addWidget(self.le_ymin_bb_zlon, 2, 2, 1, 1)

        self.sw_lon_patch.addWidget(self.sw_lon_patch_ymin_1)
        self.sw_lon_patch_ymin_2 = QWidget()
        self.sw_lon_patch_ymin_2.setObjectName(u"sw_lon_patch_ymin_2")
        self.gridLayout_21 = QGridLayout(self.sw_lon_patch_ymin_2)
        self.gridLayout_21.setObjectName(u"gridLayout_21")
        self.label_74 = QLabel(self.sw_lon_patch_ymin_2)
        self.label_74.setObjectName(u"label_74")
        self.label_74.setAlignment(Qt.AlignCenter)

        self.gridLayout_21.addWidget(self.label_74, 0, 1, 1, 1)

        self.label_75 = QLabel(self.sw_lon_patch_ymin_2)
        self.label_75.setObjectName(u"label_75")
        self.label_75.setAlignment(Qt.AlignCenter)

        self.gridLayout_21.addWidget(self.label_75, 0, 2, 1, 1)

        self.label_76 = QLabel(self.sw_lon_patch_ymin_2)
        self.label_76.setObjectName(u"label_76")

        self.gridLayout_21.addWidget(self.label_76, 1, 0, 1, 1)

        self.lineEdit_49 = QLineEdit(self.sw_lon_patch_ymin_2)
        self.lineEdit_49.setObjectName(u"lineEdit_49")

        self.gridLayout_21.addWidget(self.lineEdit_49, 1, 1, 1, 1)

        self.le_lon_segment_xmax_17 = QLineEdit(self.sw_lon_patch_ymin_2)
        self.le_lon_segment_xmax_17.setObjectName(u"le_lon_segment_xmax_17")

        self.gridLayout_21.addWidget(self.le_lon_segment_xmax_17, 1, 2, 1, 1)

        self.label_77 = QLabel(self.sw_lon_patch_ymin_2)
        self.label_77.setObjectName(u"label_77")

        self.gridLayout_21.addWidget(self.label_77, 2, 0, 1, 1)

        self.lineEdit_51 = QLineEdit(self.sw_lon_patch_ymin_2)
        self.lineEdit_51.setObjectName(u"lineEdit_51")

        self.gridLayout_21.addWidget(self.lineEdit_51, 2, 1, 1, 1)

        self.lineEdit_50 = QLineEdit(self.sw_lon_patch_ymin_2)
        self.lineEdit_50.setObjectName(u"lineEdit_50")

        self.gridLayout_21.addWidget(self.lineEdit_50, 2, 2, 1, 1)

        self.sw_lon_patch.addWidget(self.sw_lon_patch_ymin_2)
        self.sw_lon_patch_ymin_3 = QWidget()
        self.sw_lon_patch_ymin_3.setObjectName(u"sw_lon_patch_ymin_3")
        self.gridLayout_22 = QGridLayout(self.sw_lon_patch_ymin_3)
        self.gridLayout_22.setObjectName(u"gridLayout_22")
        self.label_78 = QLabel(self.sw_lon_patch_ymin_3)
        self.label_78.setObjectName(u"label_78")
        self.label_78.setAlignment(Qt.AlignCenter)

        self.gridLayout_22.addWidget(self.label_78, 0, 1, 1, 1)

        self.label_79 = QLabel(self.sw_lon_patch_ymin_3)
        self.label_79.setObjectName(u"label_79")
        self.label_79.setAlignment(Qt.AlignCenter)

        self.gridLayout_22.addWidget(self.label_79, 0, 2, 1, 1)

        self.label_80 = QLabel(self.sw_lon_patch_ymin_3)
        self.label_80.setObjectName(u"label_80")

        self.gridLayout_22.addWidget(self.label_80, 1, 0, 1, 1)

        self.lineEdit_52 = QLineEdit(self.sw_lon_patch_ymin_3)
        self.lineEdit_52.setObjectName(u"lineEdit_52")

        self.gridLayout_22.addWidget(self.lineEdit_52, 1, 1, 1, 1)

        self.le_lon_segment_xmax_18 = QLineEdit(self.sw_lon_patch_ymin_3)
        self.le_lon_segment_xmax_18.setObjectName(u"le_lon_segment_xmax_18")

        self.gridLayout_22.addWidget(self.le_lon_segment_xmax_18, 1, 2, 1, 1)

        self.label_81 = QLabel(self.sw_lon_patch_ymin_3)
        self.label_81.setObjectName(u"label_81")

        self.gridLayout_22.addWidget(self.label_81, 2, 0, 1, 1)

        self.lineEdit_54 = QLineEdit(self.sw_lon_patch_ymin_3)
        self.lineEdit_54.setObjectName(u"lineEdit_54")

        self.gridLayout_22.addWidget(self.lineEdit_54, 2, 1, 1, 1)

        self.lineEdit_53 = QLineEdit(self.sw_lon_patch_ymin_3)
        self.lineEdit_53.setObjectName(u"lineEdit_53")

        self.gridLayout_22.addWidget(self.lineEdit_53, 2, 2, 1, 1)

        self.sw_lon_patch.addWidget(self.sw_lon_patch_ymin_3)
        self.sw_lon_patch_ymin_4 = QWidget()
        self.sw_lon_patch_ymin_4.setObjectName(u"sw_lon_patch_ymin_4")
        self.gridLayout_23 = QGridLayout(self.sw_lon_patch_ymin_4)
        self.gridLayout_23.setObjectName(u"gridLayout_23")
        self.label_82 = QLabel(self.sw_lon_patch_ymin_4)
        self.label_82.setObjectName(u"label_82")
        self.label_82.setAlignment(Qt.AlignCenter)

        self.gridLayout_23.addWidget(self.label_82, 0, 1, 1, 1)

        self.label_83 = QLabel(self.sw_lon_patch_ymin_4)
        self.label_83.setObjectName(u"label_83")
        self.label_83.setAlignment(Qt.AlignCenter)

        self.gridLayout_23.addWidget(self.label_83, 0, 2, 1, 1)

        self.label_84 = QLabel(self.sw_lon_patch_ymin_4)
        self.label_84.setObjectName(u"label_84")

        self.gridLayout_23.addWidget(self.label_84, 1, 0, 1, 1)

        self.lineEdit_55 = QLineEdit(self.sw_lon_patch_ymin_4)
        self.lineEdit_55.setObjectName(u"lineEdit_55")

        self.gridLayout_23.addWidget(self.lineEdit_55, 1, 1, 1, 1)

        self.le_lon_segment_xmax_19 = QLineEdit(self.sw_lon_patch_ymin_4)
        self.le_lon_segment_xmax_19.setObjectName(u"le_lon_segment_xmax_19")

        self.gridLayout_23.addWidget(self.le_lon_segment_xmax_19, 1, 2, 1, 1)

        self.label_85 = QLabel(self.sw_lon_patch_ymin_4)
        self.label_85.setObjectName(u"label_85")

        self.gridLayout_23.addWidget(self.label_85, 2, 0, 1, 1)

        self.lineEdit_57 = QLineEdit(self.sw_lon_patch_ymin_4)
        self.lineEdit_57.setObjectName(u"lineEdit_57")

        self.gridLayout_23.addWidget(self.lineEdit_57, 2, 1, 1, 1)

        self.lineEdit_56 = QLineEdit(self.sw_lon_patch_ymin_4)
        self.lineEdit_56.setObjectName(u"lineEdit_56")

        self.gridLayout_23.addWidget(self.lineEdit_56, 2, 2, 1, 1)

        self.sw_lon_patch.addWidget(self.sw_lon_patch_ymin_4)
        self.sw_lon_patch_ymin_5 = QWidget()
        self.sw_lon_patch_ymin_5.setObjectName(u"sw_lon_patch_ymin_5")
        self.gridLayout_24 = QGridLayout(self.sw_lon_patch_ymin_5)
        self.gridLayout_24.setObjectName(u"gridLayout_24")
        self.label_86 = QLabel(self.sw_lon_patch_ymin_5)
        self.label_86.setObjectName(u"label_86")
        self.label_86.setAlignment(Qt.AlignCenter)

        self.gridLayout_24.addWidget(self.label_86, 0, 1, 1, 1)

        self.label_87 = QLabel(self.sw_lon_patch_ymin_5)
        self.label_87.setObjectName(u"label_87")
        self.label_87.setAlignment(Qt.AlignCenter)

        self.gridLayout_24.addWidget(self.label_87, 0, 2, 1, 1)

        self.label_88 = QLabel(self.sw_lon_patch_ymin_5)
        self.label_88.setObjectName(u"label_88")

        self.gridLayout_24.addWidget(self.label_88, 1, 0, 1, 1)

        self.lineEdit_58 = QLineEdit(self.sw_lon_patch_ymin_5)
        self.lineEdit_58.setObjectName(u"lineEdit_58")

        self.gridLayout_24.addWidget(self.lineEdit_58, 1, 1, 1, 1)

        self.le_lon_segment_xmax_20 = QLineEdit(self.sw_lon_patch_ymin_5)
        self.le_lon_segment_xmax_20.setObjectName(u"le_lon_segment_xmax_20")

        self.gridLayout_24.addWidget(self.le_lon_segment_xmax_20, 1, 2, 1, 1)

        self.label_89 = QLabel(self.sw_lon_patch_ymin_5)
        self.label_89.setObjectName(u"label_89")

        self.gridLayout_24.addWidget(self.label_89, 2, 0, 1, 1)

        self.lineEdit_60 = QLineEdit(self.sw_lon_patch_ymin_5)
        self.lineEdit_60.setObjectName(u"lineEdit_60")

        self.gridLayout_24.addWidget(self.lineEdit_60, 2, 1, 1, 1)

        self.lineEdit_59 = QLineEdit(self.sw_lon_patch_ymin_5)
        self.lineEdit_59.setObjectName(u"lineEdit_59")

        self.gridLayout_24.addWidget(self.lineEdit_59, 2, 2, 1, 1)

        self.sw_lon_patch.addWidget(self.sw_lon_patch_ymin_5)
        self.sw_lon_patch_zmax_1 = QWidget()
        self.sw_lon_patch_zmax_1.setObjectName(u"sw_lon_patch_zmax_1")
        self.gridLayout_25 = QGridLayout(self.sw_lon_patch_zmax_1)
        self.gridLayout_25.setObjectName(u"gridLayout_25")
        self.label_90 = QLabel(self.sw_lon_patch_zmax_1)
        self.label_90.setObjectName(u"label_90")
        self.label_90.setAlignment(Qt.AlignCenter)

        self.gridLayout_25.addWidget(self.label_90, 0, 1, 1, 1)

        self.label_91 = QLabel(self.sw_lon_patch_zmax_1)
        self.label_91.setObjectName(u"label_91")
        self.label_91.setAlignment(Qt.AlignCenter)

        self.gridLayout_25.addWidget(self.label_91, 0, 2, 1, 1)

        self.label_92 = QLabel(self.sw_lon_patch_zmax_1)
        self.label_92.setObjectName(u"label_92")

        self.gridLayout_25.addWidget(self.label_92, 1, 0, 1, 1)

        self.le_zmax_bb_xstart = QLineEdit(self.sw_lon_patch_zmax_1)
        self.le_zmax_bb_xstart.setObjectName(u"le_zmax_bb_xstart")

        self.gridLayout_25.addWidget(self.le_zmax_bb_xstart, 1, 1, 1, 1)

        self.le_zmax_bb_ystart = QLineEdit(self.sw_lon_patch_zmax_1)
        self.le_zmax_bb_ystart.setObjectName(u"le_zmax_bb_ystart")

        self.gridLayout_25.addWidget(self.le_zmax_bb_ystart, 1, 2, 1, 1)

        self.label_93 = QLabel(self.sw_lon_patch_zmax_1)
        self.label_93.setObjectName(u"label_93")

        self.gridLayout_25.addWidget(self.label_93, 2, 0, 1, 1)

        self.le_zmax_bb_xlon = QLineEdit(self.sw_lon_patch_zmax_1)
        self.le_zmax_bb_xlon.setObjectName(u"le_zmax_bb_xlon")

        self.gridLayout_25.addWidget(self.le_zmax_bb_xlon, 2, 1, 1, 1)

        self.le_zmax_bb_ylon = QLineEdit(self.sw_lon_patch_zmax_1)
        self.le_zmax_bb_ylon.setObjectName(u"le_zmax_bb_ylon")

        self.gridLayout_25.addWidget(self.le_zmax_bb_ylon, 2, 2, 1, 1)

        self.sw_lon_patch.addWidget(self.sw_lon_patch_zmax_1)
        self.sw_lon_patch_zmax_2 = QWidget()
        self.sw_lon_patch_zmax_2.setObjectName(u"sw_lon_patch_zmax_2")
        self.gridLayout_26 = QGridLayout(self.sw_lon_patch_zmax_2)
        self.gridLayout_26.setObjectName(u"gridLayout_26")
        self.label_94 = QLabel(self.sw_lon_patch_zmax_2)
        self.label_94.setObjectName(u"label_94")
        self.label_94.setAlignment(Qt.AlignCenter)

        self.gridLayout_26.addWidget(self.label_94, 0, 1, 1, 1)

        self.label_95 = QLabel(self.sw_lon_patch_zmax_2)
        self.label_95.setObjectName(u"label_95")
        self.label_95.setAlignment(Qt.AlignCenter)

        self.gridLayout_26.addWidget(self.label_95, 0, 2, 1, 1)

        self.label_97 = QLabel(self.sw_lon_patch_zmax_2)
        self.label_97.setObjectName(u"label_97")

        self.gridLayout_26.addWidget(self.label_97, 1, 0, 1, 1)

        self.lineEdit_66 = QLineEdit(self.sw_lon_patch_zmax_2)
        self.lineEdit_66.setObjectName(u"lineEdit_66")

        self.gridLayout_26.addWidget(self.lineEdit_66, 1, 1, 1, 1)

        self.le_lon_segment_xmax_22 = QLineEdit(self.sw_lon_patch_zmax_2)
        self.le_lon_segment_xmax_22.setObjectName(u"le_lon_segment_xmax_22")

        self.gridLayout_26.addWidget(self.le_lon_segment_xmax_22, 1, 2, 1, 1)

        self.label_96 = QLabel(self.sw_lon_patch_zmax_2)
        self.label_96.setObjectName(u"label_96")

        self.gridLayout_26.addWidget(self.label_96, 2, 0, 1, 1)

        self.lineEdit_64 = QLineEdit(self.sw_lon_patch_zmax_2)
        self.lineEdit_64.setObjectName(u"lineEdit_64")

        self.gridLayout_26.addWidget(self.lineEdit_64, 2, 1, 1, 1)

        self.lineEdit_65 = QLineEdit(self.sw_lon_patch_zmax_2)
        self.lineEdit_65.setObjectName(u"lineEdit_65")

        self.gridLayout_26.addWidget(self.lineEdit_65, 2, 2, 1, 1)

        self.sw_lon_patch.addWidget(self.sw_lon_patch_zmax_2)
        self.sw_lon_patch_zmax_3 = QWidget()
        self.sw_lon_patch_zmax_3.setObjectName(u"sw_lon_patch_zmax_3")
        self.gridLayout_27 = QGridLayout(self.sw_lon_patch_zmax_3)
        self.gridLayout_27.setObjectName(u"gridLayout_27")
        self.label_98 = QLabel(self.sw_lon_patch_zmax_3)
        self.label_98.setObjectName(u"label_98")
        self.label_98.setAlignment(Qt.AlignCenter)

        self.gridLayout_27.addWidget(self.label_98, 0, 1, 1, 1)

        self.label_99 = QLabel(self.sw_lon_patch_zmax_3)
        self.label_99.setObjectName(u"label_99")
        self.label_99.setAlignment(Qt.AlignCenter)

        self.gridLayout_27.addWidget(self.label_99, 0, 2, 1, 1)

        self.label_101 = QLabel(self.sw_lon_patch_zmax_3)
        self.label_101.setObjectName(u"label_101")

        self.gridLayout_27.addWidget(self.label_101, 1, 0, 1, 1)

        self.lineEdit_69 = QLineEdit(self.sw_lon_patch_zmax_3)
        self.lineEdit_69.setObjectName(u"lineEdit_69")

        self.gridLayout_27.addWidget(self.lineEdit_69, 1, 1, 1, 1)

        self.le_lon_segment_xmax_23 = QLineEdit(self.sw_lon_patch_zmax_3)
        self.le_lon_segment_xmax_23.setObjectName(u"le_lon_segment_xmax_23")

        self.gridLayout_27.addWidget(self.le_lon_segment_xmax_23, 1, 2, 1, 1)

        self.label_100 = QLabel(self.sw_lon_patch_zmax_3)
        self.label_100.setObjectName(u"label_100")

        self.gridLayout_27.addWidget(self.label_100, 2, 0, 1, 1)

        self.lineEdit_67 = QLineEdit(self.sw_lon_patch_zmax_3)
        self.lineEdit_67.setObjectName(u"lineEdit_67")

        self.gridLayout_27.addWidget(self.lineEdit_67, 2, 1, 1, 1)

        self.lineEdit_68 = QLineEdit(self.sw_lon_patch_zmax_3)
        self.lineEdit_68.setObjectName(u"lineEdit_68")

        self.gridLayout_27.addWidget(self.lineEdit_68, 2, 2, 1, 1)

        self.sw_lon_patch.addWidget(self.sw_lon_patch_zmax_3)
        self.sw_lon_patch_zmax_4 = QWidget()
        self.sw_lon_patch_zmax_4.setObjectName(u"sw_lon_patch_zmax_4")
        self.gridLayout_28 = QGridLayout(self.sw_lon_patch_zmax_4)
        self.gridLayout_28.setObjectName(u"gridLayout_28")
        self.label_102 = QLabel(self.sw_lon_patch_zmax_4)
        self.label_102.setObjectName(u"label_102")
        self.label_102.setAlignment(Qt.AlignCenter)

        self.gridLayout_28.addWidget(self.label_102, 0, 1, 1, 1)

        self.label_103 = QLabel(self.sw_lon_patch_zmax_4)
        self.label_103.setObjectName(u"label_103")
        self.label_103.setAlignment(Qt.AlignCenter)

        self.gridLayout_28.addWidget(self.label_103, 0, 2, 1, 1)

        self.label_105 = QLabel(self.sw_lon_patch_zmax_4)
        self.label_105.setObjectName(u"label_105")

        self.gridLayout_28.addWidget(self.label_105, 1, 0, 1, 1)

        self.lineEdit_72 = QLineEdit(self.sw_lon_patch_zmax_4)
        self.lineEdit_72.setObjectName(u"lineEdit_72")

        self.gridLayout_28.addWidget(self.lineEdit_72, 1, 1, 1, 1)

        self.le_lon_segment_xmax_24 = QLineEdit(self.sw_lon_patch_zmax_4)
        self.le_lon_segment_xmax_24.setObjectName(u"le_lon_segment_xmax_24")

        self.gridLayout_28.addWidget(self.le_lon_segment_xmax_24, 1, 2, 1, 1)

        self.label_104 = QLabel(self.sw_lon_patch_zmax_4)
        self.label_104.setObjectName(u"label_104")

        self.gridLayout_28.addWidget(self.label_104, 2, 0, 1, 1)

        self.lineEdit_70 = QLineEdit(self.sw_lon_patch_zmax_4)
        self.lineEdit_70.setObjectName(u"lineEdit_70")

        self.gridLayout_28.addWidget(self.lineEdit_70, 2, 1, 1, 1)

        self.lineEdit_71 = QLineEdit(self.sw_lon_patch_zmax_4)
        self.lineEdit_71.setObjectName(u"lineEdit_71")

        self.gridLayout_28.addWidget(self.lineEdit_71, 2, 2, 1, 1)

        self.sw_lon_patch.addWidget(self.sw_lon_patch_zmax_4)
        self.sw_lon_patch_zmax_5 = QWidget()
        self.sw_lon_patch_zmax_5.setObjectName(u"sw_lon_patch_zmax_5")
        self.gridLayout_29 = QGridLayout(self.sw_lon_patch_zmax_5)
        self.gridLayout_29.setObjectName(u"gridLayout_29")
        self.label_106 = QLabel(self.sw_lon_patch_zmax_5)
        self.label_106.setObjectName(u"label_106")
        self.label_106.setAlignment(Qt.AlignCenter)

        self.gridLayout_29.addWidget(self.label_106, 0, 1, 1, 1)

        self.label_107 = QLabel(self.sw_lon_patch_zmax_5)
        self.label_107.setObjectName(u"label_107")
        self.label_107.setAlignment(Qt.AlignCenter)

        self.gridLayout_29.addWidget(self.label_107, 0, 2, 1, 1)

        self.label_109 = QLabel(self.sw_lon_patch_zmax_5)
        self.label_109.setObjectName(u"label_109")

        self.gridLayout_29.addWidget(self.label_109, 1, 0, 1, 1)

        self.lineEdit_75 = QLineEdit(self.sw_lon_patch_zmax_5)
        self.lineEdit_75.setObjectName(u"lineEdit_75")

        self.gridLayout_29.addWidget(self.lineEdit_75, 1, 1, 1, 1)

        self.le_lon_segment_xmax_25 = QLineEdit(self.sw_lon_patch_zmax_5)
        self.le_lon_segment_xmax_25.setObjectName(u"le_lon_segment_xmax_25")

        self.gridLayout_29.addWidget(self.le_lon_segment_xmax_25, 1, 2, 1, 1)

        self.label_108 = QLabel(self.sw_lon_patch_zmax_5)
        self.label_108.setObjectName(u"label_108")

        self.gridLayout_29.addWidget(self.label_108, 2, 0, 1, 1)

        self.lineEdit_73 = QLineEdit(self.sw_lon_patch_zmax_5)
        self.lineEdit_73.setObjectName(u"lineEdit_73")

        self.gridLayout_29.addWidget(self.lineEdit_73, 2, 1, 1, 1)

        self.lineEdit_74 = QLineEdit(self.sw_lon_patch_zmax_5)
        self.lineEdit_74.setObjectName(u"lineEdit_74")

        self.gridLayout_29.addWidget(self.lineEdit_74, 2, 2, 1, 1)

        self.sw_lon_patch.addWidget(self.sw_lon_patch_zmax_5)
        self.sw_lon_patch_zmin_1 = QWidget()
        self.sw_lon_patch_zmin_1.setObjectName(u"sw_lon_patch_zmin_1")
        self.gridLayout_30 = QGridLayout(self.sw_lon_patch_zmin_1)
        self.gridLayout_30.setObjectName(u"gridLayout_30")
        self.label_110 = QLabel(self.sw_lon_patch_zmin_1)
        self.label_110.setObjectName(u"label_110")
        self.label_110.setAlignment(Qt.AlignCenter)

        self.gridLayout_30.addWidget(self.label_110, 0, 1, 1, 1)

        self.label_111 = QLabel(self.sw_lon_patch_zmin_1)
        self.label_111.setObjectName(u"label_111")
        self.label_111.setAlignment(Qt.AlignCenter)

        self.gridLayout_30.addWidget(self.label_111, 0, 2, 1, 1)

        self.label_113 = QLabel(self.sw_lon_patch_zmin_1)
        self.label_113.setObjectName(u"label_113")

        self.gridLayout_30.addWidget(self.label_113, 1, 0, 1, 1)

        self.le_zmin_bb_xstart = QLineEdit(self.sw_lon_patch_zmin_1)
        self.le_zmin_bb_xstart.setObjectName(u"le_zmin_bb_xstart")

        self.gridLayout_30.addWidget(self.le_zmin_bb_xstart, 1, 1, 1, 1)

        self.le_zmin_bb_ystart = QLineEdit(self.sw_lon_patch_zmin_1)
        self.le_zmin_bb_ystart.setObjectName(u"le_zmin_bb_ystart")

        self.gridLayout_30.addWidget(self.le_zmin_bb_ystart, 1, 2, 1, 1)

        self.label_112 = QLabel(self.sw_lon_patch_zmin_1)
        self.label_112.setObjectName(u"label_112")

        self.gridLayout_30.addWidget(self.label_112, 2, 0, 1, 1)

        self.le_zmin_bb_xlon = QLineEdit(self.sw_lon_patch_zmin_1)
        self.le_zmin_bb_xlon.setObjectName(u"le_zmin_bb_xlon")

        self.gridLayout_30.addWidget(self.le_zmin_bb_xlon, 2, 1, 1, 1)

        self.le_zmin_bb_ylon = QLineEdit(self.sw_lon_patch_zmin_1)
        self.le_zmin_bb_ylon.setObjectName(u"le_zmin_bb_ylon")

        self.gridLayout_30.addWidget(self.le_zmin_bb_ylon, 2, 2, 1, 1)

        self.sw_lon_patch.addWidget(self.sw_lon_patch_zmin_1)
        self.sw_lon_patch_zmin_2 = QWidget()
        self.sw_lon_patch_zmin_2.setObjectName(u"sw_lon_patch_zmin_2")
        self.gridLayout_31 = QGridLayout(self.sw_lon_patch_zmin_2)
        self.gridLayout_31.setObjectName(u"gridLayout_31")
        self.label_114 = QLabel(self.sw_lon_patch_zmin_2)
        self.label_114.setObjectName(u"label_114")
        self.label_114.setAlignment(Qt.AlignCenter)

        self.gridLayout_31.addWidget(self.label_114, 0, 1, 1, 1)

        self.label_115 = QLabel(self.sw_lon_patch_zmin_2)
        self.label_115.setObjectName(u"label_115")
        self.label_115.setAlignment(Qt.AlignCenter)

        self.gridLayout_31.addWidget(self.label_115, 0, 2, 1, 1)

        self.label_117 = QLabel(self.sw_lon_patch_zmin_2)
        self.label_117.setObjectName(u"label_117")

        self.gridLayout_31.addWidget(self.label_117, 1, 0, 1, 1)

        self.lineEdit_81 = QLineEdit(self.sw_lon_patch_zmin_2)
        self.lineEdit_81.setObjectName(u"lineEdit_81")

        self.gridLayout_31.addWidget(self.lineEdit_81, 1, 1, 1, 1)

        self.le_lon_segment_xmax_27 = QLineEdit(self.sw_lon_patch_zmin_2)
        self.le_lon_segment_xmax_27.setObjectName(u"le_lon_segment_xmax_27")

        self.gridLayout_31.addWidget(self.le_lon_segment_xmax_27, 1, 2, 1, 1)

        self.label_116 = QLabel(self.sw_lon_patch_zmin_2)
        self.label_116.setObjectName(u"label_116")

        self.gridLayout_31.addWidget(self.label_116, 2, 0, 1, 1)

        self.lineEdit_79 = QLineEdit(self.sw_lon_patch_zmin_2)
        self.lineEdit_79.setObjectName(u"lineEdit_79")

        self.gridLayout_31.addWidget(self.lineEdit_79, 2, 1, 1, 1)

        self.lineEdit_80 = QLineEdit(self.sw_lon_patch_zmin_2)
        self.lineEdit_80.setObjectName(u"lineEdit_80")

        self.gridLayout_31.addWidget(self.lineEdit_80, 2, 2, 1, 1)

        self.sw_lon_patch.addWidget(self.sw_lon_patch_zmin_2)
        self.sw_lon_patch_zmin_3 = QWidget()
        self.sw_lon_patch_zmin_3.setObjectName(u"sw_lon_patch_zmin_3")
        self.gridLayout_32 = QGridLayout(self.sw_lon_patch_zmin_3)
        self.gridLayout_32.setObjectName(u"gridLayout_32")
        self.label_118 = QLabel(self.sw_lon_patch_zmin_3)
        self.label_118.setObjectName(u"label_118")
        self.label_118.setAlignment(Qt.AlignCenter)

        self.gridLayout_32.addWidget(self.label_118, 0, 1, 1, 1)

        self.label_119 = QLabel(self.sw_lon_patch_zmin_3)
        self.label_119.setObjectName(u"label_119")
        self.label_119.setAlignment(Qt.AlignCenter)

        self.gridLayout_32.addWidget(self.label_119, 0, 2, 1, 1)

        self.label_121 = QLabel(self.sw_lon_patch_zmin_3)
        self.label_121.setObjectName(u"label_121")

        self.gridLayout_32.addWidget(self.label_121, 1, 0, 1, 1)

        self.lineEdit_84 = QLineEdit(self.sw_lon_patch_zmin_3)
        self.lineEdit_84.setObjectName(u"lineEdit_84")

        self.gridLayout_32.addWidget(self.lineEdit_84, 1, 1, 1, 1)

        self.le_lon_segment_xmax_28 = QLineEdit(self.sw_lon_patch_zmin_3)
        self.le_lon_segment_xmax_28.setObjectName(u"le_lon_segment_xmax_28")

        self.gridLayout_32.addWidget(self.le_lon_segment_xmax_28, 1, 2, 1, 1)

        self.label_120 = QLabel(self.sw_lon_patch_zmin_3)
        self.label_120.setObjectName(u"label_120")

        self.gridLayout_32.addWidget(self.label_120, 2, 0, 1, 1)

        self.lineEdit_82 = QLineEdit(self.sw_lon_patch_zmin_3)
        self.lineEdit_82.setObjectName(u"lineEdit_82")

        self.gridLayout_32.addWidget(self.lineEdit_82, 2, 1, 1, 1)

        self.lineEdit_83 = QLineEdit(self.sw_lon_patch_zmin_3)
        self.lineEdit_83.setObjectName(u"lineEdit_83")

        self.gridLayout_32.addWidget(self.lineEdit_83, 2, 2, 1, 1)

        self.sw_lon_patch.addWidget(self.sw_lon_patch_zmin_3)
        self.sw_lon_patch_zmin_4 = QWidget()
        self.sw_lon_patch_zmin_4.setObjectName(u"sw_lon_patch_zmin_4")
        self.gridLayout_33 = QGridLayout(self.sw_lon_patch_zmin_4)
        self.gridLayout_33.setObjectName(u"gridLayout_33")
        self.label_122 = QLabel(self.sw_lon_patch_zmin_4)
        self.label_122.setObjectName(u"label_122")
        self.label_122.setAlignment(Qt.AlignCenter)

        self.gridLayout_33.addWidget(self.label_122, 0, 1, 1, 1)

        self.label_123 = QLabel(self.sw_lon_patch_zmin_4)
        self.label_123.setObjectName(u"label_123")
        self.label_123.setAlignment(Qt.AlignCenter)

        self.gridLayout_33.addWidget(self.label_123, 0, 2, 1, 1)

        self.label_125 = QLabel(self.sw_lon_patch_zmin_4)
        self.label_125.setObjectName(u"label_125")

        self.gridLayout_33.addWidget(self.label_125, 1, 0, 1, 1)

        self.lineEdit_87 = QLineEdit(self.sw_lon_patch_zmin_4)
        self.lineEdit_87.setObjectName(u"lineEdit_87")

        self.gridLayout_33.addWidget(self.lineEdit_87, 1, 1, 1, 1)

        self.le_lon_segment_xmax_29 = QLineEdit(self.sw_lon_patch_zmin_4)
        self.le_lon_segment_xmax_29.setObjectName(u"le_lon_segment_xmax_29")

        self.gridLayout_33.addWidget(self.le_lon_segment_xmax_29, 1, 2, 1, 1)

        self.label_124 = QLabel(self.sw_lon_patch_zmin_4)
        self.label_124.setObjectName(u"label_124")

        self.gridLayout_33.addWidget(self.label_124, 2, 0, 1, 1)

        self.lineEdit_85 = QLineEdit(self.sw_lon_patch_zmin_4)
        self.lineEdit_85.setObjectName(u"lineEdit_85")

        self.gridLayout_33.addWidget(self.lineEdit_85, 2, 1, 1, 1)

        self.lineEdit_86 = QLineEdit(self.sw_lon_patch_zmin_4)
        self.lineEdit_86.setObjectName(u"lineEdit_86")

        self.gridLayout_33.addWidget(self.lineEdit_86, 2, 2, 1, 1)

        self.sw_lon_patch.addWidget(self.sw_lon_patch_zmin_4)
        self.sw_lon_patch_zmin_5 = QWidget()
        self.sw_lon_patch_zmin_5.setObjectName(u"sw_lon_patch_zmin_5")
        self.gridLayout_34 = QGridLayout(self.sw_lon_patch_zmin_5)
        self.gridLayout_34.setObjectName(u"gridLayout_34")
        self.label_126 = QLabel(self.sw_lon_patch_zmin_5)
        self.label_126.setObjectName(u"label_126")
        self.label_126.setAlignment(Qt.AlignCenter)

        self.gridLayout_34.addWidget(self.label_126, 0, 1, 1, 1)

        self.label_127 = QLabel(self.sw_lon_patch_zmin_5)
        self.label_127.setObjectName(u"label_127")
        self.label_127.setAlignment(Qt.AlignCenter)

        self.gridLayout_34.addWidget(self.label_127, 0, 2, 1, 1)

        self.label_129 = QLabel(self.sw_lon_patch_zmin_5)
        self.label_129.setObjectName(u"label_129")

        self.gridLayout_34.addWidget(self.label_129, 1, 0, 1, 1)

        self.lineEdit_90 = QLineEdit(self.sw_lon_patch_zmin_5)
        self.lineEdit_90.setObjectName(u"lineEdit_90")

        self.gridLayout_34.addWidget(self.lineEdit_90, 1, 1, 1, 1)

        self.le_lon_segment_xmax_30 = QLineEdit(self.sw_lon_patch_zmin_5)
        self.le_lon_segment_xmax_30.setObjectName(u"le_lon_segment_xmax_30")

        self.gridLayout_34.addWidget(self.le_lon_segment_xmax_30, 1, 2, 1, 1)

        self.label_128 = QLabel(self.sw_lon_patch_zmin_5)
        self.label_128.setObjectName(u"label_128")

        self.gridLayout_34.addWidget(self.label_128, 2, 0, 1, 1)

        self.lineEdit_88 = QLineEdit(self.sw_lon_patch_zmin_5)
        self.lineEdit_88.setObjectName(u"lineEdit_88")

        self.gridLayout_34.addWidget(self.lineEdit_88, 2, 1, 1, 1)

        self.lineEdit_89 = QLineEdit(self.sw_lon_patch_zmin_5)
        self.lineEdit_89.setObjectName(u"lineEdit_89")

        self.gridLayout_34.addWidget(self.lineEdit_89, 2, 2, 1, 1)

        self.sw_lon_patch.addWidget(self.sw_lon_patch_zmin_5)

        self.horizontalLayout_35.addWidget(self.sw_lon_patch)


        self.gridLayout.addWidget(self.groupBox_2, 1, 0, 1, 4)


        self.gridLayout_3.addWidget(self.groupBox, 0, 0, 1, 1)


        self.retranslateUi(bordes_window)

        self.sw_patchlist.setCurrentIndex(0)
        self.sw_patch_addremove.setCurrentIndex(5)
        self.sw_lon_patch.setCurrentIndex(0)


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
        self.groupBox_5.setTitle(QCoreApplication.translate("bordes_window", u"Salida de la masa", None))
        self.label_6.setText(QCoreApplication.translate("bordes_window", u"Fracci\u00f3n", None))
        self.gb_tipo_segment.setTitle(QCoreApplication.translate("bordes_window", u"Tipo de segmento", None))
        self.chb_wall.setText(QCoreApplication.translate("bordes_window", u"Pared", None))
        self.chb_inmass.setText(QCoreApplication.translate("bordes_window", u"Entrada de la masa", None))
        self.chb_outmass.setText(QCoreApplication.translate("bordes_window", u"Salida de la masa", None))
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
        self.label_11.setText(QCoreApplication.translate("bordes_window", u"Z", None))
        self.label_10.setText(QCoreApplication.translate("bordes_window", u"Y", None))
        self.label_12.setText(QCoreApplication.translate("bordes_window", u"Empieza", None))
        self.label_13.setText(QCoreApplication.translate("bordes_window", u"Longitud", None))
        self.label_16.setText(QCoreApplication.translate("bordes_window", u"Y", None))
        self.label_17.setText(QCoreApplication.translate("bordes_window", u"Z", None))
        self.label_14.setText(QCoreApplication.translate("bordes_window", u"Empieza", None))
        self.label_15.setText(QCoreApplication.translate("bordes_window", u"Longitud", None))
        self.label_19.setText(QCoreApplication.translate("bordes_window", u"Y", None))
        self.label_21.setText(QCoreApplication.translate("bordes_window", u"Z", None))
        self.label_20.setText(QCoreApplication.translate("bordes_window", u"Empieza", None))
        self.label_18.setText(QCoreApplication.translate("bordes_window", u"Longitud", None))
        self.label_23.setText(QCoreApplication.translate("bordes_window", u"Y", None))
        self.label_25.setText(QCoreApplication.translate("bordes_window", u"Z", None))
        self.label_24.setText(QCoreApplication.translate("bordes_window", u"Empieza", None))
        self.label_22.setText(QCoreApplication.translate("bordes_window", u"Longitud", None))
        self.label_27.setText(QCoreApplication.translate("bordes_window", u"Y", None))
        self.label_29.setText(QCoreApplication.translate("bordes_window", u"Z", None))
        self.label_28.setText(QCoreApplication.translate("bordes_window", u"Empieza", None))
        self.label_26.setText(QCoreApplication.translate("bordes_window", u"Longitud", None))
        self.label_31.setText(QCoreApplication.translate("bordes_window", u"Y", None))
        self.label_33.setText(QCoreApplication.translate("bordes_window", u"Z", None))
        self.label_32.setText(QCoreApplication.translate("bordes_window", u"Empieza", None))
        self.label_30.setText(QCoreApplication.translate("bordes_window", u"Longitud", None))
        self.label_35.setText(QCoreApplication.translate("bordes_window", u"Y", None))
        self.label_37.setText(QCoreApplication.translate("bordes_window", u"Z", None))
        self.label_36.setText(QCoreApplication.translate("bordes_window", u"Empieza", None))
        self.label_34.setText(QCoreApplication.translate("bordes_window", u"Longitud", None))
        self.label_39.setText(QCoreApplication.translate("bordes_window", u"Y", None))
        self.label_41.setText(QCoreApplication.translate("bordes_window", u"Z", None))
        self.label_40.setText(QCoreApplication.translate("bordes_window", u"Empieza", None))
        self.label_38.setText(QCoreApplication.translate("bordes_window", u"Longitud", None))
        self.label_43.setText(QCoreApplication.translate("bordes_window", u"Y", None))
        self.label_45.setText(QCoreApplication.translate("bordes_window", u"Z", None))
        self.label_44.setText(QCoreApplication.translate("bordes_window", u"Empieza", None))
        self.label_42.setText(QCoreApplication.translate("bordes_window", u"Longitud", None))
        self.label_47.setText(QCoreApplication.translate("bordes_window", u"Y", None))
        self.label_49.setText(QCoreApplication.translate("bordes_window", u"Z", None))
        self.label_48.setText(QCoreApplication.translate("bordes_window", u"Empieza", None))
        self.label_46.setText(QCoreApplication.translate("bordes_window", u"Longitud", None))
        self.label_51.setText(QCoreApplication.translate("bordes_window", u"X", None))
        self.label_53.setText(QCoreApplication.translate("bordes_window", u"Z", None))
        self.label_52.setText(QCoreApplication.translate("bordes_window", u"Empieza", None))
        self.label_50.setText(QCoreApplication.translate("bordes_window", u"Longitud", None))
        self.label_54.setText(QCoreApplication.translate("bordes_window", u"X", None))
        self.label_55.setText(QCoreApplication.translate("bordes_window", u"Z", None))
        self.label_56.setText(QCoreApplication.translate("bordes_window", u"Empieza", None))
        self.label_57.setText(QCoreApplication.translate("bordes_window", u"Longitud", None))
        self.label_58.setText(QCoreApplication.translate("bordes_window", u"X", None))
        self.label_59.setText(QCoreApplication.translate("bordes_window", u"Z", None))
        self.label_60.setText(QCoreApplication.translate("bordes_window", u"Empieza", None))
        self.label_61.setText(QCoreApplication.translate("bordes_window", u"Longitud", None))
        self.label_62.setText(QCoreApplication.translate("bordes_window", u"X", None))
        self.label_63.setText(QCoreApplication.translate("bordes_window", u"Z", None))
        self.label_64.setText(QCoreApplication.translate("bordes_window", u"Empieza", None))
        self.label_65.setText(QCoreApplication.translate("bordes_window", u"Longitud", None))
        self.label_66.setText(QCoreApplication.translate("bordes_window", u"X", None))
        self.label_67.setText(QCoreApplication.translate("bordes_window", u"Z", None))
        self.label_68.setText(QCoreApplication.translate("bordes_window", u"Empieza", None))
        self.label_69.setText(QCoreApplication.translate("bordes_window", u"Longitud", None))
        self.label_70.setText(QCoreApplication.translate("bordes_window", u"X", None))
        self.label_71.setText(QCoreApplication.translate("bordes_window", u"Z", None))
        self.label_72.setText(QCoreApplication.translate("bordes_window", u"Empieza", None))
        self.label_73.setText(QCoreApplication.translate("bordes_window", u"Longitud", None))
        self.label_74.setText(QCoreApplication.translate("bordes_window", u"X", None))
        self.label_75.setText(QCoreApplication.translate("bordes_window", u"Z", None))
        self.label_76.setText(QCoreApplication.translate("bordes_window", u"Empieza", None))
        self.label_77.setText(QCoreApplication.translate("bordes_window", u"Longitud", None))
        self.label_78.setText(QCoreApplication.translate("bordes_window", u"X", None))
        self.label_79.setText(QCoreApplication.translate("bordes_window", u"Z", None))
        self.label_80.setText(QCoreApplication.translate("bordes_window", u"Empieza", None))
        self.label_81.setText(QCoreApplication.translate("bordes_window", u"Longitud", None))
        self.label_82.setText(QCoreApplication.translate("bordes_window", u"X", None))
        self.label_83.setText(QCoreApplication.translate("bordes_window", u"Z", None))
        self.label_84.setText(QCoreApplication.translate("bordes_window", u"Empieza", None))
        self.label_85.setText(QCoreApplication.translate("bordes_window", u"Longitud", None))
        self.label_86.setText(QCoreApplication.translate("bordes_window", u"X", None))
        self.label_87.setText(QCoreApplication.translate("bordes_window", u"Z", None))
        self.label_88.setText(QCoreApplication.translate("bordes_window", u"Empieza", None))
        self.label_89.setText(QCoreApplication.translate("bordes_window", u"Longitud", None))
        self.label_90.setText(QCoreApplication.translate("bordes_window", u"X", None))
        self.label_91.setText(QCoreApplication.translate("bordes_window", u"Y", None))
        self.label_92.setText(QCoreApplication.translate("bordes_window", u"Empieza", None))
        self.label_93.setText(QCoreApplication.translate("bordes_window", u"Longitud", None))
        self.label_94.setText(QCoreApplication.translate("bordes_window", u"X", None))
        self.label_95.setText(QCoreApplication.translate("bordes_window", u"Y", None))
        self.label_97.setText(QCoreApplication.translate("bordes_window", u"Empieza", None))
        self.label_96.setText(QCoreApplication.translate("bordes_window", u"Longitud", None))
        self.label_98.setText(QCoreApplication.translate("bordes_window", u"X", None))
        self.label_99.setText(QCoreApplication.translate("bordes_window", u"Y", None))
        self.label_101.setText(QCoreApplication.translate("bordes_window", u"Empieza", None))
        self.label_100.setText(QCoreApplication.translate("bordes_window", u"Longitud", None))
        self.label_102.setText(QCoreApplication.translate("bordes_window", u"X", None))
        self.label_103.setText(QCoreApplication.translate("bordes_window", u"Y", None))
        self.label_105.setText(QCoreApplication.translate("bordes_window", u"Empieza", None))
        self.label_104.setText(QCoreApplication.translate("bordes_window", u"Longitud", None))
        self.label_106.setText(QCoreApplication.translate("bordes_window", u"X", None))
        self.label_107.setText(QCoreApplication.translate("bordes_window", u"Y", None))
        self.label_109.setText(QCoreApplication.translate("bordes_window", u"Empieza", None))
        self.label_108.setText(QCoreApplication.translate("bordes_window", u"Longitud", None))
        self.label_110.setText(QCoreApplication.translate("bordes_window", u"X", None))
        self.label_111.setText(QCoreApplication.translate("bordes_window", u"Y", None))
        self.label_113.setText(QCoreApplication.translate("bordes_window", u"Empieza", None))
        self.label_112.setText(QCoreApplication.translate("bordes_window", u"Longitud", None))
        self.label_114.setText(QCoreApplication.translate("bordes_window", u"X", None))
        self.label_115.setText(QCoreApplication.translate("bordes_window", u"Y", None))
        self.label_117.setText(QCoreApplication.translate("bordes_window", u"Empieza", None))
        self.label_116.setText(QCoreApplication.translate("bordes_window", u"Longitud", None))
        self.label_118.setText(QCoreApplication.translate("bordes_window", u"X", None))
        self.label_119.setText(QCoreApplication.translate("bordes_window", u"Y", None))
        self.label_121.setText(QCoreApplication.translate("bordes_window", u"Empieza", None))
        self.label_120.setText(QCoreApplication.translate("bordes_window", u"Longitud", None))
        self.label_122.setText(QCoreApplication.translate("bordes_window", u"X", None))
        self.label_123.setText(QCoreApplication.translate("bordes_window", u"Y", None))
        self.label_125.setText(QCoreApplication.translate("bordes_window", u"Empieza", None))
        self.label_124.setText(QCoreApplication.translate("bordes_window", u"Longitud", None))
        self.label_126.setText(QCoreApplication.translate("bordes_window", u"X", None))
        self.label_127.setText(QCoreApplication.translate("bordes_window", u"Y", None))
        self.label_129.setText(QCoreApplication.translate("bordes_window", u"Empieza", None))
        self.label_128.setText(QCoreApplication.translate("bordes_window", u"Longitud", None))
    # retranslateUi

