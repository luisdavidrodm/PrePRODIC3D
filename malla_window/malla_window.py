from PySide6 import QtWidgets as qtw
from PySide6.QtCore import Signal

from malla_window.ui.malla_window_ui import Ui_malla_window


class MallaWindow(qtw.QDialog, Ui_malla_window):

    longitudes_actualizadas_signal = Signal(list)

    def __init__(self, config_manager):
        # fmt: off
        super().__init__()
        self.setupUi(self)
        self.config_manager = config_manager
        self.config_name = "GRID"

        self.cb_tipocoord.currentTextChanged.connect(self.change_zones)
        self.cb_tipozonas.currentTextChanged.connect(self.change_zones)
        self.cb_tipocoord.currentTextChanged.connect(self.on_coordinate_system_changed)
        self.cb_tipozonas.currentTextChanged.connect(self.on_zones_system_changed)

        self.sb_dirx_numz.valueChanged.connect(lambda value: self.handle_generic_numz_change(value, "le_dirx", "nvcx"))
        self.sb_diry_numz.valueChanged.connect(lambda value: self.handle_generic_numz_change(value, "le_diry", "nvcy"))
        self.sb_dirz_numz.valueChanged.connect(lambda value: self.handle_generic_numz_change(value, "le_dirz", "nvcz"))
        self.sb_dirtita_numz.valueChanged.connect(lambda value: self.handle_generic_numz_change(value, "le_dirtita", "nvctita"))
        self.sb_dirr_numz.valueChanged.connect(lambda value: self.handle_generic_numz_change(value, "le_dirr", "nvcr"))
        self.sb_dirzcil_numz.valueChanged.connect(lambda value: self.handle_generic_numz_change(value, "le_dirzcil", "nvczcil"))

        # Conexion con ConfigManager
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

        self.config_manager.connect_config(self)
        # Cargar configuración inicial
        self.initialize_spin_boxes()
        self.load_malla_config()
        # fmt: on

    def initialize_spin_boxes(self):
        for direction in ["dirx", "diry", "dirz", "dirtita", "dirr", "dirzcil"]:
            spin_box = getattr(self, f"sb_{direction}_numz")
            spin_box.setMinimum(2)
            spin_box.setMaximum(10)

    def load_malla_config(self):
        # Carga la configuración desde config_manager
        self.config_manager.load_config(self)

        # Para asegurar que al abrir la ventana se habiliten los LineEdit dependiendo del NZ cargados
        self.handle_generic_numz_change(self.sb_dirx_numz.value(), "le_dirx", "nvcx")
        self.handle_generic_numz_change(self.sb_diry_numz.value(), "le_diry", "nvcy")
        self.handle_generic_numz_change(self.sb_dirz_numz.value(), "le_dirz", "nvcz")
        self.handle_generic_numz_change(self.sb_dirtita_numz.value(), "le_dirtita", "nvctita")
        self.handle_generic_numz_change(self.sb_dirr_numz.value(), "le_dirr", "nvcr")
        self.handle_generic_numz_change(self.sb_dirzcil_numz.value(), "le_dirzcil", "nvczcil")

    def value_changed(self, value):
        sender = self.sender()
        self.config_manager.config_structure[self.config_name][sender.objectName()] = value

    def change_zones(self):
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
        self.config_manager.config_structure[self.config_name]["MODE"] = mode
        self.load_malla_config()

    def on_zones_system_changed(self, selection):
        zone = "zgrid" if selection == "Varias zonas" else "ezgrid"
        self.config_manager.config_structure[self.config_name]["ZONEGRID"] = zone
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
