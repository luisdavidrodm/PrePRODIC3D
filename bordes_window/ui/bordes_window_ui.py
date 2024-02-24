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
    QStackedWidget, QVBoxLayout, QWidget)

class Ui_bordes_window(object):
    def setupUi(self, bordes_window):
        if not bordes_window.objectName():
            bordes_window.setObjectName(u"bordes_window")
        bordes_window.resize(445, 521)
        self.gridLayout_3 = QGridLayout(bordes_window)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
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

        self.groupBox = QGroupBox(bordes_window)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout = QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 2)

        self.sw_segment_addremove = QStackedWidget(self.groupBox)
        self.sw_segment_addremove.setObjectName(u"sw_segment_addremove")
        self.sw_segment_addremove_xmax = QWidget()
        self.sw_segment_addremove_xmax.setObjectName(u"sw_segment_addremove_xmax")
        self.verticalLayout_5 = QVBoxLayout(self.sw_segment_addremove_xmax)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.pb_addsegment_xmax = QPushButton(self.sw_segment_addremove_xmax)
        self.pb_addsegment_xmax.setObjectName(u"pb_addsegment_xmax")

        self.verticalLayout_5.addWidget(self.pb_addsegment_xmax)

        self.pb_remsegment_xmax = QPushButton(self.sw_segment_addremove_xmax)
        self.pb_remsegment_xmax.setObjectName(u"pb_remsegment_xmax")

        self.verticalLayout_5.addWidget(self.pb_remsegment_xmax)

        self.sw_segment_addremove.addWidget(self.sw_segment_addremove_xmax)
        self.sw_segment_addremove_xmin = QWidget()
        self.sw_segment_addremove_xmin.setObjectName(u"sw_segment_addremove_xmin")
        self.verticalLayout_6 = QVBoxLayout(self.sw_segment_addremove_xmin)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.pb_addsegment_xmin = QPushButton(self.sw_segment_addremove_xmin)
        self.pb_addsegment_xmin.setObjectName(u"pb_addsegment_xmin")

        self.verticalLayout_6.addWidget(self.pb_addsegment_xmin)

        self.pb_remsegment_xmin = QPushButton(self.sw_segment_addremove_xmin)
        self.pb_remsegment_xmin.setObjectName(u"pb_remsegment_xmin")

        self.verticalLayout_6.addWidget(self.pb_remsegment_xmin)

        self.sw_segment_addremove.addWidget(self.sw_segment_addremove_xmin)
        self.sw_segment_addremove_ymax = QWidget()
        self.sw_segment_addremove_ymax.setObjectName(u"sw_segment_addremove_ymax")
        self.verticalLayout_7 = QVBoxLayout(self.sw_segment_addremove_ymax)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.pb_addsegment_ymax = QPushButton(self.sw_segment_addremove_ymax)
        self.pb_addsegment_ymax.setObjectName(u"pb_addsegment_ymax")

        self.verticalLayout_7.addWidget(self.pb_addsegment_ymax)

        self.pb_remsegment_ymax = QPushButton(self.sw_segment_addremove_ymax)
        self.pb_remsegment_ymax.setObjectName(u"pb_remsegment_ymax")

        self.verticalLayout_7.addWidget(self.pb_remsegment_ymax)

        self.sw_segment_addremove.addWidget(self.sw_segment_addremove_ymax)
        self.sw_segment_addremove_ymin = QWidget()
        self.sw_segment_addremove_ymin.setObjectName(u"sw_segment_addremove_ymin")
        self.verticalLayout_8 = QVBoxLayout(self.sw_segment_addremove_ymin)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.pb_addsegment_ymin = QPushButton(self.sw_segment_addremove_ymin)
        self.pb_addsegment_ymin.setObjectName(u"pb_addsegment_ymin")

        self.verticalLayout_8.addWidget(self.pb_addsegment_ymin)

        self.pb_remsegment_ymin = QPushButton(self.sw_segment_addremove_ymin)
        self.pb_remsegment_ymin.setObjectName(u"pb_remsegment_ymin")

        self.verticalLayout_8.addWidget(self.pb_remsegment_ymin)

        self.sw_segment_addremove.addWidget(self.sw_segment_addremove_ymin)
        self.sw_segment_addremove_zmax = QWidget()
        self.sw_segment_addremove_zmax.setObjectName(u"sw_segment_addremove_zmax")
        self.verticalLayout_9 = QVBoxLayout(self.sw_segment_addremove_zmax)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.pb_addsegment_zmax = QPushButton(self.sw_segment_addremove_zmax)
        self.pb_addsegment_zmax.setObjectName(u"pb_addsegment_zmax")

        self.verticalLayout_9.addWidget(self.pb_addsegment_zmax)

        self.pb_remsegment_zmax = QPushButton(self.sw_segment_addremove_zmax)
        self.pb_remsegment_zmax.setObjectName(u"pb_remsegment_zmax")

        self.verticalLayout_9.addWidget(self.pb_remsegment_zmax)

        self.sw_segment_addremove.addWidget(self.sw_segment_addremove_zmax)
        self.sw_segment_addremove_zmin = QWidget()
        self.sw_segment_addremove_zmin.setObjectName(u"sw_segment_addremove_zmin")
        self.verticalLayout_10 = QVBoxLayout(self.sw_segment_addremove_zmin)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.pb_addsegment_zmin = QPushButton(self.sw_segment_addremove_zmin)
        self.pb_addsegment_zmin.setObjectName(u"pb_addsegment_zmin")

        self.verticalLayout_10.addWidget(self.pb_addsegment_zmin)

        self.pb_remsegment_zmin = QPushButton(self.sw_segment_addremove_zmin)
        self.pb_remsegment_zmin.setObjectName(u"pb_remsegment_zmin")

        self.verticalLayout_10.addWidget(self.pb_remsegment_zmin)

        self.sw_segment_addremove.addWidget(self.sw_segment_addremove_zmin)

        self.gridLayout.addWidget(self.sw_segment_addremove, 3, 0, 1, 4)

        self.lw_bordes = QListWidget(self.groupBox)
        QListWidgetItem(self.lw_bordes)
        QListWidgetItem(self.lw_bordes)
        QListWidgetItem(self.lw_bordes)
        QListWidgetItem(self.lw_bordes)
        QListWidgetItem(self.lw_bordes)
        QListWidgetItem(self.lw_bordes)
        self.lw_bordes.setObjectName(u"lw_bordes")

        self.gridLayout.addWidget(self.lw_bordes, 2, 0, 1, 3)

        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 1, 3, 1, 1)

        self.sw_segmentlist = QStackedWidget(self.groupBox)
        self.sw_segmentlist.setObjectName(u"sw_segmentlist")
        self.sw_segmentlist_xmax = QWidget()
        self.sw_segmentlist_xmax.setObjectName(u"sw_segmentlist_xmax")
        self.verticalLayout_4 = QVBoxLayout(self.sw_segmentlist_xmax)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.lw_segmentlist_xmax = QListWidget(self.sw_segmentlist_xmax)
        QListWidgetItem(self.lw_segmentlist_xmax)
        self.lw_segmentlist_xmax.setObjectName(u"lw_segmentlist_xmax")

        self.verticalLayout_4.addWidget(self.lw_segmentlist_xmax)

        self.sw_segmentlist.addWidget(self.sw_segmentlist_xmax)
        self.sw_segmentlist_xmin = QWidget()
        self.sw_segmentlist_xmin.setObjectName(u"sw_segmentlist_xmin")
        self.horizontalLayout_2 = QHBoxLayout(self.sw_segmentlist_xmin)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.lw_segmentlist_xmin = QListWidget(self.sw_segmentlist_xmin)
        QListWidgetItem(self.lw_segmentlist_xmin)
        self.lw_segmentlist_xmin.setObjectName(u"lw_segmentlist_xmin")

        self.horizontalLayout_2.addWidget(self.lw_segmentlist_xmin)

        self.sw_segmentlist.addWidget(self.sw_segmentlist_xmin)
        self.sw_segmentlist_ymax = QWidget()
        self.sw_segmentlist_ymax.setObjectName(u"sw_segmentlist_ymax")
        self.horizontalLayout_3 = QHBoxLayout(self.sw_segmentlist_ymax)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.lw_segmentlist_ymax = QListWidget(self.sw_segmentlist_ymax)
        QListWidgetItem(self.lw_segmentlist_ymax)
        self.lw_segmentlist_ymax.setObjectName(u"lw_segmentlist_ymax")

        self.horizontalLayout_3.addWidget(self.lw_segmentlist_ymax)

        self.sw_segmentlist.addWidget(self.sw_segmentlist_ymax)
        self.sw_segmentlist_ymin = QWidget()
        self.sw_segmentlist_ymin.setObjectName(u"sw_segmentlist_ymin")
        self.verticalLayout_11 = QVBoxLayout(self.sw_segmentlist_ymin)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.lw_segmentlist_ymin = QListWidget(self.sw_segmentlist_ymin)
        QListWidgetItem(self.lw_segmentlist_ymin)
        self.lw_segmentlist_ymin.setObjectName(u"lw_segmentlist_ymin")

        self.verticalLayout_11.addWidget(self.lw_segmentlist_ymin)

        self.sw_segmentlist.addWidget(self.sw_segmentlist_ymin)
        self.sw_segmentlist_zmax = QWidget()
        self.sw_segmentlist_zmax.setObjectName(u"sw_segmentlist_zmax")
        self.horizontalLayout_4 = QHBoxLayout(self.sw_segmentlist_zmax)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.lw_segmentlist_zmax = QListWidget(self.sw_segmentlist_zmax)
        QListWidgetItem(self.lw_segmentlist_zmax)
        self.lw_segmentlist_zmax.setObjectName(u"lw_segmentlist_zmax")

        self.horizontalLayout_4.addWidget(self.lw_segmentlist_zmax)

        self.sw_segmentlist.addWidget(self.sw_segmentlist_zmax)
        self.sw_segmentlist_zmin = QWidget()
        self.sw_segmentlist_zmin.setObjectName(u"sw_segmentlist_zmin")
        self.verticalLayout_12 = QVBoxLayout(self.sw_segmentlist_zmin)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.lw_segmentlist_zmin = QListWidget(self.sw_segmentlist_zmin)
        QListWidgetItem(self.lw_segmentlist_zmin)
        self.lw_segmentlist_zmin.setObjectName(u"lw_segmentlist_zmin")

        self.verticalLayout_12.addWidget(self.lw_segmentlist_zmin)

        self.sw_segmentlist.addWidget(self.sw_segmentlist_zmin)

        self.gridLayout.addWidget(self.sw_segmentlist, 2, 3, 1, 1)

        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.sw_lon_segment = QStackedWidget(self.groupBox)
        self.sw_lon_segment.setObjectName(u"sw_lon_segment")
        self.sw_lon_segment_xmax_1 = QWidget()
        self.sw_lon_segment_xmax_1.setObjectName(u"sw_lon_segment_xmax_1")
        self.verticalLayout_13 = QVBoxLayout(self.sw_lon_segment_xmax_1)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.le_lon_segment_xmax_1 = QLineEdit(self.sw_lon_segment_xmax_1)
        self.le_lon_segment_xmax_1.setObjectName(u"le_lon_segment_xmax_1")

        self.verticalLayout_13.addWidget(self.le_lon_segment_xmax_1)

        self.sw_lon_segment.addWidget(self.sw_lon_segment_xmax_1)
        self.sw_lon_segment_xmax_2 = QWidget()
        self.sw_lon_segment_xmax_2.setObjectName(u"sw_lon_segment_xmax_2")
        self.horizontalLayout_5 = QHBoxLayout(self.sw_lon_segment_xmax_2)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.le_lon_segment_xmax_2 = QLineEdit(self.sw_lon_segment_xmax_2)
        self.le_lon_segment_xmax_2.setObjectName(u"le_lon_segment_xmax_2")

        self.horizontalLayout_5.addWidget(self.le_lon_segment_xmax_2)

        self.sw_lon_segment.addWidget(self.sw_lon_segment_xmax_2)
        self.sw_lon_segment_xmax_3 = QWidget()
        self.sw_lon_segment_xmax_3.setObjectName(u"sw_lon_segment_xmax_3")
        self.horizontalLayout_6 = QHBoxLayout(self.sw_lon_segment_xmax_3)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.le_lon_segment_xmax_3 = QLineEdit(self.sw_lon_segment_xmax_3)
        self.le_lon_segment_xmax_3.setObjectName(u"le_lon_segment_xmax_3")

        self.horizontalLayout_6.addWidget(self.le_lon_segment_xmax_3)

        self.sw_lon_segment.addWidget(self.sw_lon_segment_xmax_3)
        self.sw_lon_segment_xmax_4 = QWidget()
        self.sw_lon_segment_xmax_4.setObjectName(u"sw_lon_segment_xmax_4")
        self.horizontalLayout_7 = QHBoxLayout(self.sw_lon_segment_xmax_4)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.le_lon_segment_xmax_4 = QLineEdit(self.sw_lon_segment_xmax_4)
        self.le_lon_segment_xmax_4.setObjectName(u"le_lon_segment_xmax_4")

        self.horizontalLayout_7.addWidget(self.le_lon_segment_xmax_4)

        self.sw_lon_segment.addWidget(self.sw_lon_segment_xmax_4)
        self.sw_lon_segment_xmax_5 = QWidget()
        self.sw_lon_segment_xmax_5.setObjectName(u"sw_lon_segment_xmax_5")
        self.horizontalLayout_8 = QHBoxLayout(self.sw_lon_segment_xmax_5)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.le_lon_segment_xmax_5 = QLineEdit(self.sw_lon_segment_xmax_5)
        self.le_lon_segment_xmax_5.setObjectName(u"le_lon_segment_xmax_5")

        self.horizontalLayout_8.addWidget(self.le_lon_segment_xmax_5)

        self.sw_lon_segment.addWidget(self.sw_lon_segment_xmax_5)
        self.sw_lon_segment_xmin_1 = QWidget()
        self.sw_lon_segment_xmin_1.setObjectName(u"sw_lon_segment_xmin_1")
        self.horizontalLayout_9 = QHBoxLayout(self.sw_lon_segment_xmin_1)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.le_lon_segment_xmin_1 = QLineEdit(self.sw_lon_segment_xmin_1)
        self.le_lon_segment_xmin_1.setObjectName(u"le_lon_segment_xmin_1")

        self.horizontalLayout_9.addWidget(self.le_lon_segment_xmin_1)

        self.sw_lon_segment.addWidget(self.sw_lon_segment_xmin_1)
        self.sw_lon_segment_xmin_2 = QWidget()
        self.sw_lon_segment_xmin_2.setObjectName(u"sw_lon_segment_xmin_2")
        self.horizontalLayout_10 = QHBoxLayout(self.sw_lon_segment_xmin_2)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.le_lon_segment_xmin_2 = QLineEdit(self.sw_lon_segment_xmin_2)
        self.le_lon_segment_xmin_2.setObjectName(u"le_lon_segment_xmin_2")

        self.horizontalLayout_10.addWidget(self.le_lon_segment_xmin_2)

        self.sw_lon_segment.addWidget(self.sw_lon_segment_xmin_2)
        self.sw_lon_segment_xmin_3 = QWidget()
        self.sw_lon_segment_xmin_3.setObjectName(u"sw_lon_segment_xmin_3")
        self.horizontalLayout_11 = QHBoxLayout(self.sw_lon_segment_xmin_3)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.le_lon_segment_xmin_3 = QLineEdit(self.sw_lon_segment_xmin_3)
        self.le_lon_segment_xmin_3.setObjectName(u"le_lon_segment_xmin_3")

        self.horizontalLayout_11.addWidget(self.le_lon_segment_xmin_3)

        self.sw_lon_segment.addWidget(self.sw_lon_segment_xmin_3)
        self.sw_lon_segment_xmin_4 = QWidget()
        self.sw_lon_segment_xmin_4.setObjectName(u"sw_lon_segment_xmin_4")
        self.horizontalLayout_12 = QHBoxLayout(self.sw_lon_segment_xmin_4)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.le_lon_segment_xmin_4 = QLineEdit(self.sw_lon_segment_xmin_4)
        self.le_lon_segment_xmin_4.setObjectName(u"le_lon_segment_xmin_4")

        self.horizontalLayout_12.addWidget(self.le_lon_segment_xmin_4)

        self.sw_lon_segment.addWidget(self.sw_lon_segment_xmin_4)
        self.sw_lon_segment_xmin_5 = QWidget()
        self.sw_lon_segment_xmin_5.setObjectName(u"sw_lon_segment_xmin_5")
        self.horizontalLayout_13 = QHBoxLayout(self.sw_lon_segment_xmin_5)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.le_lon_segment_xmin_5 = QLineEdit(self.sw_lon_segment_xmin_5)
        self.le_lon_segment_xmin_5.setObjectName(u"le_lon_segment_xmin_5")

        self.horizontalLayout_13.addWidget(self.le_lon_segment_xmin_5)

        self.sw_lon_segment.addWidget(self.sw_lon_segment_xmin_5)
        self.sw_lon_segment_ymax_1 = QWidget()
        self.sw_lon_segment_ymax_1.setObjectName(u"sw_lon_segment_ymax_1")
        self.horizontalLayout_14 = QHBoxLayout(self.sw_lon_segment_ymax_1)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.le_lon_segment_ymax_1 = QLineEdit(self.sw_lon_segment_ymax_1)
        self.le_lon_segment_ymax_1.setObjectName(u"le_lon_segment_ymax_1")

        self.horizontalLayout_14.addWidget(self.le_lon_segment_ymax_1)

        self.sw_lon_segment.addWidget(self.sw_lon_segment_ymax_1)
        self.sw_lon_segment_ymax_2 = QWidget()
        self.sw_lon_segment_ymax_2.setObjectName(u"sw_lon_segment_ymax_2")
        self.horizontalLayout_15 = QHBoxLayout(self.sw_lon_segment_ymax_2)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.le_lon_segment_ymax_2 = QLineEdit(self.sw_lon_segment_ymax_2)
        self.le_lon_segment_ymax_2.setObjectName(u"le_lon_segment_ymax_2")

        self.horizontalLayout_15.addWidget(self.le_lon_segment_ymax_2)

        self.sw_lon_segment.addWidget(self.sw_lon_segment_ymax_2)
        self.sw_lon_segment_ymax_3 = QWidget()
        self.sw_lon_segment_ymax_3.setObjectName(u"sw_lon_segment_ymax_3")
        self.horizontalLayout_16 = QHBoxLayout(self.sw_lon_segment_ymax_3)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.le_lon_segment_ymax_3 = QLineEdit(self.sw_lon_segment_ymax_3)
        self.le_lon_segment_ymax_3.setObjectName(u"le_lon_segment_ymax_3")

        self.horizontalLayout_16.addWidget(self.le_lon_segment_ymax_3)

        self.sw_lon_segment.addWidget(self.sw_lon_segment_ymax_3)
        self.sw_lon_segment_ymax_4 = QWidget()
        self.sw_lon_segment_ymax_4.setObjectName(u"sw_lon_segment_ymax_4")
        self.horizontalLayout_17 = QHBoxLayout(self.sw_lon_segment_ymax_4)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.le_lon_segment_ymax_4 = QLineEdit(self.sw_lon_segment_ymax_4)
        self.le_lon_segment_ymax_4.setObjectName(u"le_lon_segment_ymax_4")

        self.horizontalLayout_17.addWidget(self.le_lon_segment_ymax_4)

        self.sw_lon_segment.addWidget(self.sw_lon_segment_ymax_4)
        self.sw_lon_segment_ymax_5 = QWidget()
        self.sw_lon_segment_ymax_5.setObjectName(u"sw_lon_segment_ymax_5")
        self.horizontalLayout_18 = QHBoxLayout(self.sw_lon_segment_ymax_5)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.le_lon_segment_ymax_5 = QLineEdit(self.sw_lon_segment_ymax_5)
        self.le_lon_segment_ymax_5.setObjectName(u"le_lon_segment_ymax_5")

        self.horizontalLayout_18.addWidget(self.le_lon_segment_ymax_5)

        self.sw_lon_segment.addWidget(self.sw_lon_segment_ymax_5)
        self.sw_lon_segment_ymin_1 = QWidget()
        self.sw_lon_segment_ymin_1.setObjectName(u"sw_lon_segment_ymin_1")
        self.horizontalLayout_19 = QHBoxLayout(self.sw_lon_segment_ymin_1)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.le_lon_segment_ymin_1 = QLineEdit(self.sw_lon_segment_ymin_1)
        self.le_lon_segment_ymin_1.setObjectName(u"le_lon_segment_ymin_1")

        self.horizontalLayout_19.addWidget(self.le_lon_segment_ymin_1)

        self.sw_lon_segment.addWidget(self.sw_lon_segment_ymin_1)
        self.sw_lon_segment_ymin_2 = QWidget()
        self.sw_lon_segment_ymin_2.setObjectName(u"sw_lon_segment_ymin_2")
        self.horizontalLayout_20 = QHBoxLayout(self.sw_lon_segment_ymin_2)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.le_lon_segment_ymin_2 = QLineEdit(self.sw_lon_segment_ymin_2)
        self.le_lon_segment_ymin_2.setObjectName(u"le_lon_segment_ymin_2")

        self.horizontalLayout_20.addWidget(self.le_lon_segment_ymin_2)

        self.sw_lon_segment.addWidget(self.sw_lon_segment_ymin_2)
        self.sw_lon_segment_ymin_3 = QWidget()
        self.sw_lon_segment_ymin_3.setObjectName(u"sw_lon_segment_ymin_3")
        self.horizontalLayout_21 = QHBoxLayout(self.sw_lon_segment_ymin_3)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.le_lon_segment_ymin_3 = QLineEdit(self.sw_lon_segment_ymin_3)
        self.le_lon_segment_ymin_3.setObjectName(u"le_lon_segment_ymin_3")

        self.horizontalLayout_21.addWidget(self.le_lon_segment_ymin_3)

        self.sw_lon_segment.addWidget(self.sw_lon_segment_ymin_3)
        self.sw_lon_segment_ymin_4 = QWidget()
        self.sw_lon_segment_ymin_4.setObjectName(u"sw_lon_segment_ymin_4")
        self.horizontalLayout_22 = QHBoxLayout(self.sw_lon_segment_ymin_4)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.le_lon_segment_ymin_4 = QLineEdit(self.sw_lon_segment_ymin_4)
        self.le_lon_segment_ymin_4.setObjectName(u"le_lon_segment_ymin_4")

        self.horizontalLayout_22.addWidget(self.le_lon_segment_ymin_4)

        self.sw_lon_segment.addWidget(self.sw_lon_segment_ymin_4)
        self.sw_lon_segment_ymin_5 = QWidget()
        self.sw_lon_segment_ymin_5.setObjectName(u"sw_lon_segment_ymin_5")
        self.horizontalLayout_23 = QHBoxLayout(self.sw_lon_segment_ymin_5)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.le_lon_segment_ymin_5 = QLineEdit(self.sw_lon_segment_ymin_5)
        self.le_lon_segment_ymin_5.setObjectName(u"le_lon_segment_ymin_5")

        self.horizontalLayout_23.addWidget(self.le_lon_segment_ymin_5)

        self.sw_lon_segment.addWidget(self.sw_lon_segment_ymin_5)
        self.sw_lon_segment_zmax_1 = QWidget()
        self.sw_lon_segment_zmax_1.setObjectName(u"sw_lon_segment_zmax_1")
        self.horizontalLayout_24 = QHBoxLayout(self.sw_lon_segment_zmax_1)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.le_lon_segment_zmax_1 = QLineEdit(self.sw_lon_segment_zmax_1)
        self.le_lon_segment_zmax_1.setObjectName(u"le_lon_segment_zmax_1")

        self.horizontalLayout_24.addWidget(self.le_lon_segment_zmax_1)

        self.sw_lon_segment.addWidget(self.sw_lon_segment_zmax_1)
        self.sw_lon_segment_zmax_2 = QWidget()
        self.sw_lon_segment_zmax_2.setObjectName(u"sw_lon_segment_zmax_2")
        self.horizontalLayout_25 = QHBoxLayout(self.sw_lon_segment_zmax_2)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.le_lon_segment_zmax_2 = QLineEdit(self.sw_lon_segment_zmax_2)
        self.le_lon_segment_zmax_2.setObjectName(u"le_lon_segment_zmax_2")

        self.horizontalLayout_25.addWidget(self.le_lon_segment_zmax_2)

        self.sw_lon_segment.addWidget(self.sw_lon_segment_zmax_2)
        self.sw_lon_segment_zmax_3 = QWidget()
        self.sw_lon_segment_zmax_3.setObjectName(u"sw_lon_segment_zmax_3")
        self.horizontalLayout_26 = QHBoxLayout(self.sw_lon_segment_zmax_3)
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.le_lon_segment_zmax_3 = QLineEdit(self.sw_lon_segment_zmax_3)
        self.le_lon_segment_zmax_3.setObjectName(u"le_lon_segment_zmax_3")

        self.horizontalLayout_26.addWidget(self.le_lon_segment_zmax_3)

        self.sw_lon_segment.addWidget(self.sw_lon_segment_zmax_3)
        self.sw_lon_segment_zmax_4 = QWidget()
        self.sw_lon_segment_zmax_4.setObjectName(u"sw_lon_segment_zmax_4")
        self.horizontalLayout_27 = QHBoxLayout(self.sw_lon_segment_zmax_4)
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.le_lon_segment_zmax_4 = QLineEdit(self.sw_lon_segment_zmax_4)
        self.le_lon_segment_zmax_4.setObjectName(u"le_lon_segment_zmax_4")

        self.horizontalLayout_27.addWidget(self.le_lon_segment_zmax_4)

        self.sw_lon_segment.addWidget(self.sw_lon_segment_zmax_4)
        self.sw_lon_segment_zmax_5 = QWidget()
        self.sw_lon_segment_zmax_5.setObjectName(u"sw_lon_segment_zmax_5")
        self.horizontalLayout_28 = QHBoxLayout(self.sw_lon_segment_zmax_5)
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.le_lon_segment_zmax_5 = QLineEdit(self.sw_lon_segment_zmax_5)
        self.le_lon_segment_zmax_5.setObjectName(u"le_lon_segment_zmax_5")

        self.horizontalLayout_28.addWidget(self.le_lon_segment_zmax_5)

        self.sw_lon_segment.addWidget(self.sw_lon_segment_zmax_5)
        self.sw_lon_segment_zmin_1 = QWidget()
        self.sw_lon_segment_zmin_1.setObjectName(u"sw_lon_segment_zmin_1")
        self.horizontalLayout_29 = QHBoxLayout(self.sw_lon_segment_zmin_1)
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.le_lon_segment_zmin_1 = QLineEdit(self.sw_lon_segment_zmin_1)
        self.le_lon_segment_zmin_1.setObjectName(u"le_lon_segment_zmin_1")

        self.horizontalLayout_29.addWidget(self.le_lon_segment_zmin_1)

        self.sw_lon_segment.addWidget(self.sw_lon_segment_zmin_1)
        self.sw_lon_segment_zmin_2 = QWidget()
        self.sw_lon_segment_zmin_2.setObjectName(u"sw_lon_segment_zmin_2")
        self.horizontalLayout_30 = QHBoxLayout(self.sw_lon_segment_zmin_2)
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.le_lon_segment_zmin_2 = QLineEdit(self.sw_lon_segment_zmin_2)
        self.le_lon_segment_zmin_2.setObjectName(u"le_lon_segment_zmin_2")

        self.horizontalLayout_30.addWidget(self.le_lon_segment_zmin_2)

        self.sw_lon_segment.addWidget(self.sw_lon_segment_zmin_2)
        self.sw_lon_segment_zmin_3 = QWidget()
        self.sw_lon_segment_zmin_3.setObjectName(u"sw_lon_segment_zmin_3")
        self.horizontalLayout_31 = QHBoxLayout(self.sw_lon_segment_zmin_3)
        self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
        self.le_lon_segment_zmin_3 = QLineEdit(self.sw_lon_segment_zmin_3)
        self.le_lon_segment_zmin_3.setObjectName(u"le_lon_segment_zmin_3")

        self.horizontalLayout_31.addWidget(self.le_lon_segment_zmin_3)

        self.sw_lon_segment.addWidget(self.sw_lon_segment_zmin_3)
        self.sw_lon_segment_zmin_4 = QWidget()
        self.sw_lon_segment_zmin_4.setObjectName(u"sw_lon_segment_zmin_4")
        self.horizontalLayout_32 = QHBoxLayout(self.sw_lon_segment_zmin_4)
        self.horizontalLayout_32.setObjectName(u"horizontalLayout_32")
        self.le_lon_segment_zmin_4 = QLineEdit(self.sw_lon_segment_zmin_4)
        self.le_lon_segment_zmin_4.setObjectName(u"le_lon_segment_zmin_4")

        self.horizontalLayout_32.addWidget(self.le_lon_segment_zmin_4)

        self.sw_lon_segment.addWidget(self.sw_lon_segment_zmin_4)
        self.sw_lon_segment_zmin_5 = QWidget()
        self.sw_lon_segment_zmin_5.setObjectName(u"sw_lon_segment_zmin_5")
        self.horizontalLayout_33 = QHBoxLayout(self.sw_lon_segment_zmin_5)
        self.horizontalLayout_33.setObjectName(u"horizontalLayout_33")
        self.le_lon_segment_zmin_5 = QLineEdit(self.sw_lon_segment_zmin_5)
        self.le_lon_segment_zmin_5.setObjectName(u"le_lon_segment_zmin_5")

        self.horizontalLayout_33.addWidget(self.le_lon_segment_zmin_5)

        self.sw_lon_segment.addWidget(self.sw_lon_segment_zmin_5)

        self.gridLayout.addWidget(self.sw_lon_segment, 0, 3, 1, 1)


        self.gridLayout_3.addWidget(self.groupBox, 0, 0, 1, 1)


        self.retranslateUi(bordes_window)

        self.sw_segment_addremove.setCurrentIndex(0)
        self.sw_segmentlist.setCurrentIndex(0)
        self.sw_lon_segment.setCurrentIndex(29)


        QMetaObject.connectSlotsByName(bordes_window)
    # setupUi

    def retranslateUi(self, bordes_window):
        bordes_window.setWindowTitle(QCoreApplication.translate("bordes_window", u"Bordes - PrePRODIC3D", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("bordes_window", u"Tipo de segmento", None))
        self.checkBox.setText(QCoreApplication.translate("bordes_window", u"Pared", None))
        self.checkBox_3.setText(QCoreApplication.translate("bordes_window", u"Entrada de la masa", None))
        self.checkBox_4.setText(QCoreApplication.translate("bordes_window", u"Salida de la masa", None))
        self.checkBox_5.setText(QCoreApplication.translate("bordes_window", u"Nodos internos", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("bordes_window", u"Velocidad", None))
        self.label_4.setText(QCoreApplication.translate("bordes_window", u"Normal", None))
        self.label_5.setText(QCoreApplication.translate("bordes_window", u"Tangencial", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("bordes_window", u"Salida de la masa", None))
        self.label_6.setText(QCoreApplication.translate("bordes_window", u"Fracci\u00f3n", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("bordes_window", u"Variables escalares", None))
        self.groupBox_6.setTitle("")

        __sortingEnabled = self.listWidget_3.isSortingEnabled()
        self.listWidget_3.setSortingEnabled(False)
        ___qlistwidgetitem = self.listWidget_3.item(0)
        ___qlistwidgetitem.setText(QCoreApplication.translate("bordes_window", u"Temperatura", None));
        self.listWidget_3.setSortingEnabled(__sortingEnabled)

        self.groupBox_7.setTitle("")
        self.checkBox_6.setText(QCoreApplication.translate("bordes_window", u"Valor", None))
        self.checkBox_7.setText(QCoreApplication.translate("bordes_window", u"Flujo", None))
        self.checkBox_8.setText(QCoreApplication.translate("bordes_window", u"Convecci\u00f3n", None))
        self.groupBox_8.setTitle("")
        self.label_7.setText(QCoreApplication.translate("bordes_window", u"Valor", None))
        self.label_8.setText(QCoreApplication.translate("bordes_window", u"Temp. ambiente", None))
        self.groupBox.setTitle(QCoreApplication.translate("bordes_window", u"Divisi\u00f3n de bordes", None))
        self.label_2.setText(QCoreApplication.translate("bordes_window", u"Borde", None))
        self.pb_addsegment_xmax.setText(QCoreApplication.translate("bordes_window", u"Agregar un segmento", None))
        self.pb_remsegment_xmax.setText(QCoreApplication.translate("bordes_window", u"Eliminar un segmento", None))
        self.pb_addsegment_xmin.setText(QCoreApplication.translate("bordes_window", u"Agregar un segmento", None))
        self.pb_remsegment_xmin.setText(QCoreApplication.translate("bordes_window", u"Eliminar un segmento", None))
        self.pb_addsegment_ymax.setText(QCoreApplication.translate("bordes_window", u"Agregar un segmento", None))
        self.pb_remsegment_ymax.setText(QCoreApplication.translate("bordes_window", u"Eliminar un segmento", None))
        self.pb_addsegment_ymin.setText(QCoreApplication.translate("bordes_window", u"Agregar un segmento", None))
        self.pb_remsegment_ymin.setText(QCoreApplication.translate("bordes_window", u"Eliminar un segmento", None))
        self.pb_addsegment_zmax.setText(QCoreApplication.translate("bordes_window", u"Agregar un segmento", None))
        self.pb_remsegment_zmax.setText(QCoreApplication.translate("bordes_window", u"Eliminar un segmento", None))
        self.pb_addsegment_zmin.setText(QCoreApplication.translate("bordes_window", u"Agregar un segmento", None))
        self.pb_remsegment_zmin.setText(QCoreApplication.translate("bordes_window", u"Eliminar un segmento", None))

        __sortingEnabled1 = self.lw_bordes.isSortingEnabled()
        self.lw_bordes.setSortingEnabled(False)
        ___qlistwidgetitem1 = self.lw_bordes.item(0)
        ___qlistwidgetitem1.setText(QCoreApplication.translate("bordes_window", u"X Max", None));
        ___qlistwidgetitem2 = self.lw_bordes.item(1)
        ___qlistwidgetitem2.setText(QCoreApplication.translate("bordes_window", u"X Min", None));
        ___qlistwidgetitem3 = self.lw_bordes.item(2)
        ___qlistwidgetitem3.setText(QCoreApplication.translate("bordes_window", u"Y Max", None));
        ___qlistwidgetitem4 = self.lw_bordes.item(3)
        ___qlistwidgetitem4.setText(QCoreApplication.translate("bordes_window", u"Y Min", None));
        ___qlistwidgetitem5 = self.lw_bordes.item(4)
        ___qlistwidgetitem5.setText(QCoreApplication.translate("bordes_window", u"Z Max", None));
        ___qlistwidgetitem6 = self.lw_bordes.item(5)
        ___qlistwidgetitem6.setText(QCoreApplication.translate("bordes_window", u"Z Min", None));
        self.lw_bordes.setSortingEnabled(__sortingEnabled1)

        self.label_3.setText(QCoreApplication.translate("bordes_window", u"Segmento", None))

        __sortingEnabled2 = self.lw_segmentlist_xmax.isSortingEnabled()
        self.lw_segmentlist_xmax.setSortingEnabled(False)
        ___qlistwidgetitem7 = self.lw_segmentlist_xmax.item(0)
        ___qlistwidgetitem7.setText(QCoreApplication.translate("bordes_window", u"Segmento 1", None));
        self.lw_segmentlist_xmax.setSortingEnabled(__sortingEnabled2)


        __sortingEnabled3 = self.lw_segmentlist_xmin.isSortingEnabled()
        self.lw_segmentlist_xmin.setSortingEnabled(False)
        ___qlistwidgetitem8 = self.lw_segmentlist_xmin.item(0)
        ___qlistwidgetitem8.setText(QCoreApplication.translate("bordes_window", u"Segmento 1", None));
        self.lw_segmentlist_xmin.setSortingEnabled(__sortingEnabled3)


        __sortingEnabled4 = self.lw_segmentlist_ymax.isSortingEnabled()
        self.lw_segmentlist_ymax.setSortingEnabled(False)
        ___qlistwidgetitem9 = self.lw_segmentlist_ymax.item(0)
        ___qlistwidgetitem9.setText(QCoreApplication.translate("bordes_window", u"Segmento 1", None));
        self.lw_segmentlist_ymax.setSortingEnabled(__sortingEnabled4)


        __sortingEnabled5 = self.lw_segmentlist_ymin.isSortingEnabled()
        self.lw_segmentlist_ymin.setSortingEnabled(False)
        ___qlistwidgetitem10 = self.lw_segmentlist_ymin.item(0)
        ___qlistwidgetitem10.setText(QCoreApplication.translate("bordes_window", u"Segmento 1", None));
        self.lw_segmentlist_ymin.setSortingEnabled(__sortingEnabled5)


        __sortingEnabled6 = self.lw_segmentlist_zmax.isSortingEnabled()
        self.lw_segmentlist_zmax.setSortingEnabled(False)
        ___qlistwidgetitem11 = self.lw_segmentlist_zmax.item(0)
        ___qlistwidgetitem11.setText(QCoreApplication.translate("bordes_window", u"Segmento 1", None));
        self.lw_segmentlist_zmax.setSortingEnabled(__sortingEnabled6)


        __sortingEnabled7 = self.lw_segmentlist_zmin.isSortingEnabled()
        self.lw_segmentlist_zmin.setSortingEnabled(False)
        ___qlistwidgetitem12 = self.lw_segmentlist_zmin.item(0)
        ___qlistwidgetitem12.setText(QCoreApplication.translate("bordes_window", u"Segmento 1", None));
        self.lw_segmentlist_zmin.setSortingEnabled(__sortingEnabled7)

        self.label.setText(QCoreApplication.translate("bordes_window", u"Longitud", None))
    # retranslateUi

