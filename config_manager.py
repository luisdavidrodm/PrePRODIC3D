import json
from collections import OrderedDict


class ConfigManager:
    def __init__(self):
        # Inicializar la estructura de la configuración con las secciones requeridas
        # fmt: off
        self.config_structure = OrderedDict([
            ('HEADER', OrderedDict()),
            ('GRID', OrderedDict()),
            (
                'VARIABLES', OrderedDict([
                ('FT', 'Difusivo')
                ])
                ),
            ('BOUND', OrderedDict([
                ('X_MAX', OrderedDict([('BORDE_BASE', OrderedDict())])),
                ('X_MIN', OrderedDict([('BORDE_BASE', OrderedDict())])),
                ('Y_MAX', OrderedDict([('BORDE_BASE', OrderedDict())])),
                ('Y_MIN', OrderedDict([('BORDE_BASE', OrderedDict())])),
                ('Z_MAX', OrderedDict([('BORDE_BASE', OrderedDict())])),
                ('Z_MIN', OrderedDict([('BORDE_BASE', OrderedDict())])),
            ]))])
        # fmt: on

    ################################################################################
    ##
    ## Slots usados por señales
    ##
    ################################################################################

    def save_to_json(self, filename):
        # Guardar la configuración en un archivo JSON
        with open(filename, "w") as f:
            json.dump(self.config_structure, f, indent=4)

    def load_from_json(self, filename):
        # Cargar la configuración desde un archivo JSON
        with open(filename, "r") as f:
            self.config_structure = json.load(f, object_pairs_hook=OrderedDict)

    def update_patch_config(self, borde, segment_name, key, value):
        # Asegúrate de que la clave del borde y el nombre del segmento estén presentes
        if borde not in self.config_structure:
            self.config_structure[borde] = OrderedDict()
        if segment_name not in self.config_structure[borde]:
            self.config_structure[borde][segment_name] = OrderedDict()

        # Actualiza el valor específico
        self.config_structure[borde][segment_name][key] = value

        # Considera guardar el archivo después de cada cambio o más esporádicamente
        # self.save_to_json('config_file.json')
