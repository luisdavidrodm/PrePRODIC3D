# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'bordes_windowOKaVEx.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QGridLayout, QGroupBox,
    QHBoxLayout, QLabel, QLineEdit, QListWidget,
    QListWidgetItem, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_bordes_window(object):
    def setupUi(self, bordes_window):
        if not bordes_window.objectName():
            bordes_window.setObjectName(u"bordes_window")
        bordes_window.resize(445, 729)
        self.gridLayout_3 = QGridLayout(bordes_window)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
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
        self.lw_bordes = QListWidget(self.groupBox)
        QListWidgetItem(self.lw_bordes)
        QListWidgetItem(self.lw_bordes)
        QListWidgetItem(self.lw_bordes)
        QListWidgetItem(self.lw_bordes)
        QListWidgetItem(self.lw_bordes)
        QListWidgetItem(self.lw_bordes)
        self.lw_bordes.setObjectName(u"lw_bordes")

        self.gridLayout.addWidget(self.lw_bordes, 3, 0, 1, 3)

        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 2, 3, 1, 1)

        self.groupBox_2 = QGroupBox(self.groupBox)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.gridLayout_5 = QGridLayout(self.groupBox_2)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.le_vertical_start = QLineEdit(self.groupBox_2)
        self.le_vertical_start.setObjectName(u"le_vertical_start")

        self.gridLayout_5.addWidget(self.le_vertical_start, 1, 2, 1, 1)

        self.le_transversal_end = QLineEdit(self.groupBox_2)
        self.le_transversal_end.setObjectName(u"le_transversal_end")

        self.gridLayout_5.addWidget(self.le_transversal_end, 3, 1, 1, 1)

        self.label = QLabel(self.groupBox_2)
        self.label.setObjectName(u"label")

        self.gridLayout_5.addWidget(self.label, 1, 0, 1, 1)

        self.label_10 = QLabel(self.groupBox_2)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout_5.addWidget(self.label_10, 3, 0, 1, 1)

        self.le_transversal_start = QLineEdit(self.groupBox_2)
        self.le_transversal_start.setObjectName(u"le_transversal_start")

        self.gridLayout_5.addWidget(self.le_transversal_start, 1, 1, 1, 1)

        self.le_vertical_end = QLineEdit(self.groupBox_2)
        self.le_vertical_end.setObjectName(u"le_vertical_end")

        self.gridLayout_5.addWidget(self.le_vertical_end, 3, 2, 1, 1)

        self.lb_transversal = QLabel(self.groupBox_2)
        self.lb_transversal.setObjectName(u"lb_transversal")
        self.lb_transversal.setLayoutDirection(Qt.LeftToRight)
        self.lb_transversal.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.lb_transversal, 0, 1, 1, 1)

        self.lb_vertical = QLabel(self.groupBox_2)
        self.lb_vertical.setObjectName(u"lb_vertical")
        self.lb_vertical.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.lb_vertical, 0, 2, 1, 1)

        self.chb_exclude_borders = QCheckBox(self.groupBox_2)
        self.chb_exclude_borders.setObjectName(u"chb_exclude_borders")

        self.gridLayout_5.addWidget(self.chb_exclude_borders, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.groupBox_2, 1, 0, 1, 4)

        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 2)

        self.groupBox_7 = QGroupBox(self.groupBox)
        self.groupBox_7.setObjectName(u"groupBox_7")
        self.verticalLayout_5 = QVBoxLayout(self.groupBox_7)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.pb_addpatch = QPushButton(self.groupBox_7)
        self.pb_addpatch.setObjectName(u"pb_addpatch")

        self.verticalLayout_5.addWidget(self.pb_addpatch)

        self.pb_rempatch = QPushButton(self.groupBox_7)
        self.pb_rempatch.setObjectName(u"pb_rempatch")

        self.verticalLayout_5.addWidget(self.pb_rempatch)


        self.gridLayout.addWidget(self.groupBox_7, 4, 0, 1, 4)

        self.lw_patchlist = QListWidget(self.groupBox)
        QListWidgetItem(self.lw_patchlist)
        self.lw_patchlist.setObjectName(u"lw_patchlist")

        self.gridLayout.addWidget(self.lw_patchlist, 3, 3, 1, 1)


        self.gridLayout_3.addWidget(self.groupBox, 0, 0, 1, 1)

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


        self.gridLayout_3.addWidget(self.groupBox_5, 2, 1, 2, 1)

        self.label_7 = QLabel(bordes_window)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout_3.addWidget(self.label_7, 5, 0, 1, 1)

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
        self.gridLayout_6 = QGridLayout(self.groupBox_8)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.le_tempamb = QLineEdit(self.groupBox_8)
        self.le_tempamb.setObjectName(u"le_tempamb")
        self.le_tempamb.setEnabled(False)

        self.gridLayout_6.addWidget(self.le_tempamb, 4, 0, 1, 1)

        self.lb_variable = QLabel(self.groupBox_8)
        self.lb_variable.setObjectName(u"lb_variable")

        self.gridLayout_6.addWidget(self.lb_variable, 3, 0, 1, 1)

        self.le_value = QLineEdit(self.groupBox_8)
        self.le_value.setObjectName(u"le_value")

        self.gridLayout_6.addWidget(self.le_value, 2, 0, 1, 1)

        self.lb_value = QLabel(self.groupBox_8)
        self.lb_value.setObjectName(u"lb_value")

        self.gridLayout_6.addWidget(self.lb_value, 0, 0, 1, 1)

        self.chb_ex_value = QCheckBox(self.groupBox_8)
        self.chb_ex_value.setObjectName(u"chb_ex_value")

        self.gridLayout_6.addWidget(self.chb_ex_value, 2, 1, 1, 1)


        self.horizontalLayout.addWidget(self.groupBox_8)


        self.gridLayout_3.addWidget(self.groupBox_3, 1, 0, 1, 2)

        self.groupBox_4 = QGroupBox(bordes_window)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.gridLayout_4 = QGridLayout(self.groupBox_4)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.le_value_veloc_v = QLineEdit(self.groupBox_4)
        self.le_value_veloc_v.setObjectName(u"le_value_veloc_v")
        self.le_value_veloc_v.setEnabled(True)

        self.gridLayout_4.addWidget(self.le_value_veloc_v, 1, 2, 1, 1)

        self.label_4 = QLabel(self.groupBox_4)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_4.addWidget(self.label_4, 0, 1, 1, 1)

        self.label_5 = QLabel(self.groupBox_4)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_4.addWidget(self.label_5, 1, 1, 1, 1)

        self.le_value_veloc_w = QLineEdit(self.groupBox_4)
        self.le_value_veloc_w.setObjectName(u"le_value_veloc_w")
        self.le_value_veloc_w.setEnabled(True)

        self.gridLayout_4.addWidget(self.le_value_veloc_w, 2, 2, 1, 1)

        self.le_value_veloc_u = QLineEdit(self.groupBox_4)
        self.le_value_veloc_u.setObjectName(u"le_value_veloc_u")
        self.le_value_veloc_u.setEnabled(True)

        self.gridLayout_4.addWidget(self.le_value_veloc_u, 0, 2, 1, 1)

        self.label_9 = QLabel(self.groupBox_4)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout_4.addWidget(self.label_9, 2, 1, 1, 1)

        self.chb_ex_veloc_u = QCheckBox(self.groupBox_4)
        self.chb_ex_veloc_u.setObjectName(u"chb_ex_veloc_u")

        self.gridLayout_4.addWidget(self.chb_ex_veloc_u, 0, 3, 1, 1)

        self.chb_ex_veloc_v = QCheckBox(self.groupBox_4)
        self.chb_ex_veloc_v.setObjectName(u"chb_ex_veloc_v")

        self.gridLayout_4.addWidget(self.chb_ex_veloc_v, 1, 3, 1, 1)

        self.chb_ex_veloc_w = QCheckBox(self.groupBox_4)
        self.chb_ex_veloc_w.setObjectName(u"chb_ex_veloc_w")

        self.gridLayout_4.addWidget(self.chb_ex_veloc_w, 2, 3, 1, 1)


        self.gridLayout_3.addWidget(self.groupBox_4, 2, 0, 1, 1)

        self.le_k = QLineEdit(bordes_window)
        self.le_k.setObjectName(u"le_k")

        self.gridLayout_3.addWidget(self.le_k, 5, 1, 1, 1)

        self.chb_ex_k = QCheckBox(bordes_window)
        self.chb_ex_k.setObjectName(u"chb_ex_k")

        self.gridLayout_3.addWidget(self.chb_ex_k, 6, 1, 1, 1)


        self.retranslateUi(bordes_window)

        QMetaObject.connectSlotsByName(bordes_window)
    # setupUi

    def retranslateUi(self, bordes_window):
        bordes_window.setWindowTitle(QCoreApplication.translate("bordes_window", u"Bordes - PrePRODIC3D", None))
        self.gb_tipo_segment.setTitle(QCoreApplication.translate("bordes_window", u"Tipo de segmento", None))
        self.chb_wall.setText(QCoreApplication.translate("bordes_window", u"Pared", None))
        self.chb_inmass.setText(QCoreApplication.translate("bordes_window", u"Entrada de la masa", None))
        self.chb_outmass.setText(QCoreApplication.translate("bordes_window", u"Salida de la masa", None))
        self.groupBox.setTitle(QCoreApplication.translate("bordes_window", u"Divisi\u00f3n de bordes", None))

        __sortingEnabled = self.lw_bordes.isSortingEnabled()
        self.lw_bordes.setSortingEnabled(False)
        ___qlistwidgetitem = self.lw_bordes.item(0)
        ___qlistwidgetitem.setText(QCoreApplication.translate("bordes_window", u"X Max", None));
        ___qlistwidgetitem1 = self.lw_bordes.item(1)
        ___qlistwidgetitem1.setText(QCoreApplication.translate("bordes_window", u"X Min", None));
        ___qlistwidgetitem2 = self.lw_bordes.item(2)
        ___qlistwidgetitem2.setText(QCoreApplication.translate("bordes_window", u"Y Max", None));
        ___qlistwidgetitem3 = self.lw_bordes.item(3)
        ___qlistwidgetitem3.setText(QCoreApplication.translate("bordes_window", u"Y Min", None));
        ___qlistwidgetitem4 = self.lw_bordes.item(4)
        ___qlistwidgetitem4.setText(QCoreApplication.translate("bordes_window", u"Z Max", None));
        ___qlistwidgetitem5 = self.lw_bordes.item(5)
        ___qlistwidgetitem5.setText(QCoreApplication.translate("bordes_window", u"Z Min", None));
        self.lw_bordes.setSortingEnabled(__sortingEnabled)

        self.label_3.setText(QCoreApplication.translate("bordes_window", u"Segmento", None))
        self.groupBox_2.setTitle("")
        self.label.setText(QCoreApplication.translate("bordes_window", u"Empieza", None))
        self.label_10.setText(QCoreApplication.translate("bordes_window", u"Termina", None))
        self.lb_transversal.setText(QCoreApplication.translate("bordes_window", u"Y", None))
        self.lb_vertical.setText(QCoreApplication.translate("bordes_window", u"Z", None))
        self.chb_exclude_borders.setText(QCoreApplication.translate("bordes_window", u"Bordes", None))
        self.label_2.setText(QCoreApplication.translate("bordes_window", u"Borde", None))
        self.groupBox_7.setTitle("")
        self.pb_addpatch.setText(QCoreApplication.translate("bordes_window", u"Agregar un segmento", None))
        self.pb_rempatch.setText(QCoreApplication.translate("bordes_window", u"Eliminar un segmento", None))

        __sortingEnabled1 = self.lw_patchlist.isSortingEnabled()
        self.lw_patchlist.setSortingEnabled(False)
        ___qlistwidgetitem6 = self.lw_patchlist.item(0)
        ___qlistwidgetitem6.setText(QCoreApplication.translate("bordes_window", u"Borde base", None));
        self.lw_patchlist.setSortingEnabled(__sortingEnabled1)

        self.groupBox_5.setTitle(QCoreApplication.translate("bordes_window", u"Salida de la masa", None))
        self.label_6.setText(QCoreApplication.translate("bordes_window", u"Fracci\u00f3n", None))
        self.label_7.setText(QCoreApplication.translate("bordes_window", u"Conductividad", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("bordes_window", u"Variables escalares", None))
        self.groupBox_6.setTitle("")

        __sortingEnabled2 = self.lw_variables.isSortingEnabled()
        self.lw_variables.setSortingEnabled(False)
        ___qlistwidgetitem7 = self.lw_variables.item(0)
        ___qlistwidgetitem7.setText(QCoreApplication.translate("bordes_window", u"Temperatura", None));
        self.lw_variables.setSortingEnabled(__sortingEnabled2)

        self.gb_chbvalues.setTitle("")
        self.chb_value.setText(QCoreApplication.translate("bordes_window", u"Valor", None))
        self.chb_flux.setText(QCoreApplication.translate("bordes_window", u"Flujo", None))
        self.chb_convec.setText(QCoreApplication.translate("bordes_window", u"Convecci\u00f3n", None))
        self.groupBox_8.setTitle("")
        self.lb_variable.setText(QCoreApplication.translate("bordes_window", u"Temp. ambiente", None))
        self.lb_value.setText(QCoreApplication.translate("bordes_window", u"Valor", None))
#if QT_CONFIG(tooltip)
        self.chb_ex_value.setToolTip(QCoreApplication.translate("bordes_window", u"Hola", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.chb_ex_value.setWhatsThis(QCoreApplication.translate("bordes_window", u"Probando", None))
#endif // QT_CONFIG(whatsthis)
        self.chb_ex_value.setText("")
        self.groupBox_4.setTitle(QCoreApplication.translate("bordes_window", u"Velocidad", None))
        self.label_4.setText(QCoreApplication.translate("bordes_window", u"Velocidad U", None))
        self.label_5.setText(QCoreApplication.translate("bordes_window", u"Velocidad V", None))
        self.label_9.setText(QCoreApplication.translate("bordes_window", u"Velocidad W", None))
        self.chb_ex_veloc_u.setText("")
        self.chb_ex_veloc_v.setText("")
        self.chb_ex_veloc_w.setText("")
        self.le_k.setPlaceholderText("")
        self.chb_ex_k.setText("")
    # retranslateUi

