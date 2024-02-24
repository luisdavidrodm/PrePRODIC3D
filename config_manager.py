import json
from collections import OrderedDict


class ConfigManager:
    def __init__(self):
        # Inicializar la estructura de la configuración con las secciones requeridas
        self.config_structure = OrderedDict(
            [
                ("HEADER", OrderedDict()),
                ("GRID", OrderedDict()),
                ("VARIABLES", OrderedDict()),
            ]
        )

    ######################################################################################

    def save_to_json(self, filename):
        # Guardar la configuración en un archivo JSON
        with open(filename, "w") as f:
            json.dump(self.config_structure, f, indent=4)

    def load_from_json(self, filename):
        # Cargar la configuración desde un archivo JSON
        with open(filename, "r") as f:
            self.config_structure = json.load(f, object_pairs_hook=OrderedDict)
