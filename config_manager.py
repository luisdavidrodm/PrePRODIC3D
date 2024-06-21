import json

from PySide6.QtWidgets import QLineEdit, QSpinBox, QComboBox, QCheckBox, QListWidget


class ConfigManager:
    def __init__(self):
        # Inicializar la estructura de la configuración con las secciones requeridas
        # fmt: off
        self._config_structure = {
            'HEADER': {
                'le_tituloimpre': 'PRINTF',
                'le_titulograf': 'PLOTF'
            },
            'GRID': {
                'cb_tipocoord': 'Cartesianas',
                'cb_tipozonas': 'Zona única',
                'cb_tiposistema': 'Cerrado'
            },
            'VARIABLES': {
                'cb_tsimu': 'Permanente',
                'cb_tipoflujo': 'Difusivo',
                'cb_trataborde': 'Esquema de bajo orden',
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
                'checkBox': 2,
            },
            'BOUND': {
                'X Max': {
                    'Borde base': {}
                },
                'X Min': {
                    'Borde base': {}
                },
                'Y Max': {
                    'Borde base': {}
                },
                'Y Min': {
                    'Borde base': {}
                },
                'Z Max': {
                    'Borde base': {}
                },
                'Z Min': {
                    'Borde base': {}
                }
            },
            'VALUES': {
                'le_var_title1': {
                    'name': 'Velocidad U',
                    'Region 1': {
                        'Volumen 1': {}
                    }
                },
                'le_var_title2': {
                    'name': 'Velocidad V',
                    'Region 1': {
                        'Volumen 1': {}
                    }
                },
                'le_var_title3': {
                    'name': 'Velocidad W',
                    'Region 1': {
                        'Volumen 1': {}
                    }
                },
                'le_var_title4': {
                    'name': 'Corrección de presión',
                    'Region 1': {
                        'Volumen 1': {}
                    }
                },
                'le_var_title5': {
                    'name': 'Temperatura',
                    'Region 1': {
                        'Volumen 1': {}
                    }
                },
                'le_var_title11': {
                    'name': 'Presión',
                    'Region 1': {
                        'Volumen 1': {}
                    }
                },
                'le_var_title12': {
                    'name': 'Función de corriente',
                    'Region 1': {
                        'Volumen 1': {}
                    }
                }
            },
            'OUTPUT': {
                'le_var_title1': {},
                'le_var_title2': {},
                'le_var_title3': {},
                'le_var_title4': {},
                'le_var_title5': {},
                'le_var_title11': {},
                'le_var_title12': {},
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
        # print(f"LOAD_CONFIG: {config}")
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

    def load_patch_config(self):
        # TODO
        return None

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
        return self.grid.get("cb_tipocoord") == "Cartesianas"

    @property
    def is_diffusive(self):
        return self.variables.get("cb_tipoflujo") == "Difusivo"

    @property
    def is_mesh_info_complete(self):
        if self.is_cartesian:
            required_keys = ["le_xlon", "le_ylon", "le_zlon"]
        else:
            required_keys = ["le_titalon", "le_rini", "le_rlon", "le_zloncil"]
        return all(self.grid.get(key) is not None for key in required_keys)
