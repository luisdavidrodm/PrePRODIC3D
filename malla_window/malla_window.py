from PySide6 import QtWidgets as qtw
from PySide6.QtCore import Signal
from PySide6.QtWidgets import QSpinBox, QComboBox, QLineEdit
from malla_window.ui.malla_window_ui import Ui_malla_window


class MallaWindow(qtw.QDialog, Ui_malla_window):

    longitudes_actualizadas_signal = Signal(list)

    def __init__(self, config_manager):
        # fmt: off
        super().__init__()
        self.setupUi(self)
        self.ui = Ui_malla_window()
        self.config_manager = config_manager

        self.cb_tipocoord.currentTextChanged.connect(self.changeZonas)
        self.cb_tipozonas.currentTextChanged.connect(self.changeZonas)
        self.cb_tipocoord.currentTextChanged.connect(self.on_coordinate_system_changed)
        self.cb_tipozonas.currentTextChanged.connect(self.on_zones_system_changed)

        # TODO DELETE Conexiones para la actualización de configuraciones
        # self.connect_line_edits()

        self.sb_dirx_numz.valueChanged.connect(lambda value: self.handle_generic_numz_change(value, "le_dirx", "nvcx"))
        self.sb_diry_numz.valueChanged.connect(lambda value: self.handle_generic_numz_change(value, "le_diry", "nvcy"))
        self.sb_dirz_numz.valueChanged.connect(lambda value: self.handle_generic_numz_change(value, "le_dirz", "nvcz"))
        self.sb_dirtita_numz.valueChanged.connect(lambda value: self.handle_generic_numz_change(value, "le_dirtita", "nvctita"))
        self.sb_dirr_numz.valueChanged.connect(lambda value: self.handle_generic_numz_change(value, "le_dirr", "nvcr"))
        self.sb_dirzcil_numz.valueChanged.connect(lambda value: self.handle_generic_numz_change(value, "le_dirzcil", "nvczcil"))

        # TODO DELETE
        ##############################################################################################
        # CONEXION DE WIDGETS ZONA UNICA - CARTESIANA

        # self.le_xlon.textChanged.connect(lambda text: self.update_config("CART_XL", text))
        # self.le_nvcx.textChanged.connect(lambda text: self.update_config("CART_NVCX", text))
        # self.le_potenciax.textChanged.connect(lambda text: self.update_config("CART_POWERX", text))
        # self.le_ylon.textChanged.connect(lambda text: self.update_config("CART_YL", text))
        # self.le_nvcy.textChanged.connect(lambda text: self.update_config("CART_NVCY", text))
        # self.le_potenciay.textChanged.connect(lambda text: self.update_config("CART_POWERY", text))
        # self.le_zlon.textChanged.connect(lambda text: self.update_config("CART_ZL", text))
        # self.le_nvcz.textChanged.connect(lambda text: self.update_config("CART_NVCZ", text))
        # self.le_potenciaz.textChanged.connect(lambda text: self.update_config("CART_POWERZ", text))

        ##############################################################################################
        # CONEXION DE WIDGETS ZONA UNICA - CILINDRICA

        # self.le_titalon.textChanged.connect(lambda text: self.update_config("CIL_TITAL", text))
        # self.le_nvctita.textChanged.connect(lambda text: self.update_config("CIL_NVCTITA", text))
        # self.le_potenciatita.textChanged.connect(lambda text: self.update_config("CIL_POWERTITA", text))
        # self.le_rini.textChanged.connect(lambda text: self.update_config("CIL_R(1)_ZU", text))
        # self.le_rlon.textChanged.connect(lambda text: self.update_config("CIL_RL", text))
        # self.le_nvcr.textChanged.connect(lambda text: self.update_config("CIL_NVCR", text))
        # self.le_potenciar.textChanged.connect(lambda text: self.update_config("CIL_POWERR", text))
        # self.le_zloncil.textChanged.connect(lambda text: self.update_config("CIL_ZL", text))
        # self.le_nvczcil.textChanged.connect(lambda text: self.update_config("CIL_NVCZ", text))
        # self.le_potenciazcil.textChanged.connect(lambda text: self.update_config("CIL_POWERZ", text))

        #####################################################################################
        # CONEXION DE WIDGETS VARIAS ZONAS - CARTESIANA

        # -COORDENADA X (CARTESIANA)

        # self.sb_dirx_numz.textChanged.connect(lambda text: self.update_config("CART_NZX", text))

        # for i in range(1, 11):
            # getattr(self, f"le_dirx_lon_zon{i}").textChanged.connect(
            #     lambda text, i=i: self.update_config(f"XZONE({i})", text)
            # )
            # getattr(self, f"le_dirx_nvcx_zon{i}").textChanged.connect(
            #     lambda text, i=i: self.update_config(f"NCVX({i})", text)
            # )
            # getattr(self, f"le_dirx_poten_zon{i}").textChanged.connect(
            #     lambda text, i=i: self.update_config(f"POWERX({i})", text)
            # )

        # -COORDENADA Y (CARTESIANA)

        # self.sb_diry_numz.textChanged.connect(lambda text: self.update_config("CART_NZY", text))

        # for i in range(1, 11):
            # getattr(self, f"le_diry_lon_zon{i}").textChanged.connect(
            #     lambda text, i=i: self.update_config(f"YZONE({i})", text)
            # )
            # getattr(self, f"le_diry_nvcy_zon{i}").textChanged.connect(
            #     lambda text, i=i: self.update_config(f"NCVY({i})", text)
            # )
            # getattr(self, f"le_diry_poten_zon{i}").textChanged.connect(
            #     lambda text, i=i: self.update_config(f"POWERY({i})", text)
            # )

        # -COORDENADA Z (CARTESIANA)

        # self.sb_dirz_numz.textChanged.connect(lambda text: self.update_config("CART_NZZ", text))

        # for i in range(1, 11):
            # getattr(self, f"le_dirz_lon_zon{i}").textChanged.connect(
            #     lambda text, i=i: self.update_config(f"ZZONE({i})", text)
            # )
            # getattr(self, f"le_dirz_nvcz_zon{i}").textChanged.connect(
            #     lambda text, i=i: self.update_config(f"NCVZ({i})", text)
            # )
            # getattr(self, f"le_dirz_poten_zon{i}").textChanged.connect(
            #     lambda text, i=i: self.update_config(f"POWERZ({i})", text)
            # )

        #####################################################################################

        # CONEXION DE WIDGETS VARIAS ZONAS - CARTESIANA

        # -COORDENADA TITA (CILINDRICA) - VARIAS ZONAS

        # self.sb_dirtita_numz.textChanged.connect(lambda text: self.update_config("CIL_NZX", text))

        # for i in range(1, 11):
            # getattr(self, f"le_dirtita_lon_zon{i}").textChanged.connect(
            #     lambda text, i=i: self.update_config(f"CIL_XZONE({i})", text)
            # )
            # getattr(self, f"le_dirtita_nvctita_zon{i}").textChanged.connect(
            #     lambda text, i=i: self.update_config(f"CIL_NCVX({i})", text)
            # )
            # getattr(self, f"le_dirtita_poten_zon{i}").textChanged.connect(
            #     lambda text, i=i: self.update_config(f"CIL_POWERX({i})", text)
            # )

        #####################################################################################

        # -COORDENADA RADIO (CILINDRICA) - VARIAS ZONAS

        # self.sb_dirr_numz.textChanged.connect(lambda text: self.update_config("CIL_NZY", text))

        # self.le_dirr_inidom.textChanged.connect(lambda text: self.update_config("CIL_R(1)_VZ", text))

        # for i in range(1, 11):
            # getattr(self, f"le_dirr_lon_zon{i}").textChanged.connect(
            #     lambda text, i=i: self.update_config(f"CIL_YZONE({i})", text)
            # )
            # getattr(self, f"le_dirr_nvcr_zon{i}").textChanged.connect(
            #     lambda text, i=i: self.update_config(f"CIL_NCVY({i})", text)
            # )
            # getattr(self, f"le_dirr_poten_zon{i}").textChanged.connect(
            #     lambda text, i=i: self.update_config(f"CIL_POWERY({i})", text)
            # )

        #####################################################################################

        # -COORDENADA Z (CILINDRICA) - VARIAS ZONAS

        # self.sb_dirzcil_numz.textChanged.connect(lambda text: self.update_config("CIL_VZ_NZZ", text))

        # for i in range(1, 11):
            # getattr(self, f"le_dirzcil_lon_zon{i}").textChanged.connect(
            #     lambda text, i=i: self.update_config(f"CIL_VZ_ZZONE({i})", text)
            # )
            # getattr(self, f"le_dirzcil_nvczcil_zon{i}").textChanged.connect(
            #     lambda text, i=i: self.update_config(f"CIL_VZ_NCVZ({i})", text)
            # )
            # getattr(self, f"le_dirzcil_poten_zon{i}").textChanged.connect(
            #     lambda text, i=i: self.update_config(f"CIL_VZ_POWERZ({i})", text)
            # )

        #####################################################################################

        self.widgets = [
            "le_xlon", "le_nvcx", "le_potenciax", "le_ylon", "le_nvcy",
            "le_potenciay", "le_zlon", "le_nvcz", "le_potenciaz", "le_titalon",
            "le_nvctita", "le_potenciatita", "le_rini", "le_rlon", "le_nvcr",
            "le_potenciar", "le_zloncil", "le_nvczcil", "le_potenciazcil",
            "sb_dirx_numz", "sb_diry_numz", "sb_dirz_numz", "sb_dirtita_numz",
            "sb_dirr_numz", "le_dirr_inidom", "sb_dirzcil_numz",
        ]

        self.widgets_to_extend = [
            "le_dirx_lon_zon{0}", "le_dirx_nvcx_zon{0}", "le_dirx_poten_zon{0}",
            "le_diry_lon_zon{0}", "le_diry_nvcy_zon{0}", "le_diry_poten_zon{0}",
            "le_dirz_lon_zon{0}", "le_dirz_nvcz_zon{0}", "le_dirz_poten_zon{0}",
            "le_dirr_lon_zon{0}", "le_dirr_nvcr_zon{0}", "le_dirr_poten_zon{0}",
            "le_dirtita_lon_zon{0}", "le_dirtita_nvctita_zon{0}", "le_dirtita_poten_zon{0}",
            "le_dirzcil_lon_zon{0}", "le_dirzcil_nvczcil_zon{0}", "le_dirzcil_poten_zon{0}"
        ]
        
        for i in range(1, 11):
            for widget_name in self.widgets_to_extend:
                self.widgets.append(widget_name.format(i))
                    
        for widget_name  in self.widgets:
            widget = getattr(self, widget_name)
            if isinstance(widget, QComboBox):
                signal = widget.currentTextChanged
            elif isinstance(widget, QSpinBox):
                signal = widget.valueChanged
            elif isinstance(widget, QLineEdit):
                signal = widget.textChanged
            else:
                continue
            signal.connect(self.value_changed)
        # fmt: on

        # Cargar configuración inicial
        self.initialize_spin_boxes()
        self.load_malla_config()

    def initialize_spin_boxes(self):
        for direction in ["dirx", "diry", "dirz", "dirtita", "dirr", "dirzcil"]:
            spin_box = getattr(self, f"sb_{direction}_numz")
            spin_box.setMinimum(2)
            spin_box.setMaximum(10)

    # TODO DELETE
    # def connect_line_edits(self):
    ##ZONA UNICA COORDENADAS CARTESIANAS

    # self.le_xlon.textChanged.connect(lambda: self.value_changed(self.le_xlon.text(), "CART_XL"))
    # self.le_nvcx.textChanged.connect(lambda: self.value_changed(self.le_nvcx.text(), "CART_NVCX"))
    # self.le_potenciax.textChanged.connect(lambda: self.value_changed(self.le_potenciax.text(), "CART_POWERX"))
    # self.le_ylon.textChanged.connect(lambda text: self.value_changed(self.le_ylon.text(), "CART_YL"))
    # self.le_nvcy.textChanged.connect(lambda text: self.value_changed(self.le_nvcy.text(), "CART_NVCY"))
    # self.le_potenciay.textChanged.connect(lambda text: self.value_changed(self.le_potenciay.text(), "CART_POWERY"))
    # self.le_zlon.textChanged.connect(lambda text: self.value_changed(self.le_zlon.text(), "CART_ZL"))
    # self.le_nvcz.textChanged.connect(lambda text: self.value_changed(self.le_nvcz.text(), "CART_NVCZ"))
    # self.le_potenciaz.textChanged.connect(lambda text: self.value_changed(self.le_potenciaz.text(), "CART_POWERZ"))

    ##ZONA UNICA COORDENADAS CILINDRICAS
    # self.le_titalon.textChanged.connect(lambda: self.value_changed(self.le_titalon.text(), "CIL_TITAL"))
    # self.le_nvctita.textChanged.connect(lambda: self.value_changed(self.le_nvctita.text(), "CIL_NVCTITA"))
    # self.le_potenciatita.textChanged.connect(
    #     lambda: self.value_changed(self.le_potenciatita.text(), "CIL_POWERTITA")
    # )
    # self.le_rini.textChanged.connect(lambda: self.value_changed(self.le_rini.text(), "CIL_R(1)_ZU"))
    # self.le_rlon.textChanged.connect(lambda: self.value_changed(self.le_rlon.text(), "CIL_RL"))
    # self.le_nvcr.textChanged.connect(lambda: self.value_changed(self.le_nvcr.text(), "CIL_NVCR"))
    # self.le_potenciar.textChanged.connect(lambda: self.value_changed(self.le_potenciar.text(), "CIL_POWERR"))
    # self.le_zloncil.textChanged.connect(lambda: self.value_changed(self.le_zloncil.text(), "CIL_ZL"))
    # self.le_nvczcil.textChanged.connect(lambda: self.value_changed(self.le_nvczcil.text(), "CIL_NVCZ"))
    # self.le_potenciazcil.textChanged.connect(lambda: self.value_changed(self.le_potenciazcil.text(), "CIL_POWERZ"))

    ##VARIAS ZONAS COORDENADAS CARTESIANAS

    # -COORDENADA X (CARTESIANA)
    # self.sb_dirx_numz.valueChanged.connect(lambda value: self.value_changed(str(value), "CART_NZX"))

    # for i in range(1, 11):
    # getattr(self, f"le_dirx_lon_zon{i}").textChanged.connect(
    #     lambda text, i=i: self.value_changed(text, f"XZONE({i})")
    # )
    # getattr(self, f"le_dirx_nvcx_zon{i}").textChanged.connect(
    #     lambda text, i=i: self.value_changed(text, f"NCVX({i})")
    # )
    # getattr(self, f"le_dirx_poten_zon{i}").textChanged.connect(
    #     lambda text, i=i: self.value_changed(text, f"POWERX({i})")
    # )

    # -COORDENADA Y (CARTESIANA)
    # self.sb_diry_numz.valueChanged.connect(lambda value: self.value_changed(str(value), "CART_NZY"))

    # for i in range(1, 11):
    #     getattr(self, f"le_diry_lon_zon{i}").textChanged.connect(
    #         lambda text, i=i: self.value_changed(text, f"YZONE({i})")
    #     )
    # getattr(self, f"le_diry_nvcy_zon{i}").textChanged.connect(
    #     lambda text, i=i: self.value_changed(text, f"NCVY({i})")
    # )
    # getattr(self, f"le_diry_poten_zon{i}").textChanged.connect(
    #     lambda text, i=i: self.value_changed(text, f"POWERY({i})")
    # )

    # -COORDENADA Z (CARTESIANA)
    # self.sb_dirz_numz.valueChanged.connect(lambda value: self.value_changed(str(value), "CART_NZZ"))

    # for i in range(1, 11):
    #     getattr(self, f"le_dirz_lon_zon{i}").textChanged.connect(
    #         lambda text, i=i: self.value_changed(text, f"ZZONE({i})")
    #     )
    # getattr(self, f"le_dirz_nvcz_zon{i}").textChanged.connect(
    #     lambda text, i=i: self.value_changed(text, f"NCVZ({i})")
    # )
    # getattr(self, f"le_dirz_poten_zon{i}").textChanged.connect(
    #     lambda text, i=i: self.value_changed(text, f"POWERZ({i})")
    # )

    ##VARIAS ZONAS COORDENADAS CILINDRICAS

    # -COORDENADA TITA (CILINDRICA) - VARIAS ZONAS
    # self.sb_dirtita_numz.valueChanged.connect(lambda value: self.value_changed(str(value), "CIL_NZX"))

    # for i in range(1, 11):
    #     getattr(self, f"le_dirtita_lon_zon{i}").textChanged.connect(
    #         lambda text, i=i: self.value_changed(text, f"CIL_XZONE({i})")
    #     )
    # getattr(self, f"le_dirtita_nvctita_zon{i}").textChanged.connect(
    #     lambda text, i=i: self.value_changed(text, f"CIL_NCVX({i})")
    # )
    # getattr(self, f"le_dirtita_poten_zon{i}").textChanged.connect(
    #     lambda text, i=i: self.value_changed(text, f"CIL_POWERX({i})")
    # )

    # -COORDENADA RADIO (CILINDRICA) - VARIAS ZONAS
    # self.sb_dirr_numz.valueChanged.connect(lambda value: self.value_changed(str(value), "CIL_NZY"))

    # self.le_dirr_inidom.textChanged.connect(lambda text: self.value_changed(text, "CIL_R(1)_VZ"))

    # for i in range(1, 11):
    #     getattr(self, f"le_dirr_lon_zon{i}").textChanged.connect(
    #         lambda text, i=i: self.value_changed(text, f"CIL_YZONE({i})")
    #     )
    # getattr(self, f"le_dirr_nvcr_zon{i}").textChanged.connect(
    #     lambda text, i=i: self.value_changed(text, f"CIL_NCVY({i})")
    # )
    # getattr(self, f"le_dirr_poten_zon{i}").textChanged.connect(
    #     lambda text, i=i: self.value_changed(text, f"CIL_POWERY({i})")
    # )

    # -COORDENADA Z (CILINDRICA) - VARIAS ZONAS
    # self.sb_dirzcil_numz.valueChanged.connect(lambda value: self.value_changed(str(value), "CIL_VZ_NZZ"))

    # for i in range(1, 11):
    #     getattr(self, f"le_dirzcil_lon_zon{i}").textChanged.connect(
    #         lambda text, i=i: self.value_changed(text, f"CIL_VZ_ZZONE({i})")
    #     )
    # getattr(self, f"le_dirzcil_nvczcil_zon{i}").textChanged.connect(
    #     lambda text, i=i: self.value_changed(text, f"CIL_VZ_NCVZ({i})")
    # )
    # getattr(self, f"le_dirzcil_poten_zon{i}").textChanged.connect(
    #     lambda text, i=i: self.value_changed(text, f"CIL_VZ_POWERZ({i})")
    # )

    # self.sb_dirx_numz.valueChanged.connect(lambda value: self.value_changed(str(value), "CART_NZX"))
    # self.sb_diry_numz.valueChanged.connect(lambda value: self.value_changed(str(value), "CART_NZY"))
    # self.sb_dirz_numz.valueChanged.connect(lambda value: self.value_changed(str(value), "CART_NZZ"))
    # self.sb_dirtita_numz.valueChanged.connect(lambda value: self.value_changed(str(value), "CIL_NZTITA"))
    # self.sb_dirr_numz.valueChanged.connect(lambda value: self.value_changed(str(value), "CIL_NZR"))
    # self.sb_dirzcil_numz.valueChanged.connect(lambda value: self.value_changed(str(value), "CIL_NZZCIL"))

    def load_malla_config(self):
        # Carga la configuración desde config_manager
        config = self.config_manager.config_structure["GRID"]

        ##ZONA UNICA COORDENADAS CARTESIANAS

        for widget_name, value in config.items():
            widget = getattr(self, widget_name)
            if isinstance(widget, QLineEdit) or isinstance(widget, QComboBox):
                widget.setText(value)
            elif isinstance(widget, QSpinBox):
                widget.setValue(value)
            else:
                continue

        # TODO DELETE
        # self.le_xlon.setText(config.get("CART_XL", ""))
        # self.le_nvcx.setText(config.get("CART_NVCX", ""))
        # self.le_potenciax.setText(config.get("CART_POWERX", ""))
        # self.le_ylon.setText(config.get("CART_YL", ""))
        # self.le_nvcy.setText(config.get("CART_NVCY", ""))
        # self.le_potenciay.setText(config.get("CART_POWERY", ""))
        # self.le_zlon.setText(config.get("CART_ZL", ""))
        # self.le_nvcz.setText(config.get("CART_NVCZ", ""))
        # self.le_potenciaz.setText(config.get("CART_POWERZ", ""))

        ##ZONA UNICA COORDENADAS CILINDRICAS
        # self.le_titalon.setText(config.get("CIL_TITAL", ""))
        # self.le_nvctita.setText(config.get("CIL_NVCTITA", ""))
        # self.le_potenciatita.setText(config.get("CIL_POWERTITA", ""))
        # self.le_rini.setText(config.get("CIL_R(1)_ZU", ""))
        # self.le_rlon.setText(config.get("CIL_RL", ""))
        # self.le_nvcr.setText(config.get("CIL_NVCR", ""))
        # self.le_potenciar.setText(config.get("CIL_POWERR", ""))
        # self.le_zloncil.setText(config.get("CIL_ZL", ""))
        # self.le_nvczcil.setText(config.get("CIL_NVCZ", ""))
        # self.le_potenciazcil.setText(config.get("CIL_POWERZ", ""))

        # Para varias zonas en coordenadas cartesianas
        # for i in range(1, 11):
        #     getattr(self, f"le_dirx_lon_zon{i}").setText(config.get(f"XZONE({i})", ""))
        #     getattr(self, f"le_dirx_nvcx_zon{i}").setText(config.get(f"NCVX({i})", ""))
        #     getattr(self, f"le_dirx_poten_zon{i}").setText(config.get(f"POWERX({i})", ""))

        #     getattr(self, f"le_diry_lon_zon{i}").setText(config.get(f"YZONE({i})", ""))
        #     getattr(self, f"le_diry_nvcy_zon{i}").setText(config.get(f"NCVY({i})", ""))
        #     getattr(self, f"le_diry_poten_zon{i}").setText(config.get(f"POWERY({i})", ""))

        #     getattr(self, f"le_dirz_lon_zon{i}").setText(config.get(f"ZZONE({i})", ""))
        #     getattr(self, f"le_dirz_nvcz_zon{i}").setText(config.get(f"NCVZ({i})", ""))
        #     getattr(self, f"le_dirz_poten_zon{i}").setText(config.get(f"POWERZ({i})", ""))

        # Para varias zonas en coordenadas cilíndricas
        # self.le_dirr_inidom.setText(config.get("CIL_R(1)_VZ", ""))

        # for i in range(1, 11):
        #     getattr(self, f"le_dirtita_lon_zon{i}").setText(config.get(f"CIL_XZONE({i})", ""))
        #     getattr(self, f"le_dirtita_nvctita_zon{i}").setText(config.get(f"CIL_NCVX({i})", ""))
        #     getattr(self, f"le_dirtita_poten_zon{i}").setText(config.get(f"CIL_POWERX({i})", ""))

        #     getattr(self, f"le_dirr_lon_zon{i}").setText(config.get(f"CIL_YZONE({i})", ""))
        #     getattr(self, f"le_dirr_nvcr_zon{i}").setText(config.get(f"CIL_NCVY({i})", ""))
        #     getattr(self, f"le_dirr_poten_zon{i}").setText(config.get(f"CIL_POWERY({i})", ""))

        #     getattr(self, f"le_dirzcil_lon_zon{i}").setText(config.get(f"CIL_VZ_ZZONE({i})", ""))
        #     getattr(self, f"le_dirzcil_nvczcil_zon{i}").setText(config.get(f"CIL_VZ_NCVZ({i})", ""))
        #     getattr(self, f"le_dirzcil_poten_zon{i}").setText(config.get(f"CIL_VZ_POWERZ({i})", ""))

        # Carga el número de zonas guardado y ajusta los SpinBoxes
        # self.sb_dirx_numz.setValue(int(config.get("CART_NZX", 2)))
        # self.sb_diry_numz.setValue(int(config.get("CART_NZY", 2)))
        # self.sb_dirz_numz.setValue(int(config.get("CART_NZZ", 2)))
        # self.sb_dirtita_numz.setValue(int(config.get("CIL_NZTITA", 2)))
        # self.sb_dirr_numz.setValue(int(config.get("CIL_NZR", 2)))
        # self.sb_dirzcil_numz.setValue(int(config.get("CIL_NZZCIL", 2)))

        ##Para asegurar que al abrir la ventana se habiliten los LineEdit dependiendo del NZ cargados
        self.handle_generic_numz_change(self.sb_dirx_numz.value(), "le_dirx", "nvcx")
        self.handle_generic_numz_change(self.sb_diry_numz.value(), "le_diry", "nvcy")
        self.handle_generic_numz_change(self.sb_dirz_numz.value(), "le_dirz", "nvcz")
        self.handle_generic_numz_change(self.sb_dirtita_numz.value(), "le_dirtita", "nvctita")
        self.handle_generic_numz_change(self.sb_dirr_numz.value(), "le_dirr", "nvcr")
        self.handle_generic_numz_change(self.sb_dirzcil_numz.value(), "le_dirzcil", "nvczcil")

    def value_changed(self, value):
        sender = self.sender()
        self.config_manager.config_structure["GRID"][sender.objectName()] = value

    def changeZonas(self):
        current_text_coord = self.cb_tipocoord.currentText()
        current_text_zona = self.cb_tipozonas.currentText()
        capaIndex = {
            ("Zona única", "Cartesianas"): 0,
            ("Zona única", "Cilindricas"): 1,
            ("Varias zonas", "Cartesianas"): 2,
            ("Varias zonas", "Cilindricas"): 3,
        }.get((current_text_zona, current_text_coord), 0)

        self.gbsw_malla2.setCurrentIndex(capaIndex)
        self.load_malla_config()

    def on_coordinate_system_changed(self, selection):
        mode = 1 if selection == "Cartesianas" else 2
        self.config_manager.config_structure["GRID"]["MODE"] = mode
        self.load_malla_config()

    def on_zones_system_changed(self, selection):
        zone = "zgrid" if selection == "Varias zonas" else "ezgrid"
        self.config_manager.config_structure["GRID"]["ZONEGRID"] = zone
        self.load_malla_config()

    def handle_generic_numz_change(self, value, prefix, ncv_prefix):
        for i in range(1, 11):
            le_lon = getattr(self, f"{prefix}_lon_zon{i}", None)
            le_ncv = getattr(self, f"{prefix}_{ncv_prefix}_zon{i}", None)
            le_pot = getattr(self, f"{prefix}_poten_zon{i}", None)

            if i <= value:
                if le_lon:
                    le_lon.setEnabled(True)
                if le_ncv:
                    le_ncv.setEnabled(True)
                if le_pot:
                    le_pot.setEnabled(True)
            else:
                if le_lon:
                    le_lon.setEnabled(False)
                if le_ncv:
                    le_ncv.setEnabled(False)
                if le_pot:
                    le_pot.setEnabled(False)
