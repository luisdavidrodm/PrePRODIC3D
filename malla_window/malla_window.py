from PySide6 import QtWidgets as qtw
from PySide6.QtCore import Signal

from malla_window.ui.malla_window_ui import Ui_malla_window


class MallaWindow(qtw.QDialog, Ui_malla_window):

    longitudes_actualizadas_signal = Signal(list)

    def __init__(self, config_manager):
        super().__init__()
        self.setupUi(self)
        self.ui = Ui_malla_window()
        self.config_manager = config_manager

        self.cb_tipocoord.currentTextChanged.connect(self.changeZonas)
        self.cb_tipozonas.currentTextChanged.connect(self.changeZonas)

        self.cb_tipocoord.currentTextChanged.connect(self.on_coordinate_system_changed)

        self.cb_tipozonas.currentTextChanged.connect(self.on_zones_system_changed)

        self.le_xlon.textChanged.connect(self.actualizar_longitudes)
        self.le_ylon.textChanged.connect(self.actualizar_longitudes)
        self.le_zlon.textChanged.connect(self.actualizar_longitudes)

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

        for i in range(1, 11):
            getattr(self, f"le_dirx_lon_zon{i}").textChanged.connect(
                lambda text, i=i: self.update_config(f"XZONE({i})", text)
            )
            getattr(self, f"le_dirx_nvcx_zon{i}").textChanged.connect(
                lambda text, i=i: self.update_config(f"NCVX({i})", text)
            )
            getattr(self, f"le_dirx_poten_zon{i}").textChanged.connect(
                lambda text, i=i: self.update_config(f"POWERX({i})", text)
            )

        # -COORDENADA Y (CARTESIANA)

        self.sb_diry_numz.textChanged.connect(lambda text: self.update_config("CART_NZY", text))

        for i in range(1, 11):
            getattr(self, f"le_diry_lon_zon{i}").textChanged.connect(
                lambda text, i=i: self.update_config(f"YZONE({i})", text)
            )
            getattr(self, f"le_diry_nvcy_zon{i}").textChanged.connect(
                lambda text, i=i: self.update_config(f"NCVY({i})", text)
            )
            getattr(self, f"le_diry_poten_zon{i}").textChanged.connect(
                lambda text, i=i: self.update_config(f"POWERY({i})", text)
            )

        # -COORDENADA Z (CARTESIANA)

        self.sb_dirz_numz.textChanged.connect(lambda text: self.update_config("CART_NZZ", text))

        for i in range(1, 11):
            getattr(self, f"le_dirz_lon_zon{i}").textChanged.connect(
                lambda text, i=i: self.update_config(f"ZZONE({i})", text)
            )
            getattr(self, f"le_dirz_nvcz_zon{i}").textChanged.connect(
                lambda text, i=i: self.update_config(f"NCVZ({i})", text)
            )
            getattr(self, f"le_dirz_poten_zon{i}").textChanged.connect(
                lambda text, i=i: self.update_config(f"POWERZ({i})", text)
            )

        #####################################################################################

        # CONEXION DE WIDGETS VARIAS ZONAS - CARTESIANA

        # -COORDENADA TITA (CILINDRICA) - VARIAS ZONAS

        self.sb_dirtita_numz.textChanged.connect(lambda text: self.update_config("CIL_NZX", text))

        for i in range(1, 11):
            getattr(self, f"le_dirtita_lon_zon{i}").textChanged.connect(
                lambda text, i=i: self.update_config(f"CIL_XZONE({i})", text)
            )
            getattr(self, f"le_dirtita_nvctita_zon{i}").textChanged.connect(
                lambda text, i=i: self.update_config(f"CIL_NCVX({i})", text)
            )
            getattr(self, f"le_dirtita_poten_zon{i}").textChanged.connect(
                lambda text, i=i: self.update_config(f"CIL_POWERX({i})", text)
            )

        #####################################################################################

        # -COORDENADA RADIO (CILINDRICA) - VARIAS ZONAS

        self.sb_dirr_numz.textChanged.connect(lambda text: self.update_config("CIL_NZY", text))

        self.le_dirr_inidom.textChanged.connect(lambda text: self.update_config("CIL_R(1)_VZ", text))

        for i in range(1, 11):
            getattr(self, f"le_dirr_lon_zon{i}").textChanged.connect(
                lambda text, i=i: self.update_config(f"CIL_YZONE({i})", text)
            )
            getattr(self, f"le_dirr_nvcr_zon{i}").textChanged.connect(
                lambda text, i=i: self.update_config(f"CIL_NCVY({i})", text)
            )
            getattr(self, f"le_dirr_poten_zon{i}").textChanged.connect(
                lambda text, i=i: self.update_config(f"CIL_POWERY({i})", text)
            )

        #####################################################################################

        # -COORDENADA Z (CILINDRICA) - VARIAS ZONAS

        self.sb_dirzcil_numz.textChanged.connect(lambda text: self.update_config("CIL_VZ_NZZ", text))

        for i in range(1, 11):
            getattr(self, f"le_dirzcil_lon_zon{i}").textChanged.connect(
                lambda text, i=i: self.update_config(f"CIL_VZ_ZZONE({i})", text)
            )
            getattr(self, f"le_dirzcil_nvczcil_zon{i}").textChanged.connect(
                lambda text, i=i: self.update_config(f"CIL_VZ_NCVZ({i})", text)
            )
            getattr(self, f"le_dirzcil_poten_zon{i}").textChanged.connect(
                lambda text, i=i: self.update_config(f"CIL_VZ_POWERZ({i})", text)
            )

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

    def actualizar_longitudes(self):

        longitud_x = self.le_xlon.text()
        longitud_y = self.le_ylon.text()
        longitud_z = self.le_zlon.text()

        self.longitudes_actualizadas_signal.emit([longitud_x, longitud_y, longitud_z])
