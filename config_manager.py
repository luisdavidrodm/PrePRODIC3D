import json
from collections import OrderedDict


class ConfigManager:
    def __init__(self):
        # Inicializar la estructura de la configuración con las secciones requeridas
        self.config_structure = OrderedDict(
            [
                ("HEADER", OrderedDict()),
                ("GRID", OrderedDict()),
            ]
        )

    ######################################################################################
    # CONFIGURACION DE VALORES PARA SECCION INICIO

    def set_header(self, header):
        # Configurar los valores para la sección HEADER
        self.config_structure["HEADER"]["HEADER"] = header

    def set_printf(self, printf):
        # Configurar los valores para la sección PRINTF
        self.config_structure["HEADER"]["PRINTF"] = printf

    def set_plotf(self, plotf):
        # Configurar los valores para la sección PLOTF
        self.config_structure["HEADER"]["PLOTF"] = plotf

    ######################################################################################
    # CONFIGURACION DE VALORES PARA SECCION GRID

    def set_grid_mode(self, mode):
        # Configurar el modo para la sección GRID
        self.config_structure["GRID"]["MODE"] = mode

    def set_grid_zgrid_ezgrid(self, zone):
        self.config_structure["GRID"]["ZONEGRID"] = zone

    ##CONFIGURACION DE VALORES PARA ZONAS UNICAS - CARTESIANO

    def set_grid_cart_xl(self, cart_xl):
        self.config_structure["GRID"]["CART_XL"] = cart_xl

    def set_grid_cart_nvcx(self, cart_nvcx):
        self.config_structure["GRID"]["CART_NVCX"] = cart_nvcx

    def set_grid_cart_potenciax(self, cart_powerx):
        self.config_structure["GRID"]["CART_POWERX"] = cart_powerx

    def set_grid_cart_yl(self, cart_yl):
        self.config_structure["GRID"]["CART_YL"] = cart_yl

    def set_grid_cart_nvcy(self, cart_nvcy):
        self.config_structure["GRID"]["CART_NVCY"] = cart_nvcy

    def set_grid_cart_potenciay(self, cart_powery):
        self.config_structure["GRID"]["CART_POWERY"] = cart_powery

    def set_grid_cart_zl(self, cart_zl):
        self.config_structure["GRID"]["CART_ZL"] = cart_zl

    def set_grid_cart_nvcz(self, cart_nvcz):
        self.config_structure["GRID"]["CART_NVCZ"] = cart_nvcz

    def set_grid_cart_potenciaz(self, cart_powerz):
        self.config_structure["GRID"]["CART_POWERZ"] = cart_powerz

    ##CONFIGURACION DE VALORES PARA ZONAS UNICAS - CILINDRICO

    def set_grid_cil_tital(self, cil_tital):
        self.config_structure["GRID"]["CIL_TITAL"] = cil_tital

    def set_grid_cil_nvctita(self, cil_nvctita):
        self.config_structure["GRID"]["CIL_NVCTITA"] = cil_nvctita

    def set_grid_cil_potenciatita(self, cil_powertita):
        self.config_structure["GRID"]["CIL_POWERTITA"] = cil_powertita

    def set_grid_cil_rini(self, cil_rini):
        self.config_structure["GRID"]["CIL_RINI"] = cil_rini

    def set_grid_cil_rl(self, cil_rl):
        self.config_structure["GRID"]["CIL_RL"] = cil_rl

    def set_grid_cil_nvcr(self, cil_nvcr):
        self.config_structure["GRID"]["CIL_NVCR"] = cil_nvcr

    def set_grid_cil_potenciar(self, cil_powerr):
        self.config_structure["GRID"]["CIL_POWERR"] = cil_powerr

    def set_grid_cil_zl(self, cil_zl):
        self.config_structure["GRID"]["CIL_ZL"] = cil_zl

    def set_grid_cil_nvcz(self, cil_nvcz):
        self.config_structure["GRID"]["CIL_NVCZ"] = cil_nvcz

    def set_grid_cil_potenciaz(self, cil_powerz):
        self.config_structure["GRID"]["CIL_POWERZ"] = cil_powerz

    ######################################################################################

    def save_to_json(self, filename):
        # Guardar la configuración en un archivo JSON
        with open(filename, "w") as f:
            json.dump(self.config_structure, f, indent=4)

    def load_from_json(self, filename):
        # Cargar la configuración desde un archivo JSON
        with open(filename, "r") as f:
            self.config_structure = json.load(f, object_pairs_hook=OrderedDict)
