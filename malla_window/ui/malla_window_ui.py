# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'malla_windowsEfKoM.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFormLayout, QGridLayout,
    QGroupBox, QHBoxLayout, QLabel, QLineEdit,
    QSizePolicy, QSpinBox, QStackedWidget, QVBoxLayout,
    QWidget)

class Ui_malla_window(object):
    def setupUi(self, malla_window):
        if not malla_window.objectName():
            malla_window.setObjectName(u"malla_window")
        malla_window.resize(861, 584)
        self.verticalLayout = QVBoxLayout(malla_window)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gb_malla = QGroupBox(malla_window)
        self.gb_malla.setObjectName(u"gb_malla")
        self.formLayout = QFormLayout(self.gb_malla)
        self.formLayout.setObjectName(u"formLayout")
        self.lb_tipocoord = QLabel(self.gb_malla)
        self.lb_tipocoord.setObjectName(u"lb_tipocoord")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.lb_tipocoord)

        self.cb_coord_type = QComboBox(self.gb_malla)
        self.cb_coord_type.addItem("")
        self.cb_coord_type.addItem("")
        self.cb_coord_type.setObjectName(u"cb_coord_type")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.cb_coord_type)

        self.lb_tipozonas = QLabel(self.gb_malla)
        self.lb_tipozonas.setObjectName(u"lb_tipozonas")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.lb_tipozonas)

        self.cb_zone_type = QComboBox(self.gb_malla)
        self.cb_zone_type.addItem("")
        self.cb_zone_type.addItem("")
        self.cb_zone_type.setObjectName(u"cb_zone_type")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.cb_zone_type)

        self.label = QLabel(self.gb_malla)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label)

        self.cb_system_type = QComboBox(self.gb_malla)
        self.cb_system_type.addItem("")
        self.cb_system_type.addItem("")
        self.cb_system_type.setObjectName(u"cb_system_type")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.cb_system_type)


        self.verticalLayout.addWidget(self.gb_malla)

        self.gbsw_malla = QStackedWidget(malla_window)
        self.gbsw_malla.setObjectName(u"gbsw_malla")
        self.gbsw_cart_zu = QWidget()
        self.gbsw_cart_zu.setObjectName(u"gbsw_cart_zu")
        self.horizontalLayout = QHBoxLayout(self.gbsw_cart_zu)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.gb_malla2_dirx = QGroupBox(self.gbsw_cart_zu)
        self.gb_malla2_dirx.setObjectName(u"gb_malla2_dirx")
        self.formLayout_2 = QFormLayout(self.gb_malla2_dirx)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.lb_xlon = QLabel(self.gb_malla2_dirx)
        self.lb_xlon.setObjectName(u"lb_xlon")

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.lb_xlon)

        self.le_xlon = QLineEdit(self.gb_malla2_dirx)
        self.le_xlon.setObjectName(u"le_xlon")

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.le_xlon)

        self.lb_nvcx = QLabel(self.gb_malla2_dirx)
        self.lb_nvcx.setObjectName(u"lb_nvcx")

        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.lb_nvcx)

        self.le_nvcx = QLineEdit(self.gb_malla2_dirx)
        self.le_nvcx.setObjectName(u"le_nvcx")

        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.le_nvcx)

        self.lb_potenciax = QLabel(self.gb_malla2_dirx)
        self.lb_potenciax.setObjectName(u"lb_potenciax")

        self.formLayout_2.setWidget(2, QFormLayout.LabelRole, self.lb_potenciax)

        self.le_potenciax = QLineEdit(self.gb_malla2_dirx)
        self.le_potenciax.setObjectName(u"le_potenciax")

        self.formLayout_2.setWidget(2, QFormLayout.FieldRole, self.le_potenciax)


        self.horizontalLayout.addWidget(self.gb_malla2_dirx)

        self.gb_malla2_diry = QGroupBox(self.gbsw_cart_zu)
        self.gb_malla2_diry.setObjectName(u"gb_malla2_diry")
        self.formLayout_3 = QFormLayout(self.gb_malla2_diry)
        self.formLayout_3.setObjectName(u"formLayout_3")
        self.lb_ylon = QLabel(self.gb_malla2_diry)
        self.lb_ylon.setObjectName(u"lb_ylon")

        self.formLayout_3.setWidget(0, QFormLayout.LabelRole, self.lb_ylon)

        self.le_ylon = QLineEdit(self.gb_malla2_diry)
        self.le_ylon.setObjectName(u"le_ylon")

        self.formLayout_3.setWidget(0, QFormLayout.FieldRole, self.le_ylon)

        self.lb_nvcy = QLabel(self.gb_malla2_diry)
        self.lb_nvcy.setObjectName(u"lb_nvcy")

        self.formLayout_3.setWidget(1, QFormLayout.LabelRole, self.lb_nvcy)

        self.le_nvcy = QLineEdit(self.gb_malla2_diry)
        self.le_nvcy.setObjectName(u"le_nvcy")

        self.formLayout_3.setWidget(1, QFormLayout.FieldRole, self.le_nvcy)

        self.lb_potenciay = QLabel(self.gb_malla2_diry)
        self.lb_potenciay.setObjectName(u"lb_potenciay")

        self.formLayout_3.setWidget(2, QFormLayout.LabelRole, self.lb_potenciay)

        self.le_potenciay = QLineEdit(self.gb_malla2_diry)
        self.le_potenciay.setObjectName(u"le_potenciay")

        self.formLayout_3.setWidget(2, QFormLayout.FieldRole, self.le_potenciay)


        self.horizontalLayout.addWidget(self.gb_malla2_diry)

        self.gb_malla2_dirz = QGroupBox(self.gbsw_cart_zu)
        self.gb_malla2_dirz.setObjectName(u"gb_malla2_dirz")
        self.formLayout_4 = QFormLayout(self.gb_malla2_dirz)
        self.formLayout_4.setObjectName(u"formLayout_4")
        self.lb_zlon = QLabel(self.gb_malla2_dirz)
        self.lb_zlon.setObjectName(u"lb_zlon")

        self.formLayout_4.setWidget(0, QFormLayout.LabelRole, self.lb_zlon)

        self.le_zlon = QLineEdit(self.gb_malla2_dirz)
        self.le_zlon.setObjectName(u"le_zlon")

        self.formLayout_4.setWidget(0, QFormLayout.FieldRole, self.le_zlon)

        self.lb_nvcz = QLabel(self.gb_malla2_dirz)
        self.lb_nvcz.setObjectName(u"lb_nvcz")

        self.formLayout_4.setWidget(1, QFormLayout.LabelRole, self.lb_nvcz)

        self.le_nvcz = QLineEdit(self.gb_malla2_dirz)
        self.le_nvcz.setObjectName(u"le_nvcz")

        self.formLayout_4.setWidget(1, QFormLayout.FieldRole, self.le_nvcz)

        self.lb_potenciaz = QLabel(self.gb_malla2_dirz)
        self.lb_potenciaz.setObjectName(u"lb_potenciaz")

        self.formLayout_4.setWidget(2, QFormLayout.LabelRole, self.lb_potenciaz)

        self.le_potenciaz = QLineEdit(self.gb_malla2_dirz)
        self.le_potenciaz.setObjectName(u"le_potenciaz")

        self.formLayout_4.setWidget(2, QFormLayout.FieldRole, self.le_potenciaz)


        self.horizontalLayout.addWidget(self.gb_malla2_dirz)

        self.gbsw_malla.addWidget(self.gbsw_cart_zu)
        self.gbsw_cil_zu = QWidget()
        self.gbsw_cil_zu.setObjectName(u"gbsw_cil_zu")
        self.horizontalLayout_2 = QHBoxLayout(self.gbsw_cil_zu)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.gb_dirtita = QGroupBox(self.gbsw_cil_zu)
        self.gb_dirtita.setObjectName(u"gb_dirtita")
        self.formLayout_7 = QFormLayout(self.gb_dirtita)
        self.formLayout_7.setObjectName(u"formLayout_7")
        self.lb_titalon = QLabel(self.gb_dirtita)
        self.lb_titalon.setObjectName(u"lb_titalon")

        self.formLayout_7.setWidget(0, QFormLayout.LabelRole, self.lb_titalon)

        self.le_titalon = QLineEdit(self.gb_dirtita)
        self.le_titalon.setObjectName(u"le_titalon")

        self.formLayout_7.setWidget(0, QFormLayout.FieldRole, self.le_titalon)

        self.lb_nvctita = QLabel(self.gb_dirtita)
        self.lb_nvctita.setObjectName(u"lb_nvctita")

        self.formLayout_7.setWidget(1, QFormLayout.LabelRole, self.lb_nvctita)

        self.le_nvctita = QLineEdit(self.gb_dirtita)
        self.le_nvctita.setObjectName(u"le_nvctita")

        self.formLayout_7.setWidget(1, QFormLayout.FieldRole, self.le_nvctita)

        self.lb_potenciatita = QLabel(self.gb_dirtita)
        self.lb_potenciatita.setObjectName(u"lb_potenciatita")

        self.formLayout_7.setWidget(2, QFormLayout.LabelRole, self.lb_potenciatita)

        self.le_potenciatita = QLineEdit(self.gb_dirtita)
        self.le_potenciatita.setObjectName(u"le_potenciatita")

        self.formLayout_7.setWidget(2, QFormLayout.FieldRole, self.le_potenciatita)


        self.horizontalLayout_2.addWidget(self.gb_dirtita)

        self.gb_dirr = QGroupBox(self.gbsw_cil_zu)
        self.gb_dirr.setObjectName(u"gb_dirr")
        self.formLayout_6 = QFormLayout(self.gb_dirr)
        self.formLayout_6.setObjectName(u"formLayout_6")
        self.lb_rlon = QLabel(self.gb_dirr)
        self.lb_rlon.setObjectName(u"lb_rlon")

        self.formLayout_6.setWidget(1, QFormLayout.LabelRole, self.lb_rlon)

        self.le_rlon = QLineEdit(self.gb_dirr)
        self.le_rlon.setObjectName(u"le_rlon")

        self.formLayout_6.setWidget(1, QFormLayout.FieldRole, self.le_rlon)

        self.lb_nvcr = QLabel(self.gb_dirr)
        self.lb_nvcr.setObjectName(u"lb_nvcr")

        self.formLayout_6.setWidget(2, QFormLayout.LabelRole, self.lb_nvcr)

        self.le_nvcr = QLineEdit(self.gb_dirr)
        self.le_nvcr.setObjectName(u"le_nvcr")

        self.formLayout_6.setWidget(2, QFormLayout.FieldRole, self.le_nvcr)

        self.lb_potenciar = QLabel(self.gb_dirr)
        self.lb_potenciar.setObjectName(u"lb_potenciar")

        self.formLayout_6.setWidget(3, QFormLayout.LabelRole, self.lb_potenciar)

        self.le_potenciar = QLineEdit(self.gb_dirr)
        self.le_potenciar.setObjectName(u"le_potenciar")

        self.formLayout_6.setWidget(3, QFormLayout.FieldRole, self.le_potenciar)

        self.lb_rini = QLabel(self.gb_dirr)
        self.lb_rini.setObjectName(u"lb_rini")

        self.formLayout_6.setWidget(0, QFormLayout.LabelRole, self.lb_rini)

        self.le_rini = QLineEdit(self.gb_dirr)
        self.le_rini.setObjectName(u"le_rini")

        self.formLayout_6.setWidget(0, QFormLayout.FieldRole, self.le_rini)


        self.horizontalLayout_2.addWidget(self.gb_dirr)

        self.gb_dirz = QGroupBox(self.gbsw_cil_zu)
        self.gb_dirz.setObjectName(u"gb_dirz")
        self.formLayout_5 = QFormLayout(self.gb_dirz)
        self.formLayout_5.setObjectName(u"formLayout_5")
        self.lb_zloncil = QLabel(self.gb_dirz)
        self.lb_zloncil.setObjectName(u"lb_zloncil")

        self.formLayout_5.setWidget(0, QFormLayout.LabelRole, self.lb_zloncil)

        self.le_zloncil = QLineEdit(self.gb_dirz)
        self.le_zloncil.setObjectName(u"le_zloncil")

        self.formLayout_5.setWidget(0, QFormLayout.FieldRole, self.le_zloncil)

        self.lb_nvczcil = QLabel(self.gb_dirz)
        self.lb_nvczcil.setObjectName(u"lb_nvczcil")

        self.formLayout_5.setWidget(1, QFormLayout.LabelRole, self.lb_nvczcil)

        self.le_nvczcil = QLineEdit(self.gb_dirz)
        self.le_nvczcil.setObjectName(u"le_nvczcil")

        self.formLayout_5.setWidget(1, QFormLayout.FieldRole, self.le_nvczcil)

        self.lb_potenciazcil = QLabel(self.gb_dirz)
        self.lb_potenciazcil.setObjectName(u"lb_potenciazcil")

        self.formLayout_5.setWidget(2, QFormLayout.LabelRole, self.lb_potenciazcil)

        self.le_potenciazcil = QLineEdit(self.gb_dirz)
        self.le_potenciazcil.setObjectName(u"le_potenciazcil")

        self.formLayout_5.setWidget(2, QFormLayout.FieldRole, self.le_potenciazcil)


        self.horizontalLayout_2.addWidget(self.gb_dirz)

        self.gbsw_malla.addWidget(self.gbsw_cil_zu)
        self.gbsw_cart_vz = QWidget()
        self.gbsw_cart_vz.setObjectName(u"gbsw_cart_vz")
        self.horizontalLayout_3 = QHBoxLayout(self.gbsw_cart_vz)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.gb_dirx_vz = QGroupBox(self.gbsw_cart_vz)
        self.gb_dirx_vz.setObjectName(u"gb_dirx_vz")
        self.verticalLayout_2 = QVBoxLayout(self.gb_dirx_vz)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.gb_dirx_vz1 = QGroupBox(self.gb_dirx_vz)
        self.gb_dirx_vz1.setObjectName(u"gb_dirx_vz1")
        self.horizontalLayout_5 = QHBoxLayout(self.gb_dirx_vz1)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.lb_dirx_numz = QLabel(self.gb_dirx_vz1)
        self.lb_dirx_numz.setObjectName(u"lb_dirx_numz")

        self.horizontalLayout_5.addWidget(self.lb_dirx_numz)

        self.sb_dirx_numz = QSpinBox(self.gb_dirx_vz1)
        self.sb_dirx_numz.setObjectName(u"sb_dirx_numz")
        self.sb_dirx_numz.setMinimum(1)
        self.sb_dirx_numz.setMaximum(10)
        self.sb_dirx_numz.setValue(1)

        self.horizontalLayout_5.addWidget(self.sb_dirx_numz)


        self.verticalLayout_2.addWidget(self.gb_dirx_vz1)

        self.gb_dirx_vz2 = QGroupBox(self.gb_dirx_vz)
        self.gb_dirx_vz2.setObjectName(u"gb_dirx_vz2")
        self.gridLayout = QGridLayout(self.gb_dirx_vz2)
        self.gridLayout.setObjectName(u"gridLayout")
        self.lb_dirx_zon8 = QLabel(self.gb_dirx_vz2)
        self.lb_dirx_zon8.setObjectName(u"lb_dirx_zon8")
        self.lb_dirx_zon8.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.lb_dirx_zon8, 8, 0, 1, 1)

        self.le_dirx_lon_zon4 = QLineEdit(self.gb_dirx_vz2)
        self.le_dirx_lon_zon4.setObjectName(u"le_dirx_lon_zon4")
        self.le_dirx_lon_zon4.setEnabled(False)
        self.le_dirx_lon_zon4.setMaxLength(32768)
        self.le_dirx_lon_zon4.setAlignment(Qt.AlignCenter)
        self.le_dirx_lon_zon4.setDragEnabled(False)

        self.gridLayout.addWidget(self.le_dirx_lon_zon4, 4, 1, 1, 1)

        self.le_dirx_nvcx_zon9 = QLineEdit(self.gb_dirx_vz2)
        self.le_dirx_nvcx_zon9.setObjectName(u"le_dirx_nvcx_zon9")
        self.le_dirx_nvcx_zon9.setEnabled(False)
        self.le_dirx_nvcx_zon9.setMaxLength(32768)
        self.le_dirx_nvcx_zon9.setAlignment(Qt.AlignCenter)
        self.le_dirx_nvcx_zon9.setDragEnabled(False)

        self.gridLayout.addWidget(self.le_dirx_nvcx_zon9, 9, 2, 1, 1)

        self.lb_dirx_poten = QLabel(self.gb_dirx_vz2)
        self.lb_dirx_poten.setObjectName(u"lb_dirx_poten")
        self.lb_dirx_poten.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.lb_dirx_poten, 0, 3, 1, 1)

        self.le_dirx_nvcx_zon2 = QLineEdit(self.gb_dirx_vz2)
        self.le_dirx_nvcx_zon2.setObjectName(u"le_dirx_nvcx_zon2")
        self.le_dirx_nvcx_zon2.setEnabled(False)
        self.le_dirx_nvcx_zon2.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.le_dirx_nvcx_zon2, 2, 2, 1, 1)

        self.le_dirx_poten_zon2 = QLineEdit(self.gb_dirx_vz2)
        self.le_dirx_poten_zon2.setObjectName(u"le_dirx_poten_zon2")
        self.le_dirx_poten_zon2.setEnabled(False)
        self.le_dirx_poten_zon2.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.le_dirx_poten_zon2, 2, 3, 1, 1)

        self.le_dirx_nvcx_zon4 = QLineEdit(self.gb_dirx_vz2)
        self.le_dirx_nvcx_zon4.setObjectName(u"le_dirx_nvcx_zon4")
        self.le_dirx_nvcx_zon4.setEnabled(False)
        self.le_dirx_nvcx_zon4.setMaxLength(32768)
        self.le_dirx_nvcx_zon4.setAlignment(Qt.AlignCenter)
        self.le_dirx_nvcx_zon4.setDragEnabled(False)

        self.gridLayout.addWidget(self.le_dirx_nvcx_zon4, 4, 2, 1, 1)

        self.lb_dirx_zon5 = QLabel(self.gb_dirx_vz2)
        self.lb_dirx_zon5.setObjectName(u"lb_dirx_zon5")
        self.lb_dirx_zon5.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.lb_dirx_zon5, 5, 0, 1, 1)

        self.le_dirx_nvcx_zon5 = QLineEdit(self.gb_dirx_vz2)
        self.le_dirx_nvcx_zon5.setObjectName(u"le_dirx_nvcx_zon5")
        self.le_dirx_nvcx_zon5.setEnabled(False)
        self.le_dirx_nvcx_zon5.setMaxLength(32768)
        self.le_dirx_nvcx_zon5.setAlignment(Qt.AlignCenter)
        self.le_dirx_nvcx_zon5.setDragEnabled(False)

        self.gridLayout.addWidget(self.le_dirx_nvcx_zon5, 5, 2, 1, 1)

        self.le_dirx_lon_zon2 = QLineEdit(self.gb_dirx_vz2)
        self.le_dirx_lon_zon2.setObjectName(u"le_dirx_lon_zon2")
        self.le_dirx_lon_zon2.setEnabled(False)
        self.le_dirx_lon_zon2.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.le_dirx_lon_zon2, 2, 1, 1, 1)

        self.le_dirx_poten_zon4 = QLineEdit(self.gb_dirx_vz2)
        self.le_dirx_poten_zon4.setObjectName(u"le_dirx_poten_zon4")
        self.le_dirx_poten_zon4.setEnabled(False)
        self.le_dirx_poten_zon4.setMaxLength(32768)
        self.le_dirx_poten_zon4.setAlignment(Qt.AlignCenter)
        self.le_dirx_poten_zon4.setDragEnabled(False)

        self.gridLayout.addWidget(self.le_dirx_poten_zon4, 4, 3, 1, 1)

        self.le_dirx_poten_zon5 = QLineEdit(self.gb_dirx_vz2)
        self.le_dirx_poten_zon5.setObjectName(u"le_dirx_poten_zon5")
        self.le_dirx_poten_zon5.setEnabled(False)
        self.le_dirx_poten_zon5.setMaxLength(32768)
        self.le_dirx_poten_zon5.setAlignment(Qt.AlignCenter)
        self.le_dirx_poten_zon5.setDragEnabled(False)

        self.gridLayout.addWidget(self.le_dirx_poten_zon5, 5, 3, 1, 1)

        self.le_dirx_nvcx_zon1 = QLineEdit(self.gb_dirx_vz2)
        self.le_dirx_nvcx_zon1.setObjectName(u"le_dirx_nvcx_zon1")
        self.le_dirx_nvcx_zon1.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.le_dirx_nvcx_zon1, 1, 2, 1, 1)

        self.lb_dirx_zon9 = QLabel(self.gb_dirx_vz2)
        self.lb_dirx_zon9.setObjectName(u"lb_dirx_zon9")
        self.lb_dirx_zon9.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.lb_dirx_zon9, 9, 0, 1, 1)

        self.lb_dirx_zon4 = QLabel(self.gb_dirx_vz2)
        self.lb_dirx_zon4.setObjectName(u"lb_dirx_zon4")
        self.lb_dirx_zon4.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.lb_dirx_zon4, 4, 0, 1, 1)

        self.le_dirx_lon_zon7 = QLineEdit(self.gb_dirx_vz2)
        self.le_dirx_lon_zon7.setObjectName(u"le_dirx_lon_zon7")
        self.le_dirx_lon_zon7.setEnabled(False)
        self.le_dirx_lon_zon7.setMaxLength(32768)
        self.le_dirx_lon_zon7.setAlignment(Qt.AlignCenter)
        self.le_dirx_lon_zon7.setDragEnabled(False)

        self.gridLayout.addWidget(self.le_dirx_lon_zon7, 7, 1, 1, 1)

        self.le_dirx_poten_zon7 = QLineEdit(self.gb_dirx_vz2)
        self.le_dirx_poten_zon7.setObjectName(u"le_dirx_poten_zon7")
        self.le_dirx_poten_zon7.setEnabled(False)
        self.le_dirx_poten_zon7.setMaxLength(32768)
        self.le_dirx_poten_zon7.setAlignment(Qt.AlignCenter)
        self.le_dirx_poten_zon7.setDragEnabled(False)

        self.gridLayout.addWidget(self.le_dirx_poten_zon7, 7, 3, 1, 1)

        self.le_dirx_poten_zon8 = QLineEdit(self.gb_dirx_vz2)
        self.le_dirx_poten_zon8.setObjectName(u"le_dirx_poten_zon8")
        self.le_dirx_poten_zon8.setEnabled(False)
        self.le_dirx_poten_zon8.setMaxLength(32768)
        self.le_dirx_poten_zon8.setAlignment(Qt.AlignCenter)
        self.le_dirx_poten_zon8.setDragEnabled(False)

        self.gridLayout.addWidget(self.le_dirx_poten_zon8, 8, 3, 1, 1)

        self.le_dirx_nvcx_zon8 = QLineEdit(self.gb_dirx_vz2)
        self.le_dirx_nvcx_zon8.setObjectName(u"le_dirx_nvcx_zon8")
        self.le_dirx_nvcx_zon8.setEnabled(False)
        self.le_dirx_nvcx_zon8.setMaxLength(32768)
        self.le_dirx_nvcx_zon8.setAlignment(Qt.AlignCenter)
        self.le_dirx_nvcx_zon8.setDragEnabled(False)

        self.gridLayout.addWidget(self.le_dirx_nvcx_zon8, 8, 2, 1, 1)

        self.le_dirx_lon_zon6 = QLineEdit(self.gb_dirx_vz2)
        self.le_dirx_lon_zon6.setObjectName(u"le_dirx_lon_zon6")
        self.le_dirx_lon_zon6.setEnabled(False)
        self.le_dirx_lon_zon6.setMaxLength(32768)
        self.le_dirx_lon_zon6.setAlignment(Qt.AlignCenter)
        self.le_dirx_lon_zon6.setDragEnabled(False)

        self.gridLayout.addWidget(self.le_dirx_lon_zon6, 6, 1, 1, 1)

        self.lb_dirx_zon1 = QLabel(self.gb_dirx_vz2)
        self.lb_dirx_zon1.setObjectName(u"lb_dirx_zon1")
        self.lb_dirx_zon1.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.lb_dirx_zon1, 1, 0, 1, 1)

        self.lb_dirx_zon3 = QLabel(self.gb_dirx_vz2)
        self.lb_dirx_zon3.setObjectName(u"lb_dirx_zon3")
        self.lb_dirx_zon3.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.lb_dirx_zon3, 3, 0, 1, 1)

        self.le_dirx_nvcx_zon3 = QLineEdit(self.gb_dirx_vz2)
        self.le_dirx_nvcx_zon3.setObjectName(u"le_dirx_nvcx_zon3")
        self.le_dirx_nvcx_zon3.setEnabled(False)
        self.le_dirx_nvcx_zon3.setMaxLength(32768)
        self.le_dirx_nvcx_zon3.setAlignment(Qt.AlignCenter)
        self.le_dirx_nvcx_zon3.setDragEnabled(False)

        self.gridLayout.addWidget(self.le_dirx_nvcx_zon3, 3, 2, 1, 1)

        self.le_dirx_lon_zon5 = QLineEdit(self.gb_dirx_vz2)
        self.le_dirx_lon_zon5.setObjectName(u"le_dirx_lon_zon5")
        self.le_dirx_lon_zon5.setEnabled(False)
        self.le_dirx_lon_zon5.setMaxLength(32768)
        self.le_dirx_lon_zon5.setAlignment(Qt.AlignCenter)
        self.le_dirx_lon_zon5.setDragEnabled(False)

        self.gridLayout.addWidget(self.le_dirx_lon_zon5, 5, 1, 1, 1)

        self.le_dirx_poten_zon6 = QLineEdit(self.gb_dirx_vz2)
        self.le_dirx_poten_zon6.setObjectName(u"le_dirx_poten_zon6")
        self.le_dirx_poten_zon6.setEnabled(False)
        self.le_dirx_poten_zon6.setMaxLength(32768)
        self.le_dirx_poten_zon6.setAlignment(Qt.AlignCenter)
        self.le_dirx_poten_zon6.setDragEnabled(False)

        self.gridLayout.addWidget(self.le_dirx_poten_zon6, 6, 3, 1, 1)

        self.le_dirx_lon_zon9 = QLineEdit(self.gb_dirx_vz2)
        self.le_dirx_lon_zon9.setObjectName(u"le_dirx_lon_zon9")
        self.le_dirx_lon_zon9.setEnabled(False)
        self.le_dirx_lon_zon9.setMaxLength(32768)
        self.le_dirx_lon_zon9.setAlignment(Qt.AlignCenter)
        self.le_dirx_lon_zon9.setDragEnabled(False)

        self.gridLayout.addWidget(self.le_dirx_lon_zon9, 9, 1, 1, 1)

        self.le_dirx_poten_zon9 = QLineEdit(self.gb_dirx_vz2)
        self.le_dirx_poten_zon9.setObjectName(u"le_dirx_poten_zon9")
        self.le_dirx_poten_zon9.setEnabled(False)
        self.le_dirx_poten_zon9.setMaxLength(32768)
        self.le_dirx_poten_zon9.setAlignment(Qt.AlignCenter)
        self.le_dirx_poten_zon9.setDragEnabled(False)

        self.gridLayout.addWidget(self.le_dirx_poten_zon9, 9, 3, 1, 1)

        self.lb_dirx_lon = QLabel(self.gb_dirx_vz2)
        self.lb_dirx_lon.setObjectName(u"lb_dirx_lon")
        self.lb_dirx_lon.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.lb_dirx_lon, 0, 1, 1, 1)

        self.lb_dirx_nvcx = QLabel(self.gb_dirx_vz2)
        self.lb_dirx_nvcx.setObjectName(u"lb_dirx_nvcx")
        self.lb_dirx_nvcx.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.lb_dirx_nvcx, 0, 2, 1, 1)

        self.le_dirx_poten_zon3 = QLineEdit(self.gb_dirx_vz2)
        self.le_dirx_poten_zon3.setObjectName(u"le_dirx_poten_zon3")
        self.le_dirx_poten_zon3.setEnabled(False)
        self.le_dirx_poten_zon3.setMaxLength(32768)
        self.le_dirx_poten_zon3.setAlignment(Qt.AlignCenter)
        self.le_dirx_poten_zon3.setDragEnabled(False)

        self.gridLayout.addWidget(self.le_dirx_poten_zon3, 3, 3, 1, 1)

        self.le_dirx_nvcx_zon7 = QLineEdit(self.gb_dirx_vz2)
        self.le_dirx_nvcx_zon7.setObjectName(u"le_dirx_nvcx_zon7")
        self.le_dirx_nvcx_zon7.setEnabled(False)
        self.le_dirx_nvcx_zon7.setMaxLength(32768)
        self.le_dirx_nvcx_zon7.setAlignment(Qt.AlignCenter)
        self.le_dirx_nvcx_zon7.setDragEnabled(False)

        self.gridLayout.addWidget(self.le_dirx_nvcx_zon7, 7, 2, 1, 1)

        self.le_dirx_lon_zon1 = QLineEdit(self.gb_dirx_vz2)
        self.le_dirx_lon_zon1.setObjectName(u"le_dirx_lon_zon1")
        self.le_dirx_lon_zon1.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.le_dirx_lon_zon1, 1, 1, 1, 1)

        self.lb_dirx_zon7 = QLabel(self.gb_dirx_vz2)
        self.lb_dirx_zon7.setObjectName(u"lb_dirx_zon7")
        self.lb_dirx_zon7.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.lb_dirx_zon7, 7, 0, 1, 1)

        self.le_dirx_lon_zon3 = QLineEdit(self.gb_dirx_vz2)
        self.le_dirx_lon_zon3.setObjectName(u"le_dirx_lon_zon3")
        self.le_dirx_lon_zon3.setEnabled(False)
        self.le_dirx_lon_zon3.setMaxLength(32768)
        self.le_dirx_lon_zon3.setAlignment(Qt.AlignCenter)
        self.le_dirx_lon_zon3.setDragEnabled(False)

        self.gridLayout.addWidget(self.le_dirx_lon_zon3, 3, 1, 1, 1)

        self.lb_dirx_zon6 = QLabel(self.gb_dirx_vz2)
        self.lb_dirx_zon6.setObjectName(u"lb_dirx_zon6")
        self.lb_dirx_zon6.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.lb_dirx_zon6, 6, 0, 1, 1)

        self.le_dirx_lon_zon8 = QLineEdit(self.gb_dirx_vz2)
        self.le_dirx_lon_zon8.setObjectName(u"le_dirx_lon_zon8")
        self.le_dirx_lon_zon8.setEnabled(False)
        self.le_dirx_lon_zon8.setMaxLength(32768)
        self.le_dirx_lon_zon8.setAlignment(Qt.AlignCenter)
        self.le_dirx_lon_zon8.setDragEnabled(False)

        self.gridLayout.addWidget(self.le_dirx_lon_zon8, 8, 1, 1, 1)

        self.le_dirx_poten_zon1 = QLineEdit(self.gb_dirx_vz2)
        self.le_dirx_poten_zon1.setObjectName(u"le_dirx_poten_zon1")
        self.le_dirx_poten_zon1.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.le_dirx_poten_zon1, 1, 3, 1, 1)

        self.le_dirx_nvcx_zon6 = QLineEdit(self.gb_dirx_vz2)
        self.le_dirx_nvcx_zon6.setObjectName(u"le_dirx_nvcx_zon6")
        self.le_dirx_nvcx_zon6.setEnabled(False)
        self.le_dirx_nvcx_zon6.setMaxLength(32768)
        self.le_dirx_nvcx_zon6.setAlignment(Qt.AlignCenter)
        self.le_dirx_nvcx_zon6.setDragEnabled(False)

        self.gridLayout.addWidget(self.le_dirx_nvcx_zon6, 6, 2, 1, 1)

        self.lb_dirx_zona = QLabel(self.gb_dirx_vz2)
        self.lb_dirx_zona.setObjectName(u"lb_dirx_zona")
        self.lb_dirx_zona.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.lb_dirx_zona, 0, 0, 1, 1)

        self.lb_dirx_zon2 = QLabel(self.gb_dirx_vz2)
        self.lb_dirx_zon2.setObjectName(u"lb_dirx_zon2")
        self.lb_dirx_zon2.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.lb_dirx_zon2, 2, 0, 1, 1)

        self.lb_dirx_zon10 = QLabel(self.gb_dirx_vz2)
        self.lb_dirx_zon10.setObjectName(u"lb_dirx_zon10")
        self.lb_dirx_zon10.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.lb_dirx_zon10, 10, 0, 1, 1)

        self.le_dirx_lon_zon10 = QLineEdit(self.gb_dirx_vz2)
        self.le_dirx_lon_zon10.setObjectName(u"le_dirx_lon_zon10")
        self.le_dirx_lon_zon10.setEnabled(False)
        self.le_dirx_lon_zon10.setMaxLength(32768)
        self.le_dirx_lon_zon10.setAlignment(Qt.AlignCenter)
        self.le_dirx_lon_zon10.setDragEnabled(False)

        self.gridLayout.addWidget(self.le_dirx_lon_zon10, 10, 1, 1, 1)

        self.le_dirx_nvcx_zon10 = QLineEdit(self.gb_dirx_vz2)
        self.le_dirx_nvcx_zon10.setObjectName(u"le_dirx_nvcx_zon10")
        self.le_dirx_nvcx_zon10.setEnabled(False)
        self.le_dirx_nvcx_zon10.setMaxLength(32768)
        self.le_dirx_nvcx_zon10.setAlignment(Qt.AlignCenter)
        self.le_dirx_nvcx_zon10.setDragEnabled(False)

        self.gridLayout.addWidget(self.le_dirx_nvcx_zon10, 10, 2, 1, 1)

        self.le_dirx_poten_zon10 = QLineEdit(self.gb_dirx_vz2)
        self.le_dirx_poten_zon10.setObjectName(u"le_dirx_poten_zon10")
        self.le_dirx_poten_zon10.setEnabled(False)
        self.le_dirx_poten_zon10.setMaxLength(32768)
        self.le_dirx_poten_zon10.setAlignment(Qt.AlignCenter)
        self.le_dirx_poten_zon10.setDragEnabled(False)

        self.gridLayout.addWidget(self.le_dirx_poten_zon10, 10, 3, 1, 1)


        self.verticalLayout_2.addWidget(self.gb_dirx_vz2)


        self.horizontalLayout_3.addWidget(self.gb_dirx_vz)

        self.gb_diry_vz = QGroupBox(self.gbsw_cart_vz)
        self.gb_diry_vz.setObjectName(u"gb_diry_vz")
        self.verticalLayout_3 = QVBoxLayout(self.gb_diry_vz)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.gb_diry_vz1 = QGroupBox(self.gb_diry_vz)
        self.gb_diry_vz1.setObjectName(u"gb_diry_vz1")
        self.horizontalLayout_6 = QHBoxLayout(self.gb_diry_vz1)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.lb_diry_numz = QLabel(self.gb_diry_vz1)
        self.lb_diry_numz.setObjectName(u"lb_diry_numz")

        self.horizontalLayout_6.addWidget(self.lb_diry_numz)

        self.sb_diry_numz = QSpinBox(self.gb_diry_vz1)
        self.sb_diry_numz.setObjectName(u"sb_diry_numz")
        self.sb_diry_numz.setMinimum(1)
        self.sb_diry_numz.setMaximum(10)
        self.sb_diry_numz.setValue(1)

        self.horizontalLayout_6.addWidget(self.sb_diry_numz)


        self.verticalLayout_3.addWidget(self.gb_diry_vz1)

        self.gb_diry_vz2 = QGroupBox(self.gb_diry_vz)
        self.gb_diry_vz2.setObjectName(u"gb_diry_vz2")
        self.gridLayout_2 = QGridLayout(self.gb_diry_vz2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.lb_diry_zona8 = QLabel(self.gb_diry_vz2)
        self.lb_diry_zona8.setObjectName(u"lb_diry_zona8")
        self.lb_diry_zona8.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.lb_diry_zona8, 8, 0, 1, 1)

        self.le_diry_lon_zon4 = QLineEdit(self.gb_diry_vz2)
        self.le_diry_lon_zon4.setObjectName(u"le_diry_lon_zon4")
        self.le_diry_lon_zon4.setEnabled(False)
        self.le_diry_lon_zon4.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.le_diry_lon_zon4, 4, 1, 1, 1)

        self.le_diry_nvcy_zon9 = QLineEdit(self.gb_diry_vz2)
        self.le_diry_nvcy_zon9.setObjectName(u"le_diry_nvcy_zon9")
        self.le_diry_nvcy_zon9.setEnabled(False)
        self.le_diry_nvcy_zon9.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.le_diry_nvcy_zon9, 9, 2, 1, 1)

        self.lb_diry_poten = QLabel(self.gb_diry_vz2)
        self.lb_diry_poten.setObjectName(u"lb_diry_poten")
        self.lb_diry_poten.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.lb_diry_poten, 0, 3, 1, 1)

        self.le_diry_nvcy_zon2 = QLineEdit(self.gb_diry_vz2)
        self.le_diry_nvcy_zon2.setObjectName(u"le_diry_nvcy_zon2")
        self.le_diry_nvcy_zon2.setEnabled(False)
        self.le_diry_nvcy_zon2.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.le_diry_nvcy_zon2, 2, 2, 1, 1)

        self.le_diry_poten_zon2 = QLineEdit(self.gb_diry_vz2)
        self.le_diry_poten_zon2.setObjectName(u"le_diry_poten_zon2")
        self.le_diry_poten_zon2.setEnabled(False)
        self.le_diry_poten_zon2.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.le_diry_poten_zon2, 2, 3, 1, 1)

        self.le_diry_nvcy_zon4 = QLineEdit(self.gb_diry_vz2)
        self.le_diry_nvcy_zon4.setObjectName(u"le_diry_nvcy_zon4")
        self.le_diry_nvcy_zon4.setEnabled(False)
        self.le_diry_nvcy_zon4.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.le_diry_nvcy_zon4, 4, 2, 1, 1)

        self.lb_diry_zona5 = QLabel(self.gb_diry_vz2)
        self.lb_diry_zona5.setObjectName(u"lb_diry_zona5")
        self.lb_diry_zona5.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.lb_diry_zona5, 5, 0, 1, 1)

        self.le_diry_nvcy_zon5 = QLineEdit(self.gb_diry_vz2)
        self.le_diry_nvcy_zon5.setObjectName(u"le_diry_nvcy_zon5")
        self.le_diry_nvcy_zon5.setEnabled(False)
        self.le_diry_nvcy_zon5.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.le_diry_nvcy_zon5, 5, 2, 1, 1)

        self.le_diry_lon_zon2 = QLineEdit(self.gb_diry_vz2)
        self.le_diry_lon_zon2.setObjectName(u"le_diry_lon_zon2")
        self.le_diry_lon_zon2.setEnabled(False)
        self.le_diry_lon_zon2.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.le_diry_lon_zon2, 2, 1, 1, 1)

        self.le_diry_poten_zon4 = QLineEdit(self.gb_diry_vz2)
        self.le_diry_poten_zon4.setObjectName(u"le_diry_poten_zon4")
        self.le_diry_poten_zon4.setEnabled(False)
        self.le_diry_poten_zon4.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.le_diry_poten_zon4, 4, 3, 1, 1)

        self.le_diry_poten_zon5 = QLineEdit(self.gb_diry_vz2)
        self.le_diry_poten_zon5.setObjectName(u"le_diry_poten_zon5")
        self.le_diry_poten_zon5.setEnabled(False)
        self.le_diry_poten_zon5.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.le_diry_poten_zon5, 5, 3, 1, 1)

        self.le_diry_nvcy_zon1 = QLineEdit(self.gb_diry_vz2)
        self.le_diry_nvcy_zon1.setObjectName(u"le_diry_nvcy_zon1")
        self.le_diry_nvcy_zon1.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.le_diry_nvcy_zon1, 1, 2, 1, 1)

        self.lb_diry_zona9 = QLabel(self.gb_diry_vz2)
        self.lb_diry_zona9.setObjectName(u"lb_diry_zona9")
        self.lb_diry_zona9.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.lb_diry_zona9, 9, 0, 1, 1)

        self.lb_diry_zona4 = QLabel(self.gb_diry_vz2)
        self.lb_diry_zona4.setObjectName(u"lb_diry_zona4")
        self.lb_diry_zona4.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.lb_diry_zona4, 4, 0, 1, 1)

        self.le_diry_lon_zon7 = QLineEdit(self.gb_diry_vz2)
        self.le_diry_lon_zon7.setObjectName(u"le_diry_lon_zon7")
        self.le_diry_lon_zon7.setEnabled(False)
        self.le_diry_lon_zon7.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.le_diry_lon_zon7, 7, 1, 1, 1)

        self.le_diry_poten_zon7 = QLineEdit(self.gb_diry_vz2)
        self.le_diry_poten_zon7.setObjectName(u"le_diry_poten_zon7")
        self.le_diry_poten_zon7.setEnabled(False)
        self.le_diry_poten_zon7.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.le_diry_poten_zon7, 7, 3, 1, 1)

        self.le_diry_poten_zon8 = QLineEdit(self.gb_diry_vz2)
        self.le_diry_poten_zon8.setObjectName(u"le_diry_poten_zon8")
        self.le_diry_poten_zon8.setEnabled(False)
        self.le_diry_poten_zon8.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.le_diry_poten_zon8, 8, 3, 1, 1)

        self.le_diry_nvcy_zon8 = QLineEdit(self.gb_diry_vz2)
        self.le_diry_nvcy_zon8.setObjectName(u"le_diry_nvcy_zon8")
        self.le_diry_nvcy_zon8.setEnabled(False)
        self.le_diry_nvcy_zon8.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.le_diry_nvcy_zon8, 8, 2, 1, 1)

        self.le_diry_lon_zon6 = QLineEdit(self.gb_diry_vz2)
        self.le_diry_lon_zon6.setObjectName(u"le_diry_lon_zon6")
        self.le_diry_lon_zon6.setEnabled(False)
        self.le_diry_lon_zon6.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.le_diry_lon_zon6, 6, 1, 1, 1)

        self.lb_diry_zona1 = QLabel(self.gb_diry_vz2)
        self.lb_diry_zona1.setObjectName(u"lb_diry_zona1")
        self.lb_diry_zona1.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.lb_diry_zona1, 1, 0, 1, 1)

        self.lb_diry_zona3 = QLabel(self.gb_diry_vz2)
        self.lb_diry_zona3.setObjectName(u"lb_diry_zona3")
        self.lb_diry_zona3.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.lb_diry_zona3, 3, 0, 1, 1)

        self.le_diry_nvcy_zon3 = QLineEdit(self.gb_diry_vz2)
        self.le_diry_nvcy_zon3.setObjectName(u"le_diry_nvcy_zon3")
        self.le_diry_nvcy_zon3.setEnabled(False)
        self.le_diry_nvcy_zon3.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.le_diry_nvcy_zon3, 3, 2, 1, 1)

        self.le_diry_lon_zon5 = QLineEdit(self.gb_diry_vz2)
        self.le_diry_lon_zon5.setObjectName(u"le_diry_lon_zon5")
        self.le_diry_lon_zon5.setEnabled(False)
        self.le_diry_lon_zon5.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.le_diry_lon_zon5, 5, 1, 1, 1)

        self.le_diry_poten_zon6 = QLineEdit(self.gb_diry_vz2)
        self.le_diry_poten_zon6.setObjectName(u"le_diry_poten_zon6")
        self.le_diry_poten_zon6.setEnabled(False)
        self.le_diry_poten_zon6.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.le_diry_poten_zon6, 6, 3, 1, 1)

        self.le_diry_lon_zon9 = QLineEdit(self.gb_diry_vz2)
        self.le_diry_lon_zon9.setObjectName(u"le_diry_lon_zon9")
        self.le_diry_lon_zon9.setEnabled(False)
        self.le_diry_lon_zon9.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.le_diry_lon_zon9, 9, 1, 1, 1)

        self.le_diry_poten_zon9 = QLineEdit(self.gb_diry_vz2)
        self.le_diry_poten_zon9.setObjectName(u"le_diry_poten_zon9")
        self.le_diry_poten_zon9.setEnabled(False)
        self.le_diry_poten_zon9.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.le_diry_poten_zon9, 9, 3, 1, 1)

        self.lb_diry_lon = QLabel(self.gb_diry_vz2)
        self.lb_diry_lon.setObjectName(u"lb_diry_lon")
        self.lb_diry_lon.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.lb_diry_lon, 0, 1, 1, 1)

        self.lb_diry_nvcy = QLabel(self.gb_diry_vz2)
        self.lb_diry_nvcy.setObjectName(u"lb_diry_nvcy")
        self.lb_diry_nvcy.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.lb_diry_nvcy, 0, 2, 1, 1)

        self.le_diry_poten_zon3 = QLineEdit(self.gb_diry_vz2)
        self.le_diry_poten_zon3.setObjectName(u"le_diry_poten_zon3")
        self.le_diry_poten_zon3.setEnabled(False)
        self.le_diry_poten_zon3.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.le_diry_poten_zon3, 3, 3, 1, 1)

        self.le_diry_nvcy_zon7 = QLineEdit(self.gb_diry_vz2)
        self.le_diry_nvcy_zon7.setObjectName(u"le_diry_nvcy_zon7")
        self.le_diry_nvcy_zon7.setEnabled(False)
        self.le_diry_nvcy_zon7.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.le_diry_nvcy_zon7, 7, 2, 1, 1)

        self.le_diry_lon_zon1 = QLineEdit(self.gb_diry_vz2)
        self.le_diry_lon_zon1.setObjectName(u"le_diry_lon_zon1")
        self.le_diry_lon_zon1.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.le_diry_lon_zon1, 1, 1, 1, 1)

        self.lb_diry_zona7 = QLabel(self.gb_diry_vz2)
        self.lb_diry_zona7.setObjectName(u"lb_diry_zona7")
        self.lb_diry_zona7.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.lb_diry_zona7, 7, 0, 1, 1)

        self.le_diry_lon_zon3 = QLineEdit(self.gb_diry_vz2)
        self.le_diry_lon_zon3.setObjectName(u"le_diry_lon_zon3")
        self.le_diry_lon_zon3.setEnabled(False)
        self.le_diry_lon_zon3.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.le_diry_lon_zon3, 3, 1, 1, 1)

        self.lb_diry_zona6 = QLabel(self.gb_diry_vz2)
        self.lb_diry_zona6.setObjectName(u"lb_diry_zona6")
        self.lb_diry_zona6.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.lb_diry_zona6, 6, 0, 1, 1)

        self.le_diry_lon_zon8 = QLineEdit(self.gb_diry_vz2)
        self.le_diry_lon_zon8.setObjectName(u"le_diry_lon_zon8")
        self.le_diry_lon_zon8.setEnabled(False)
        self.le_diry_lon_zon8.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.le_diry_lon_zon8, 8, 1, 1, 1)

        self.le_diry_poten_zon1 = QLineEdit(self.gb_diry_vz2)
        self.le_diry_poten_zon1.setObjectName(u"le_diry_poten_zon1")
        self.le_diry_poten_zon1.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.le_diry_poten_zon1, 1, 3, 1, 1)

        self.le_diry_nvcy_zon6 = QLineEdit(self.gb_diry_vz2)
        self.le_diry_nvcy_zon6.setObjectName(u"le_diry_nvcy_zon6")
        self.le_diry_nvcy_zon6.setEnabled(False)
        self.le_diry_nvcy_zon6.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.le_diry_nvcy_zon6, 6, 2, 1, 1)

        self.lb_diry_zona = QLabel(self.gb_diry_vz2)
        self.lb_diry_zona.setObjectName(u"lb_diry_zona")
        self.lb_diry_zona.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.lb_diry_zona, 0, 0, 1, 1)

        self.lb_diry_zona2 = QLabel(self.gb_diry_vz2)
        self.lb_diry_zona2.setObjectName(u"lb_diry_zona2")
        self.lb_diry_zona2.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.lb_diry_zona2, 2, 0, 1, 1)

        self.lb_diry_zona10 = QLabel(self.gb_diry_vz2)
        self.lb_diry_zona10.setObjectName(u"lb_diry_zona10")
        self.lb_diry_zona10.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.lb_diry_zona10, 10, 0, 1, 1)

        self.le_diry_lon_zon10 = QLineEdit(self.gb_diry_vz2)
        self.le_diry_lon_zon10.setObjectName(u"le_diry_lon_zon10")
        self.le_diry_lon_zon10.setEnabled(False)
        self.le_diry_lon_zon10.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.le_diry_lon_zon10, 10, 1, 1, 1)

        self.le_diry_nvcy_zon10 = QLineEdit(self.gb_diry_vz2)
        self.le_diry_nvcy_zon10.setObjectName(u"le_diry_nvcy_zon10")
        self.le_diry_nvcy_zon10.setEnabled(False)
        self.le_diry_nvcy_zon10.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.le_diry_nvcy_zon10, 10, 2, 1, 1)

        self.le_diry_poten_zon10 = QLineEdit(self.gb_diry_vz2)
        self.le_diry_poten_zon10.setObjectName(u"le_diry_poten_zon10")
        self.le_diry_poten_zon10.setEnabled(False)
        self.le_diry_poten_zon10.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.le_diry_poten_zon10, 10, 3, 1, 1)


        self.verticalLayout_3.addWidget(self.gb_diry_vz2)


        self.horizontalLayout_3.addWidget(self.gb_diry_vz)

        self.gb_dirz_vz = QGroupBox(self.gbsw_cart_vz)
        self.gb_dirz_vz.setObjectName(u"gb_dirz_vz")
        self.verticalLayout_4 = QVBoxLayout(self.gb_dirz_vz)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.gb_dirz_vz1 = QGroupBox(self.gb_dirz_vz)
        self.gb_dirz_vz1.setObjectName(u"gb_dirz_vz1")
        self.horizontalLayout_7 = QHBoxLayout(self.gb_dirz_vz1)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.lb_dirz_numz = QLabel(self.gb_dirz_vz1)
        self.lb_dirz_numz.setObjectName(u"lb_dirz_numz")

        self.horizontalLayout_7.addWidget(self.lb_dirz_numz)

        self.sb_dirz_numz = QSpinBox(self.gb_dirz_vz1)
        self.sb_dirz_numz.setObjectName(u"sb_dirz_numz")
        self.sb_dirz_numz.setMinimum(1)
        self.sb_dirz_numz.setMaximum(10)
        self.sb_dirz_numz.setValue(1)

        self.horizontalLayout_7.addWidget(self.sb_dirz_numz)


        self.verticalLayout_4.addWidget(self.gb_dirz_vz1)

        self.gb_dirz_vz2 = QGroupBox(self.gb_dirz_vz)
        self.gb_dirz_vz2.setObjectName(u"gb_dirz_vz2")
        self.gridLayout_3 = QGridLayout(self.gb_dirz_vz2)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.lb_dirz_zona8 = QLabel(self.gb_dirz_vz2)
        self.lb_dirz_zona8.setObjectName(u"lb_dirz_zona8")
        self.lb_dirz_zona8.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.lb_dirz_zona8, 8, 0, 1, 1)

        self.le_dirz_lon_zon4 = QLineEdit(self.gb_dirz_vz2)
        self.le_dirz_lon_zon4.setObjectName(u"le_dirz_lon_zon4")
        self.le_dirz_lon_zon4.setEnabled(False)
        self.le_dirz_lon_zon4.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.le_dirz_lon_zon4, 4, 1, 1, 1)

        self.le_dirz_nvcz_zon9 = QLineEdit(self.gb_dirz_vz2)
        self.le_dirz_nvcz_zon9.setObjectName(u"le_dirz_nvcz_zon9")
        self.le_dirz_nvcz_zon9.setEnabled(False)
        self.le_dirz_nvcz_zon9.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.le_dirz_nvcz_zon9, 9, 2, 1, 1)

        self.lb_dirz_poten = QLabel(self.gb_dirz_vz2)
        self.lb_dirz_poten.setObjectName(u"lb_dirz_poten")
        self.lb_dirz_poten.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.lb_dirz_poten, 0, 3, 1, 1)

        self.le_dirz_nvcz_zon2 = QLineEdit(self.gb_dirz_vz2)
        self.le_dirz_nvcz_zon2.setObjectName(u"le_dirz_nvcz_zon2")
        self.le_dirz_nvcz_zon2.setEnabled(False)
        self.le_dirz_nvcz_zon2.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.le_dirz_nvcz_zon2, 2, 2, 1, 1)

        self.le_dirz_poten_zon2 = QLineEdit(self.gb_dirz_vz2)
        self.le_dirz_poten_zon2.setObjectName(u"le_dirz_poten_zon2")
        self.le_dirz_poten_zon2.setEnabled(False)
        self.le_dirz_poten_zon2.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.le_dirz_poten_zon2, 2, 3, 1, 1)

        self.le_dirz_nvcz_zon4 = QLineEdit(self.gb_dirz_vz2)
        self.le_dirz_nvcz_zon4.setObjectName(u"le_dirz_nvcz_zon4")
        self.le_dirz_nvcz_zon4.setEnabled(False)
        self.le_dirz_nvcz_zon4.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.le_dirz_nvcz_zon4, 4, 2, 1, 1)

        self.lb_dirz_zona5 = QLabel(self.gb_dirz_vz2)
        self.lb_dirz_zona5.setObjectName(u"lb_dirz_zona5")
        self.lb_dirz_zona5.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.lb_dirz_zona5, 5, 0, 1, 1)

        self.le_dirz_nvcz_zon5 = QLineEdit(self.gb_dirz_vz2)
        self.le_dirz_nvcz_zon5.setObjectName(u"le_dirz_nvcz_zon5")
        self.le_dirz_nvcz_zon5.setEnabled(False)
        self.le_dirz_nvcz_zon5.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.le_dirz_nvcz_zon5, 5, 2, 1, 1)

        self.le_dirz_lon_zon2 = QLineEdit(self.gb_dirz_vz2)
        self.le_dirz_lon_zon2.setObjectName(u"le_dirz_lon_zon2")
        self.le_dirz_lon_zon2.setEnabled(False)
        self.le_dirz_lon_zon2.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.le_dirz_lon_zon2, 2, 1, 1, 1)

        self.le_dirz_poten_zon4 = QLineEdit(self.gb_dirz_vz2)
        self.le_dirz_poten_zon4.setObjectName(u"le_dirz_poten_zon4")
        self.le_dirz_poten_zon4.setEnabled(False)
        self.le_dirz_poten_zon4.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.le_dirz_poten_zon4, 4, 3, 1, 1)

        self.le_dirz_poten_zon5 = QLineEdit(self.gb_dirz_vz2)
        self.le_dirz_poten_zon5.setObjectName(u"le_dirz_poten_zon5")
        self.le_dirz_poten_zon5.setEnabled(False)
        self.le_dirz_poten_zon5.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.le_dirz_poten_zon5, 5, 3, 1, 1)

        self.le_dirz_nvcz_zon1 = QLineEdit(self.gb_dirz_vz2)
        self.le_dirz_nvcz_zon1.setObjectName(u"le_dirz_nvcz_zon1")
        self.le_dirz_nvcz_zon1.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.le_dirz_nvcz_zon1, 1, 2, 1, 1)

        self.lb_dirz_zona9 = QLabel(self.gb_dirz_vz2)
        self.lb_dirz_zona9.setObjectName(u"lb_dirz_zona9")
        self.lb_dirz_zona9.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.lb_dirz_zona9, 9, 0, 1, 1)

        self.lb_dirz_zona4 = QLabel(self.gb_dirz_vz2)
        self.lb_dirz_zona4.setObjectName(u"lb_dirz_zona4")
        self.lb_dirz_zona4.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.lb_dirz_zona4, 4, 0, 1, 1)

        self.le_dirz_lon_zon7 = QLineEdit(self.gb_dirz_vz2)
        self.le_dirz_lon_zon7.setObjectName(u"le_dirz_lon_zon7")
        self.le_dirz_lon_zon7.setEnabled(False)
        self.le_dirz_lon_zon7.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.le_dirz_lon_zon7, 7, 1, 1, 1)

        self.le_dirz_poten_zon7 = QLineEdit(self.gb_dirz_vz2)
        self.le_dirz_poten_zon7.setObjectName(u"le_dirz_poten_zon7")
        self.le_dirz_poten_zon7.setEnabled(False)
        self.le_dirz_poten_zon7.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.le_dirz_poten_zon7, 7, 3, 1, 1)

        self.le_dirz_poten_zon8 = QLineEdit(self.gb_dirz_vz2)
        self.le_dirz_poten_zon8.setObjectName(u"le_dirz_poten_zon8")
        self.le_dirz_poten_zon8.setEnabled(False)
        self.le_dirz_poten_zon8.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.le_dirz_poten_zon8, 8, 3, 1, 1)

        self.le_dirz_nvcz_zon8 = QLineEdit(self.gb_dirz_vz2)
        self.le_dirz_nvcz_zon8.setObjectName(u"le_dirz_nvcz_zon8")
        self.le_dirz_nvcz_zon8.setEnabled(False)
        self.le_dirz_nvcz_zon8.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.le_dirz_nvcz_zon8, 8, 2, 1, 1)

        self.le_dirz_lon_zon6 = QLineEdit(self.gb_dirz_vz2)
        self.le_dirz_lon_zon6.setObjectName(u"le_dirz_lon_zon6")
        self.le_dirz_lon_zon6.setEnabled(False)
        self.le_dirz_lon_zon6.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.le_dirz_lon_zon6, 6, 1, 1, 1)

        self.lb_dirz_zona1 = QLabel(self.gb_dirz_vz2)
        self.lb_dirz_zona1.setObjectName(u"lb_dirz_zona1")
        self.lb_dirz_zona1.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.lb_dirz_zona1, 1, 0, 1, 1)

        self.lb_dirz_zona3 = QLabel(self.gb_dirz_vz2)
        self.lb_dirz_zona3.setObjectName(u"lb_dirz_zona3")
        self.lb_dirz_zona3.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.lb_dirz_zona3, 3, 0, 1, 1)

        self.le_dirz_nvcz_zon3 = QLineEdit(self.gb_dirz_vz2)
        self.le_dirz_nvcz_zon3.setObjectName(u"le_dirz_nvcz_zon3")
        self.le_dirz_nvcz_zon3.setEnabled(False)
        self.le_dirz_nvcz_zon3.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.le_dirz_nvcz_zon3, 3, 2, 1, 1)

        self.le_dirz_lon_zon5 = QLineEdit(self.gb_dirz_vz2)
        self.le_dirz_lon_zon5.setObjectName(u"le_dirz_lon_zon5")
        self.le_dirz_lon_zon5.setEnabled(False)
        self.le_dirz_lon_zon5.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.le_dirz_lon_zon5, 5, 1, 1, 1)

        self.le_dirz_poten_zon6 = QLineEdit(self.gb_dirz_vz2)
        self.le_dirz_poten_zon6.setObjectName(u"le_dirz_poten_zon6")
        self.le_dirz_poten_zon6.setEnabled(False)
        self.le_dirz_poten_zon6.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.le_dirz_poten_zon6, 6, 3, 1, 1)

        self.le_dirz_lon_zon9 = QLineEdit(self.gb_dirz_vz2)
        self.le_dirz_lon_zon9.setObjectName(u"le_dirz_lon_zon9")
        self.le_dirz_lon_zon9.setEnabled(False)
        self.le_dirz_lon_zon9.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.le_dirz_lon_zon9, 9, 1, 1, 1)

        self.le_dirz_poten_zon9 = QLineEdit(self.gb_dirz_vz2)
        self.le_dirz_poten_zon9.setObjectName(u"le_dirz_poten_zon9")
        self.le_dirz_poten_zon9.setEnabled(False)
        self.le_dirz_poten_zon9.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.le_dirz_poten_zon9, 9, 3, 1, 1)

        self.lb_dirz_lon = QLabel(self.gb_dirz_vz2)
        self.lb_dirz_lon.setObjectName(u"lb_dirz_lon")
        self.lb_dirz_lon.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.lb_dirz_lon, 0, 1, 1, 1)

        self.lb_dirz_nvcz = QLabel(self.gb_dirz_vz2)
        self.lb_dirz_nvcz.setObjectName(u"lb_dirz_nvcz")
        self.lb_dirz_nvcz.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.lb_dirz_nvcz, 0, 2, 1, 1)

        self.le_dirz_poten_zon3 = QLineEdit(self.gb_dirz_vz2)
        self.le_dirz_poten_zon3.setObjectName(u"le_dirz_poten_zon3")
        self.le_dirz_poten_zon3.setEnabled(False)
        self.le_dirz_poten_zon3.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.le_dirz_poten_zon3, 3, 3, 1, 1)

        self.le_dirz_nvcz_zon7 = QLineEdit(self.gb_dirz_vz2)
        self.le_dirz_nvcz_zon7.setObjectName(u"le_dirz_nvcz_zon7")
        self.le_dirz_nvcz_zon7.setEnabled(False)
        self.le_dirz_nvcz_zon7.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.le_dirz_nvcz_zon7, 7, 2, 1, 1)

        self.le_dirz_lon_zon1 = QLineEdit(self.gb_dirz_vz2)
        self.le_dirz_lon_zon1.setObjectName(u"le_dirz_lon_zon1")
        self.le_dirz_lon_zon1.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.le_dirz_lon_zon1, 1, 1, 1, 1)

        self.lb_dirz_zona7 = QLabel(self.gb_dirz_vz2)
        self.lb_dirz_zona7.setObjectName(u"lb_dirz_zona7")
        self.lb_dirz_zona7.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.lb_dirz_zona7, 7, 0, 1, 1)

        self.le_dirz_lon_zon3 = QLineEdit(self.gb_dirz_vz2)
        self.le_dirz_lon_zon3.setObjectName(u"le_dirz_lon_zon3")
        self.le_dirz_lon_zon3.setEnabled(False)
        self.le_dirz_lon_zon3.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.le_dirz_lon_zon3, 3, 1, 1, 1)

        self.lb_dirz_zona6 = QLabel(self.gb_dirz_vz2)
        self.lb_dirz_zona6.setObjectName(u"lb_dirz_zona6")
        self.lb_dirz_zona6.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.lb_dirz_zona6, 6, 0, 1, 1)

        self.le_dirz_lon_zon8 = QLineEdit(self.gb_dirz_vz2)
        self.le_dirz_lon_zon8.setObjectName(u"le_dirz_lon_zon8")
        self.le_dirz_lon_zon8.setEnabled(False)
        self.le_dirz_lon_zon8.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.le_dirz_lon_zon8, 8, 1, 1, 1)

        self.le_dirz_poten_zon1 = QLineEdit(self.gb_dirz_vz2)
        self.le_dirz_poten_zon1.setObjectName(u"le_dirz_poten_zon1")
        self.le_dirz_poten_zon1.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.le_dirz_poten_zon1, 1, 3, 1, 1)

        self.le_dirz_nvcz_zon6 = QLineEdit(self.gb_dirz_vz2)
        self.le_dirz_nvcz_zon6.setObjectName(u"le_dirz_nvcz_zon6")
        self.le_dirz_nvcz_zon6.setEnabled(False)
        self.le_dirz_nvcz_zon6.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.le_dirz_nvcz_zon6, 6, 2, 1, 1)

        self.lb_dirz_zona = QLabel(self.gb_dirz_vz2)
        self.lb_dirz_zona.setObjectName(u"lb_dirz_zona")
        self.lb_dirz_zona.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.lb_dirz_zona, 0, 0, 1, 1)

        self.lb_dirz_zona2 = QLabel(self.gb_dirz_vz2)
        self.lb_dirz_zona2.setObjectName(u"lb_dirz_zona2")
        self.lb_dirz_zona2.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.lb_dirz_zona2, 2, 0, 1, 1)

        self.lb_dirz_zona10 = QLabel(self.gb_dirz_vz2)
        self.lb_dirz_zona10.setObjectName(u"lb_dirz_zona10")
        self.lb_dirz_zona10.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.lb_dirz_zona10, 10, 0, 1, 1)

        self.le_dirz_lon_zon10 = QLineEdit(self.gb_dirz_vz2)
        self.le_dirz_lon_zon10.setObjectName(u"le_dirz_lon_zon10")
        self.le_dirz_lon_zon10.setEnabled(False)
        self.le_dirz_lon_zon10.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.le_dirz_lon_zon10, 10, 1, 1, 1)

        self.le_dirz_nvcz_zon10 = QLineEdit(self.gb_dirz_vz2)
        self.le_dirz_nvcz_zon10.setObjectName(u"le_dirz_nvcz_zon10")
        self.le_dirz_nvcz_zon10.setEnabled(False)
        self.le_dirz_nvcz_zon10.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.le_dirz_nvcz_zon10, 10, 2, 1, 1)

        self.le_dirz_poten_zon10 = QLineEdit(self.gb_dirz_vz2)
        self.le_dirz_poten_zon10.setObjectName(u"le_dirz_poten_zon10")
        self.le_dirz_poten_zon10.setEnabled(False)
        self.le_dirz_poten_zon10.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.le_dirz_poten_zon10, 10, 3, 1, 1)


        self.verticalLayout_4.addWidget(self.gb_dirz_vz2)


        self.horizontalLayout_3.addWidget(self.gb_dirz_vz)

        self.gbsw_malla.addWidget(self.gbsw_cart_vz)
        self.gbsw_cil_vz = QWidget()
        self.gbsw_cil_vz.setObjectName(u"gbsw_cil_vz")
        self.horizontalLayout_4 = QHBoxLayout(self.gbsw_cil_vz)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.gb_dirtita_vz = QGroupBox(self.gbsw_cil_vz)
        self.gb_dirtita_vz.setObjectName(u"gb_dirtita_vz")
        self.verticalLayout_5 = QVBoxLayout(self.gb_dirtita_vz)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.gb_dirtita_vz1 = QGroupBox(self.gb_dirtita_vz)
        self.gb_dirtita_vz1.setObjectName(u"gb_dirtita_vz1")
        self.horizontalLayout_8 = QHBoxLayout(self.gb_dirtita_vz1)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.lb_dirtita_numz = QLabel(self.gb_dirtita_vz1)
        self.lb_dirtita_numz.setObjectName(u"lb_dirtita_numz")

        self.horizontalLayout_8.addWidget(self.lb_dirtita_numz)

        self.sb_dirtita_numz = QSpinBox(self.gb_dirtita_vz1)
        self.sb_dirtita_numz.setObjectName(u"sb_dirtita_numz")
        self.sb_dirtita_numz.setMinimum(1)
        self.sb_dirtita_numz.setMaximum(10)
        self.sb_dirtita_numz.setValue(1)

        self.horizontalLayout_8.addWidget(self.sb_dirtita_numz)


        self.verticalLayout_5.addWidget(self.gb_dirtita_vz1)

        self.gb_dirtita_vz2 = QGroupBox(self.gb_dirtita_vz)
        self.gb_dirtita_vz2.setObjectName(u"gb_dirtita_vz2")
        self.gridLayout_4 = QGridLayout(self.gb_dirtita_vz2)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.lb_dirtita_zona8 = QLabel(self.gb_dirtita_vz2)
        self.lb_dirtita_zona8.setObjectName(u"lb_dirtita_zona8")
        self.lb_dirtita_zona8.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.lb_dirtita_zona8, 8, 0, 1, 1)

        self.le_dirtita_lon_zon4 = QLineEdit(self.gb_dirtita_vz2)
        self.le_dirtita_lon_zon4.setObjectName(u"le_dirtita_lon_zon4")
        self.le_dirtita_lon_zon4.setEnabled(False)
        self.le_dirtita_lon_zon4.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.le_dirtita_lon_zon4, 4, 1, 1, 1)

        self.le_dirtita_nvctita_zon9 = QLineEdit(self.gb_dirtita_vz2)
        self.le_dirtita_nvctita_zon9.setObjectName(u"le_dirtita_nvctita_zon9")
        self.le_dirtita_nvctita_zon9.setEnabled(False)
        self.le_dirtita_nvctita_zon9.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.le_dirtita_nvctita_zon9, 9, 2, 1, 1)

        self.lb_dirtita_poten = QLabel(self.gb_dirtita_vz2)
        self.lb_dirtita_poten.setObjectName(u"lb_dirtita_poten")
        self.lb_dirtita_poten.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.lb_dirtita_poten, 0, 3, 1, 1)

        self.le_dirtita_nvctita_zon2 = QLineEdit(self.gb_dirtita_vz2)
        self.le_dirtita_nvctita_zon2.setObjectName(u"le_dirtita_nvctita_zon2")
        self.le_dirtita_nvctita_zon2.setEnabled(False)
        self.le_dirtita_nvctita_zon2.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.le_dirtita_nvctita_zon2, 2, 2, 1, 1)

        self.le_dirtita_poten_zon2 = QLineEdit(self.gb_dirtita_vz2)
        self.le_dirtita_poten_zon2.setObjectName(u"le_dirtita_poten_zon2")
        self.le_dirtita_poten_zon2.setEnabled(False)
        self.le_dirtita_poten_zon2.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.le_dirtita_poten_zon2, 2, 3, 1, 1)

        self.le_dirtita_nvctita_zon4 = QLineEdit(self.gb_dirtita_vz2)
        self.le_dirtita_nvctita_zon4.setObjectName(u"le_dirtita_nvctita_zon4")
        self.le_dirtita_nvctita_zon4.setEnabled(False)
        self.le_dirtita_nvctita_zon4.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.le_dirtita_nvctita_zon4, 4, 2, 1, 1)

        self.lb_dirtita_zona5 = QLabel(self.gb_dirtita_vz2)
        self.lb_dirtita_zona5.setObjectName(u"lb_dirtita_zona5")
        self.lb_dirtita_zona5.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.lb_dirtita_zona5, 5, 0, 1, 1)

        self.le_dirtita_nvctita_zon5 = QLineEdit(self.gb_dirtita_vz2)
        self.le_dirtita_nvctita_zon5.setObjectName(u"le_dirtita_nvctita_zon5")
        self.le_dirtita_nvctita_zon5.setEnabled(False)
        self.le_dirtita_nvctita_zon5.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.le_dirtita_nvctita_zon5, 5, 2, 1, 1)

        self.le_dirtita_lon_zon2 = QLineEdit(self.gb_dirtita_vz2)
        self.le_dirtita_lon_zon2.setObjectName(u"le_dirtita_lon_zon2")
        self.le_dirtita_lon_zon2.setEnabled(False)
        self.le_dirtita_lon_zon2.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.le_dirtita_lon_zon2, 2, 1, 1, 1)

        self.le_dirtita_poten_zon4 = QLineEdit(self.gb_dirtita_vz2)
        self.le_dirtita_poten_zon4.setObjectName(u"le_dirtita_poten_zon4")
        self.le_dirtita_poten_zon4.setEnabled(False)
        self.le_dirtita_poten_zon4.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.le_dirtita_poten_zon4, 4, 3, 1, 1)

        self.le_dirtita_poten_zon5 = QLineEdit(self.gb_dirtita_vz2)
        self.le_dirtita_poten_zon5.setObjectName(u"le_dirtita_poten_zon5")
        self.le_dirtita_poten_zon5.setEnabled(False)
        self.le_dirtita_poten_zon5.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.le_dirtita_poten_zon5, 5, 3, 1, 1)

        self.le_dirtita_nvctita_zon1 = QLineEdit(self.gb_dirtita_vz2)
        self.le_dirtita_nvctita_zon1.setObjectName(u"le_dirtita_nvctita_zon1")
        self.le_dirtita_nvctita_zon1.setEnabled(True)
        self.le_dirtita_nvctita_zon1.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.le_dirtita_nvctita_zon1, 1, 2, 1, 1)

        self.lb_dirtita_zona9 = QLabel(self.gb_dirtita_vz2)
        self.lb_dirtita_zona9.setObjectName(u"lb_dirtita_zona9")
        self.lb_dirtita_zona9.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.lb_dirtita_zona9, 9, 0, 1, 1)

        self.lb_dirtita_zona4 = QLabel(self.gb_dirtita_vz2)
        self.lb_dirtita_zona4.setObjectName(u"lb_dirtita_zona4")
        self.lb_dirtita_zona4.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.lb_dirtita_zona4, 4, 0, 1, 1)

        self.le_dirtita_lon_zon7 = QLineEdit(self.gb_dirtita_vz2)
        self.le_dirtita_lon_zon7.setObjectName(u"le_dirtita_lon_zon7")
        self.le_dirtita_lon_zon7.setEnabled(False)
        self.le_dirtita_lon_zon7.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.le_dirtita_lon_zon7, 7, 1, 1, 1)

        self.le_dirtita_poten_zon7 = QLineEdit(self.gb_dirtita_vz2)
        self.le_dirtita_poten_zon7.setObjectName(u"le_dirtita_poten_zon7")
        self.le_dirtita_poten_zon7.setEnabled(False)
        self.le_dirtita_poten_zon7.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.le_dirtita_poten_zon7, 7, 3, 1, 1)

        self.le_dirtita_poten_zon8 = QLineEdit(self.gb_dirtita_vz2)
        self.le_dirtita_poten_zon8.setObjectName(u"le_dirtita_poten_zon8")
        self.le_dirtita_poten_zon8.setEnabled(False)
        self.le_dirtita_poten_zon8.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.le_dirtita_poten_zon8, 8, 3, 1, 1)

        self.le_dirtita_nvctita_zon8 = QLineEdit(self.gb_dirtita_vz2)
        self.le_dirtita_nvctita_zon8.setObjectName(u"le_dirtita_nvctita_zon8")
        self.le_dirtita_nvctita_zon8.setEnabled(False)
        self.le_dirtita_nvctita_zon8.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.le_dirtita_nvctita_zon8, 8, 2, 1, 1)

        self.le_dirtita_lon_zon6 = QLineEdit(self.gb_dirtita_vz2)
        self.le_dirtita_lon_zon6.setObjectName(u"le_dirtita_lon_zon6")
        self.le_dirtita_lon_zon6.setEnabled(False)
        self.le_dirtita_lon_zon6.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.le_dirtita_lon_zon6, 6, 1, 1, 1)

        self.lb_dirtita_zona1 = QLabel(self.gb_dirtita_vz2)
        self.lb_dirtita_zona1.setObjectName(u"lb_dirtita_zona1")
        self.lb_dirtita_zona1.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.lb_dirtita_zona1, 1, 0, 1, 1)

        self.lb_dirtita_zona3 = QLabel(self.gb_dirtita_vz2)
        self.lb_dirtita_zona3.setObjectName(u"lb_dirtita_zona3")
        self.lb_dirtita_zona3.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.lb_dirtita_zona3, 3, 0, 1, 1)

        self.le_dirtita_nvctita_zon3 = QLineEdit(self.gb_dirtita_vz2)
        self.le_dirtita_nvctita_zon3.setObjectName(u"le_dirtita_nvctita_zon3")
        self.le_dirtita_nvctita_zon3.setEnabled(False)
        self.le_dirtita_nvctita_zon3.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.le_dirtita_nvctita_zon3, 3, 2, 1, 1)

        self.le_dirtita_lon_zon5 = QLineEdit(self.gb_dirtita_vz2)
        self.le_dirtita_lon_zon5.setObjectName(u"le_dirtita_lon_zon5")
        self.le_dirtita_lon_zon5.setEnabled(False)
        self.le_dirtita_lon_zon5.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.le_dirtita_lon_zon5, 5, 1, 1, 1)

        self.le_dirtita_poten_zon6 = QLineEdit(self.gb_dirtita_vz2)
        self.le_dirtita_poten_zon6.setObjectName(u"le_dirtita_poten_zon6")
        self.le_dirtita_poten_zon6.setEnabled(False)
        self.le_dirtita_poten_zon6.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.le_dirtita_poten_zon6, 6, 3, 1, 1)

        self.le_dirtita_lon_zon9 = QLineEdit(self.gb_dirtita_vz2)
        self.le_dirtita_lon_zon9.setObjectName(u"le_dirtita_lon_zon9")
        self.le_dirtita_lon_zon9.setEnabled(False)
        self.le_dirtita_lon_zon9.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.le_dirtita_lon_zon9, 9, 1, 1, 1)

        self.le_dirtita_poten_zon9 = QLineEdit(self.gb_dirtita_vz2)
        self.le_dirtita_poten_zon9.setObjectName(u"le_dirtita_poten_zon9")
        self.le_dirtita_poten_zon9.setEnabled(False)
        self.le_dirtita_poten_zon9.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.le_dirtita_poten_zon9, 9, 3, 1, 1)

        self.lb_dirtita_lon = QLabel(self.gb_dirtita_vz2)
        self.lb_dirtita_lon.setObjectName(u"lb_dirtita_lon")
        self.lb_dirtita_lon.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.lb_dirtita_lon, 0, 1, 1, 1)

        self.lb_dirtita_nvctita = QLabel(self.gb_dirtita_vz2)
        self.lb_dirtita_nvctita.setObjectName(u"lb_dirtita_nvctita")
        self.lb_dirtita_nvctita.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.lb_dirtita_nvctita, 0, 2, 1, 1)

        self.le_dirtita_poten_zon3 = QLineEdit(self.gb_dirtita_vz2)
        self.le_dirtita_poten_zon3.setObjectName(u"le_dirtita_poten_zon3")
        self.le_dirtita_poten_zon3.setEnabled(False)
        self.le_dirtita_poten_zon3.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.le_dirtita_poten_zon3, 3, 3, 1, 1)

        self.le_dirtita_nvctita_zon7 = QLineEdit(self.gb_dirtita_vz2)
        self.le_dirtita_nvctita_zon7.setObjectName(u"le_dirtita_nvctita_zon7")
        self.le_dirtita_nvctita_zon7.setEnabled(False)
        self.le_dirtita_nvctita_zon7.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.le_dirtita_nvctita_zon7, 7, 2, 1, 1)

        self.le_dirtita_lon_zon1 = QLineEdit(self.gb_dirtita_vz2)
        self.le_dirtita_lon_zon1.setObjectName(u"le_dirtita_lon_zon1")
        self.le_dirtita_lon_zon1.setEnabled(True)
        self.le_dirtita_lon_zon1.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.le_dirtita_lon_zon1, 1, 1, 1, 1)

        self.lb_dirtita_zona7 = QLabel(self.gb_dirtita_vz2)
        self.lb_dirtita_zona7.setObjectName(u"lb_dirtita_zona7")
        self.lb_dirtita_zona7.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.lb_dirtita_zona7, 7, 0, 1, 1)

        self.le_dirtita_lon_zon3 = QLineEdit(self.gb_dirtita_vz2)
        self.le_dirtita_lon_zon3.setObjectName(u"le_dirtita_lon_zon3")
        self.le_dirtita_lon_zon3.setEnabled(False)
        self.le_dirtita_lon_zon3.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.le_dirtita_lon_zon3, 3, 1, 1, 1)

        self.lb_dirtita_zona6 = QLabel(self.gb_dirtita_vz2)
        self.lb_dirtita_zona6.setObjectName(u"lb_dirtita_zona6")
        self.lb_dirtita_zona6.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.lb_dirtita_zona6, 6, 0, 1, 1)

        self.le_dirtita_lon_zon8 = QLineEdit(self.gb_dirtita_vz2)
        self.le_dirtita_lon_zon8.setObjectName(u"le_dirtita_lon_zon8")
        self.le_dirtita_lon_zon8.setEnabled(False)
        self.le_dirtita_lon_zon8.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.le_dirtita_lon_zon8, 8, 1, 1, 1)

        self.le_dirtita_poten_zon1 = QLineEdit(self.gb_dirtita_vz2)
        self.le_dirtita_poten_zon1.setObjectName(u"le_dirtita_poten_zon1")
        self.le_dirtita_poten_zon1.setEnabled(True)
        self.le_dirtita_poten_zon1.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.le_dirtita_poten_zon1, 1, 3, 1, 1)

        self.le_dirtita_nvctita_zon6 = QLineEdit(self.gb_dirtita_vz2)
        self.le_dirtita_nvctita_zon6.setObjectName(u"le_dirtita_nvctita_zon6")
        self.le_dirtita_nvctita_zon6.setEnabled(False)
        self.le_dirtita_nvctita_zon6.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.le_dirtita_nvctita_zon6, 6, 2, 1, 1)

        self.lb_dirtita_zona = QLabel(self.gb_dirtita_vz2)
        self.lb_dirtita_zona.setObjectName(u"lb_dirtita_zona")
        self.lb_dirtita_zona.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.lb_dirtita_zona, 0, 0, 1, 1)

        self.lb_dirtita_zona2 = QLabel(self.gb_dirtita_vz2)
        self.lb_dirtita_zona2.setObjectName(u"lb_dirtita_zona2")
        self.lb_dirtita_zona2.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.lb_dirtita_zona2, 2, 0, 1, 1)

        self.lb_dirtita_zona10 = QLabel(self.gb_dirtita_vz2)
        self.lb_dirtita_zona10.setObjectName(u"lb_dirtita_zona10")
        self.lb_dirtita_zona10.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.lb_dirtita_zona10, 10, 0, 1, 1)

        self.le_dirtita_lon_zon10 = QLineEdit(self.gb_dirtita_vz2)
        self.le_dirtita_lon_zon10.setObjectName(u"le_dirtita_lon_zon10")
        self.le_dirtita_lon_zon10.setEnabled(False)
        self.le_dirtita_lon_zon10.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.le_dirtita_lon_zon10, 10, 1, 1, 1)

        self.le_dirtita_nvctita_zon10 = QLineEdit(self.gb_dirtita_vz2)
        self.le_dirtita_nvctita_zon10.setObjectName(u"le_dirtita_nvctita_zon10")
        self.le_dirtita_nvctita_zon10.setEnabled(False)
        self.le_dirtita_nvctita_zon10.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.le_dirtita_nvctita_zon10, 10, 2, 1, 1)

        self.le_dirtita_poten_zon10 = QLineEdit(self.gb_dirtita_vz2)
        self.le_dirtita_poten_zon10.setObjectName(u"le_dirtita_poten_zon10")
        self.le_dirtita_poten_zon10.setEnabled(False)
        self.le_dirtita_poten_zon10.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.le_dirtita_poten_zon10, 10, 3, 1, 1)


        self.verticalLayout_5.addWidget(self.gb_dirtita_vz2)


        self.horizontalLayout_4.addWidget(self.gb_dirtita_vz)

        self.gb_dirr_vz = QGroupBox(self.gbsw_cil_vz)
        self.gb_dirr_vz.setObjectName(u"gb_dirr_vz")
        self.verticalLayout_6 = QVBoxLayout(self.gb_dirr_vz)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.gb_dirr_vz1 = QGroupBox(self.gb_dirr_vz)
        self.gb_dirr_vz1.setObjectName(u"gb_dirr_vz1")
        self.formLayout_12 = QFormLayout(self.gb_dirr_vz1)
        self.formLayout_12.setObjectName(u"formLayout_12")
        self.lb_dirr_numz = QLabel(self.gb_dirr_vz1)
        self.lb_dirr_numz.setObjectName(u"lb_dirr_numz")

        self.formLayout_12.setWidget(0, QFormLayout.LabelRole, self.lb_dirr_numz)

        self.sb_dirr_numz = QSpinBox(self.gb_dirr_vz1)
        self.sb_dirr_numz.setObjectName(u"sb_dirr_numz")
        self.sb_dirr_numz.setMinimum(1)
        self.sb_dirr_numz.setMaximum(10)
        self.sb_dirr_numz.setValue(1)

        self.formLayout_12.setWidget(0, QFormLayout.FieldRole, self.sb_dirr_numz)

        self.lb_dirr_inidom = QLabel(self.gb_dirr_vz1)
        self.lb_dirr_inidom.setObjectName(u"lb_dirr_inidom")

        self.formLayout_12.setWidget(1, QFormLayout.LabelRole, self.lb_dirr_inidom)

        self.le_dirr_inidom = QLineEdit(self.gb_dirr_vz1)
        self.le_dirr_inidom.setObjectName(u"le_dirr_inidom")
        self.le_dirr_inidom.setEnabled(True)

        self.formLayout_12.setWidget(1, QFormLayout.FieldRole, self.le_dirr_inidom)


        self.verticalLayout_6.addWidget(self.gb_dirr_vz1)

        self.gb_dirr_vz2 = QGroupBox(self.gb_dirr_vz)
        self.gb_dirr_vz2.setObjectName(u"gb_dirr_vz2")
        self.gridLayout_5 = QGridLayout(self.gb_dirr_vz2)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.lb_dirr_zona8 = QLabel(self.gb_dirr_vz2)
        self.lb_dirr_zona8.setObjectName(u"lb_dirr_zona8")
        self.lb_dirr_zona8.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.lb_dirr_zona8, 8, 0, 1, 1)

        self.le_dirr_lon_zon4 = QLineEdit(self.gb_dirr_vz2)
        self.le_dirr_lon_zon4.setObjectName(u"le_dirr_lon_zon4")
        self.le_dirr_lon_zon4.setEnabled(False)
        self.le_dirr_lon_zon4.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.le_dirr_lon_zon4, 4, 1, 1, 1)

        self.le_dirr_nvcr_zon9 = QLineEdit(self.gb_dirr_vz2)
        self.le_dirr_nvcr_zon9.setObjectName(u"le_dirr_nvcr_zon9")
        self.le_dirr_nvcr_zon9.setEnabled(False)
        self.le_dirr_nvcr_zon9.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.le_dirr_nvcr_zon9, 9, 2, 1, 1)

        self.lb_dirr_poten = QLabel(self.gb_dirr_vz2)
        self.lb_dirr_poten.setObjectName(u"lb_dirr_poten")
        self.lb_dirr_poten.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.lb_dirr_poten, 0, 3, 1, 1)

        self.le_dirr_nvcr_zon2 = QLineEdit(self.gb_dirr_vz2)
        self.le_dirr_nvcr_zon2.setObjectName(u"le_dirr_nvcr_zon2")
        self.le_dirr_nvcr_zon2.setEnabled(False)
        self.le_dirr_nvcr_zon2.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.le_dirr_nvcr_zon2, 2, 2, 1, 1)

        self.le_dirr_poten_zon2 = QLineEdit(self.gb_dirr_vz2)
        self.le_dirr_poten_zon2.setObjectName(u"le_dirr_poten_zon2")
        self.le_dirr_poten_zon2.setEnabled(False)
        self.le_dirr_poten_zon2.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.le_dirr_poten_zon2, 2, 3, 1, 1)

        self.le_dirr_nvcr_zon4 = QLineEdit(self.gb_dirr_vz2)
        self.le_dirr_nvcr_zon4.setObjectName(u"le_dirr_nvcr_zon4")
        self.le_dirr_nvcr_zon4.setEnabled(False)
        self.le_dirr_nvcr_zon4.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.le_dirr_nvcr_zon4, 4, 2, 1, 1)

        self.lb_dirr_zona5 = QLabel(self.gb_dirr_vz2)
        self.lb_dirr_zona5.setObjectName(u"lb_dirr_zona5")
        self.lb_dirr_zona5.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.lb_dirr_zona5, 5, 0, 1, 1)

        self.le_dirr_nvcr_zon5 = QLineEdit(self.gb_dirr_vz2)
        self.le_dirr_nvcr_zon5.setObjectName(u"le_dirr_nvcr_zon5")
        self.le_dirr_nvcr_zon5.setEnabled(False)
        self.le_dirr_nvcr_zon5.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.le_dirr_nvcr_zon5, 5, 2, 1, 1)

        self.le_dirr_lon_zon2 = QLineEdit(self.gb_dirr_vz2)
        self.le_dirr_lon_zon2.setObjectName(u"le_dirr_lon_zon2")
        self.le_dirr_lon_zon2.setEnabled(False)
        self.le_dirr_lon_zon2.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.le_dirr_lon_zon2, 2, 1, 1, 1)

        self.le_dirr_poten_zon4 = QLineEdit(self.gb_dirr_vz2)
        self.le_dirr_poten_zon4.setObjectName(u"le_dirr_poten_zon4")
        self.le_dirr_poten_zon4.setEnabled(False)
        self.le_dirr_poten_zon4.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.le_dirr_poten_zon4, 4, 3, 1, 1)

        self.le_dirr_poten_zon5 = QLineEdit(self.gb_dirr_vz2)
        self.le_dirr_poten_zon5.setObjectName(u"le_dirr_poten_zon5")
        self.le_dirr_poten_zon5.setEnabled(False)
        self.le_dirr_poten_zon5.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.le_dirr_poten_zon5, 5, 3, 1, 1)

        self.le_dirr_nvcr_zon1 = QLineEdit(self.gb_dirr_vz2)
        self.le_dirr_nvcr_zon1.setObjectName(u"le_dirr_nvcr_zon1")
        self.le_dirr_nvcr_zon1.setEnabled(True)
        self.le_dirr_nvcr_zon1.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.le_dirr_nvcr_zon1, 1, 2, 1, 1)

        self.lb_dirr_zona9 = QLabel(self.gb_dirr_vz2)
        self.lb_dirr_zona9.setObjectName(u"lb_dirr_zona9")
        self.lb_dirr_zona9.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.lb_dirr_zona9, 9, 0, 1, 1)

        self.lb_dirr_zona4 = QLabel(self.gb_dirr_vz2)
        self.lb_dirr_zona4.setObjectName(u"lb_dirr_zona4")
        self.lb_dirr_zona4.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.lb_dirr_zona4, 4, 0, 1, 1)

        self.le_dirr_lon_zon7 = QLineEdit(self.gb_dirr_vz2)
        self.le_dirr_lon_zon7.setObjectName(u"le_dirr_lon_zon7")
        self.le_dirr_lon_zon7.setEnabled(False)
        self.le_dirr_lon_zon7.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.le_dirr_lon_zon7, 7, 1, 1, 1)

        self.le_dirr_poten_zon7 = QLineEdit(self.gb_dirr_vz2)
        self.le_dirr_poten_zon7.setObjectName(u"le_dirr_poten_zon7")
        self.le_dirr_poten_zon7.setEnabled(False)
        self.le_dirr_poten_zon7.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.le_dirr_poten_zon7, 7, 3, 1, 1)

        self.le_dirr_poten_zon8 = QLineEdit(self.gb_dirr_vz2)
        self.le_dirr_poten_zon8.setObjectName(u"le_dirr_poten_zon8")
        self.le_dirr_poten_zon8.setEnabled(False)
        self.le_dirr_poten_zon8.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.le_dirr_poten_zon8, 8, 3, 1, 1)

        self.le_dirr_nvcr_zon8 = QLineEdit(self.gb_dirr_vz2)
        self.le_dirr_nvcr_zon8.setObjectName(u"le_dirr_nvcr_zon8")
        self.le_dirr_nvcr_zon8.setEnabled(False)
        self.le_dirr_nvcr_zon8.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.le_dirr_nvcr_zon8, 8, 2, 1, 1)

        self.le_dirr_lon_zon6 = QLineEdit(self.gb_dirr_vz2)
        self.le_dirr_lon_zon6.setObjectName(u"le_dirr_lon_zon6")
        self.le_dirr_lon_zon6.setEnabled(False)
        self.le_dirr_lon_zon6.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.le_dirr_lon_zon6, 6, 1, 1, 1)

        self.lb_dirr_zona1 = QLabel(self.gb_dirr_vz2)
        self.lb_dirr_zona1.setObjectName(u"lb_dirr_zona1")
        self.lb_dirr_zona1.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.lb_dirr_zona1, 1, 0, 1, 1)

        self.lb_dirr_zona3 = QLabel(self.gb_dirr_vz2)
        self.lb_dirr_zona3.setObjectName(u"lb_dirr_zona3")
        self.lb_dirr_zona3.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.lb_dirr_zona3, 3, 0, 1, 1)

        self.le_dirr_nvcr_zon3 = QLineEdit(self.gb_dirr_vz2)
        self.le_dirr_nvcr_zon3.setObjectName(u"le_dirr_nvcr_zon3")
        self.le_dirr_nvcr_zon3.setEnabled(False)
        self.le_dirr_nvcr_zon3.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.le_dirr_nvcr_zon3, 3, 2, 1, 1)

        self.le_dirr_lon_zon5 = QLineEdit(self.gb_dirr_vz2)
        self.le_dirr_lon_zon5.setObjectName(u"le_dirr_lon_zon5")
        self.le_dirr_lon_zon5.setEnabled(False)
        self.le_dirr_lon_zon5.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.le_dirr_lon_zon5, 5, 1, 1, 1)

        self.le_dirr_poten_zon6 = QLineEdit(self.gb_dirr_vz2)
        self.le_dirr_poten_zon6.setObjectName(u"le_dirr_poten_zon6")
        self.le_dirr_poten_zon6.setEnabled(False)
        self.le_dirr_poten_zon6.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.le_dirr_poten_zon6, 6, 3, 1, 1)

        self.le_dirr_lon_zon9 = QLineEdit(self.gb_dirr_vz2)
        self.le_dirr_lon_zon9.setObjectName(u"le_dirr_lon_zon9")
        self.le_dirr_lon_zon9.setEnabled(False)
        self.le_dirr_lon_zon9.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.le_dirr_lon_zon9, 9, 1, 1, 1)

        self.le_dirr_poten_zon9 = QLineEdit(self.gb_dirr_vz2)
        self.le_dirr_poten_zon9.setObjectName(u"le_dirr_poten_zon9")
        self.le_dirr_poten_zon9.setEnabled(False)
        self.le_dirr_poten_zon9.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.le_dirr_poten_zon9, 9, 3, 1, 1)

        self.lb_dirr_lon = QLabel(self.gb_dirr_vz2)
        self.lb_dirr_lon.setObjectName(u"lb_dirr_lon")
        self.lb_dirr_lon.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.lb_dirr_lon, 0, 1, 1, 1)

        self.lb_dirr_nvcr = QLabel(self.gb_dirr_vz2)
        self.lb_dirr_nvcr.setObjectName(u"lb_dirr_nvcr")
        self.lb_dirr_nvcr.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.lb_dirr_nvcr, 0, 2, 1, 1)

        self.le_dirr_poten_zon3 = QLineEdit(self.gb_dirr_vz2)
        self.le_dirr_poten_zon3.setObjectName(u"le_dirr_poten_zon3")
        self.le_dirr_poten_zon3.setEnabled(False)
        self.le_dirr_poten_zon3.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.le_dirr_poten_zon3, 3, 3, 1, 1)

        self.le_dirr_nvcr_zon7 = QLineEdit(self.gb_dirr_vz2)
        self.le_dirr_nvcr_zon7.setObjectName(u"le_dirr_nvcr_zon7")
        self.le_dirr_nvcr_zon7.setEnabled(False)
        self.le_dirr_nvcr_zon7.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.le_dirr_nvcr_zon7, 7, 2, 1, 1)

        self.le_dirr_lon_zon1 = QLineEdit(self.gb_dirr_vz2)
        self.le_dirr_lon_zon1.setObjectName(u"le_dirr_lon_zon1")
        self.le_dirr_lon_zon1.setEnabled(True)
        self.le_dirr_lon_zon1.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.le_dirr_lon_zon1, 1, 1, 1, 1)

        self.lb_dirr_zona7 = QLabel(self.gb_dirr_vz2)
        self.lb_dirr_zona7.setObjectName(u"lb_dirr_zona7")
        self.lb_dirr_zona7.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.lb_dirr_zona7, 7, 0, 1, 1)

        self.le_dirr_lon_zon3 = QLineEdit(self.gb_dirr_vz2)
        self.le_dirr_lon_zon3.setObjectName(u"le_dirr_lon_zon3")
        self.le_dirr_lon_zon3.setEnabled(False)
        self.le_dirr_lon_zon3.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.le_dirr_lon_zon3, 3, 1, 1, 1)

        self.lb_dirr_zona6 = QLabel(self.gb_dirr_vz2)
        self.lb_dirr_zona6.setObjectName(u"lb_dirr_zona6")
        self.lb_dirr_zona6.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.lb_dirr_zona6, 6, 0, 1, 1)

        self.le_dirr_lon_zon8 = QLineEdit(self.gb_dirr_vz2)
        self.le_dirr_lon_zon8.setObjectName(u"le_dirr_lon_zon8")
        self.le_dirr_lon_zon8.setEnabled(False)
        self.le_dirr_lon_zon8.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.le_dirr_lon_zon8, 8, 1, 1, 1)

        self.le_dirr_poten_zon1 = QLineEdit(self.gb_dirr_vz2)
        self.le_dirr_poten_zon1.setObjectName(u"le_dirr_poten_zon1")
        self.le_dirr_poten_zon1.setEnabled(True)
        self.le_dirr_poten_zon1.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.le_dirr_poten_zon1, 1, 3, 1, 1)

        self.le_dirr_nvcr_zon6 = QLineEdit(self.gb_dirr_vz2)
        self.le_dirr_nvcr_zon6.setObjectName(u"le_dirr_nvcr_zon6")
        self.le_dirr_nvcr_zon6.setEnabled(False)
        self.le_dirr_nvcr_zon6.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.le_dirr_nvcr_zon6, 6, 2, 1, 1)

        self.lb_dirr_zona = QLabel(self.gb_dirr_vz2)
        self.lb_dirr_zona.setObjectName(u"lb_dirr_zona")
        self.lb_dirr_zona.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.lb_dirr_zona, 0, 0, 1, 1)

        self.lb_dirr_zona2 = QLabel(self.gb_dirr_vz2)
        self.lb_dirr_zona2.setObjectName(u"lb_dirr_zona2")
        self.lb_dirr_zona2.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.lb_dirr_zona2, 2, 0, 1, 1)

        self.lb_dirr_zona10 = QLabel(self.gb_dirr_vz2)
        self.lb_dirr_zona10.setObjectName(u"lb_dirr_zona10")
        self.lb_dirr_zona10.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.lb_dirr_zona10, 10, 0, 1, 1)

        self.le_dirr_lon_zon10 = QLineEdit(self.gb_dirr_vz2)
        self.le_dirr_lon_zon10.setObjectName(u"le_dirr_lon_zon10")
        self.le_dirr_lon_zon10.setEnabled(False)
        self.le_dirr_lon_zon10.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.le_dirr_lon_zon10, 10, 1, 1, 1)

        self.le_dirr_nvcr_zon10 = QLineEdit(self.gb_dirr_vz2)
        self.le_dirr_nvcr_zon10.setObjectName(u"le_dirr_nvcr_zon10")
        self.le_dirr_nvcr_zon10.setEnabled(False)
        self.le_dirr_nvcr_zon10.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.le_dirr_nvcr_zon10, 10, 2, 1, 1)

        self.le_dirr_poten_zon10 = QLineEdit(self.gb_dirr_vz2)
        self.le_dirr_poten_zon10.setObjectName(u"le_dirr_poten_zon10")
        self.le_dirr_poten_zon10.setEnabled(False)
        self.le_dirr_poten_zon10.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.le_dirr_poten_zon10, 10, 3, 1, 1)


        self.verticalLayout_6.addWidget(self.gb_dirr_vz2)


        self.horizontalLayout_4.addWidget(self.gb_dirr_vz)

        self.gb_dirzvz_vz = QGroupBox(self.gbsw_cil_vz)
        self.gb_dirzvz_vz.setObjectName(u"gb_dirzvz_vz")
        self.verticalLayout_7 = QVBoxLayout(self.gb_dirzvz_vz)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.gb_dirzcil_vz1 = QGroupBox(self.gb_dirzvz_vz)
        self.gb_dirzcil_vz1.setObjectName(u"gb_dirzcil_vz1")
        self.horizontalLayout_9 = QHBoxLayout(self.gb_dirzcil_vz1)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.lb_dirzcil_numz = QLabel(self.gb_dirzcil_vz1)
        self.lb_dirzcil_numz.setObjectName(u"lb_dirzcil_numz")

        self.horizontalLayout_9.addWidget(self.lb_dirzcil_numz)

        self.sb_dirzcil_numz = QSpinBox(self.gb_dirzcil_vz1)
        self.sb_dirzcil_numz.setObjectName(u"sb_dirzcil_numz")
        self.sb_dirzcil_numz.setMinimum(1)
        self.sb_dirzcil_numz.setMaximum(10)
        self.sb_dirzcil_numz.setValue(1)

        self.horizontalLayout_9.addWidget(self.sb_dirzcil_numz)


        self.verticalLayout_7.addWidget(self.gb_dirzcil_vz1)

        self.gb_dirzcil_vz2 = QGroupBox(self.gb_dirzvz_vz)
        self.gb_dirzcil_vz2.setObjectName(u"gb_dirzcil_vz2")
        self.gridLayout_6 = QGridLayout(self.gb_dirzcil_vz2)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.lb_dirzcil_zona8 = QLabel(self.gb_dirzcil_vz2)
        self.lb_dirzcil_zona8.setObjectName(u"lb_dirzcil_zona8")
        self.lb_dirzcil_zona8.setAlignment(Qt.AlignCenter)

        self.gridLayout_6.addWidget(self.lb_dirzcil_zona8, 8, 0, 1, 1)

        self.le_dirzcil_lon_zon4 = QLineEdit(self.gb_dirzcil_vz2)
        self.le_dirzcil_lon_zon4.setObjectName(u"le_dirzcil_lon_zon4")
        self.le_dirzcil_lon_zon4.setEnabled(False)
        self.le_dirzcil_lon_zon4.setAlignment(Qt.AlignCenter)

        self.gridLayout_6.addWidget(self.le_dirzcil_lon_zon4, 4, 1, 1, 1)

        self.le_dirzcil_nvczcil_zon9 = QLineEdit(self.gb_dirzcil_vz2)
        self.le_dirzcil_nvczcil_zon9.setObjectName(u"le_dirzcil_nvczcil_zon9")
        self.le_dirzcil_nvczcil_zon9.setEnabled(False)
        self.le_dirzcil_nvczcil_zon9.setAlignment(Qt.AlignCenter)

        self.gridLayout_6.addWidget(self.le_dirzcil_nvczcil_zon9, 9, 2, 1, 1)

        self.lb_dirzcil_poten = QLabel(self.gb_dirzcil_vz2)
        self.lb_dirzcil_poten.setObjectName(u"lb_dirzcil_poten")
        self.lb_dirzcil_poten.setAlignment(Qt.AlignCenter)

        self.gridLayout_6.addWidget(self.lb_dirzcil_poten, 0, 3, 1, 1)

        self.le_dirzcil_nvczcil_zon2 = QLineEdit(self.gb_dirzcil_vz2)
        self.le_dirzcil_nvczcil_zon2.setObjectName(u"le_dirzcil_nvczcil_zon2")
        self.le_dirzcil_nvczcil_zon2.setEnabled(False)
        self.le_dirzcil_nvczcil_zon2.setAlignment(Qt.AlignCenter)

        self.gridLayout_6.addWidget(self.le_dirzcil_nvczcil_zon2, 2, 2, 1, 1)

        self.le_dirzcil_poten_zon2 = QLineEdit(self.gb_dirzcil_vz2)
        self.le_dirzcil_poten_zon2.setObjectName(u"le_dirzcil_poten_zon2")
        self.le_dirzcil_poten_zon2.setEnabled(False)
        self.le_dirzcil_poten_zon2.setAlignment(Qt.AlignCenter)

        self.gridLayout_6.addWidget(self.le_dirzcil_poten_zon2, 2, 3, 1, 1)

        self.le_dirzcil_nvczcil_zon4 = QLineEdit(self.gb_dirzcil_vz2)
        self.le_dirzcil_nvczcil_zon4.setObjectName(u"le_dirzcil_nvczcil_zon4")
        self.le_dirzcil_nvczcil_zon4.setEnabled(False)
        self.le_dirzcil_nvczcil_zon4.setAlignment(Qt.AlignCenter)

        self.gridLayout_6.addWidget(self.le_dirzcil_nvczcil_zon4, 4, 2, 1, 1)

        self.lb_dirzcil_zona5 = QLabel(self.gb_dirzcil_vz2)
        self.lb_dirzcil_zona5.setObjectName(u"lb_dirzcil_zona5")
        self.lb_dirzcil_zona5.setAlignment(Qt.AlignCenter)

        self.gridLayout_6.addWidget(self.lb_dirzcil_zona5, 5, 0, 1, 1)

        self.le_dirzcil_nvczcil_zon5 = QLineEdit(self.gb_dirzcil_vz2)
        self.le_dirzcil_nvczcil_zon5.setObjectName(u"le_dirzcil_nvczcil_zon5")
        self.le_dirzcil_nvczcil_zon5.setEnabled(False)
        self.le_dirzcil_nvczcil_zon5.setAlignment(Qt.AlignCenter)

        self.gridLayout_6.addWidget(self.le_dirzcil_nvczcil_zon5, 5, 2, 1, 1)

        self.le_dirzcil_lon_zon2 = QLineEdit(self.gb_dirzcil_vz2)
        self.le_dirzcil_lon_zon2.setObjectName(u"le_dirzcil_lon_zon2")
        self.le_dirzcil_lon_zon2.setEnabled(False)
        self.le_dirzcil_lon_zon2.setAlignment(Qt.AlignCenter)

        self.gridLayout_6.addWidget(self.le_dirzcil_lon_zon2, 2, 1, 1, 1)

        self.le_dirzcil_poten_zon4 = QLineEdit(self.gb_dirzcil_vz2)
        self.le_dirzcil_poten_zon4.setObjectName(u"le_dirzcil_poten_zon4")
        self.le_dirzcil_poten_zon4.setEnabled(False)
        self.le_dirzcil_poten_zon4.setAlignment(Qt.AlignCenter)

        self.gridLayout_6.addWidget(self.le_dirzcil_poten_zon4, 4, 3, 1, 1)

        self.le_dirzcil_poten_zon5 = QLineEdit(self.gb_dirzcil_vz2)
        self.le_dirzcil_poten_zon5.setObjectName(u"le_dirzcil_poten_zon5")
        self.le_dirzcil_poten_zon5.setEnabled(False)
        self.le_dirzcil_poten_zon5.setAlignment(Qt.AlignCenter)

        self.gridLayout_6.addWidget(self.le_dirzcil_poten_zon5, 5, 3, 1, 1)

        self.le_dirzcil_nvczcil_zon1 = QLineEdit(self.gb_dirzcil_vz2)
        self.le_dirzcil_nvczcil_zon1.setObjectName(u"le_dirzcil_nvczcil_zon1")
        self.le_dirzcil_nvczcil_zon1.setEnabled(True)
        self.le_dirzcil_nvczcil_zon1.setAlignment(Qt.AlignCenter)

        self.gridLayout_6.addWidget(self.le_dirzcil_nvczcil_zon1, 1, 2, 1, 1)

        self.lb_dirzcil_zona9 = QLabel(self.gb_dirzcil_vz2)
        self.lb_dirzcil_zona9.setObjectName(u"lb_dirzcil_zona9")
        self.lb_dirzcil_zona9.setAlignment(Qt.AlignCenter)

        self.gridLayout_6.addWidget(self.lb_dirzcil_zona9, 9, 0, 1, 1)

        self.lb_dirzcil_zona4 = QLabel(self.gb_dirzcil_vz2)
        self.lb_dirzcil_zona4.setObjectName(u"lb_dirzcil_zona4")
        self.lb_dirzcil_zona4.setAlignment(Qt.AlignCenter)

        self.gridLayout_6.addWidget(self.lb_dirzcil_zona4, 4, 0, 1, 1)

        self.le_dirzcil_lon_zon7 = QLineEdit(self.gb_dirzcil_vz2)
        self.le_dirzcil_lon_zon7.setObjectName(u"le_dirzcil_lon_zon7")
        self.le_dirzcil_lon_zon7.setEnabled(False)
        self.le_dirzcil_lon_zon7.setAlignment(Qt.AlignCenter)

        self.gridLayout_6.addWidget(self.le_dirzcil_lon_zon7, 7, 1, 1, 1)

        self.le_dirzcil_poten_zon7 = QLineEdit(self.gb_dirzcil_vz2)
        self.le_dirzcil_poten_zon7.setObjectName(u"le_dirzcil_poten_zon7")
        self.le_dirzcil_poten_zon7.setEnabled(False)
        self.le_dirzcil_poten_zon7.setAlignment(Qt.AlignCenter)

        self.gridLayout_6.addWidget(self.le_dirzcil_poten_zon7, 7, 3, 1, 1)

        self.le_dirzcil_poten_zon8 = QLineEdit(self.gb_dirzcil_vz2)
        self.le_dirzcil_poten_zon8.setObjectName(u"le_dirzcil_poten_zon8")
        self.le_dirzcil_poten_zon8.setEnabled(False)
        self.le_dirzcil_poten_zon8.setAlignment(Qt.AlignCenter)

        self.gridLayout_6.addWidget(self.le_dirzcil_poten_zon8, 8, 3, 1, 1)

        self.le_dirzcil_nvczcil_zon8 = QLineEdit(self.gb_dirzcil_vz2)
        self.le_dirzcil_nvczcil_zon8.setObjectName(u"le_dirzcil_nvczcil_zon8")
        self.le_dirzcil_nvczcil_zon8.setEnabled(False)
        self.le_dirzcil_nvczcil_zon8.setAlignment(Qt.AlignCenter)

        self.gridLayout_6.addWidget(self.le_dirzcil_nvczcil_zon8, 8, 2, 1, 1)

        self.le_dirzcil_lon_zon6 = QLineEdit(self.gb_dirzcil_vz2)
        self.le_dirzcil_lon_zon6.setObjectName(u"le_dirzcil_lon_zon6")
        self.le_dirzcil_lon_zon6.setEnabled(False)
        self.le_dirzcil_lon_zon6.setAlignment(Qt.AlignCenter)

        self.gridLayout_6.addWidget(self.le_dirzcil_lon_zon6, 6, 1, 1, 1)

        self.lb_dirzcil_zona1 = QLabel(self.gb_dirzcil_vz2)
        self.lb_dirzcil_zona1.setObjectName(u"lb_dirzcil_zona1")
        self.lb_dirzcil_zona1.setAlignment(Qt.AlignCenter)

        self.gridLayout_6.addWidget(self.lb_dirzcil_zona1, 1, 0, 1, 1)

        self.lb_dirzcil_zona3 = QLabel(self.gb_dirzcil_vz2)
        self.lb_dirzcil_zona3.setObjectName(u"lb_dirzcil_zona3")
        self.lb_dirzcil_zona3.setAlignment(Qt.AlignCenter)

        self.gridLayout_6.addWidget(self.lb_dirzcil_zona3, 3, 0, 1, 1)

        self.le_dirzcil_nvczcil_zon3 = QLineEdit(self.gb_dirzcil_vz2)
        self.le_dirzcil_nvczcil_zon3.setObjectName(u"le_dirzcil_nvczcil_zon3")
        self.le_dirzcil_nvczcil_zon3.setEnabled(False)
        self.le_dirzcil_nvczcil_zon3.setAlignment(Qt.AlignCenter)

        self.gridLayout_6.addWidget(self.le_dirzcil_nvczcil_zon3, 3, 2, 1, 1)

        self.le_dirzcil_lon_zon5 = QLineEdit(self.gb_dirzcil_vz2)
        self.le_dirzcil_lon_zon5.setObjectName(u"le_dirzcil_lon_zon5")
        self.le_dirzcil_lon_zon5.setEnabled(False)
        self.le_dirzcil_lon_zon5.setAlignment(Qt.AlignCenter)

        self.gridLayout_6.addWidget(self.le_dirzcil_lon_zon5, 5, 1, 1, 1)

        self.le_dirzcil_poten_zon6 = QLineEdit(self.gb_dirzcil_vz2)
        self.le_dirzcil_poten_zon6.setObjectName(u"le_dirzcil_poten_zon6")
        self.le_dirzcil_poten_zon6.setEnabled(False)
        self.le_dirzcil_poten_zon6.setAlignment(Qt.AlignCenter)

        self.gridLayout_6.addWidget(self.le_dirzcil_poten_zon6, 6, 3, 1, 1)

        self.le_dirzcil_lon_zon9 = QLineEdit(self.gb_dirzcil_vz2)
        self.le_dirzcil_lon_zon9.setObjectName(u"le_dirzcil_lon_zon9")
        self.le_dirzcil_lon_zon9.setEnabled(False)
        self.le_dirzcil_lon_zon9.setAlignment(Qt.AlignCenter)

        self.gridLayout_6.addWidget(self.le_dirzcil_lon_zon9, 9, 1, 1, 1)

        self.le_dirzcil_poten_zon9 = QLineEdit(self.gb_dirzcil_vz2)
        self.le_dirzcil_poten_zon9.setObjectName(u"le_dirzcil_poten_zon9")
        self.le_dirzcil_poten_zon9.setEnabled(False)
        self.le_dirzcil_poten_zon9.setAlignment(Qt.AlignCenter)

        self.gridLayout_6.addWidget(self.le_dirzcil_poten_zon9, 9, 3, 1, 1)

        self.lb_dirzcil_lon = QLabel(self.gb_dirzcil_vz2)
        self.lb_dirzcil_lon.setObjectName(u"lb_dirzcil_lon")
        self.lb_dirzcil_lon.setAlignment(Qt.AlignCenter)

        self.gridLayout_6.addWidget(self.lb_dirzcil_lon, 0, 1, 1, 1)

        self.lb_dirzcil_nvczcil = QLabel(self.gb_dirzcil_vz2)
        self.lb_dirzcil_nvczcil.setObjectName(u"lb_dirzcil_nvczcil")
        self.lb_dirzcil_nvczcil.setAlignment(Qt.AlignCenter)

        self.gridLayout_6.addWidget(self.lb_dirzcil_nvczcil, 0, 2, 1, 1)

        self.le_dirzcil_poten_zon3 = QLineEdit(self.gb_dirzcil_vz2)
        self.le_dirzcil_poten_zon3.setObjectName(u"le_dirzcil_poten_zon3")
        self.le_dirzcil_poten_zon3.setEnabled(False)
        self.le_dirzcil_poten_zon3.setAlignment(Qt.AlignCenter)

        self.gridLayout_6.addWidget(self.le_dirzcil_poten_zon3, 3, 3, 1, 1)

        self.le_dirzcil_nvczcil_zon7 = QLineEdit(self.gb_dirzcil_vz2)
        self.le_dirzcil_nvczcil_zon7.setObjectName(u"le_dirzcil_nvczcil_zon7")
        self.le_dirzcil_nvczcil_zon7.setEnabled(False)
        self.le_dirzcil_nvczcil_zon7.setAlignment(Qt.AlignCenter)

        self.gridLayout_6.addWidget(self.le_dirzcil_nvczcil_zon7, 7, 2, 1, 1)

        self.le_dirzcil_lon_zon1 = QLineEdit(self.gb_dirzcil_vz2)
        self.le_dirzcil_lon_zon1.setObjectName(u"le_dirzcil_lon_zon1")
        self.le_dirzcil_lon_zon1.setEnabled(True)
        self.le_dirzcil_lon_zon1.setAlignment(Qt.AlignCenter)

        self.gridLayout_6.addWidget(self.le_dirzcil_lon_zon1, 1, 1, 1, 1)

        self.lb_dirzcil_zona7 = QLabel(self.gb_dirzcil_vz2)
        self.lb_dirzcil_zona7.setObjectName(u"lb_dirzcil_zona7")
        self.lb_dirzcil_zona7.setAlignment(Qt.AlignCenter)

        self.gridLayout_6.addWidget(self.lb_dirzcil_zona7, 7, 0, 1, 1)

        self.le_dirzcil_lon_zon3 = QLineEdit(self.gb_dirzcil_vz2)
        self.le_dirzcil_lon_zon3.setObjectName(u"le_dirzcil_lon_zon3")
        self.le_dirzcil_lon_zon3.setEnabled(False)
        self.le_dirzcil_lon_zon3.setAlignment(Qt.AlignCenter)

        self.gridLayout_6.addWidget(self.le_dirzcil_lon_zon3, 3, 1, 1, 1)

        self.lb_dirzcil_zona6 = QLabel(self.gb_dirzcil_vz2)
        self.lb_dirzcil_zona6.setObjectName(u"lb_dirzcil_zona6")
        self.lb_dirzcil_zona6.setAlignment(Qt.AlignCenter)

        self.gridLayout_6.addWidget(self.lb_dirzcil_zona6, 6, 0, 1, 1)

        self.le_dirzcil_lon_zon8 = QLineEdit(self.gb_dirzcil_vz2)
        self.le_dirzcil_lon_zon8.setObjectName(u"le_dirzcil_lon_zon8")
        self.le_dirzcil_lon_zon8.setEnabled(False)
        self.le_dirzcil_lon_zon8.setAlignment(Qt.AlignCenter)

        self.gridLayout_6.addWidget(self.le_dirzcil_lon_zon8, 8, 1, 1, 1)

        self.le_dirzcil_poten_zon1 = QLineEdit(self.gb_dirzcil_vz2)
        self.le_dirzcil_poten_zon1.setObjectName(u"le_dirzcil_poten_zon1")
        self.le_dirzcil_poten_zon1.setEnabled(True)
        self.le_dirzcil_poten_zon1.setAlignment(Qt.AlignCenter)

        self.gridLayout_6.addWidget(self.le_dirzcil_poten_zon1, 1, 3, 1, 1)

        self.le_dirzcil_nvczcil_zon6 = QLineEdit(self.gb_dirzcil_vz2)
        self.le_dirzcil_nvczcil_zon6.setObjectName(u"le_dirzcil_nvczcil_zon6")
        self.le_dirzcil_nvczcil_zon6.setEnabled(False)
        self.le_dirzcil_nvczcil_zon6.setAlignment(Qt.AlignCenter)

        self.gridLayout_6.addWidget(self.le_dirzcil_nvczcil_zon6, 6, 2, 1, 1)

        self.lb_dirzcil_zona = QLabel(self.gb_dirzcil_vz2)
        self.lb_dirzcil_zona.setObjectName(u"lb_dirzcil_zona")
        self.lb_dirzcil_zona.setAlignment(Qt.AlignCenter)

        self.gridLayout_6.addWidget(self.lb_dirzcil_zona, 0, 0, 1, 1)

        self.lb_dirzcil_zona2 = QLabel(self.gb_dirzcil_vz2)
        self.lb_dirzcil_zona2.setObjectName(u"lb_dirzcil_zona2")
        self.lb_dirzcil_zona2.setAlignment(Qt.AlignCenter)

        self.gridLayout_6.addWidget(self.lb_dirzcil_zona2, 2, 0, 1, 1)

        self.lb_dirzcil_zona10 = QLabel(self.gb_dirzcil_vz2)
        self.lb_dirzcil_zona10.setObjectName(u"lb_dirzcil_zona10")
        self.lb_dirzcil_zona10.setAlignment(Qt.AlignCenter)

        self.gridLayout_6.addWidget(self.lb_dirzcil_zona10, 10, 0, 1, 1)

        self.le_dirzcil_lon_zon10 = QLineEdit(self.gb_dirzcil_vz2)
        self.le_dirzcil_lon_zon10.setObjectName(u"le_dirzcil_lon_zon10")
        self.le_dirzcil_lon_zon10.setEnabled(False)
        self.le_dirzcil_lon_zon10.setAlignment(Qt.AlignCenter)

        self.gridLayout_6.addWidget(self.le_dirzcil_lon_zon10, 10, 1, 1, 1)

        self.le_dirzcil_nvczcil_zon10 = QLineEdit(self.gb_dirzcil_vz2)
        self.le_dirzcil_nvczcil_zon10.setObjectName(u"le_dirzcil_nvczcil_zon10")
        self.le_dirzcil_nvczcil_zon10.setEnabled(False)
        self.le_dirzcil_nvczcil_zon10.setAlignment(Qt.AlignCenter)

        self.gridLayout_6.addWidget(self.le_dirzcil_nvczcil_zon10, 10, 2, 1, 1)

        self.le_dirzcil_poten_zon10 = QLineEdit(self.gb_dirzcil_vz2)
        self.le_dirzcil_poten_zon10.setObjectName(u"le_dirzcil_poten_zon10")
        self.le_dirzcil_poten_zon10.setEnabled(False)
        self.le_dirzcil_poten_zon10.setAlignment(Qt.AlignCenter)

        self.gridLayout_6.addWidget(self.le_dirzcil_poten_zon10, 10, 3, 1, 1)


        self.verticalLayout_7.addWidget(self.gb_dirzcil_vz2)


        self.horizontalLayout_4.addWidget(self.gb_dirzvz_vz)

        self.gbsw_malla.addWidget(self.gbsw_cil_vz)

        self.verticalLayout.addWidget(self.gbsw_malla)


        self.retranslateUi(malla_window)

        self.gbsw_malla.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(malla_window)
    # setupUi

    def retranslateUi(self, malla_window):
        malla_window.setWindowTitle(QCoreApplication.translate("malla_window", u"Malla - PrePRODIC3D", None))
        self.gb_malla.setTitle(QCoreApplication.translate("malla_window", u"Malla", None))
        self.lb_tipocoord.setText(QCoreApplication.translate("malla_window", u"Coordenadas:", None))
        self.cb_coord_type.setItemText(0, QCoreApplication.translate("malla_window", u"Cartesianas", None))
        self.cb_coord_type.setItemText(1, QCoreApplication.translate("malla_window", u"Cilindricas", None))

        self.lb_tipozonas.setText(QCoreApplication.translate("malla_window", u"Numero de zonas:  ", None))
        self.cb_zone_type.setItemText(0, QCoreApplication.translate("malla_window", u"Zona \u00fanica", None))
        self.cb_zone_type.setItemText(1, QCoreApplication.translate("malla_window", u"Varias zonas", None))

        self.label.setText(QCoreApplication.translate("malla_window", u"Sistema:", None))
        self.cb_system_type.setItemText(0, QCoreApplication.translate("malla_window", u"Abierto", None))
        self.cb_system_type.setItemText(1, QCoreApplication.translate("malla_window", u"Cerrado", None))

        self.gb_malla2_dirx.setTitle(QCoreApplication.translate("malla_window", u"Direcci\u00f3n X", None))
        self.lb_xlon.setText(QCoreApplication.translate("malla_window", u"X Longitud:", None))
        self.lb_nvcx.setText(QCoreApplication.translate("malla_window", u"NVCX:", None))
        self.lb_potenciax.setText(QCoreApplication.translate("malla_window", u"Potencia:", None))
        self.gb_malla2_diry.setTitle(QCoreApplication.translate("malla_window", u"Direcci\u00f3n Y", None))
        self.lb_ylon.setText(QCoreApplication.translate("malla_window", u"Y Longitud:", None))
        self.lb_nvcy.setText(QCoreApplication.translate("malla_window", u"NVCY", None))
        self.lb_potenciay.setText(QCoreApplication.translate("malla_window", u"Potencia:", None))
        self.gb_malla2_dirz.setTitle(QCoreApplication.translate("malla_window", u"Direcci\u00f3n Z", None))
        self.lb_zlon.setText(QCoreApplication.translate("malla_window", u"Z Longitud: ", None))
        self.lb_nvcz.setText(QCoreApplication.translate("malla_window", u"NVCZ", None))
        self.lb_potenciaz.setText(QCoreApplication.translate("malla_window", u"Potencia:", None))
        self.gb_dirtita.setTitle(QCoreApplication.translate("malla_window", u"Direcci\u00f3n \u03b8", None))
        self.lb_titalon.setText(QCoreApplication.translate("malla_window", u"\u03b8 Longitud:", None))
        self.lb_nvctita.setText(QCoreApplication.translate("malla_window", u"NVC\u03b8:", None))
        self.lb_potenciatita.setText(QCoreApplication.translate("malla_window", u"Potencia:", None))
        self.gb_dirr.setTitle(QCoreApplication.translate("malla_window", u"Direcci\u00f3n R", None))
        self.lb_rlon.setText(QCoreApplication.translate("malla_window", u"R Longitud:", None))
        self.lb_nvcr.setText(QCoreApplication.translate("malla_window", u"NVCR:", None))
        self.lb_potenciar.setText(QCoreApplication.translate("malla_window", u"Potencia:", None))
        self.lb_rini.setText(QCoreApplication.translate("malla_window", u"R Inicial:", None))
        self.gb_dirz.setTitle(QCoreApplication.translate("malla_window", u"Direcci\u00f3n Z", None))
        self.lb_zloncil.setText(QCoreApplication.translate("malla_window", u"Z Longitud:", None))
        self.lb_nvczcil.setText(QCoreApplication.translate("malla_window", u"NVCZ:", None))
        self.lb_potenciazcil.setText(QCoreApplication.translate("malla_window", u"Potencia:", None))
        self.gb_dirx_vz.setTitle(QCoreApplication.translate("malla_window", u"Direcci\u00f3n X", None))
        self.gb_dirx_vz1.setTitle("")
        self.lb_dirx_numz.setText(QCoreApplication.translate("malla_window", u"Zonas en X (2-10):", None))
        self.gb_dirx_vz2.setTitle("")
        self.lb_dirx_zon8.setText(QCoreApplication.translate("malla_window", u"8", None))
        self.le_dirx_lon_zon4.setText("")
        self.le_dirx_lon_zon4.setPlaceholderText("")
        self.le_dirx_nvcx_zon9.setText("")
        self.le_dirx_nvcx_zon9.setPlaceholderText("")
        self.lb_dirx_poten.setText(QCoreApplication.translate("malla_window", u"Potencia", None))
        self.le_dirx_nvcx_zon2.setText("")
        self.le_dirx_poten_zon2.setText("")
        self.le_dirx_nvcx_zon4.setText("")
        self.le_dirx_nvcx_zon4.setPlaceholderText("")
        self.lb_dirx_zon5.setText(QCoreApplication.translate("malla_window", u"5", None))
        self.le_dirx_nvcx_zon5.setText("")
        self.le_dirx_nvcx_zon5.setPlaceholderText("")
        self.le_dirx_lon_zon2.setText("")
        self.le_dirx_poten_zon4.setText("")
        self.le_dirx_poten_zon4.setPlaceholderText("")
        self.le_dirx_poten_zon5.setText("")
        self.le_dirx_poten_zon5.setPlaceholderText("")
        self.le_dirx_nvcx_zon1.setText("")
        self.lb_dirx_zon9.setText(QCoreApplication.translate("malla_window", u"9", None))
        self.lb_dirx_zon4.setText(QCoreApplication.translate("malla_window", u"4", None))
        self.le_dirx_lon_zon7.setText("")
        self.le_dirx_lon_zon7.setPlaceholderText("")
        self.le_dirx_poten_zon7.setText("")
        self.le_dirx_poten_zon7.setPlaceholderText("")
        self.le_dirx_poten_zon8.setText("")
        self.le_dirx_poten_zon8.setPlaceholderText("")
        self.le_dirx_nvcx_zon8.setText("")
        self.le_dirx_nvcx_zon8.setPlaceholderText("")
        self.le_dirx_lon_zon6.setText("")
        self.le_dirx_lon_zon6.setPlaceholderText("")
        self.lb_dirx_zon1.setText(QCoreApplication.translate("malla_window", u"1", None))
        self.lb_dirx_zon3.setText(QCoreApplication.translate("malla_window", u"3", None))
        self.le_dirx_nvcx_zon3.setText("")
        self.le_dirx_nvcx_zon3.setPlaceholderText("")
        self.le_dirx_lon_zon5.setText("")
        self.le_dirx_lon_zon5.setPlaceholderText("")
        self.le_dirx_poten_zon6.setText("")
        self.le_dirx_poten_zon6.setPlaceholderText("")
        self.le_dirx_lon_zon9.setText("")
        self.le_dirx_lon_zon9.setPlaceholderText("")
        self.le_dirx_poten_zon9.setText("")
        self.le_dirx_poten_zon9.setPlaceholderText("")
        self.lb_dirx_lon.setText(QCoreApplication.translate("malla_window", u"Longitud", None))
        self.lb_dirx_nvcx.setText(QCoreApplication.translate("malla_window", u"NCVX", None))
        self.le_dirx_poten_zon3.setText("")
        self.le_dirx_poten_zon3.setPlaceholderText("")
        self.le_dirx_nvcx_zon7.setText("")
        self.le_dirx_nvcx_zon7.setPlaceholderText("")
        self.le_dirx_lon_zon1.setText("")
        self.lb_dirx_zon7.setText(QCoreApplication.translate("malla_window", u"7", None))
        self.le_dirx_lon_zon3.setText("")
        self.le_dirx_lon_zon3.setPlaceholderText("")
        self.lb_dirx_zon6.setText(QCoreApplication.translate("malla_window", u"6", None))
        self.le_dirx_lon_zon8.setText("")
        self.le_dirx_lon_zon8.setPlaceholderText("")
        self.le_dirx_poten_zon1.setText("")
        self.le_dirx_nvcx_zon6.setText("")
        self.le_dirx_nvcx_zon6.setPlaceholderText("")
        self.lb_dirx_zona.setText(QCoreApplication.translate("malla_window", u"Zona", None))
        self.lb_dirx_zon2.setText(QCoreApplication.translate("malla_window", u"2", None))
        self.lb_dirx_zon10.setText(QCoreApplication.translate("malla_window", u"10", None))
        self.le_dirx_lon_zon10.setText("")
        self.le_dirx_lon_zon10.setPlaceholderText("")
        self.le_dirx_nvcx_zon10.setText("")
        self.le_dirx_nvcx_zon10.setPlaceholderText("")
        self.le_dirx_poten_zon10.setText("")
        self.le_dirx_poten_zon10.setPlaceholderText("")
        self.gb_diry_vz.setTitle(QCoreApplication.translate("malla_window", u"Direcci\u00f3n Y", None))
        self.gb_diry_vz1.setTitle("")
        self.lb_diry_numz.setText(QCoreApplication.translate("malla_window", u"Zonas en Y (2-10):", None))
        self.gb_diry_vz2.setTitle("")
        self.lb_diry_zona8.setText(QCoreApplication.translate("malla_window", u"8", None))
        self.le_diry_lon_zon4.setText("")
        self.le_diry_nvcy_zon9.setText("")
        self.lb_diry_poten.setText(QCoreApplication.translate("malla_window", u"Potencia", None))
        self.le_diry_nvcy_zon2.setText("")
        self.le_diry_poten_zon2.setText("")
        self.le_diry_nvcy_zon4.setText("")
        self.lb_diry_zona5.setText(QCoreApplication.translate("malla_window", u"5", None))
        self.le_diry_nvcy_zon5.setText("")
        self.le_diry_lon_zon2.setText("")
        self.le_diry_poten_zon4.setText("")
        self.le_diry_poten_zon5.setText("")
        self.le_diry_nvcy_zon1.setText("")
        self.lb_diry_zona9.setText(QCoreApplication.translate("malla_window", u"9", None))
        self.lb_diry_zona4.setText(QCoreApplication.translate("malla_window", u"4", None))
        self.le_diry_lon_zon7.setText("")
        self.le_diry_poten_zon7.setText("")
        self.le_diry_poten_zon8.setText("")
        self.le_diry_nvcy_zon8.setText("")
        self.le_diry_lon_zon6.setText("")
        self.lb_diry_zona1.setText(QCoreApplication.translate("malla_window", u"1", None))
        self.lb_diry_zona3.setText(QCoreApplication.translate("malla_window", u"3", None))
        self.le_diry_nvcy_zon3.setText("")
        self.le_diry_lon_zon5.setText("")
        self.le_diry_poten_zon6.setText("")
        self.le_diry_lon_zon9.setText("")
        self.le_diry_poten_zon9.setText("")
        self.lb_diry_lon.setText(QCoreApplication.translate("malla_window", u"Longitud", None))
        self.lb_diry_nvcy.setText(QCoreApplication.translate("malla_window", u"NCVY", None))
        self.le_diry_poten_zon3.setText("")
        self.le_diry_nvcy_zon7.setText("")
        self.le_diry_lon_zon1.setText("")
        self.lb_diry_zona7.setText(QCoreApplication.translate("malla_window", u"7", None))
        self.le_diry_lon_zon3.setText("")
        self.lb_diry_zona6.setText(QCoreApplication.translate("malla_window", u"6", None))
        self.le_diry_lon_zon8.setText("")
        self.le_diry_poten_zon1.setText("")
        self.le_diry_nvcy_zon6.setText("")
        self.lb_diry_zona.setText(QCoreApplication.translate("malla_window", u"Zona", None))
        self.lb_diry_zona2.setText(QCoreApplication.translate("malla_window", u"2", None))
        self.lb_diry_zona10.setText(QCoreApplication.translate("malla_window", u"10", None))
        self.le_diry_lon_zon10.setText("")
        self.le_diry_nvcy_zon10.setText("")
        self.le_diry_poten_zon10.setText("")
        self.gb_dirz_vz.setTitle(QCoreApplication.translate("malla_window", u"Direcci\u00f3n Z", None))
        self.gb_dirz_vz1.setTitle("")
        self.lb_dirz_numz.setText(QCoreApplication.translate("malla_window", u"Zonas en Z (2-10):", None))
        self.gb_dirz_vz2.setTitle("")
        self.lb_dirz_zona8.setText(QCoreApplication.translate("malla_window", u"8", None))
        self.le_dirz_lon_zon4.setText("")
        self.le_dirz_nvcz_zon9.setText("")
        self.lb_dirz_poten.setText(QCoreApplication.translate("malla_window", u"Potencia", None))
        self.le_dirz_nvcz_zon2.setText("")
        self.le_dirz_poten_zon2.setText("")
        self.le_dirz_nvcz_zon4.setText("")
        self.lb_dirz_zona5.setText(QCoreApplication.translate("malla_window", u"5", None))
        self.le_dirz_nvcz_zon5.setText("")
        self.le_dirz_lon_zon2.setText("")
        self.le_dirz_poten_zon4.setText("")
        self.le_dirz_poten_zon5.setText("")
        self.le_dirz_nvcz_zon1.setText("")
        self.lb_dirz_zona9.setText(QCoreApplication.translate("malla_window", u"9", None))
        self.lb_dirz_zona4.setText(QCoreApplication.translate("malla_window", u"4", None))
        self.le_dirz_lon_zon7.setText("")
        self.le_dirz_poten_zon7.setText("")
        self.le_dirz_poten_zon8.setText("")
        self.le_dirz_nvcz_zon8.setText("")
        self.le_dirz_lon_zon6.setText("")
        self.lb_dirz_zona1.setText(QCoreApplication.translate("malla_window", u"1", None))
        self.lb_dirz_zona3.setText(QCoreApplication.translate("malla_window", u"3", None))
        self.le_dirz_nvcz_zon3.setText("")
        self.le_dirz_lon_zon5.setText("")
        self.le_dirz_poten_zon6.setText("")
        self.le_dirz_lon_zon9.setText("")
        self.le_dirz_poten_zon9.setText("")
        self.lb_dirz_lon.setText(QCoreApplication.translate("malla_window", u"Longitud", None))
        self.lb_dirz_nvcz.setText(QCoreApplication.translate("malla_window", u"NCVZ", None))
        self.le_dirz_poten_zon3.setText("")
        self.le_dirz_nvcz_zon7.setText("")
        self.le_dirz_lon_zon1.setText("")
        self.lb_dirz_zona7.setText(QCoreApplication.translate("malla_window", u"7", None))
        self.le_dirz_lon_zon3.setText("")
        self.lb_dirz_zona6.setText(QCoreApplication.translate("malla_window", u"6", None))
        self.le_dirz_lon_zon8.setText("")
        self.le_dirz_poten_zon1.setText("")
        self.le_dirz_nvcz_zon6.setText("")
        self.lb_dirz_zona.setText(QCoreApplication.translate("malla_window", u"Zona", None))
        self.lb_dirz_zona2.setText(QCoreApplication.translate("malla_window", u"2", None))
        self.lb_dirz_zona10.setText(QCoreApplication.translate("malla_window", u"10", None))
        self.le_dirz_lon_zon10.setText("")
        self.le_dirz_nvcz_zon10.setText("")
        self.le_dirz_poten_zon10.setText("")
        self.gb_dirtita_vz.setTitle(QCoreApplication.translate("malla_window", u"Direcci\u00f3n \u03b8", None))
        self.gb_dirtita_vz1.setTitle("")
        self.lb_dirtita_numz.setText(QCoreApplication.translate("malla_window", u"Zonas en \u03b8 (2-10):", None))
        self.gb_dirtita_vz2.setTitle("")
        self.lb_dirtita_zona8.setText(QCoreApplication.translate("malla_window", u"8", None))
        self.le_dirtita_lon_zon4.setText("")
        self.le_dirtita_nvctita_zon9.setText("")
        self.lb_dirtita_poten.setText(QCoreApplication.translate("malla_window", u"Potencia", None))
        self.le_dirtita_nvctita_zon2.setInputMask("")
        self.le_dirtita_nvctita_zon2.setText("")
        self.le_dirtita_poten_zon2.setInputMask("")
        self.le_dirtita_poten_zon2.setText("")
        self.le_dirtita_nvctita_zon4.setText("")
        self.lb_dirtita_zona5.setText(QCoreApplication.translate("malla_window", u"5", None))
        self.le_dirtita_nvctita_zon5.setText("")
        self.le_dirtita_lon_zon2.setInputMask("")
        self.le_dirtita_lon_zon2.setText("")
        self.le_dirtita_poten_zon4.setText("")
        self.le_dirtita_poten_zon5.setText("")
        self.le_dirtita_nvctita_zon1.setInputMask("")
        self.le_dirtita_nvctita_zon1.setText("")
        self.lb_dirtita_zona9.setText(QCoreApplication.translate("malla_window", u"9", None))
        self.lb_dirtita_zona4.setText(QCoreApplication.translate("malla_window", u"4", None))
        self.le_dirtita_lon_zon7.setText("")
        self.le_dirtita_poten_zon7.setText("")
        self.le_dirtita_poten_zon8.setText("")
        self.le_dirtita_nvctita_zon8.setText("")
        self.le_dirtita_lon_zon6.setText("")
        self.lb_dirtita_zona1.setText(QCoreApplication.translate("malla_window", u"1", None))
        self.lb_dirtita_zona3.setText(QCoreApplication.translate("malla_window", u"3", None))
        self.le_dirtita_nvctita_zon3.setText("")
        self.le_dirtita_lon_zon5.setText("")
        self.le_dirtita_poten_zon6.setText("")
        self.le_dirtita_lon_zon9.setText("")
        self.le_dirtita_poten_zon9.setText("")
        self.lb_dirtita_lon.setText(QCoreApplication.translate("malla_window", u"Longitud", None))
        self.lb_dirtita_nvctita.setText(QCoreApplication.translate("malla_window", u"NCV\u03b8", None))
        self.le_dirtita_poten_zon3.setText("")
        self.le_dirtita_nvctita_zon7.setText("")
        self.le_dirtita_lon_zon1.setInputMask("")
        self.le_dirtita_lon_zon1.setText("")
        self.lb_dirtita_zona7.setText(QCoreApplication.translate("malla_window", u"7", None))
        self.le_dirtita_lon_zon3.setText("")
        self.lb_dirtita_zona6.setText(QCoreApplication.translate("malla_window", u"6", None))
        self.le_dirtita_lon_zon8.setText("")
        self.le_dirtita_poten_zon1.setInputMask("")
        self.le_dirtita_poten_zon1.setText("")
        self.le_dirtita_nvctita_zon6.setText("")
        self.lb_dirtita_zona.setText(QCoreApplication.translate("malla_window", u"Zona", None))
        self.lb_dirtita_zona2.setText(QCoreApplication.translate("malla_window", u"2", None))
        self.lb_dirtita_zona10.setText(QCoreApplication.translate("malla_window", u"10", None))
        self.le_dirtita_lon_zon10.setText("")
        self.le_dirtita_nvctita_zon10.setText("")
        self.le_dirtita_poten_zon10.setText("")
        self.gb_dirr_vz.setTitle(QCoreApplication.translate("malla_window", u"Direcci\u00f3n R", None))
        self.gb_dirr_vz1.setTitle("")
        self.lb_dirr_numz.setText(QCoreApplication.translate("malla_window", u"Zonas en Y (2-10):", None))
        self.lb_dirr_inidom.setText(QCoreApplication.translate("malla_window", u"R Inicial", None))
        self.le_dirr_inidom.setText(QCoreApplication.translate("malla_window", u"0", None))
        self.gb_dirr_vz2.setTitle("")
        self.lb_dirr_zona8.setText(QCoreApplication.translate("malla_window", u"8", None))
        self.le_dirr_lon_zon4.setText("")
        self.le_dirr_nvcr_zon9.setText("")
        self.lb_dirr_poten.setText(QCoreApplication.translate("malla_window", u"Potencia", None))
        self.le_dirr_nvcr_zon2.setText("")
        self.le_dirr_poten_zon2.setText("")
        self.le_dirr_nvcr_zon4.setText("")
        self.lb_dirr_zona5.setText(QCoreApplication.translate("malla_window", u"5", None))
        self.le_dirr_nvcr_zon5.setText("")
        self.le_dirr_lon_zon2.setText("")
        self.le_dirr_poten_zon4.setText("")
        self.le_dirr_poten_zon5.setText("")
        self.le_dirr_nvcr_zon1.setText("")
        self.lb_dirr_zona9.setText(QCoreApplication.translate("malla_window", u"9", None))
        self.lb_dirr_zona4.setText(QCoreApplication.translate("malla_window", u"4", None))
        self.le_dirr_lon_zon7.setText("")
        self.le_dirr_poten_zon7.setText("")
        self.le_dirr_poten_zon8.setText("")
        self.le_dirr_nvcr_zon8.setText("")
        self.le_dirr_lon_zon6.setText("")
        self.lb_dirr_zona1.setText(QCoreApplication.translate("malla_window", u"1", None))
        self.lb_dirr_zona3.setText(QCoreApplication.translate("malla_window", u"3", None))
        self.le_dirr_nvcr_zon3.setText("")
        self.le_dirr_lon_zon5.setText("")
        self.le_dirr_poten_zon6.setText("")
        self.le_dirr_lon_zon9.setText("")
        self.le_dirr_poten_zon9.setText("")
        self.lb_dirr_lon.setText(QCoreApplication.translate("malla_window", u"Longitud", None))
        self.lb_dirr_nvcr.setText(QCoreApplication.translate("malla_window", u"NCVR", None))
        self.le_dirr_poten_zon3.setText("")
        self.le_dirr_nvcr_zon7.setText("")
        self.le_dirr_lon_zon1.setText("")
        self.lb_dirr_zona7.setText(QCoreApplication.translate("malla_window", u"7", None))
        self.le_dirr_lon_zon3.setText("")
        self.lb_dirr_zona6.setText(QCoreApplication.translate("malla_window", u"6", None))
        self.le_dirr_lon_zon8.setText("")
        self.le_dirr_poten_zon1.setText("")
        self.le_dirr_nvcr_zon6.setText("")
        self.lb_dirr_zona.setText(QCoreApplication.translate("malla_window", u"Zona", None))
        self.lb_dirr_zona2.setText(QCoreApplication.translate("malla_window", u"2", None))
        self.lb_dirr_zona10.setText(QCoreApplication.translate("malla_window", u"10", None))
        self.le_dirr_lon_zon10.setText("")
        self.le_dirr_nvcr_zon10.setText("")
        self.le_dirr_poten_zon10.setText("")
        self.gb_dirzvz_vz.setTitle(QCoreApplication.translate("malla_window", u"Direcci\u00f3n Z", None))
        self.gb_dirzcil_vz1.setTitle("")
        self.lb_dirzcil_numz.setText(QCoreApplication.translate("malla_window", u"Zonas en Z (2-10):", None))
        self.gb_dirzcil_vz2.setTitle("")
        self.lb_dirzcil_zona8.setText(QCoreApplication.translate("malla_window", u"8", None))
        self.le_dirzcil_lon_zon4.setText("")
        self.le_dirzcil_nvczcil_zon9.setText("")
        self.lb_dirzcil_poten.setText(QCoreApplication.translate("malla_window", u"Potencia", None))
        self.le_dirzcil_nvczcil_zon2.setText("")
        self.le_dirzcil_poten_zon2.setText("")
        self.le_dirzcil_nvczcil_zon4.setText("")
        self.lb_dirzcil_zona5.setText(QCoreApplication.translate("malla_window", u"5", None))
        self.le_dirzcil_nvczcil_zon5.setText("")
        self.le_dirzcil_lon_zon2.setText("")
        self.le_dirzcil_poten_zon4.setText("")
        self.le_dirzcil_poten_zon5.setText("")
        self.le_dirzcil_nvczcil_zon1.setText("")
        self.lb_dirzcil_zona9.setText(QCoreApplication.translate("malla_window", u"9", None))
        self.lb_dirzcil_zona4.setText(QCoreApplication.translate("malla_window", u"4", None))
        self.le_dirzcil_lon_zon7.setText("")
        self.le_dirzcil_poten_zon7.setText("")
        self.le_dirzcil_poten_zon8.setText("")
        self.le_dirzcil_nvczcil_zon8.setText("")
        self.le_dirzcil_lon_zon6.setText("")
        self.lb_dirzcil_zona1.setText(QCoreApplication.translate("malla_window", u"1", None))
        self.lb_dirzcil_zona3.setText(QCoreApplication.translate("malla_window", u"3", None))
        self.le_dirzcil_nvczcil_zon3.setText("")
        self.le_dirzcil_lon_zon5.setText("")
        self.le_dirzcil_poten_zon6.setText("")
        self.le_dirzcil_lon_zon9.setText("")
        self.le_dirzcil_poten_zon9.setText("")
        self.lb_dirzcil_lon.setText(QCoreApplication.translate("malla_window", u"Longitud", None))
        self.lb_dirzcil_nvczcil.setText(QCoreApplication.translate("malla_window", u"NCVZ", None))
        self.le_dirzcil_poten_zon3.setText("")
        self.le_dirzcil_nvczcil_zon7.setText("")
        self.le_dirzcil_lon_zon1.setText("")
        self.lb_dirzcil_zona7.setText(QCoreApplication.translate("malla_window", u"7", None))
        self.le_dirzcil_lon_zon3.setText("")
        self.lb_dirzcil_zona6.setText(QCoreApplication.translate("malla_window", u"6", None))
        self.le_dirzcil_lon_zon8.setText("")
        self.le_dirzcil_poten_zon1.setText("")
        self.le_dirzcil_nvczcil_zon6.setText("")
        self.lb_dirzcil_zona.setText(QCoreApplication.translate("malla_window", u"Zona", None))
        self.lb_dirzcil_zona2.setText(QCoreApplication.translate("malla_window", u"2", None))
        self.lb_dirzcil_zona10.setText(QCoreApplication.translate("malla_window", u"10", None))
        self.le_dirzcil_lon_zon10.setText("")
        self.le_dirzcil_nvczcil_zon10.setText("")
        self.le_dirzcil_poten_zon10.setText("")
    # retranslateUi

