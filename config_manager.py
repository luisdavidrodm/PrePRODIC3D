import json
from collections import OrderedDict


class ConfigManager:
    def __init__(self):
        # Inicializar la estructura de la configuración con las secciones requeridas
        # fmt: off
        self.config_structure = OrderedDict([
            ('HEADER', OrderedDict()),
            ('GRID', OrderedDict()),
            ('VARIABLES', OrderedDict([
                ('FT', 'Difusivo')
                ])),
            ('BOUND', OrderedDict([
                ('X Max', OrderedDict([('Borde base', OrderedDict())])),
                ('X Min', OrderedDict([('Borde base', OrderedDict())])),
                ('Y Max', OrderedDict([('Borde base', OrderedDict())])),
                ('Y Min', OrderedDict([('Borde base', OrderedDict())])),
                ('Z Max', OrderedDict([('Borde base', OrderedDict())])),
                ('Z Min', OrderedDict([('Borde base', OrderedDict())])),
            ]))])
        # fmt: on

    ################################################################################
    ##
    ## Slots usados por señales
    ##
    ################################################################################

    def save_to_json(self, filename):
        # Guardar la configuración en un archivo JSON
        with open(filename, "w", encoding="utf8") as f:
            json.dump(self.config_structure, f, indent=4)

    def load_from_json(self, filename):
        # Cargar la configuración desde un archivo JSON
        with open(filename, "r", encoding="utf8") as f:
            self.config_structure = json.load(f, object_pairs_hook=OrderedDict)

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
            if border not in self.config_structure["BOUND"]:
                self.config_structure["BOUND"][border] = OrderedDict()
            if patch not in self.config_structure["BOUND"][border]:
                self.config_structure["BOUND"][border][patch] = OrderedDict()
            self.config_structure["BOUND"][border][patch][key] = value
        else:
            self.config_structure["BOUND"][border][patch].pop(key, None)
            if len(self.config_structure["BOUND"][border][patch]) == 0 and patch != "Borde base":
                self.config_structure["BOUND"][border].pop(patch, None)

    def get_patch_config(self, border, patch):
        """
        Obtiene la configuración para un parche específico.

        :param border: str - El nombre del borde (ejemplo: "X Max").
        :param patch: str - El nombre del parche (ejemplo: "Borde Base").
        :return: dict - La configuración del parche o None si no existe.
        """
        return self.config_structure["BOUND"].get(border, {}).get(patch, None)
