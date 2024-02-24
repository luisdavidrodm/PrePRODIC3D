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

        self.le_xlon.textChanged.connect(lambda text: self.update_config("CART_XL", text))
        self.le_nvcx.textChanged.connect(lambda text: self.update_config("CART_NVCX", text))
        self.le_potenciax.textChanged.connect(lambda text: self.update_config("CART_POWERX", text))
        self.le_ylon.textChanged.connect(lambda text: self.update_config("CART_YL", text))
        self.le_nvcy.textChanged.connect(lambda text: self.update_config("CART_NVCY", text))
        self.le_potenciay.textChanged.connect(lambda text: self.update_config("CART_POWERY", text))
        self.le_zlon.textChanged.connect(lambda text: self.update_config("CART_ZL", text))
        self.le_nvcz.textChanged.connect(lambda text: self.update_config("CART_NVCZ", text))
        self.le_potenciaz.textChanged.connect(lambda text: self.update_config("CART_POWERZ", text))

        ##############################################################################################
        # CONEXION DE WIDGETS ZONA UNICA - CILINDRICA

        self.le_titalon.textChanged.connect(lambda text: self.update_config("CIL_TITAL", text))
        self.le_nvctita.textChanged.connect(lambda text: self.update_config("CIL_NVCTITA", text))
        self.le_potenciatita.textChanged.connect(lambda text: self.update_config("CIL_POWERTITA", text))
        self.le_rini.textChanged.connect(lambda text: self.update_config("CIL_R(1)_ZU", text))
        self.le_rlon.textChanged.connect(lambda text: self.update_config("CIL_RL", text))
        self.le_nvcr.textChanged.connect(lambda text: self.update_config("CIL_NVCR", text))
        self.le_potenciar.textChanged.connect(lambda text: self.update_config("CIL_POWERR", text))
        self.le_zloncil.textChanged.connect(lambda text: self.update_config("CIL_ZL", text))
        self.le_nvczcil.textChanged.connect(lambda text: self.update_config("CIL_NVCZ", text))
        self.le_potenciazcil.textChanged.connect(lambda text: self.update_config("CIL_POWERZ", text))

        #####################################################################################
        # CONEXION DE WIDGETS VARIAS ZONAS - CARTESIANA

        # -COORDENADA X (CARTESIANA)

        self.sb_dirx_numz.textChanged.connect(lambda text: self.update_config("CART_NZX", text))

        self.le_dirx_lon_zon1.textChanged.connect(lambda text: self.update_config("XZONE(1)", text))
        self.le_dirx_nvcx_zon1.textChanged.connect(lambda text: self.update_config("NCVX(1)", text))
        self.le_dirx_poten_zon1.textChanged.connect(lambda text: self.update_config("POWERX(1)", text))

        self.le_dirx_lon_zon2.textChanged.connect(lambda text: self.update_config("XZONE(2)", text))
        self.le_dirx_nvcx_zon2.textChanged.connect(lambda text: self.update_config("NCVX(2)", text))
        self.le_dirx_poten_zon2.textChanged.connect(lambda text: self.update_config("POWERX(2)", text))

        self.le_dirx_lon_zon3.textChanged.connect(lambda text: self.update_config("XZONE(3)", text))
        self.le_dirx_nvcx_zon3.textChanged.connect(lambda text: self.update_config("NCVX(3)", text))
        self.le_dirx_poten_zon3.textChanged.connect(lambda text: self.update_config("POWERX(3)", text))

        self.le_dirx_lon_zon4.textChanged.connect(lambda text: self.update_config("XZONE(4)", text))
        self.le_dirx_nvcx_zon4.textChanged.connect(lambda text: self.update_config("NCVX(4)", text))
        self.le_dirx_poten_zon4.textChanged.connect(lambda text: self.update_config("POWERX(4)", text))

        self.le_dirx_lon_zon5.textChanged.connect(lambda text: self.update_config("XZONE(5)", text))
        self.le_dirx_nvcx_zon5.textChanged.connect(lambda text: self.update_config("NCVX(5)", text))
        self.le_dirx_poten_zon5.textChanged.connect(lambda text: self.update_config("POWERX(5)", text))

        self.le_dirx_lon_zon6.textChanged.connect(lambda text: self.update_config("XZONE(6)", text))
        self.le_dirx_nvcx_zon6.textChanged.connect(lambda text: self.update_config("NCVX(6)", text))
        self.le_dirx_poten_zon6.textChanged.connect(lambda text: self.update_config("POWERX(6)", text))

        self.le_dirx_lon_zon7.textChanged.connect(lambda text: self.update_config("XZONE(7)", text))
        self.le_dirx_nvcx_zon7.textChanged.connect(lambda text: self.update_config("NCVX(7)", text))
        self.le_dirx_poten_zon7.textChanged.connect(lambda text: self.update_config("POWERX(7)", text))

        self.le_dirx_lon_zon8.textChanged.connect(lambda text: self.update_config("XZONE(8)", text))
        self.le_dirx_nvcx_zon8.textChanged.connect(lambda text: self.update_config("NCVX(8)", text))
        self.le_dirx_poten_zon8.textChanged.connect(lambda text: self.update_config("POWERX(8)", text))

        self.le_dirx_lon_zon9.textChanged.connect(lambda text: self.update_config("XZONE(9)", text))
        self.le_dirx_nvcx_zon9.textChanged.connect(lambda text: self.update_config("NCVX(9)", text))
        self.le_dirx_poten_zon9.textChanged.connect(lambda text: self.update_config("POWERX(9)", text))

        self.le_dirx_lon_zon10.textChanged.connect(lambda text: self.update_config("XZONE(10)", text))
        self.le_dirx_nvcx_zon10.textChanged.connect(lambda text: self.update_config("NCVX(10)", text))
        self.le_dirx_poten_zon10.textChanged.connect(lambda text: self.update_config("POWERX(10)", text))

        # -COORDENADA Y (CARTESIANA)

        self.sb_diry_numz.textChanged.connect(lambda text: self.update_config("CART_NZY", text))

        self.le_diry_lon_zon1.textChanged.connect(lambda text: self.update_config("YZONE(1)", text))
        self.le_diry_nvcy_zon1.textChanged.connect(lambda text: self.update_config("NCVY(1)", text))
        self.le_diry_poten_zon1.textChanged.connect(lambda text: self.update_config("POWERY(1)", text))

        self.le_diry_lon_zon2.textChanged.connect(lambda text: self.update_config("YZONE(2)", text))
        self.le_diry_nvcy_zon2.textChanged.connect(lambda text: self.update_config("NCVY(2)", text))
        self.le_diry_poten_zon2.textChanged.connect(lambda text: self.update_config("POWERY(2)", text))

        self.le_diry_lon_zon3.textChanged.connect(lambda text: self.update_config("YZONE(3)", text))
        self.le_diry_nvcy_zon3.textChanged.connect(lambda text: self.update_config("NCVY(3)", text))
        self.le_diry_poten_zon3.textChanged.connect(lambda text: self.update_config("POWERY(3)", text))

        self.le_diry_lon_zon4.textChanged.connect(lambda text: self.update_config("YZONE(4)", text))
        self.le_diry_nvcy_zon4.textChanged.connect(lambda text: self.update_config("NCVY(4)", text))
        self.le_diry_poten_zon4.textChanged.connect(lambda text: self.update_config("POWERY(4)", text))

        self.le_diry_lon_zon5.textChanged.connect(lambda text: self.update_config("YZONE(5)", text))
        self.le_diry_nvcy_zon5.textChanged.connect(lambda text: self.update_config("NCVY(5)", text))
        self.le_diry_poten_zon5.textChanged.connect(lambda text: self.update_config("POWERY(5)", text))

        self.le_diry_lon_zon6.textChanged.connect(lambda text: self.update_config("YZONE(6)", text))
        self.le_diry_nvcy_zon6.textChanged.connect(lambda text: self.update_config("NCVY(6)", text))
        self.le_diry_poten_zon6.textChanged.connect(lambda text: self.update_config("POWERY(6)", text))

        self.le_diry_lon_zon7.textChanged.connect(lambda text: self.update_config("YZONE(7)", text))
        self.le_diry_nvcy_zon7.textChanged.connect(lambda text: self.update_config("NCVY(7)", text))
        self.le_diry_poten_zon7.textChanged.connect(lambda text: self.update_config("POWERY(7)", text))

        self.le_diry_lon_zon8.textChanged.connect(lambda text: self.update_config("YZONE(8)", text))
        self.le_diry_nvcy_zon8.textChanged.connect(lambda text: self.update_config("NCVY(8)", text))
        self.le_diry_poten_zon8.textChanged.connect(lambda text: self.update_config("POWERY(8)", text))

        self.le_diry_lon_zon9.textChanged.connect(lambda text: self.update_config("YZONE(9)", text))
        self.le_diry_nvcy_zon9.textChanged.connect(lambda text: self.update_config("NCVY(9)", text))
        self.le_diry_poten_zon9.textChanged.connect(lambda text: self.update_config("POWERY(9)", text))

        self.le_diry_lon_zon10.textChanged.connect(lambda text: self.update_config("YZONE(10)", text))
        self.le_diry_nvcy_zon10.textChanged.connect(lambda text: self.update_config("NCVY(10)", text))
        self.le_diry_poten_zon10.textChanged.connect(lambda text: self.update_config("POWERY(10)", text))

        # -COORDENADA Z (CARTESIANA)

        self.sb_dirz_numz.textChanged.connect(lambda text: self.update_config("CART_NZZ", text))

        self.le_dirz_lon_zon1.textChanged.connect(lambda text: self.update_config("ZZONE(1)", text))
        self.le_dirz_nvcz_zon1.textChanged.connect(lambda text: self.update_config("NCVZ(1)", text))
        self.le_dirz_poten_zon1.textChanged.connect(lambda text: self.update_config("POWERZ(1)", text))

        self.le_dirz_lon_zon2.textChanged.connect(lambda text: self.update_config("ZZONE(2)", text))
        self.le_dirz_nvcz_zon2.textChanged.connect(lambda text: self.update_config("NCVZ(2)", text))
        self.le_dirz_poten_zon2.textChanged.connect(lambda text: self.update_config("POWERZ(2)", text))

        self.le_dirz_lon_zon3.textChanged.connect(lambda text: self.update_config("ZZONE(3)", text))
        self.le_dirz_nvcz_zon3.textChanged.connect(lambda text: self.update_config("NCVZ(3)", text))
        self.le_dirz_poten_zon3.textChanged.connect(lambda text: self.update_config("POWERZ(3)", text))

        self.le_dirz_lon_zon4.textChanged.connect(lambda text: self.update_config("ZZONE(4)", text))
        self.le_dirz_nvcz_zon4.textChanged.connect(lambda text: self.update_config("NCVZ(4)", text))
        self.le_dirz_poten_zon4.textChanged.connect(lambda text: self.update_config("POWERZ(4)", text))

        self.le_dirz_lon_zon5.textChanged.connect(lambda text: self.update_config("ZZONE(5)", text))
        self.le_dirz_nvcz_zon5.textChanged.connect(lambda text: self.update_config("NCVZ(5)", text))
        self.le_dirz_poten_zon5.textChanged.connect(lambda text: self.update_config("POWERZ(5)", text))

        self.le_dirz_lon_zon6.textChanged.connect(lambda text: self.update_config("ZZONE(6)", text))
        self.le_dirz_nvcz_zon6.textChanged.connect(lambda text: self.update_config("NCVZ(6)", text))
        self.le_dirz_poten_zon6.textChanged.connect(lambda text: self.update_config("POWERZ(6)", text))

        self.le_dirz_lon_zon7.textChanged.connect(lambda text: self.update_config("ZZONE(7)", text))
        self.le_dirz_nvcz_zon7.textChanged.connect(lambda text: self.update_config("NCVZ(7)", text))
        self.le_dirz_poten_zon7.textChanged.connect(lambda text: self.update_config("POWERZ(7)", text))

        self.le_dirz_lon_zon8.textChanged.connect(lambda text: self.update_config("ZZONE(8)", text))
        self.le_dirz_nvcz_zon8.textChanged.connect(lambda text: self.update_config("NCVZ(8)", text))
        self.le_dirz_poten_zon8.textChanged.connect(lambda text: self.update_config("POWERZ(8)", text))

        self.le_dirz_lon_zon9.textChanged.connect(lambda text: self.update_config("ZZONE(9)", text))
        self.le_dirz_nvcz_zon9.textChanged.connect(lambda text: self.update_config("NCVZ(9)", text))
        self.le_dirz_poten_zon9.textChanged.connect(lambda text: self.update_config("POWERZ(9)", text))

        self.le_dirz_lon_zon10.textChanged.connect(lambda text: self.update_config("ZZONE(10)", text))
        self.le_dirz_nvcz_zon10.textChanged.connect(lambda text: self.update_config("NCVZ(10)", text))
        self.le_dirz_poten_zon10.textChanged.connect(lambda text: self.update_config("POWERZ(10)", text))

        #####################################################################################

        # CONEXION DE WIDGETS VARIAS ZONAS - CARTESIANA

        # -COORDENADA TITA (CILINDRICA) - VARIAS ZONAS

        self.sb_dirtita_numz.textChanged.connect(lambda text: self.update_config("CIL_NZX", text))

        self.le_dirtita_lon_zon1.textChanged.connect(lambda text: self.update_config("CIL_XZONE(1)", text))
        self.le_dirtita_nvctita_zon1.textChanged.connect(lambda text: self.update_config("CIL_NCVX(1)", text))
        self.le_dirtita_poten_zon1.textChanged.connect(lambda text: self.update_config("CIL_POWERX(1)", text))

        self.le_dirtita_lon_zon2.textChanged.connect(lambda text: self.update_config("CIL_XZONE(2)", text))
        self.le_dirtita_nvctita_zon2.textChanged.connect(lambda text: self.update_config("CIL_NCVX(2)", text))
        self.le_dirtita_poten_zon2.textChanged.connect(lambda text: self.update_config("CIL_POWERX(2)", text))

        self.le_dirtita_lon_zon3.textChanged.connect(lambda text: self.update_config("CIL_XZONE(3)", text))
        self.le_dirtita_nvctita_zon3.textChanged.connect(lambda text: self.update_config("CIL_NCVX(3)", text))
        self.le_dirtita_poten_zon3.textChanged.connect(lambda text: self.update_config("CIL_POWERX(3)", text))

        self.le_dirtita_lon_zon4.textChanged.connect(lambda text: self.update_config("CIL_XZONE(4)", text))
        self.le_dirtita_nvctita_zon4.textChanged.connect(lambda text: self.update_config("CIL_NCVX(4)", text))
        self.le_dirtita_poten_zon4.textChanged.connect(lambda text: self.update_config("CIL_POWERX(4)", text))

        self.le_dirtita_lon_zon5.textChanged.connect(lambda text: self.update_config("CIL_XZONE(5)", text))
        self.le_dirtita_nvctita_zon5.textChanged.connect(lambda text: self.update_config("CIL_NCVX(5)", text))
        self.le_dirtita_poten_zon5.textChanged.connect(lambda text: self.update_config("CIL_POWERX(5)", text))

        self.le_dirtita_lon_zon6.textChanged.connect(lambda text: self.update_config("CIL_XZONE(6)", text))
        self.le_dirtita_nvctita_zon6.textChanged.connect(lambda text: self.update_config("CIL_NCVX(6)", text))
        self.le_dirtita_poten_zon6.textChanged.connect(lambda text: self.update_config("CIL_POWERX(6)", text))

        self.le_dirtita_lon_zon7.textChanged.connect(lambda text: self.update_config("CIL_XZONE(7)", text))
        self.le_dirtita_nvctita_zon7.textChanged.connect(lambda text: self.update_config("CIL_NCVX(7)", text))
        self.le_dirtita_poten_zon7.textChanged.connect(lambda text: self.update_config("CIL_POWERX(7)", text))

        self.le_dirtita_lon_zon8.textChanged.connect(lambda text: self.update_config("CIL_XZONE(8)", text))
        self.le_dirtita_nvctita_zon8.textChanged.connect(lambda text: self.update_config("CIL_NCVX(8)", text))
        self.le_dirtita_poten_zon8.textChanged.connect(lambda text: self.update_config("CIL_POWERX(8)", text))

        self.le_dirtita_lon_zon9.textChanged.connect(lambda text: self.update_config("CIL_XZONE(9)", text))
        self.le_dirtita_nvctita_zon9.textChanged.connect(lambda text: self.update_config("CIL_NCVX(9)", text))
        self.le_dirtita_poten_zon9.textChanged.connect(lambda text: self.update_config("CIL_POWERX(9)", text))

        self.le_dirtita_lon_zon10.textChanged.connect(lambda text: self.update_config("CIL_XZONE(10)", text))
        self.le_dirtita_nvctita_zon10.textChanged.connect(lambda text: self.update_config("CIL_NCVX(10)", text))
        self.le_dirtita_poten_zon10.textChanged.connect(lambda text: self.update_config("CIL_POWERX(10)", text))

        #####################################################################################

        # -COORDENADA RADIO (CILINDRICA) - VARIAS ZONAS

        self.sb_dirr_numz.textChanged.connect(lambda text: self.update_config("CIL_NZY", text))

        self.le_dirr_inidom.textChanged.connect(lambda text: self.update_config("CIL_R(1)_VZ", text))

        self.le_dirr_lon_zon1.textChanged.connect(lambda text: self.update_config("CIL_YZONE(1)", text))
        self.le_dirr_nvcr_zon1.textChanged.connect(lambda text: self.update_config("CIL_NCVY(1)", text))
        self.le_dirr_poten_zon1.textChanged.connect(lambda text: self.update_config("CIL_POWERY(1)", text))

        self.le_dirr_lon_zon2.textChanged.connect(lambda text: self.update_config("CIL_YZONE(2)", text))
        self.le_dirr_nvcr_zon2.textChanged.connect(lambda text: self.update_config("CIL_NCVY(2)", text))
        self.le_dirr_poten_zon2.textChanged.connect(lambda text: self.update_config("CIL_POWERY(2)", text))

        self.le_dirr_lon_zon3.textChanged.connect(lambda text: self.update_config("CIL_YZONE(3)", text))
        self.le_dirr_nvcr_zon3.textChanged.connect(lambda text: self.update_config("CIL_NCVY(3)", text))
        self.le_dirr_poten_zon3.textChanged.connect(lambda text: self.update_config("CIL_POWERY(3)", text))

        self.le_dirr_lon_zon4.textChanged.connect(lambda text: self.update_config("CIL_YZONE(4)", text))
        self.le_dirr_nvcr_zon4.textChanged.connect(lambda text: self.update_config("CIL_NCVY(4)", text))
        self.le_dirr_poten_zon4.textChanged.connect(lambda text: self.update_config("CIL_POWERY(4)", text))

        self.le_dirr_lon_zon5.textChanged.connect(lambda text: self.update_config("CIL_YZONE(5)", text))
        self.le_dirr_nvcr_zon5.textChanged.connect(lambda text: self.update_config("CIL_NCVY(5)", text))
        self.le_dirr_poten_zon5.textChanged.connect(lambda text: self.update_config("CIL_POWERY(5)", text))

        self.le_dirr_lon_zon6.textChanged.connect(lambda text: self.update_config("CIL_YZONE(6)", text))
        self.le_dirr_nvcr_zon6.textChanged.connect(lambda text: self.update_config("CIL_NCVY(6)", text))
        self.le_dirr_poten_zon6.textChanged.connect(lambda text: self.update_config("CIL_POWERY(6)", text))

        self.le_dirr_lon_zon7.textChanged.connect(lambda text: self.update_config("CIL_YZONE(7)", text))
        self.le_dirr_nvcr_zon7.textChanged.connect(lambda text: self.update_config("CIL_NCVY(7)", text))
        self.le_dirr_poten_zon7.textChanged.connect(lambda text: self.update_config("CIL_POWERY(7)", text))

        self.le_dirr_lon_zon8.textChanged.connect(lambda text: self.update_config("CIL_YZONE(8)", text))
        self.le_dirr_nvcr_zon8.textChanged.connect(lambda text: self.update_config("CIL_NCVY(8)", text))
        self.le_dirr_poten_zon8.textChanged.connect(lambda text: self.update_config("CIL_POWERY(8)", text))

        self.le_dirr_lon_zon9.textChanged.connect(lambda text: self.update_config("CIL_YZONE(9)", text))
        self.le_dirr_nvcr_zon9.textChanged.connect(lambda text: self.update_config("CIL_NCVY(9)", text))
        self.le_dirr_poten_zon9.textChanged.connect(lambda text: self.update_config("CIL_POWERY(9)", text))

        self.le_dirr_lon_zon10.textChanged.connect(lambda text: self.update_config("CIL_YZONE(10)", text))
        self.le_dirr_nvcr_zon10.textChanged.connect(lambda text: self.update_config("CIL_NCVY(10)", text))
        self.le_dirr_poten_zon10.textChanged.connect(lambda text: self.update_config("CIL_POWERY(10)", text))

        #####################################################################################

        # -COORDENADA Z (CILINDRICA) - VARIAS ZONAS

        self.sb_dirzcil_numz.textChanged.connect(lambda text: self.update_config("CIL_VZ_NZZ", text))

        self.le_dirzcil_lon_zon1.textChanged.connect(lambda text: self.update_config("CIL_VZ_ZZONE(1)", text))
        self.le_dirzcil_nvczcil_zon1.textChanged.connect(lambda text: self.update_config("CIL_VZ_NCVZ(1)", text))
        self.le_dirzcil_poten_zon1.textChanged.connect(lambda text: self.update_config("CIL_VZ_POWERZ(1)", text))

        self.le_dirzcil_lon_zon2.textChanged.connect(lambda text: self.update_config("CIL_VZ_ZZONE(2)", text))
        self.le_dirzcil_nvczcil_zon2.textChanged.connect(lambda text: self.update_config("CIL_VZ_NCVZ(2)", text))
        self.le_dirzcil_poten_zon2.textChanged.connect(lambda text: self.update_config("CIL_VZ_POWERZ(2)", text))

        self.le_dirzcil_lon_zon3.textChanged.connect(lambda text: self.update_config("CIL_VZ_ZZONE(3)", text))
        self.le_dirzcil_nvczcil_zon3.textChanged.connect(lambda text: self.update_config("CIL_VZ_NCVZ(3)", text))
        self.le_dirzcil_poten_zon3.textChanged.connect(lambda text: self.update_config("CIL_VZ_POWERZ(3)", text))

        self.le_dirzcil_lon_zon4.textChanged.connect(lambda text: self.update_config("CIL_VZ_ZZONE(4)", text))
        self.le_dirzcil_nvczcil_zon4.textChanged.connect(lambda text: self.update_config("CIL_VZ_NCVZ(4)", text))
        self.le_dirzcil_poten_zon4.textChanged.connect(lambda text: self.update_config("CIL_VZ_POWERZ(4)", text))

        self.le_dirzcil_lon_zon5.textChanged.connect(lambda text: self.update_config("CIL_VZ_ZZONE(5)", text))
        self.le_dirzcil_nvczcil_zon5.textChanged.connect(lambda text: self.update_config("CIL_VZ_NCVZ(5)", text))
        self.le_dirzcil_poten_zon5.textChanged.connect(lambda text: self.update_config("CIL_VZ_POWERZ(5)", text))

        self.le_dirzcil_lon_zon6.textChanged.connect(lambda text: self.update_config("CIL_VZ_ZZONE(6)", text))
        self.le_dirzcil_nvczcil_zon6.textChanged.connect(lambda text: self.update_config("CIL_VZ_NCVZ(6)", text))
        self.le_dirzcil_poten_zon6.textChanged.connect(lambda text: self.update_config("CIL_VZ_POWERZ(6)", text))

        self.le_dirzcil_lon_zon7.textChanged.connect(lambda text: self.update_config("CIL_VZ_ZZONE(7)", text))
        self.le_dirzcil_nvczcil_zon7.textChanged.connect(lambda text: self.update_config("CIL_VZ_NCVZ(7)", text))
        self.le_dirzcil_poten_zon7.textChanged.connect(lambda text: self.update_config("CIL_VZ_POWERZ(7)", text))

        self.le_dirzcil_lon_zon8.textChanged.connect(lambda text: self.update_config("CIL_VZ_ZZONE(8)", text))
        self.le_dirzcil_nvczcil_zon8.textChanged.connect(lambda text: self.update_config("CIL_VZ_NCVZ(8)", text))
        self.le_dirzcil_poten_zon8.textChanged.connect(lambda text: self.update_config("CIL_VZ_POWERZ(8)", text))

        self.le_dirzcil_lon_zon9.textChanged.connect(lambda text: self.update_config("CIL_VZ_ZZONE(9)", text))
        self.le_dirzcil_nvczcil_zon9.textChanged.connect(lambda text: self.update_config("CIL_VZ_NCVZ(9)", text))
        self.le_dirzcil_poten_zon9.textChanged.connect(lambda text: self.update_config("CIL_VZ_POWERZ(9)", text))

        self.le_dirzcil_lon_zon10.textChanged.connect(lambda text: self.update_config("CIL_VZ_ZZONE(10)", text))
        self.le_dirzcil_nvczcil_zon10.textChanged.connect(lambda text: self.update_config("CIL_VZ_NCVZ(10)", text))
        self.le_dirzcil_poten_zon10.textChanged.connect(lambda text: self.update_config("CIL_VZ_POWERZ(10)", text))

        #####################################################################################

    def changeZonas(self):
        current_text_coord = self.cb_tipocoord.currentText()
        current_text_zona = self.cb_tipozonas.currentText()

        if current_text_zona == "Zona única" and current_text_coord == "Cartesianas":
            self.gbsw_malla2.setCurrentIndex(0)
        elif current_text_zona == "Zona única" and current_text_coord == "Cilindricas":
            self.gbsw_malla2.setCurrentIndex(1)
        elif current_text_zona == "Varias zonas" and current_text_coord == "Cartesianas":
            self.gbsw_malla2.setCurrentIndex(2)
        elif current_text_zona == "Varias zonas" and current_text_coord == "Cilindricas":
            self.gbsw_malla2.setCurrentIndex(3)
            self.sb_dirx_numz.valueChanged.connect(self.changingNumBoxX)

    # AYUDAAA
    def changingNumBoxX(self):
        currentNumBox = self.sb_dirx_numz.value()
        if not getattr(self.gb_dirx_vz1, "le_dirx_lon_zon{}".format(currentNumBox)).isEnabled():
            getattr(self.gb_dirx_vz1, "le_dirx_lon_zon{}".format(currentNumBox)).setEnabled(True)
            getattr(self.gb_dirx_vz1, "le_dirx_nvcx_zon{}".format(currentNumBox)).setEnabled(True)
            getattr(self.gb_dirx_vz1, "le_dirx_poten_zon{}".format(currentNumBox)).setEnabled(True)
        else:
            try:
                getattr(self.gb_dirx_vz1, "le_dirx_lon_zon{}".format(currentNumBox + 1)).setEnabled(False)
                getattr(self.gb_dirx_vz1, "le_dirx_nvcx_zon{}".format(currentNumBox + 1)).setEnabled(False)
                getattr(self.gb_dirx_vz1, "le_dirx_poten_zon{}".format(currentNumBox + 1)).setEnabled(False)
            except:
                pass

    def on_coordinate_system_changed(self, selection):
        mode = 1 if selection == "Cartesianas" else 2
        self.config_manager.config_structure["GRID"]["MODE"] = mode

    def on_zones_system_changed(self, selection):
        zone = "zgrid" if selection == "Varias zonas" else "ezgrid"
        self.config_manager.config_structure["GRID"]["ZONEGRID"] = zone

    def update_config(self, config_key, text):
        # Actualiza el valor de la configuración en el ConfigManager
        self.config_manager.config_structure["GRID"][config_key] = text


#############################################################################################

if __name__ == "__main__":
    app = qtw.QApplication(sys.argv)
    config_manager = ConfigManager()  # Crear una instancia del gestor de configuración
    form = MallaWindow(config_manager)
    form.open()
    sys.exit(app.exec())
