# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'bordes_windowXJDZWC.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_bordes_window(object):
    def setupUi(self, bordes_window):
        if not bordes_window.objectName():
            bordes_window.setObjectName(u"bordes_window")
        bordes_window.resize(579, 655)
        self.gridLayout_3 = QGridLayout(bordes_window)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
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
        self.le_value = QLineEdit(self.groupBox_8)
        self.le_value.setObjectName(u"le_value")

        self.gridLayout_6.addWidget(self.le_value, 3, 0, 1, 1)

        self.lb_value = QLabel(self.groupBox_8)
        self.lb_value.setObjectName(u"lb_value")

        self.gridLayout_6.addWidget(self.lb_value, 0, 0, 1, 1)

        self.lb_variable = QLabel(self.groupBox_8)
        self.lb_variable.setObjectName(u"lb_variable")

        self.gridLayout_6.addWidget(self.lb_variable, 5, 0, 1, 1)

        self.chb_ex_value = QCheckBox(self.groupBox_8)
        self.chb_ex_value.setObjectName(u"chb_ex_value")
#if QT_CONFIG(whatsthis)
        self.chb_ex_value.setWhatsThis(u"Activa esta opci\u00f3n para iterar este valor en la posici\u00f3n vecina del borde seleccionado en vez de iterar en el borde mismo.")
#endif // QT_CONFIG(whatsthis)

        self.gridLayout_6.addWidget(self.chb_ex_value, 3, 1, 1, 1)

        self.le_tempamb = QLineEdit(self.groupBox_8)
        self.le_tempamb.setObjectName(u"le_tempamb")
        self.le_tempamb.setEnabled(False)

        self.gridLayout_6.addWidget(self.le_tempamb, 6, 0, 1, 1)


        self.horizontalLayout.addWidget(self.groupBox_8)

        self.groupBox_9 = QGroupBox(self.groupBox_3)
        self.groupBox_9.setObjectName(u"groupBox_9")
        self.groupBox_9.setAlignment(Qt.AlignCenter)
        self.formLayout = QFormLayout(self.groupBox_9)
        self.formLayout.setObjectName(u"formLayout")
        self.label = QLabel(self.groupBox_9)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)

        self.chb_ex_k = QCheckBox(self.groupBox_9)
        self.chb_ex_k.setObjectName(u"chb_ex_k")
#if QT_CONFIG(whatsthis)
        self.chb_ex_k.setWhatsThis(u"Activa esta opci\u00f3n para iterar este valor en la posici\u00f3n vecina del borde seleccionado en vez de iterar en el borde mismo.")
