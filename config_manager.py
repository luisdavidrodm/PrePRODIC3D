import json

from PySide2.QtWidgets import QLineEdit, QSpinBox, QComboBox, QCheckBox, QListWidget


class ConfigManager:
    def __init__(self):
        # Inicializar la estructura de la configuración con las secciones requeridas
        # fmt: off
        self._config_structure = {
            'HEADER': {
                'le_tituloimpre': 'PRINTF.out',
                'le_titulograf': 'PLOTF'
            },
            'GRID': {
                'cb_coord_type': 'Cartesianas',
                'cb_zone_type': 'Zona única',
                'cb_system_type': 'Abierto', 
                'sb_dirx_numz': 1,
                'sb_diry_numz': 1,
                'sb_dirz_numz': 1,
                'sb_dirtita_numz': 1,
                'sb_dirr_numz': 1,
                'sb_dirzcil_numz': 1,
                'le_dirr_inidom': "0",
                'le_rini': "0"
            },
            'VARIABLES': {
                'cb_tsimu': 'Permanente',
                'cb_tipoflujo': 'Difusivo',
                'cb_trataborde': 'Esquema de alto orden',
                'le_var_title1': 'Velocidad U',
                'le_var_title2': 'Velocidad V',
                'le_var_title3': 'Velocidad W',
                'le_var_title4': 'Corrección de presión',
                'le_var_title5': 'Temperatura',
                'le_var_title11': 'Presión',
                'le_var_title12': 'Función de corriente',
                'chb_ksolve5': 2,
                'chb_kprint5': 2,
                'le_relax5': '1',
            },
            'DENSE': {
                'Región 1': {
                    'Volumen 1': {}
                }
            },
            'BOUND': {
                'X Max': {
                    'Borde base': {'chb_wall': 2}
                },
                'X Min': {
                    'Borde base': {'chb_wall': 2}
                },
                'Y Max': {
                    'Borde base': {'chb_wall': 2}
                },
                'Y Min': {
                    'Borde base': {'chb_wall': 2}
                },
                'Z Max': {
                    'Borde base': {'chb_wall': 2}
                },
                'Z Min': {
                    'Borde base': {'chb_wall': 2}
                }
            },
            'VALUES': {
                'chb_buoyancy': 0,
                'cb_plane': 'XY',
                'le_var_title1': {
                    'name': 'Velocidad U',
                    'Región 1': {
                        'Volumen 1': {}
                    }
                },
                'le_var_title2': {
                    'name': 'Velocidad V',
                    'Región 1': {
                        'Volumen 1': {}
                    }
                },
                'le_var_title3': {
                    'name': 'Velocidad W',
                    'Región 1': {
                        'Volumen 1': {}
                    }
                },
                'le_var_title4': {
                    'name': 'Corrección de presión',
                    'Región 1': {
                        'Volumen 1': {}
                    }
                },
                'le_var_title5': {
                    'name': 'Temperatura',
                    'Región 1': {
                        'Volumen 1': {}
                    }
                },
                'le_var_title11': {
                    'name': 'Presión',
                    'Región 1': {
                        'Volumen 1': {}
                    }
                },
                'le_var_title12': {
                    'name': 'Función de corriente',
                    'Región 1': {
                        'Volumen 1': {}
                    }
                }
            },
            'OUTPUT': {
                'le_var_title1': {'name': 'Velocidad U'},
                'le_var_title2': {'name': 'Velocidad V'},
                'le_var_title3': {'name': 'Velocidad W'},
                'le_var_title4': {'name': 'Corrección de presión'},
                'le_var_title5': {'name': 'Temperatura'},
                'le_var_title11': {'name': 'Presión'},
                'le_var_title12': {'name': 'Función de corriente'},
                'le_last': '5'
            }
        }
        # fmt: on

    ################################################################################
    ##
    ## Slots usados por señales
    ##
    ################################################################################

    def load_from_json(self, filename):
        with open(filename, "r", encoding="utf8") as f:
            self._config_structure = json.load(f)

    def save_to_json(self, filename):
        with open(filename, "w", encoding="utf8") as f:
            json.dump(self._config_structure, f, ensure_ascii=False, indent=4)

    def load_config(self, window, config=None):
        # Carga la configuración de una ventana desde config_manager
        if config is None:
            config = window.config_manager._config_structure[window.config_name]
        for widget_name, value in config.items():
            try:
                if not isinstance(value, dict):
                    widget = getattr(window, widget_name)
                    if isinstance(widget, QLineEdit):
                        widget.setText(value)
                    elif isinstance(widget, QComboBox):
                        widget.setCurrentText(value)
                    elif isinstance(widget, QSpinBox):
                        widget.setValue(value)
                    elif isinstance(widget, QCheckBox):
                        widget.setChecked(value == 2)
                    else:
                        print(f"LOAD_CONFIG / CONTINUE: {widget}")
                        continue
            except Exception as e:
                if not window.config_name == "VALUES" and not widget_name == "name":
                    print(f"ERROR AL CARGAR: {e}")

    def connect_config(self, window):
        for widget_name in window.widgets:
            try:
                widget = getattr(window, widget_name)
                if isinstance(widget, QLineEdit):
                    signal = widget.textChanged
                elif isinstance(widget, QComboBox):
                    signal = widget.currentTextChanged
                elif isinstance(widget, QSpinBox):
                    signal = widget.valueChanged
                elif isinstance(widget, QCheckBox):
                    signal = widget.stateChanged
                elif isinstance(widget, QListWidget):
                    signal = widget.currentRowChanged
                else:
                    continue
                signal.connect(window.value_changed)
            except Exception as e:
                print(f"ERROR AL CONECTAR: {e}")

    def set_patch_config(self, border, patch, key, value):
        """
        Establece la configuración para un parche específico.

        :param border: str - El nombre del borde (ejemplo: "X Max").
        :param patch: str - El nombre del parche (ejemplo: "Borde Base").
        :param config: key - El nombre de la variable a guardar.
        :param config: value - El valor de la variable a guardar.
        """
        if value is not None:
            # Asegurarse de que la estructura de borde y parche exista
            if border not in self.bound:
                self.bound[border] = {}
            if patch not in self.bound[border]:
                self.bound[border][patch] = {}
            self.bound[border][patch][key] = value
        else:
            self.bound[border][patch].pop(key, None)
            if len(self.bound[border][patch]) == 0 and patch != "Borde base":
                self.bound[border].pop(patch, None)

    @property
    def header(self):
        return self._config_structure["HEADER"]

    @property
    def grid(self):
        return self._config_structure["GRID"]

    @property
    def variables(self):
        return self._config_structure["VARIABLES"]

    @property
    def dense(self):
        return self._config_structure["DENSE"]

    @property
    def bound(self):
        return self._config_structure["BOUND"]

    @property
    def values(self):
        return self._config_structure["VALUES"]

    @property
    def output(self):
        return self._config_structure["OUTPUT"]

    @property
    def is_cartesian(self):
        return self.grid.get("cb_coord_type") == "Cartesianas"

    @property
    def is_diffusive(self):
        return self.variables.get("cb_tipoflujo") == "Difusivo"

    @property
    def is_ezgrid(self):
        return self.grid.get("cb_zone_type") == "Zona única"

    @property
    def has_in_mass(self):
        for border in self.bound.values():
            for patch in border.values():
                if patch.get("chb_inmass") == 2:
                    return True
        return False

    @property
    def has_out_mass(self):
        for border in self.bound.values():
            for patch in border.values():
                if patch.get("chb_outmass") == 2:
                    return True
        return False

    @property
    def is_mesh_info_complete(self):
        if self.is_cartesian and self.is_ezgrid:
            required_keys = ["le_xlon", "le_ylon", "le_zlon", "le_nvcx", "le_nvcy", "le_nvcz"]
        elif not self.is_cartesian and self.is_ezgrid:
            required_keys = ["le_titalon", "le_rini", "le_rlon", "le_zloncil", "le_nvctita", "le_nvcr", "le_nvczcil"]
        elif self.is_cartesian and not self.is_ezgrid:
            required_keys = []
            for i in range(1, self.grid["sb_dirx_numz"] + 1):
                required_keys.append(f"le_dirx_lon_zon{i}")
                required_keys.append(f"le_dirtita_lon_zon{i}")
            for i in range(1, self.grid["sb_diry_numz"] + 1):
                required_keys.append(f"le_diry_lon_zon{i}")
                required_keys.append(f"le_diry_nvcy_zon{i}")
            for i in range(1, self.grid["sb_dirz_numz"] + 1):
                required_keys.append(f"le_dirz_lon_zon{i}")
                required_keys.append(f"le_dirz_nvcz_zon{i}")
        else:  # if not self.is_cartesian and not self.is_ezgrid
            required_keys = []
            for i in range(1, self.grid["sb_dirtita_numz"] + 1):
                required_keys.append(f"le_dirtita_lon_zon{i}")
                required_keys.append(f"le_dirtita_nvctita_zon{i}")
            for i in range(1, self.grid["sb_dirr_numz"] + 1):
                required_keys.append(f"le_dirr_lon_zon{i}")
                required_keys.append(f"le_dirr_nvcr_zon{i}")
            for i in range(1, self.grid["sb_dirzcil_numz"] + 1):
                required_keys.append(f"le_dirzcil_lon_zon{i}")
                required_keys.append(f"le_dirzcil_nvczcil_zon{i}")
        return all(self.grid.get(key) is not None for key in required_keys)
