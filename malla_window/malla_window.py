import sys
from PySide6 import QtWidgets as qtw

from malla_window.ui.malla_window_ui import Ui_malla_window
from config_manager import ConfigManager


class MallaWindow(qtw.QDialog, Ui_malla_window):
    def __init__(self, config_manager):
        super().__init__()
        self.setupUi(self)
        self.config_manager = config_manager

        self.cb_tipocoord.currentTextChanged.connect(self.changeZonas)
        self.cb_tipozonas.currentTextChanged.connect(self.changeZonas)

        self.cb_tipocoord.currentTextChanged.connect(self.on_coordinate_system_changed)

        self.cb_tipozonas.currentTextChanged.connect(self.on_zones_system_changed)

        ##############################################################################################
        # CONEXION DE WIDGETS ZONA UNICA - CARTESIANA

        self.le_xlon.textChanged.connect(self.update_cart_xl)

        self.le_nvcx.textChanged.connect(self.update_cart_nvcx)

        self.le_potenciax.textChanged.connect(self.update_cart_potenciax)

        self.le_ylon.textChanged.connect(self.update_cart_yl)

        self.le_nvcy.textChanged.connect(self.update_cart_nvcy)

        self.le_potenciay.textChanged.connect(self.update_cart_potenciay)

        self.le_zlon.textChanged.connect(self.update_cart_zl)

        self.le_nvcz.textChanged.connect(self.update_cart_nvcz)

        self.le_potenciaz.textChanged.connect(self.update_cart_potenciaz)

        ##############################################################################################
        # CONEXION DE WIDGETS ZONA UNICA - CILINDRICA

        self.le_titalon.textChanged.connect(self.update_cil_tital)

        self.le_nvctita.textChanged.connect(self.update_cil_nvctita)

        self.le_potenciatita.textChanged.connect(self.update_cil_potenciatita)

        self.le_rini.textChanged.connect(self.update_cil_rini_zu)

        self.le_rlon.textChanged.connect(self.update_cil_rl)

        self.le_nvcr.textChanged.connect(self.update_cil_nvcr)

        self.le_potenciar.textChanged.connect(self.update_cil_potenciar)

        self.le_zloncil.textChanged.connect(self.update_cil_zl)

        self.le_nvczcil.textChanged.connect(self.update_cil_nvcz)

        self.le_potenciazcil.textChanged.connect(self.update_cil_potenciaz)

        #####################################################################################
        # CONEXION DE WIDGETS VARIAS ZONAS - CARTESIANA

        # -COORDENADA X (CARTESIANA)

        self.sb_dirx_numz.textChanged.connect(self.update_cart_nzx)

        self.le_dirx_lon_zon1.textChanged.connect(self.update_cart_xzone_1)
        self.le_dirx_nvcx_zon1.textChanged.connect(self.update_cart_ncvx_1)
        self.le_dirx_poten_zon1.textChanged.connect(self.update_cart_powerx_1)

        self.le_dirx_lon_zon2.textChanged.connect(self.update_cart_xzone_2)
        self.le_dirx_nvcx_zon2.textChanged.connect(self.update_cart_ncvx_2)
        self.le_dirx_poten_zon2.textChanged.connect(self.update_cart_powerx_2)

        self.le_dirx_lon_zon3.textChanged.connect(self.update_cart_xzone_3)
        self.le_dirx_nvcx_zon3.textChanged.connect(self.update_cart_ncvx_3)
        self.le_dirx_poten_zon3.textChanged.connect(self.update_cart_powerx_3)

        self.le_dirx_lon_zon4.textChanged.connect(self.update_cart_xzone_4)
        self.le_dirx_nvcx_zon4.textChanged.connect(self.update_cart_ncvx_4)
        self.le_dirx_poten_zon4.textChanged.connect(self.update_cart_powerx_4)

        self.le_dirx_lon_zon5.textChanged.connect(self.update_cart_xzone_5)
        self.le_dirx_nvcx_zon5.textChanged.connect(self.update_cart_ncvx_5)
        self.le_dirx_poten_zon5.textChanged.connect(self.update_cart_powerx_5)

        self.le_dirx_lon_zon6.textChanged.connect(self.update_cart_xzone_6)
        self.le_dirx_nvcx_zon6.textChanged.connect(self.update_cart_ncvx_6)
        self.le_dirx_poten_zon6.textChanged.connect(self.update_cart_powerx_6)

        self.le_dirx_lon_zon7.textChanged.connect(self.update_cart_xzone_7)
        self.le_dirx_nvcx_zon7.textChanged.connect(self.update_cart_ncvx_7)
        self.le_dirx_poten_zon7.textChanged.connect(self.update_cart_powerx_7)

        self.le_dirx_lon_zon8.textChanged.connect(self.update_cart_xzone_8)
        self.le_dirx_nvcx_zon8.textChanged.connect(self.update_cart_ncvx_8)
        self.le_dirx_poten_zon8.textChanged.connect(self.update_cart_powerx_8)

        self.le_dirx_lon_zon9.textChanged.connect(self.update_cart_xzone_9)
        self.le_dirx_nvcx_zon9.textChanged.connect(self.update_cart_ncvx_9)
        self.le_dirx_poten_zon9.textChanged.connect(self.update_cart_powerx_9)

        self.le_dirx_lon_zon10.textChanged.connect(self.update_cart_xzone_10)
        self.le_dirx_nvcx_zon10.textChanged.connect(self.update_cart_ncvx_10)
        self.le_dirx_poten_zon10.textChanged.connect(self.update_cart_powerx_10)

        # -COORDENADA Y (CARTESIANA)

        self.sb_diry_numz.textChanged.connect(self.update_cart_nzy)

        self.le_diry_lon_zon1.textChanged.connect(self.update_cart_yzone_1)
        self.le_diry_nvcy_zon1.textChanged.connect(self.update_cart_ncvy_1)
        self.le_diry_poten_zon1.textChanged.connect(self.update_cart_powery_1)

        self.le_diry_lon_zon2.textChanged.connect(self.update_cart_yzone_2)
        self.le_diry_nvcy_zon2.textChanged.connect(self.update_cart_ncvy_2)
        self.le_diry_poten_zon2.textChanged.connect(self.update_cart_powery_2)

        self.le_diry_lon_zon3.textChanged.connect(self.update_cart_yzone_3)
        self.le_diry_nvcy_zon3.textChanged.connect(self.update_cart_ncvy_3)
        self.le_diry_poten_zon3.textChanged.connect(self.update_cart_powery_3)

        self.le_diry_lon_zon4.textChanged.connect(self.update_cart_yzone_4)
        self.le_diry_nvcy_zon4.textChanged.connect(self.update_cart_ncvy_4)
        self.le_diry_poten_zon4.textChanged.connect(self.update_cart_powery_4)

        self.le_diry_lon_zon5.textChanged.connect(self.update_cart_yzone_5)
        self.le_diry_nvcy_zon5.textChanged.connect(self.update_cart_ncvy_5)
        self.le_diry_poten_zon5.textChanged.connect(self.update_cart_powery_5)

        self.le_diry_lon_zon6.textChanged.connect(self.update_cart_yzone_6)
        self.le_diry_nvcy_zon6.textChanged.connect(self.update_cart_ncvy_6)
        self.le_diry_poten_zon6.textChanged.connect(self.update_cart_powery_6)

        self.le_diry_lon_zon7.textChanged.connect(self.update_cart_yzone_7)
        self.le_diry_nvcy_zon7.textChanged.connect(self.update_cart_ncvy_7)
        self.le_diry_poten_zon7.textChanged.connect(self.update_cart_powery_7)

        self.le_diry_lon_zon8.textChanged.connect(self.update_cart_yzone_8)
        self.le_diry_nvcy_zon8.textChanged.connect(self.update_cart_ncvy_8)
        self.le_diry_poten_zon8.textChanged.connect(self.update_cart_powery_8)

        self.le_diry_lon_zon9.textChanged.connect(self.update_cart_yzone_9)
        self.le_diry_nvcy_zon9.textChanged.connect(self.update_cart_ncvy_9)
        self.le_diry_poten_zon9.textChanged.connect(self.update_cart_powery_9)

        self.le_diry_lon_zon10.textChanged.connect(self.update_cart_yzone_10)
        self.le_diry_nvcy_zon10.textChanged.connect(self.update_cart_ncvy_10)
        self.le_diry_poten_zon10.textChanged.connect(self.update_cart_powery_10)

        # -COORDENADA Z (CARTESIANA)

        self.sb_dirz_numz.textChanged.connect(self.update_cart_nzz)

        self.le_dirz_lon_zon1.textChanged.connect(self.update_cart_zzone_1)
        self.le_dirz_nvcz_zon1.textChanged.connect(self.update_cart_ncvz_1)
        self.le_dirz_poten_zon1.textChanged.connect(self.update_cart_powerz_1)

        self.le_dirz_lon_zon2.textChanged.connect(self.update_cart_zzone_2)
        self.le_dirz_nvcz_zon2.textChanged.connect(self.update_cart_ncvz_2)
        self.le_dirz_poten_zon2.textChanged.connect(self.update_cart_powerz_2)

        self.le_dirz_lon_zon3.textChanged.connect(self.update_cart_zzone_3)
        self.le_dirz_nvcz_zon3.textChanged.connect(self.update_cart_ncvz_3)
        self.le_dirz_poten_zon3.textChanged.connect(self.update_cart_powerz_3)

        self.le_dirz_lon_zon4.textChanged.connect(self.update_cart_zzone_4)
        self.le_dirz_nvcz_zon4.textChanged.connect(self.update_cart_ncvz_4)
        self.le_dirz_poten_zon4.textChanged.connect(self.update_cart_powerz_4)

        self.le_dirz_lon_zon5.textChanged.connect(self.update_cart_zzone_5)
        self.le_dirz_nvcz_zon5.textChanged.connect(self.update_cart_ncvz_5)
        self.le_dirz_poten_zon5.textChanged.connect(self.update_cart_powerz_5)

        self.le_dirz_lon_zon6.textChanged.connect(self.update_cart_zzone_6)
        self.le_dirz_nvcz_zon6.textChanged.connect(self.update_cart_ncvz_6)
        self.le_dirz_poten_zon6.textChanged.connect(self.update_cart_powerz_6)

        self.le_dirz_lon_zon7.textChanged.connect(self.update_cart_zzone_7)
        self.le_dirz_nvcz_zon7.textChanged.connect(self.update_cart_ncvz_7)
        self.le_dirz_poten_zon7.textChanged.connect(self.update_cart_powerz_7)

        self.le_dirz_lon_zon8.textChanged.connect(self.update_cart_zzone_8)
        self.le_dirz_nvcz_zon8.textChanged.connect(self.update_cart_ncvz_8)
        self.le_dirz_poten_zon8.textChanged.connect(self.update_cart_powerz_8)

        self.le_dirz_lon_zon9.textChanged.connect(self.update_cart_zzone_9)
        self.le_dirz_nvcz_zon9.textChanged.connect(self.update_cart_ncvz_9)
        self.le_dirz_poten_zon9.textChanged.connect(self.update_cart_powerz_9)

        self.le_dirz_lon_zon10.textChanged.connect(self.update_cart_zzone_10)
        self.le_dirz_nvcz_zon10.textChanged.connect(self.update_cart_ncvz_10)
        self.le_dirz_poten_zon10.textChanged.connect(self.update_cart_powerz_10)

        #####################################################################################

        # CONEXION DE WIDGETS VARIAS ZONAS - CARTESIANA

        # -COORDENADA TITA (CILINDRICA) - VARIAS ZONAS

        self.sb_dirtita_numz.textChanged.connect(self.update_cil_nztita)

        self.le_dirtita_lon_zon1.textChanged.connect(self.update_cil_titazone_1)
        self.le_dirtita_nvctita_zon1.textChanged.connect(self.update_cil_ncvtita_1)
        self.le_dirtita_poten_zon1.textChanged.connect(self.update_cil_powertita_1)

        self.le_dirtita_lon_zon2.textChanged.connect(self.update_cil_titazone_2)
        self.le_dirtita_nvctita_zon2.textChanged.connect(self.update_cil_ncvtita_2)
        self.le_dirtita_poten_zon2.textChanged.connect(self.update_cil_powertita_2)

        self.le_dirtita_lon_zon3.textChanged.connect(self.update_cil_titazone_3)
        self.le_dirtita_nvctita_zon3.textChanged.connect(self.update_cil_ncvtita_3)
        self.le_dirtita_poten_zon3.textChanged.connect(self.update_cil_powertita_3)

        self.le_dirtita_lon_zon4.textChanged.connect(self.update_cil_titazone_4)
        self.le_dirtita_nvctita_zon4.textChanged.connect(self.update_cil_ncvtita_4)
        self.le_dirtita_poten_zon4.textChanged.connect(self.update_cil_powertita_4)

        self.le_dirtita_lon_zon5.textChanged.connect(self.update_cil_titazone_5)
        self.le_dirtita_nvctita_zon5.textChanged.connect(self.update_cil_ncvtita_5)
        self.le_dirtita_poten_zon5.textChanged.connect(self.update_cil_powertita_5)

        self.le_dirtita_lon_zon6.textChanged.connect(self.update_cil_titazone_6)
        self.le_dirtita_nvctita_zon6.textChanged.connect(self.update_cil_ncvtita_6)
        self.le_dirtita_poten_zon6.textChanged.connect(self.update_cil_powertita_6)

        self.le_dirtita_lon_zon7.textChanged.connect(self.update_cil_titazone_7)
        self.le_dirtita_nvctita_zon7.textChanged.connect(self.update_cil_ncvtita_7)
        self.le_dirtita_poten_zon7.textChanged.connect(self.update_cil_powertita_7)

        self.le_dirtita_lon_zon8.textChanged.connect(self.update_cil_titazone_8)
        self.le_dirtita_nvctita_zon8.textChanged.connect(self.update_cil_ncvtita_8)
        self.le_dirtita_poten_zon8.textChanged.connect(self.update_cil_powertita_8)

        self.le_dirtita_lon_zon9.textChanged.connect(self.update_cil_titazone_9)
        self.le_dirtita_nvctita_zon9.textChanged.connect(self.update_cil_ncvtita_9)
        self.le_dirtita_poten_zon9.textChanged.connect(self.update_cil_powertita_9)

        self.le_dirtita_lon_zon10.textChanged.connect(self.update_cil_titazone_10)
        self.le_dirtita_nvctita_zon10.textChanged.connect(self.update_cil_ncvtita_10)
        self.le_dirtita_poten_zon10.textChanged.connect(self.update_cil_powertita_10)

        #####################################################################################

        # -COORDENADA RADIO (CILINDRICA) - VARIAS ZONAS

        self.sb_dirr_numz.textChanged.connect(self.update_cil_nzr)

        self.le_dirr_inidom.textChanged.connect(self.update_cil_rini_vz)

        self.le_dirr_lon_zon1.textChanged.connect(self.update_cil_rzone_1)
        self.le_dirr_nvcr_zon1.textChanged.connect(self.update_cil_ncvr_1)
        self.le_dirr_poten_zon1.textChanged.connect(self.update_cil_powerr_1)

        self.le_dirr_lon_zon2.textChanged.connect(self.update_cil_rzone_2)
        self.le_dirr_nvcr_zon2.textChanged.connect(self.update_cil_ncvr_2)
        self.le_dirr_poten_zon2.textChanged.connect(self.update_cil_powerr_2)

        self.le_dirr_lon_zon3.textChanged.connect(self.update_cil_rzone_3)
        self.le_dirr_nvcr_zon3.textChanged.connect(self.update_cil_ncvr_3)
        self.le_dirr_poten_zon3.textChanged.connect(self.update_cil_powerr_3)

        self.le_dirr_lon_zon4.textChanged.connect(self.update_cil_rzone_4)
        self.le_dirr_nvcr_zon4.textChanged.connect(self.update_cil_ncvr_4)
        self.le_dirr_poten_zon4.textChanged.connect(self.update_cil_powerr_4)

        self.le_dirr_lon_zon5.textChanged.connect(self.update_cil_rzone_5)
        self.le_dirr_nvcr_zon5.textChanged.connect(self.update_cil_ncvr_5)
        self.le_dirr_poten_zon5.textChanged.connect(self.update_cil_powerr_5)

        self.le_dirr_lon_zon6.textChanged.connect(self.update_cil_rzone_6)
        self.le_dirr_nvcr_zon6.textChanged.connect(self.update_cil_ncvr_6)
        self.le_dirr_poten_zon6.textChanged.connect(self.update_cil_powerr_6)

        self.le_dirr_lon_zon7.textChanged.connect(self.update_cil_rzone_7)
        self.le_dirr_nvcr_zon7.textChanged.connect(self.update_cil_ncvr_7)
        self.le_dirr_poten_zon7.textChanged.connect(self.update_cil_powerr_7)

        self.le_dirr_lon_zon8.textChanged.connect(self.update_cil_rzone_8)
        self.le_dirr_nvcr_zon8.textChanged.connect(self.update_cil_ncvr_8)
        self.le_dirr_poten_zon8.textChanged.connect(self.update_cil_powerr_8)

        self.le_dirr_lon_zon9.textChanged.connect(self.update_cil_rzone_9)
        self.le_dirr_nvcr_zon9.textChanged.connect(self.update_cil_ncvr_9)
        self.le_dirr_poten_zon9.textChanged.connect(self.update_cil_powerr_9)

        self.le_dirr_lon_zon10.textChanged.connect(self.update_cil_rzone_10)
        self.le_dirr_nvcr_zon10.textChanged.connect(self.update_cil_ncvr_10)
        self.le_dirr_poten_zon10.textChanged.connect(self.update_cil_powerr_10)

        #####################################################################################

        # -COORDENADA Z (CILINDRICA) - VARIAS ZONAS

        self.sb_dirzcil_numz.textChanged.connect(self.update_cil_vz_nzz)

        self.le_dirzcil_lon_zon1.textChanged.connect(self.update_cil_vz_zzone_1)
        self.le_dirzcil_nvczcil_zon1.textChanged.connect(self.update_cil_vz_ncvz_1)
        self.le_dirzcil_poten_zon1.textChanged.connect(self.update_cil_vz_powerz_1)

        self.le_dirzcil_lon_zon2.textChanged.connect(self.update_cil_vz_zzone_2)
        self.le_dirzcil_nvczcil_zon2.textChanged.connect(self.update_cil_vz_ncvz_2)
        self.le_dirzcil_poten_zon2.textChanged.connect(self.update_cil_vz_powerz_2)

        self.le_dirzcil_lon_zon3.textChanged.connect(self.update_cil_vz_zzone_3)
        self.le_dirzcil_nvczcil_zon3.textChanged.connect(self.update_cil_vz_ncvz_3)
        self.le_dirzcil_poten_zon3.textChanged.connect(self.update_cil_vz_powerz_3)

        self.le_dirzcil_lon_zon4.textChanged.connect(self.update_cil_vz_zzone_4)
        self.le_dirzcil_nvczcil_zon4.textChanged.connect(self.update_cil_vz_ncvz_4)
        self.le_dirzcil_poten_zon4.textChanged.connect(self.update_cil_vz_powerz_4)

        self.le_dirzcil_lon_zon5.textChanged.connect(self.update_cil_vz_zzone_5)
        self.le_dirzcil_nvczcil_zon5.textChanged.connect(self.update_cil_vz_ncvz_5)
        self.le_dirzcil_poten_zon5.textChanged.connect(self.update_cil_vz_powerz_5)

        self.le_dirzcil_lon_zon6.textChanged.connect(self.update_cil_vz_zzone_6)
        self.le_dirzcil_nvczcil_zon6.textChanged.connect(self.update_cil_vz_ncvz_6)
        self.le_dirzcil_poten_zon6.textChanged.connect(self.update_cil_vz_powerz_6)

        self.le_dirzcil_lon_zon7.textChanged.connect(self.update_cil_vz_zzone_7)
        self.le_dirzcil_nvczcil_zon7.textChanged.connect(self.update_cil_vz_ncvz_7)
        self.le_dirzcil_poten_zon7.textChanged.connect(self.update_cil_vz_powerz_7)

        self.le_dirzcil_lon_zon8.textChanged.connect(self.update_cil_vz_zzone_8)
        self.le_dirzcil_nvczcil_zon8.textChanged.connect(self.update_cil_vz_ncvz_8)
        self.le_dirzcil_poten_zon8.textChanged.connect(self.update_cil_vz_powerz_8)

        self.le_dirzcil_lon_zon9.textChanged.connect(self.update_cil_vz_zzone_9)
        self.le_dirzcil_nvczcil_zon9.textChanged.connect(self.update_cil_vz_ncvz_9)
        self.le_dirzcil_poten_zon9.textChanged.connect(self.update_cil_vz_powerz_9)

        self.le_dirzcil_lon_zon10.textChanged.connect(self.update_cil_vz_zzone_10)
        self.le_dirzcil_nvczcil_zon10.textChanged.connect(self.update_cil_vz_ncvz_10)
        self.le_dirzcil_poten_zon10.textChanged.connect(self.update_cil_vz_powerz_10)

        #####################################################################################

    def changeZonas(self):
        current_text_coord = self.cb_tipocoord.currentText()
        current_text_zona = self.cb_tipozonas.currentText()

        if current_text_zona == "Zona única" and current_text_coord == "Cartesianas":
            self.gbsw_malla2.setCurrentIndex(0)
        elif current_text_zona == "Zona única" and current_text_coord == "Cilindricas":
            self.gbsw_malla2.setCurrentIndex(1)
        elif (
            current_text_zona == "Varias zonas" and current_text_coord == "Cartesianas"
        ):
            self.gbsw_malla2.setCurrentIndex(2)
        elif (
            current_text_zona == "Varias zonas" and current_text_coord == "Cilindricas"
        ):
            self.gbsw_malla2.setCurrentIndex(3)
            self.sb_dirx_numz.valueChanged.connect(self.changingNumBoxX)

    # AYUDAAA
    def changingNumBoxX(self):
        currentNumBox = self.sb_dirx_numz.value()
        if not getattr(
            self.gb_dirx_vz1, "le_dirx_lon_zon{}".format(currentNumBox)
        ).isEnabled():
            getattr(
                self.gb_dirx_vz1, "le_dirx_lon_zon{}".format(currentNumBox)
            ).setEnabled(True)
            getattr(
                self.gb_dirx_vz1, "le_dirx_nvcx_zon{}".format(currentNumBox)
            ).setEnabled(True)
            getattr(
                self.gb_dirx_vz1, "le_dirx_poten_zon{}".format(currentNumBox)
            ).setEnabled(True)
        else:
            try:
                getattr(
                    self.gb_dirx_vz1, "le_dirx_lon_zon{}".format(currentNumBox + 1)
                ).setEnabled(False)
                getattr(
                    self.gb_dirx_vz1, "le_dirx_nvcx_zon{}".format(currentNumBox + 1)
                ).setEnabled(False)
                getattr(
                    self.gb_dirx_vz1, "le_dirx_poten_zon{}".format(currentNumBox + 1)
                ).setEnabled(False)
            except:
                pass

    def on_coordinate_system_changed(self, selection):
        mode = 1 if selection == "Cartesianas" else 2
        self.config_manager.config_structure["GRID"]["MODE"] = mode

    def on_zones_system_changed(self, selection):
        zone = "zgrid" if selection == "Varias zonas" else "ezgrid"
        self.config_manager.config_structure["GRID"]["ZONEGRID"] = zone

    ##############################################################################################
    # METODOS PARA CONEXION DE WIDGETS ZONA UNICA - CARTESIANA

    def update_cart_xl(self, text):
        self.config_manager.config_structure["GRID"]["CART_XL"] = text

    def update_cart_nvcx(self, text):
        self.config_manager.config_structure["GRID"]["CART_NVCX"] = text

    def update_cart_potenciax(self, text):
        self.config_manager.config_structure["GRID"]["CART_POWERX"] = text

    def update_cart_yl(self, text):
        self.config_manager.config_structure["GRID"]["CART_YL"] = text

    def update_cart_nvcy(self, text):
        self.config_manager.config_structure["GRID"]["CART_NVCY"] = text

    def update_cart_potenciay(self, text):
        self.config_manager.config_structure["GRID"]["CART_POWERY"] = text

    def update_cart_zl(self, text):
        self.config_manager.config_structure["GRID"]["CART_ZL"] = text

    def update_cart_nvcz(self, text):
        self.config_manager.config_structure["GRID"]["CART_NVCZ"] = text

    def update_cart_potenciaz(self, text):
        self.config_manager.config_structure["GRID"]["CART_POWERZ"] = text

    ##############################################################################################
    # METODOS PARA CONEXION DE WIDGETS ZONA UNICA - CILINDRICA

    def update_cil_tital(self, text):
        self.config_manager.config_structure["GRID"]["CIL_TITAL"] = text

    def update_cil_nvctita(self, text):
        self.config_manager.config_structure["GRID"]["CIL_NVCTITA"] = text

    def update_cil_potenciatita(self, text):
        self.config_manager.config_structure["GRID"]["CIL_POWERTITA"] = text

    def update_cil_rini_zu(self, text):
        self.config_manager.config_structure["GRID"]["CIL_R(1)_ZU"] = text

    def update_cil_rl(self, text):
        self.config_manager.config_structure["GRID"]["CIL_RL"] = text

    def update_cil_nvcr(self, text):
        self.config_manager.config_structure["GRID"]["CIL_NVCR"] = text

    def update_cil_potenciar(self, text):
        self.config_manager.config_structure["GRID"]["CIL_POWERR"] = text

    def update_cil_zl(self, text):
        self.config_manager.config_structure["GRID"]["CIL_ZL"] = text

    def update_cil_nvcz(self, text):
        self.config_manager.config_structure["GRID"]["CIL_NVCZ"] = text

    def update_cil_potenciaz(self, text):
        self.config_manager.config_structure["GRID"]["CIL_POWERZ"] = text

    ##############################################################################################
    # METODOS PARA CONEXION DE WIDGETS VARIAS ZONAS - CARTESIANA

    # -COORDENADA X (CARTESIANA)

    def update_cart_nzx(self, text):
        self.config_manager.config_structure["GRID"]["CART_NZX"] = text

    def update_cart_xzone_1(self, text):
        self.config_manager.config_structure["GRID"]["XZONE(1)"] = text

    def update_cart_ncvx_1(self, text):
        self.config_manager.config_structure["GRID"]["NCVX(1)"] = text

    def update_cart_powerx_1(self, text):
        self.config_manager.config_structure["GRID"]["POWERX(1)"] = text

    def update_cart_xzone_2(self, text):
        self.config_manager.config_structure["GRID"]["XZONE(2)"] = text

    def update_cart_ncvx_2(self, text):
        self.config_manager.config_structure["GRID"]["NCVX(2)"] = text

    def update_cart_powerx_2(self, text):
        self.config_manager.config_structure["GRID"]["POWERX(2)"] = text

    def update_cart_xzone_3(self, text):
        self.config_manager.config_structure["GRID"]["XZONE(3)"] = text

    def update_cart_ncvx_3(self, text):
        self.config_manager.config_structure["GRID"]["NCVX(3)"] = text

    def update_cart_powerx_3(self, text):
        self.config_manager.config_structure["GRID"]["POWERX(3)"] = text

    def update_cart_xzone_4(self, text):
        self.config_manager.config_structure["GRID"]["XZONE(4)"] = text

    def update_cart_ncvx_4(self, text):
        self.config_manager.config_structure["GRID"]["NCVX(4)"] = text

    def update_cart_powerx_4(self, text):
        self.config_manager.config_structure["GRID"]["POWERX(4)"] = text

    def update_cart_xzone_5(self, text):
        self.config_manager.config_structure["GRID"]["XZONE(5)"] = text

    def update_cart_ncvx_5(self, text):
        self.config_manager.config_structure["GRID"]["NCVX(5)"] = text

    def update_cart_powerx_5(self, text):
        self.config_manager.config_structure["GRID"]["POWERX(5)"] = text

    def update_cart_xzone_6(self, text):
        self.config_manager.config_structure["GRID"]["XZONE(6)"] = text

    def update_cart_ncvx_6(self, text):
        self.config_manager.config_structure["GRID"]["NCVX(6)"] = text

    def update_cart_powerx_6(self, text):
        self.config_manager.config_structure["GRID"]["POWERX(6)"] = text

    def update_cart_xzone_7(self, text):
        self.config_manager.config_structure["GRID"]["XZONE(7)"] = text

    def update_cart_ncvx_7(self, text):
        self.config_manager.config_structure["GRID"]["NCVX(7)"] = text

    def update_cart_powerx_7(self, text):
        self.config_manager.config_structure["GRID"]["POWERX(7)"] = text

    def update_cart_xzone_8(self, text):
        self.config_manager.config_structure["GRID"]["XZONE(8)"] = text

    def update_cart_ncvx_8(self, text):
        self.config_manager.config_structure["GRID"]["NCVX(8)"] = text

    def update_cart_powerx_8(self, text):
        self.config_manager.config_structure["GRID"]["POWERX(8)"] = text

    def update_cart_xzone_9(self, text):
        self.config_manager.config_structure["GRID"]["XZONE(9)"] = text

    def update_cart_ncvx_9(self, text):
        self.config_manager.config_structure["GRID"]["NCVX(9)"] = text

    def update_cart_powerx_9(self, text):
        self.config_manager.config_structure["GRID"]["POWERX(9)"] = text

    def update_cart_xzone_10(self, text):
        self.config_manager.config_structure["GRID"]["XZONE(10)"] = text

    def update_cart_ncvx_10(self, text):
        self.config_manager.config_structure["GRID"]["NCVX(10)"] = text

    def update_cart_powerx_10(self, text):
        self.config_manager.config_structure["GRID"]["POWERX(10)"] = text

    # -COORDENADA Y (CARTESIANA)

    def update_cart_nzy(self, text):
        self.config_manager.config_structure["GRID"]["CART_NZY"] = text

    def update_cart_yzone_1(self, text):
        self.config_manager.config_structure["GRID"]["YZONE(1)"] = text

    def update_cart_ncvy_1(self, text):
        self.config_manager.config_structure["GRID"]["NCVY(1)"] = text

    def update_cart_powery_1(self, text):
        self.config_manager.config_structure["GRID"]["POWERY(1)"] = text

    def update_cart_yzone_2(self, text):
        self.config_manager.config_structure["GRID"]["YZONE(2)"] = text

    def update_cart_ncvy_2(self, text):
        self.config_manager.config_structure["GRID"]["NCVY(2)"] = text

    def update_cart_powery_2(self, text):
        self.config_manager.config_structure["GRID"]["POWERY(2)"] = text

    def update_cart_yzone_3(self, text):
        self.config_manager.config_structure["GRID"]["YZONE(3)"] = text

    def update_cart_ncvy_3(self, text):
        self.config_manager.config_structure["GRID"]["NCVY(3)"] = text

    def update_cart_powery_3(self, text):
        self.config_manager.config_structure["GRID"]["POWERY(3)"] = text

    def update_cart_yzone_4(self, text):
        self.config_manager.config_structure["GRID"]["YZONE(4)"] = text

    def update_cart_ncvy_4(self, text):
        self.config_manager.config_structure["GRID"]["NCVY(4)"] = text

    def update_cart_powery_4(self, text):
        self.config_manager.config_structure["GRID"]["POWERY(4)"] = text

    def update_cart_yzone_5(self, text):
        self.config_manager.config_structure["GRID"]["YZONE(5)"] = text

    def update_cart_ncvy_5(self, text):
        self.config_manager.config_structure["GRID"]["NCVY(5)"] = text

    def update_cart_powery_5(self, text):
        self.config_manager.config_structure["GRID"]["POWERY(5)"] = text

    def update_cart_yzone_6(self, text):
        self.config_manager.config_structure["GRID"]["YZONE(6)"] = text

    def update_cart_ncvy_6(self, text):
        self.config_manager.config_structure["GRID"]["NCVY(6)"] = text

    def update_cart_powery_6(self, text):
        self.config_manager.config_structure["GRID"]["POWERY(6)"] = text

    def update_cart_yzone_7(self, text):
        self.config_manager.config_structure["GRID"]["YZONE(7)"] = text

    def update_cart_ncvy_7(self, text):
        self.config_manager.config_structure["GRID"]["NCVY(7)"] = text

    def update_cart_powery_7(self, text):
        self.config_manager.config_structure["GRID"]["POWERY(7)"] = text

    def update_cart_yzone_8(self, text):
        self.config_manager.config_structure["GRID"]["YZONE(8)"] = text

    def update_cart_ncvy_8(self, text):
        self.config_manager.config_structure["GRID"]["NCVY(8)"] = text

    def update_cart_powery_8(self, text):
        self.config_manager.config_structure["GRID"]["POWERY(8)"] = text

    def update_cart_yzone_9(self, text):
        self.config_manager.config_structure["GRID"]["YZONE(9)"] = text

    def update_cart_ncvy_9(self, text):
        self.config_manager.config_structure["GRID"]["NCVY(9)"] = text

    def update_cart_powery_9(self, text):
        self.config_manager.config_structure["GRID"]["POWERY(9)"] = text

    def update_cart_yzone_10(self, text):
        self.config_manager.config_structure["GRID"]["YZONE(10)"] = text

    def update_cart_ncvy_10(self, text):
        self.config_manager.config_structure["GRID"]["NCVY(10)"] = text

    def update_cart_powery_10(self, text):
        self.config_manager.config_structure["GRID"]["POWERY(10)"] = text

    # -COORDENADA Z (CARTESIANA)

    def update_cart_nzz(self, text):
        self.config_manager.config_structure["GRID"]["CART_NZZ"] = text

    def update_cart_zzone_1(self, text):
        self.config_manager.config_structure["GRID"]["ZZONE(1)"] = text

    def update_cart_ncvz_1(self, text):
        self.config_manager.config_structure["GRID"]["NCVZ(1)"] = text

    def update_cart_powerz_1(self, text):
        self.config_manager.config_structure["GRID"]["POWERZ(1)"] = text

    def update_cart_zzone_2(self, text):
        self.config_manager.config_structure["GRID"]["ZZONE(2)"] = text

    def update_cart_ncvz_2(self, text):
        self.config_manager.config_structure["GRID"]["NCVZ(2)"] = text

    def update_cart_powerz_2(self, text):
        self.config_manager.config_structure["GRID"]["POWERZ(2)"] = text

    def update_cart_zzone_3(self, text):
        self.config_manager.config_structure["GRID"]["ZZONE(3)"] = text

    def update_cart_ncvz_3(self, text):
        self.config_manager.config_structure["GRID"]["NCVZ(3)"] = text

    def update_cart_powerz_3(self, text):
        self.config_manager.config_structure["GRID"]["POWERZ(3)"] = text

    def update_cart_zzone_4(self, text):
        self.config_manager.config_structure["GRID"]["ZZONE(4)"] = text

    def update_cart_ncvz_4(self, text):
        self.config_manager.config_structure["GRID"]["NCVZ(4)"] = text

    def update_cart_powerz_4(self, text):
        self.config_manager.config_structure["GRID"]["POWERZ(4)"] = text

    def update_cart_zzone_5(self, text):
        self.config_manager.config_structure["GRID"]["ZZONE(5)"] = text

    def update_cart_ncvz_5(self, text):
        self.config_manager.config_structure["GRID"]["NCVZ(5)"] = text

    def update_cart_powerz_5(self, text):
        self.config_manager.config_structure["GRID"]["POWERZ(5)"] = text

    def update_cart_zzone_6(self, text):
        self.config_manager.config_structure["GRID"]["ZZONE(6)"] = text

    def update_cart_ncvz_6(self, text):
        self.config_manager.config_structure["GRID"]["NCVZ(6)"] = text

    def update_cart_powerz_6(self, text):
        self.config_manager.config_structure["GRID"]["POWERZ(6)"] = text

    def update_cart_zzone_7(self, text):
        self.config_manager.config_structure["GRID"]["ZZONE(7)"] = text

    def update_cart_ncvz_7(self, text):
        self.config_manager.config_structure["GRID"]["NCVZ(7)"] = text

    def update_cart_powerz_7(self, text):
        self.config_manager.config_structure["GRID"]["POWERZ(7)"] = text

    def update_cart_zzone_8(self, text):
        self.config_manager.config_structure["GRID"]["ZZONE(8)"] = text

    def update_cart_ncvz_8(self, text):
        self.config_manager.config_structure["GRID"]["NCVZ(8)"] = text

    def update_cart_powerz_8(self, text):
        self.config_manager.config_structure["GRID"]["POWERZ(8)"] = text

    def update_cart_zzone_9(self, text):
        self.config_manager.config_structure["GRID"]["ZZONE(9)"] = text

    def update_cart_ncvz_9(self, text):
        self.config_manager.config_structure["GRID"]["NCVZ(9)"] = text

    def update_cart_powerz_9(self, text):
        self.config_manager.config_structure["GRID"]["POWERZ(9)"] = text

    def update_cart_zzone_10(self, text):
        self.config_manager.config_structure["GRID"]["ZZONE(10)"] = text

    def update_cart_ncvz_10(self, text):
        self.config_manager.config_structure["GRID"]["NCVZ(10)"] = text

    def update_cart_powerz_10(self, text):
        self.config_manager.config_structure["GRID"]["POWERZ(10)"] = text

    ##############################################################################################
    # METODOS PARA CONEXION DE WIDGETS VARIAS ZONAS - CILINDRICA

    # -COORDENADA TITA (CILINDRICA) - VARIAS ZONAS

    def update_cil_nztita(self, text):
        self.config_manager.config_structure["GRID"]["CIL_NZX"] = text

    def update_cil_titazone_1(self, text):
        self.config_manager.config_structure["GRID"]["CIL_XZONE(1)"] = text

    def update_cil_ncvtita_1(self, text):
        self.config_manager.config_structure["GRID"]["CIL_NCVX(1)"] = text

    def update_cil_powertita_1(self, text):
        self.config_manager.config_structure["GRID"]["CIL_POWERX(1)"] = text

    def update_cil_titazone_2(self, text):
        self.config_manager.config_structure["GRID"]["CIL_XZONE(2)"] = text

    def update_cil_ncvtita_2(self, text):
        self.config_manager.config_structure["GRID"]["CIL_NCVX(2)"] = text

    def update_cil_powertita_2(self, text):
        self.config_manager.config_structure["GRID"]["CIL_POWERX(2)"] = text

    def update_cil_titazone_3(self, text):
        self.config_manager.config_structure["GRID"]["CIL_XZONE(3)"] = text

    def update_cil_ncvtita_3(self, text):
        self.config_manager.config_structure["GRID"]["CIL_NCVX(3)"] = text

    def update_cil_powertita_3(self, text):
        self.config_manager.config_structure["GRID"]["CIL_POWERX(3)"] = text

    def update_cil_titazone_4(self, text):
        self.config_manager.config_structure["GRID"]["CIL_XZONE(4)"] = text

    def update_cil_ncvtita_4(self, text):
        self.config_manager.config_structure["GRID"]["CIL_NCVX(4)"] = text

    def update_cil_powertita_4(self, text):
        self.config_manager.config_structure["GRID"]["CIL_POWERX(4)"] = text

    def update_cil_titazone_5(self, text):
        self.config_manager.config_structure["GRID"]["CIL_XZONE(5)"] = text

    def update_cil_ncvtita_5(self, text):
        self.config_manager.config_structure["GRID"]["CIL_NCVX(5)"] = text

    def update_cil_powertita_5(self, text):
        self.config_manager.config_structure["GRID"]["CIL_POWERX(5)"] = text

    def update_cil_titazone_6(self, text):
        self.config_manager.config_structure["GRID"]["CIL_XZONE(6)"] = text

    def update_cil_ncvtita_6(self, text):
        self.config_manager.config_structure["GRID"]["CIL_NCVX(6)"] = text

    def update_cil_powertita_6(self, text):
        self.config_manager.config_structure["GRID"]["CIL_POWERX(6)"] = text

    def update_cil_titazone_7(self, text):
        self.config_manager.config_structure["GRID"]["CIL_XZONE(7)"] = text

    def update_cil_ncvtita_7(self, text):
        self.config_manager.config_structure["GRID"]["CIL_NCVX(7)"] = text

    def update_cil_powertita_7(self, text):
        self.config_manager.config_structure["GRID"]["CIL_POWERX(7)"] = text

    def update_cil_titazone_8(self, text):
        self.config_manager.config_structure["GRID"]["CIL_XZONE(8)"] = text

    def update_cil_ncvtita_8(self, text):
        self.config_manager.config_structure["GRID"]["CIL_NCVX(8)"] = text

    def update_cil_powertita_8(self, text):
        self.config_manager.config_structure["GRID"]["CIL_POWERX(8)"] = text

    def update_cil_titazone_9(self, text):
        self.config_manager.config_structure["GRID"]["CIL_XZONE(9)"] = text

    def update_cil_ncvtita_9(self, text):
        self.config_manager.config_structure["GRID"]["CIL_NCVX(9)"] = text

    def update_cil_powertita_9(self, text):
        self.config_manager.config_structure["GRID"]["CIL_POWERX(9)"] = text

    def update_cil_titazone_10(self, text):
        self.config_manager.config_structure["GRID"]["CIL_XZONE(10)"] = text

    def update_cil_ncvtita_10(self, text):
        self.config_manager.config_structure["GRID"]["CIL_NCVX(10)"] = text

    def update_cil_powertita_10(self, text):
        self.config_manager.config_structure["GRID"]["CIL_POWERX(10)"] = text

    ##############################################################################################
    # -COORDENADA RADIO (CILINDRICA) - VARIAS ZONAS

    def update_cil_nzr(self, text):
        self.config_manager.config_structure["GRID"]["CIL_NZY"] = text

    def update_cil_rini_vz(self, text):
        self.config_manager.config_structure["GRID"]["CIL_R(1)_VZ"] = text

    def update_cil_rzone_1(self, text):
        self.config_manager.config_structure["GRID"]["CIL_YZONE(1)"] = text

    def update_cil_ncvr_1(self, text):
        self.config_manager.config_structure["GRID"]["CIL_NCVY(1)"] = text

    def update_cil_powerr_1(self, text):
        self.config_manager.config_structure["GRID"]["CIL_POWERY(1)"] = text

    def update_cil_rzone_2(self, text):
        self.config_manager.config_structure["GRID"]["CIL_YZONE(2)"] = text

    def update_cil_ncvr_2(self, text):
        self.config_manager.config_structure["GRID"]["CIL_NCVY(2)"] = text

    def update_cil_powerr_2(self, text):
        self.config_manager.config_structure["GRID"]["CIL_POWERY(2)"] = text

    def update_cil_rzone_3(self, text):
        self.config_manager.config_structure["GRID"]["CIL_YZONE(3)"] = text

    def update_cil_ncvr_3(self, text):
        self.config_manager.config_structure["GRID"]["CIL_NCVY(3)"] = text

    def update_cil_powerr_3(self, text):
        self.config_manager.config_structure["GRID"]["CIL_POWERY(3)"] = text

    def update_cil_rzone_4(self, text):
        self.config_manager.config_structure["GRID"]["CIL_YZONE(4)"] = text

    def update_cil_ncvr_4(self, text):
        self.config_manager.config_structure["GRID"]["CIL_NCVY(4)"] = text

    def update_cil_powerr_4(self, text):
        self.config_manager.config_structure["GRID"]["CIL_POWERY(4)"] = text

    def update_cil_rzone_5(self, text):
        self.config_manager.config_structure["GRID"]["CIL_YZONE(5)"] = text

    def update_cil_ncvr_5(self, text):
        self.config_manager.config_structure["GRID"]["CIL_NCVY(5)"] = text

    def update_cil_powerr_5(self, text):
        self.config_manager.config_structure["GRID"]["CIL_POWERY(5)"] = text

    def update_cil_rzone_6(self, text):
        self.config_manager.config_structure["GRID"]["CIL_YZONE(6)"] = text

    def update_cil_ncvr_6(self, text):
        self.config_manager.config_structure["GRID"]["CIL_NCVY(6)"] = text

    def update_cil_powerr_6(self, text):
        self.config_manager.config_structure["GRID"]["CIL_POWERY(6)"] = text

    def update_cil_rzone_7(self, text):
        self.config_manager.config_structure["GRID"]["CIL_YZONE(7)"] = text

    def update_cil_ncvr_7(self, text):
        self.config_manager.config_structure["GRID"]["CIL_NCVY(7)"] = text

    def update_cil_powerr_7(self, text):
        self.config_manager.config_structure["GRID"]["CIL_POWERY(7)"] = text

    def update_cil_rzone_8(self, text):
        self.config_manager.config_structure["GRID"]["CIL_YZONE(8)"] = text

    def update_cil_ncvr_8(self, text):
        self.config_manager.config_structure["GRID"]["CIL_NCVY(8)"] = text

    def update_cil_powerr_8(self, text):
        self.config_manager.config_structure["GRID"]["CIL_POWERY(8)"] = text

    def update_cil_rzone_9(self, text):
        self.config_manager.config_structure["GRID"]["CIL_YZONE(9)"] = text

    def update_cil_ncvr_9(self, text):
        self.config_manager.config_structure["GRID"]["CIL_NCVY(9)"] = text

    def update_cil_powerr_9(self, text):
        self.config_manager.config_structure["GRID"]["CIL_POWERY(9)"] = text

    def update_cil_rzone_10(self, text):
        self.config_manager.config_structure["GRID"]["CIL_YZONE(10)"] = text

    def update_cil_ncvr_10(self, text):
        self.config_manager.config_structure["GRID"]["CIL_NCVY(10)"] = text

    def update_cil_powerr_10(self, text):
        self.config_manager.config_structure["GRID"]["CIL_POWERY(10)"] = text

    ##############################################################################################
    # -COORDENADA Z (CILINDRICA) - VARIAS ZONAS

    def update_cil_vz_nzz(self, text):
        self.config_manager.config_structure["GRID"]["CIL_VZ_NZZ"] = text

    def update_cil_vz_zzone_1(self, text):
        self.config_manager.config_structure["GRID"]["CIL_VZ_ZZONE(1)"] = text

    def update_cil_vz_ncvz_1(self, text):
        self.config_manager.config_structure["GRID"]["CIL_VZ_NCVZ(1)"] = text

    def update_cil_vz_powerz_1(self, text):
        self.config_manager.config_structure["GRID"]["CIL_VZ_POWERZ(1)"] = text

    def update_cil_vz_zzone_2(self, text):
        self.config_manager.config_structure["GRID"]["CIL_VZ_ZZONE(2)"] = text

    def update_cil_vz_ncvz_2(self, text):
        self.config_manager.config_structure["GRID"]["CIL_VZ_NCVZ(2)"] = text

    def update_cil_vz_powerz_2(self, text):
        self.config_manager.config_structure["GRID"]["CIL_VZ_POWERZ(2)"] = text

    def update_cil_vz_zzone_3(self, text):
        self.config_manager.config_structure["GRID"]["CIL_VZ_ZZONE(3)"] = text

    def update_cil_vz_ncvz_3(self, text):
        self.config_manager.config_structure["GRID"]["CIL_VZ_NCVZ(3)"] = text

    def update_cil_vz_powerz_3(self, text):
        self.config_manager.config_structure["GRID"]["CIL_VZ_POWERZ(3)"] = text

    def update_cil_vz_zzone_4(self, text):
        self.config_manager.config_structure["GRID"]["CIL_VZ_ZZONE(4)"] = text

    def update_cil_vz_ncvz_4(self, text):
        self.config_manager.config_structure["GRID"]["CIL_VZ_NCVZ(4)"] = text

    def update_cil_vz_powerz_4(self, text):
        self.config_manager.config_structure["GRID"]["CIL_VZ_POWERZ(4)"] = text

    def update_cil_vz_zzone_5(self, text):
        self.config_manager.config_structure["GRID"]["CIL_VZ_ZZONE(5)"] = text

    def update_cil_vz_ncvz_5(self, text):
        self.config_manager.config_structure["GRID"]["CIL_VZ_NCVZ(5)"] = text

    def update_cil_vz_powerz_5(self, text):
        self.config_manager.config_structure["GRID"]["CIL_VZ_POWERZ(5)"] = text

    def update_cil_vz_zzone_6(self, text):
        self.config_manager.config_structure["GRID"]["CIL_VZ_ZZONE(6)"] = text

    def update_cil_vz_ncvz_6(self, text):
        self.config_manager.config_structure["GRID"]["CIL_VZ_NCVZ(6)"] = text

    def update_cil_vz_powerz_6(self, text):
        self.config_manager.config_structure["GRID"]["CIL_VZ_POWERZ(6)"] = text

    def update_cil_vz_zzone_7(self, text):
        self.config_manager.config_structure["GRID"]["CIL_VZ_ZZONE(7)"] = text

    def update_cil_vz_ncvz_7(self, text):
        self.config_manager.config_structure["GRID"]["CIL_VZ_NCVZ(7)"] = text

    def update_cil_vz_powerz_7(self, text):
        self.config_manager.config_structure["GRID"]["CIL_VZ_POWERZ(7)"] = text

    def update_cil_vz_zzone_8(self, text):
        self.config_manager.config_structure["GRID"]["CIL_VZ_ZZONE(8)"] = text

    def update_cil_vz_ncvz_8(self, text):
        self.config_manager.config_structure["GRID"]["CIL_VZ_NCVZ(8)"] = text

    def update_cil_vz_powerz_8(self, text):
        self.config_manager.config_structure["GRID"]["CIL_VZ_POWERZ(8)"] = text

    def update_cil_vz_zzone_9(self, text):
        self.config_manager.config_structure["GRID"]["CIL_VZ_ZZONE(9)"] = text

    def update_cil_vz_ncvz_9(self, text):
        self.config_manager.config_structure["GRID"]["CIL_VZ_NCVZ(9)"] = text

    def update_cil_vz_powerz_9(self, text):
        self.config_manager.config_structure["GRID"]["CIL_VZ_POWERZ(9)"] = text

    def update_cil_vz_zzone_10(self, text):
        self.config_manager.config_structure["GRID"]["CIL_VZ_ZZONE(10)"] = text

    def update_cil_vz_ncvz_10(self, text):
        self.config_manager.config_structure["GRID"]["CIL_VZ_NCVZ(10)"] = text

    def update_cil_vz_powerz_10(self, text):
        self.config_manager.config_structure["GRID"]["CIL_VZ_POWERZ(10)"] = text


#############################################################################################

if __name__ == "__main__":
    app = qtw.QApplication(sys.argv)
    config_manager = ConfigManager()  # Crear una instancia del gestor de configuración
    form = MallaWindow(config_manager)
    form.open()
    sys.exit(app.exec())