#endif // QT_CONFIG(whatsthis)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.chb_ex_k)

        self.label_6 = QLabel(self.groupBox_9)
        self.label_6.setObjectName(u"label_6")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_6)

        self.le_fracmass = QLineEdit(self.groupBox_9)
        self.le_fracmass.setObjectName(u"le_fracmass")
        self.le_fracmass.setEnabled(False)
        self.le_fracmass.setAlignment(Qt.AlignCenter)

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.le_fracmass)

        self.le_k = QLineEdit(self.groupBox_9)
        self.le_k.setObjectName(u"le_k")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.le_k)


        self.horizontalLayout.addWidget(self.groupBox_9)


        self.gridLayout_3.addWidget(self.groupBox_3, 1, 0, 1, 4)

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


        self.gridLayout_3.addWidget(self.gb_tipo_segment, 0, 3, 1, 1)

        self.groupBox = QGroupBox(bordes_window)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout = QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(u"gridLayout")
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


        self.gridLayout.addWidget(self.groupBox_7, 5, 0, 1, 4)

        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 3, 0, 1, 2)

        self.chb_exclude_borders = QCheckBox(self.groupBox)
        self.chb_exclude_borders.setObjectName(u"chb_exclude_borders")

        self.gridLayout.addWidget(self.chb_exclude_borders, 0, 0, 1, 1)

        self.groupBox_2 = QGroupBox(self.groupBox)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.gridLayout_5 = QGridLayout(self.groupBox_2)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.le_vertical_end = QLineEdit(self.groupBox_2)
        self.le_vertical_end.setObjectName(u"le_vertical_end")

        self.gridLayout_5.addWidget(self.le_vertical_end, 4, 5, 1, 1)

        self.cb_ex_vertical_end = QComboBox(self.groupBox_2)
        self.cb_ex_vertical_end.addItem("")
        self.cb_ex_vertical_end.addItem("")
        self.cb_ex_vertical_end.addItem("")
        self.cb_ex_vertical_end.setObjectName(u"cb_ex_vertical_end")

        self.gridLayout_5.addWidget(self.cb_ex_vertical_end, 4, 4, 1, 1)

        self.cb_ex_vertical_start = QComboBox(self.groupBox_2)
        self.cb_ex_vertical_start.addItem("")
        self.cb_ex_vertical_start.addItem("")
        self.cb_ex_vertical_start.addItem("")
        self.cb_ex_vertical_start.setObjectName(u"cb_ex_vertical_start")

        self.gridLayout_5.addWidget(self.cb_ex_vertical_start, 2, 4, 1, 1)

        self.lb_transversal = QLabel(self.groupBox_2)
        self.lb_transversal.setObjectName(u"lb_transversal")
        self.lb_transversal.setLayoutDirection(Qt.LeftToRight)
        self.lb_transversal.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.lb_transversal, 0, 2, 1, 1)

        self.cb_ex_transversal_start = QComboBox(self.groupBox_2)
        self.cb_ex_transversal_start.addItem("")
        self.cb_ex_transversal_start.addItem("")
        self.cb_ex_transversal_start.addItem("")
        self.cb_ex_transversal_start.setObjectName(u"cb_ex_transversal_start")

        self.gridLayout_5.addWidget(self.cb_ex_transversal_start, 2, 1, 1, 1)

        self.cb_ex_transversal_end = QComboBox(self.groupBox_2)
        self.cb_ex_transversal_end.addItem("")
        self.cb_ex_transversal_end.addItem("")
        self.cb_ex_transversal_end.addItem("")
        self.cb_ex_transversal_end.setObjectName(u"cb_ex_transversal_end")

        self.gridLayout_5.addWidget(self.cb_ex_transversal_end, 4, 1, 1, 1)

        self.lb_vertical = QLabel(self.groupBox_2)
        self.lb_vertical.setObjectName(u"lb_vertical")
        self.lb_vertical.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.lb_vertical, 0, 5, 1, 1)

        self.le_transversal_start = QLineEdit(self.groupBox_2)
        self.le_transversal_start.setObjectName(u"le_transversal_start")

        self.gridLayout_5.addWidget(self.le_transversal_start, 2, 2, 1, 1)

        self.le_vertical_start = QLineEdit(self.groupBox_2)
        self.le_vertical_start.setObjectName(u"le_vertical_start")

        self.gridLayout_5.addWidget(self.le_vertical_start, 2, 5, 1, 1)

        self.le_transversal_end = QLineEdit(self.groupBox_2)
        self.le_transversal_end.setObjectName(u"le_transversal_end")

        self.gridLayout_5.addWidget(self.le_transversal_end, 4, 2, 1, 1)


        self.gridLayout.addWidget(self.groupBox_2, 1, 0, 1, 4)

        self.lw_bordes = QListWidget(self.groupBox)
        QListWidgetItem(self.lw_bordes)
        QListWidgetItem(self.lw_bordes)
        QListWidgetItem(self.lw_bordes)
        QListWidgetItem(self.lw_bordes)
        QListWidgetItem(self.lw_bordes)
        QListWidgetItem(self.lw_bordes)
        self.lw_bordes.setObjectName(u"lw_bordes")

        self.gridLayout.addWidget(self.lw_bordes, 4, 0, 1, 3)

        self.lw_patchlist = QListWidget(self.groupBox)
        QListWidgetItem(self.lw_patchlist)
        self.lw_patchlist.setObjectName(u"lw_patchlist")

        self.gridLayout.addWidget(self.lw_patchlist, 4, 3, 1, 1)

        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 3, 3, 1, 1)


        self.gridLayout_3.addWidget(self.groupBox, 0, 0, 1, 3)


        self.retranslateUi(bordes_window)

        QMetaObject.connectSlotsByName(bordes_window)
    # setupUi

    def retranslateUi(self, bordes_window):
        bordes_window.setWindowTitle(QCoreApplication.translate("bordes_window", u"Bordes - PrePRODIC3D", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("bordes_window", u"Variables", None))
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
        self.lb_value.setText(QCoreApplication.translate("bordes_window", u"Valor", None))
        self.lb_variable.setText(QCoreApplication.translate("bordes_window", u"Temp. ambiente", None))
#if QT_CONFIG(tooltip)
        self.chb_ex_value.setToolTip(QCoreApplication.translate("bordes_window", u"<html><head/><body><p>Activa esta opci\u00f3n para iterar este<br/>valor en la posici\u00f3n vecina del borde<br/>seleccionado en vez de iterar en el<br/>borde mismo.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.chb_ex_value.setText("")
        self.groupBox_9.setTitle("")
        self.label.setText(QCoreApplication.translate("bordes_window", u"Conductividad", None))
#if QT_CONFIG(tooltip)
        self.chb_ex_k.setToolTip(QCoreApplication.translate("bordes_window", u"<html><head/><body><p>Activa esta opci\u00f3n para iterar este<br/>valor en la posici\u00f3n vecina del borde<br/>seleccionado en vez de iterar en el<br/>borde mismo.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.chb_ex_k.setText("")
        self.label_6.setText(QCoreApplication.translate("bordes_window", u"Fracci\u00f3n m\u00e1sica", None))
        self.le_fracmass.setText(QCoreApplication.translate("bordes_window", u"1", None))
        self.le_k.setPlaceholderText("")
        self.gb_tipo_segment.setTitle(QCoreApplication.translate("bordes_window", u"Tipo de segmento", None))
        self.chb_wall.setText(QCoreApplication.translate("bordes_window", u"Pared", None))
        self.chb_inmass.setText(QCoreApplication.translate("bordes_window", u"Entrada de la masa", None))
        self.chb_outmass.setText(QCoreApplication.translate("bordes_window", u"Salida de la masa", None))
        self.groupBox.setTitle(QCoreApplication.translate("bordes_window", u"Divisi\u00f3n de bordes", None))
        self.groupBox_7.setTitle("")
        self.pb_addpatch.setText(QCoreApplication.translate("bordes_window", u"Agregar un segmento", None))
        self.pb_rempatch.setText(QCoreApplication.translate("bordes_window", u"Eliminar un segmento", None))
        self.label_2.setText(QCoreApplication.translate("bordes_window", u"Borde", None))
#if QT_CONFIG(tooltip)
        self.chb_exclude_borders.setToolTip(QCoreApplication.translate("bordes_window", u"<html><head/><body><p>Activa esta opci\u00f3n para excluir<br/>los bordes inicial y final del dominio<br/>para cada iteraci\u00f3n en el parche<br/>seleccionado, independientemente<br/>de las limitantes por coordenadas.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.chb_exclude_borders.setWhatsThis(QCoreApplication.translate("bordes_window", u"Activa esta opci\u00f3n para excluir los bordes inicial y final del dominio para cada iteraci\u00f3n en el parche seleccionado, independientemente de las limitantes por coordenadas.", None))
#endif // QT_CONFIG(whatsthis)
        self.chb_exclude_borders.setText(QCoreApplication.translate("bordes_window", u"V.C. Excluir bordes", None))
        self.groupBox_2.setTitle("")
        self.cb_ex_vertical_end.setItemText(0, "")
        self.cb_ex_vertical_end.setItemText(1, QCoreApplication.translate("bordes_window", u"<", None))
        self.cb_ex_vertical_end.setItemText(2, QCoreApplication.translate("bordes_window", u"\u2264", None))

        self.cb_ex_vertical_start.setItemText(0, "")
        self.cb_ex_vertical_start.setItemText(1, QCoreApplication.translate("bordes_window", u">", None))
        self.cb_ex_vertical_start.setItemText(2, QCoreApplication.translate("bordes_window", u"\u2265", None))

        self.lb_transversal.setText(QCoreApplication.translate("bordes_window", u"Y", None))
        self.cb_ex_transversal_start.setItemText(0, "")
        self.cb_ex_transversal_start.setItemText(1, QCoreApplication.translate("bordes_window", u">", None))
        self.cb_ex_transversal_start.setItemText(2, QCoreApplication.translate("bordes_window", u"\u2265", None))

        self.cb_ex_transversal_end.setItemText(0, "")
        self.cb_ex_transversal_end.setItemText(1, QCoreApplication.translate("bordes_window", u"<", None))
        self.cb_ex_transversal_end.setItemText(2, QCoreApplication.translate("bordes_window", u"\u2264", None))

        self.lb_vertical.setText(QCoreApplication.translate("bordes_window", u"Z", None))

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


        __sortingEnabled2 = self.lw_patchlist.isSortingEnabled()
        self.lw_patchlist.setSortingEnabled(False)
        ___qlistwidgetitem7 = self.lw_patchlist.item(0)
        ___qlistwidgetitem7.setText(QCoreApplication.translate("bordes_window", u"Borde base", None));
        self.lw_patchlist.setSortingEnabled(__sortingEnabled2)

        self.label_3.setText(QCoreApplication.translate("bordes_window", u"Segmento", None))
    # retranslateUi

