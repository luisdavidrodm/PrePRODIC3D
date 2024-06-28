from PySide2 import QtWidgets as qtw

from malla_window.ui.malla_window_ui import Ui_malla_window


class MallaWindow(qtw.QDialog, Ui_malla_window):

    def __init__(self, config_manager):
        # fmt: off
        super().__init__()
        self.setupUi(self)
        self.config_manager = config_manager
        self.config_name = "GRID"

        self.sb_dirx_numz.valueChanged.connect(lambda value: self.handle_generic_numz_change(value, "le_dirx", "nvcx"))
        self.sb_diry_numz.valueChanged.connect(lambda value: self.handle_generic_numz_change(value, "le_diry", "nvcy"))
        self.sb_dirz_numz.valueChanged.connect(lambda value: self.handle_generic_numz_change(value, "le_dirz", "nvcz"))
        self.sb_dirtita_numz.valueChanged.connect(lambda value: self.handle_generic_numz_change(value, "le_dirtita", "nvctita"))
        self.sb_dirr_numz.valueChanged.connect(lambda value: self.handle_generic_numz_change(value, "le_dirr", "nvcr"))
        self.sb_dirzcil_numz.valueChanged.connect(lambda value: self.handle_generic_numz_change(value, "le_dirzcil", "nvczcil"))
    
        self.widgets = [
            "le_xlon", "le_nvcx", "le_potenciax", "le_ylon", "le_nvcy",
            "le_potenciay", "le_zlon", "le_nvcz", "le_potenciaz", "le_titalon",
            "le_nvctita", "le_potenciatita", "le_rini", "le_rlon", "le_nvcr",
            "le_potenciar", "le_zloncil", "le_nvczcil", "le_potenciazcil",
            "sb_dirx_numz", "sb_diry_numz", "sb_dirz_numz", "sb_dirtita_numz",
            "sb_dirr_numz", "le_dirr_inidom", "sb_dirzcil_numz", "cb_coord_type",
            "cb_zone_type", "cb_system_type"
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

        for direction in ["dirx", "diry", "dirz", "dirtita", "dirr", "dirzcil"]:
            spin_box = getattr(self, f"sb_{direction}_numz")
            spin_box.setMinimum(1)
            spin_box.setMaximum(10)
    
        self.config_manager.connect_config(self)
        self.load_malla_config()

        self.cb_coord_type.currentTextChanged.connect(self.load_malla_config)
        self.cb_zone_type.currentTextChanged.connect(self.load_malla_config)
        # fmt: on

    def load_malla_config(self):
        self.config_manager.load_config(self)
        zone_type = self.cb_zone_type.currentText()
        coord_type = self.cb_coord_type.currentText()
        layer_index = {
            ("Zona única", "Cartesianas"): 0,
            ("Zona única", "Cilindricas"): 1,
            ("Varias zonas", "Cartesianas"): 2,
            ("Varias zonas", "Cilindricas"): 3,
        }.get((zone_type, coord_type), 0)
        self.gbsw_malla.setCurrentIndex(layer_index)

        if layer_index == 2:
            self.handle_generic_numz_change(self.sb_dirx_numz.value(), "le_dirx", "nvcx")
            self.handle_generic_numz_change(self.sb_diry_numz.value(), "le_diry", "nvcy")
            self.handle_generic_numz_change(self.sb_dirz_numz.value(), "le_dirz", "nvcz")
        elif layer_index == 3:
            self.handle_generic_numz_change(self.sb_dirtita_numz.value(), "le_dirtita", "nvctita")
            self.handle_generic_numz_change(self.sb_dirr_numz.value(), "le_dirr", "nvcr")
            self.handle_generic_numz_change(self.sb_dirzcil_numz.value(), "le_dirzcil", "nvczcil")

    def value_changed(self, value):
        sender = self.sender()
        if value is None or value == "":
            self.config_manager.grid.pop(sender.objectName(), None)
        else:
            self.config_manager.grid[sender.objectName()] = value

    def handle_generic_numz_change(self, value, prefix, ncv_prefix):
        attribute_prefixes = [f"{prefix}_lon_zon", f"{prefix}_{ncv_prefix}_zon", f"{prefix}_poten_zon"]
        for i in range(1, 11):
            for attr_prefix in attribute_prefixes:
                le = getattr(self, f"{attr_prefix}{i}", None)
                if le:
                    if i <= value:
                        le.setEnabled(True)
                    else:
                        le.setEnabled(False)
                        le.clear()
