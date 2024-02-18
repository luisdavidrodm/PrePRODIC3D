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

    def set_grid_cil_rini_zu(self, cil_rini_zu):
        self.config_structure["GRID"]["CIL_R(1)_ZU"] = cil_rini_zu

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

    ##CONFIGURACION DE VALORES PARA VARIAS ZONAS - CARTESIANA

    # -COORDENADA X (CARTESIANA)

    def set_grid_cart_nzx(self, cart_nzx):
        self.config_structure["GRID"]["CART_NZX"] = cart_nzx

    def set_grid_cart_xzone_1(self, xzone1):
        self.config_structure["GRID"]["XZONE(1)"] = xzone1

    def set_grid_cart_ncvx_1(self, ncvx1):
        self.config_structure["GRID"]["NCVX(1)"] = ncvx1

    def set_grid_cart_powerx_1(self, powerx1):
        self.config_structure["GRID"]["POWERX(1)"] = powerx1

    def set_grid_cart_xzone_2(self, xzone2):
        self.config_structure["GRID"]["XZONE(2)"] = xzone2

    def set_grid_cart_ncvx_2(self, ncvx2):
        self.config_structure["GRID"]["NCVX(2)"] = ncvx2

    def set_grid_cart_powerx_2(self, powerx2):
        self.config_structure["GRID"]["POWERX(2)"] = powerx2

    def set_grid_cart_xzone_3(self, xzone3):
        self.config_structure["GRID"]["XZONE(3)"] = xzone3

    def set_grid_cart_ncvx_3(self, ncvx3):
        self.config_structure["GRID"]["NCVX(3)"] = ncvx3

    def set_grid_cart_powerx_3(self, powerx3):
        self.config_structure["GRID"]["POWERX(3)"] = powerx3

    def set_grid_cart_xzone_4(self, xzone4):
        self.config_structure["GRID"]["XZONE(4)"] = xzone4

    def set_grid_cart_ncvx_4(self, ncvx4):
        self.config_structure["GRID"]["NCVX(4)"] = ncvx4

    def set_grid_cart_powerx_4(self, powerx4):
        self.config_structure["GRID"]["POWERX(4)"] = powerx4

    def set_grid_cart_xzone_5(self, xzone5):
        self.config_structure["GRID"]["XZONE(5)"] = xzone5

    def set_grid_cart_ncvx_5(self, ncvx5):
        self.config_structure["GRID"]["NCVX(5)"] = ncvx5

    def set_grid_cart_powerx_5(self, powerx5):
        self.config_structure["GRID"]["POWERX(5)"] = powerx5

    def set_grid_cart_xzone_6(self, xzone6):
        self.config_structure["GRID"]["XZONE(6)"] = xzone6

    def set_grid_cart_ncvx_6(self, ncvx6):
        self.config_structure["GRID"]["NCVX(6)"] = ncvx6

    def set_grid_cart_powerx_6(self, powerx6):
        self.config_structure["GRID"]["POWERX(6)"] = powerx6

    def set_grid_cart_xzone_7(self, xzone7):
        self.config_structure["GRID"]["XZONE(7)"] = xzone7

    def set_grid_cart_ncvx_7(self, ncvx7):
        self.config_structure["GRID"]["NCVX(7)"] = ncvx7

    def set_grid_cart_powerx_7(self, powerx7):
        self.config_structure["GRID"]["POWERX(7)"] = powerx7

    def set_grid_cart_xzone_8(self, xzone8):
        self.config_structure["GRID"]["XZONE(8)"] = xzone8

    def set_grid_cart_ncvx_8(self, ncvx8):
        self.config_structure["GRID"]["NCVX(8)"] = ncvx8

    def set_grid_cart_powerx_8(self, powerx8):
        self.config_structure["GRID"]["POWERX(8)"] = powerx8

    def set_grid_cart_xzone_9(self, xzone9):
        self.config_structure["GRID"]["XZONE(9)"] = xzone9

    def set_grid_cart_ncvx_9(self, ncvx9):
        self.config_structure["GRID"]["NCVX(9)"] = ncvx9

    def set_grid_cart_powerx_9(self, powerx9):
        self.config_structure["GRID"]["POWERX(9)"] = powerx9

    def set_grid_cart_xzone_10(self, xzone10):
        self.config_structure["GRID"]["XZONE(10)"] = xzone10

    def set_grid_cart_ncvx_10(self, ncvx10):
        self.config_structure["GRID"]["NCVX(10)"] = ncvx10

    def set_grid_cart_powerx_10(self, powerx10):
        self.config_structure["GRID"]["POWERX(10)"] = powerx10

    # -COORDENADA Y (CARTESIANA)

    def set_grid_cart_nzy(self, cart_nzy):
        self.config_structure["GRID"]["CART_NZY"] = cart_nzy

    def set_grid_cart_yzone_1(self, yzone1):
        self.config_structure["GRID"]["YZONE(1)"] = yzone1

    def set_grid_cart_ncvy_1(self, ncvy1):
        self.config_structure["GRID"]["NCVY(1)"] = ncvy1

    def set_grid_cart_powery_1(self, powery1):
        self.config_structure["GRID"]["POWERY(1)"] = powery1

    def set_grid_cart_yzone_2(self, yzone2):
        self.config_structure["GRID"]["YZONE(2)"] = yzone2

    def set_grid_cart_ncvy_2(self, ncvy2):
        self.config_structure["GRID"]["NCVY(2)"] = ncvy2

    def set_grid_cart_powery_2(self, powery2):
        self.config_structure["GRID"]["POWERY(2)"] = powery2

    def set_grid_cart_yzone_3(self, yzone3):
        self.config_structure["GRID"]["YZONE(3)"] = yzone3

    def set_grid_cart_ncvy_3(self, ncvy3):
        self.config_structure["GRID"]["NCVY(3)"] = ncvy3

    def set_grid_cart_powery_3(self, powery3):
        self.config_structure["GRID"]["POWERY(3)"] = powery3

    def set_grid_cart_yzone_4(self, yzone4):
        self.config_structure["GRID"]["YZONE(4)"] = yzone4

    def set_grid_cart_ncvy_4(self, ncvy4):
        self.config_structure["GRID"]["NCVY(4)"] = ncvy4

    def set_grid_cart_powery_4(self, powery4):
        self.config_structure["GRID"]["POWERY(4)"] = powery4

    def set_grid_cart_yzone_5(self, yzone5):
        self.config_structure["GRID"]["YZONE(5)"] = yzone5

    def set_grid_cart_ncvy_5(self, ncvy5):
        self.config_structure["GRID"]["NCVY(5)"] = ncvy5

    def set_grid_cart_powery_5(self, powery5):
        self.config_structure["GRID"]["POWERY(5)"] = powery5

    def set_grid_cart_yzone_6(self, yzone6):
        self.config_structure["GRID"]["YZONE(6)"] = yzone6

    def set_grid_cart_ncvy_6(self, ncvy6):
        self.config_structure["GRID"]["NCVY(6)"] = ncvy6

    def set_grid_cart_powery_6(self, powery6):
        self.config_structure["GRID"]["POWERY(6)"] = powery6

    def set_grid_cart_yzone_7(self, yzone7):
        self.config_structure["GRID"]["YZONE(7)"] = yzone7

    def set_grid_cart_ncvy_7(self, ncvy7):
        self.config_structure["GRID"]["NCVY(7)"] = ncvy7

    def set_grid_cart_powery_7(self, powery7):
        self.config_structure["GRID"]["POWERY(7)"] = powery7

    def set_grid_cart_yzone_8(self, yzone8):
        self.config_structure["GRID"]["YZONE(8)"] = yzone8

    def set_grid_cart_ncvy_8(self, ncvy8):
        self.config_structure["GRID"]["NCVY(8)"] = ncvy8

    def set_grid_cart_powery_8(self, powery8):
        self.config_structure["GRID"]["POWERY(8)"] = powery8

    def set_grid_cart_yzone_9(self, yzone9):
        self.config_structure["GRID"]["YZONE(9)"] = yzone9

    def set_grid_cart_ncvy_9(self, ncvy9):
        self.config_structure["GRID"]["NCVY(9)"] = ncvy9

    def set_grid_cart_powery_9(self, powery9):
        self.config_structure["GRID"]["POWERY(9)"] = powery9

    def set_grid_cart_yzone_10(self, yzone10):
        self.config_structure["GRID"]["YZONE(10)"] = yzone10

    def set_grid_cart_ncvy_10(self, ncvy10):
        self.config_structure["GRID"]["NCVY(10)"] = ncvy10

    def set_grid_cart_powery_10(self, powery10):
        self.config_structure["GRID"]["POWERY(10)"] = powery10

    # -COORDENADA Z (CARTESIANA)

    def set_grid_cart_nzz(self, cart_nzz):
        self.config_structure["GRID"]["CART_NZZ"] = cart_nzz

    def set_grid_cart_zzone_1(self, zzone1):
        self.config_structure["GRID"]["ZZONE(1)"] = zzone1

    def set_grid_cart_ncvz_1(self, ncvz1):
        self.config_structure["GRID"]["NCVZ(1)"] = ncvz1

    def set_grid_cart_powerz_1(self, powerz1):
        self.config_structure["GRID"]["POWERZ(1)"] = powerz1

    def set_grid_cart_zzone_2(self, zzone2):
        self.config_structure["GRID"]["ZZONE(2)"] = zzone2

    def set_grid_cart_ncvz_2(self, ncvz2):
        self.config_structure["GRID"]["NCVZ(2)"] = ncvz2

    def set_grid_cart_powerz_2(self, powerz2):
        self.config_structure["GRID"]["POWERZ(2)"] = powerz2

    def set_grid_cart_zzone_3(self, zzone3):
        self.config_structure["GRID"]["ZZONE(3)"] = zzone3

    def set_grid_cart_ncvz_3(self, ncvz3):
        self.config_structure["GRID"]["NCVZ(3)"] = ncvz3

    def set_grid_cart_powerz_3(self, powerz3):
        self.config_structure["GRID"]["POWERZ(3)"] = powerz3

    def set_grid_cart_zzone_4(self, zzone4):
        self.config_structure["GRID"]["ZZONE(4)"] = zzone4

    def set_grid_cart_ncvz_4(self, ncvz4):
        self.config_structure["GRID"]["NCVZ(4)"] = ncvz4

    def set_grid_cart_powerz_4(self, powerz4):
        self.config_structure["GRID"]["POWERZ(4)"] = powerz4

    def set_grid_cart_zzone_5(self, zzone5):
        self.config_structure["GRID"]["ZZONE(5)"] = zzone5

    def set_grid_cart_ncvz_5(self, ncvz5):
        self.config_structure["GRID"]["NCVZ(5)"] = ncvz5

    def set_grid_cart_powerz_5(self, powerz5):
        self.config_structure["GRID"]["POWERZ(5)"] = powerz5

    def set_grid_cart_zzone_6(self, zzone6):
        self.config_structure["GRID"]["ZZONE(6)"] = zzone6

    def set_grid_cart_ncvz_6(self, ncvz6):
        self.config_structure["GRID"]["NCVZ(6)"] = ncvz6

    def set_grid_cart_powerz_6(self, powerz6):
        self.config_structure["GRID"]["POWERZ(6)"] = powerz6

    def set_grid_cart_zzone_7(self, zzone7):
        self.config_structure["GRID"]["ZZONE(7)"] = zzone7

    def set_grid_cart_ncvz_7(self, ncvz7):
        self.config_structure["GRID"]["NCVZ(7)"] = ncvz7

    def set_grid_cart_powerz_7(self, powerz7):
        self.config_structure["GRID"]["POWERZ(7)"] = powerz7

    def set_grid_cart_zzone_8(self, zzone8):
        self.config_structure["GRID"]["ZZONE(8)"] = zzone8

    def set_grid_cart_ncvz_8(self, ncvz8):
        self.config_structure["GRID"]["NCVZ(8)"] = ncvz8

    def set_grid_cart_powerz_8(self, powerz8):
        self.config_structure["GRID"]["POWERZ(8)"] = powerz8

    def set_grid_cart_zzone_9(self, zzone9):
        self.config_structure["GRID"]["ZZONE(9)"] = zzone9

    def set_grid_cart_ncvz_9(self, ncvz9):
        self.config_structure["GRID"]["NCVZ(9)"] = ncvz9

    def set_grid_cart_powerz_9(self, powerz9):
        self.config_structure["GRID"]["POWERZ(9)"] = powerz9

    def set_grid_cart_zzone_10(self, zzone10):
        self.config_structure["GRID"]["ZZONE(10)"] = zzone10

    def set_grid_cart_ncvz_10(self, ncvz10):
        self.config_structure["GRID"]["NCVZ(10)"] = ncvz10

    def set_grid_cart_powerz_10(self, powerz10):
        self.config_structure["GRID"]["POWERZ(10)"] = powerz10

    ##CONFIGURACION DE VALORES PARA VARIAS ZONAS - CILINDRICAS

    # -COORDENADA TITA (CILINDRICA)

    def set_grid_cil_nztita(self, cil_nztita):
        self.config_structure["GRID"]["CIL_NZX"] = cil_nztita

    def set_grid_cil_titazone_1(self, titazone1):
        self.config_structure["GRID"]["CIL_XZONE(1)"] = titazone1

    def set_grid_cil_ncvtita_1(self, ncvtita1):
        self.config_structure["GRID"]["CIL_NCVX(1)"] = ncvtita1

    def set_grid_cil_powertita_1(self, powertita1):
        self.config_structure["GRID"]["CIL_POWERX(1)"] = powertita1

    def set_grid_cil_titazone_2(self, titazone2):
        self.config_structure["GRID"]["CIL_XZONE(2)"] = titazone2

    def set_grid_cil_ncvtita_2(self, ncvtita2):
        self.config_structure["GRID"]["CIL_NCVX(2)"] = ncvtita2

    def set_grid_cil_powertita_2(self, powertita2):
        self.config_structure["GRID"]["CIL_POWERX(2)"] = powertita2

    def set_grid_cil_titazone_3(self, titazone3):
        self.config_structure["GRID"]["CIL_XZONE(3)"] = titazone3

    def set_grid_cil_ncvtita_3(self, ncvtita3):
        self.config_structure["GRID"]["CIL_NCVX(3)"] = ncvtita3

    def set_grid_cil_powertita_3(self, powertita3):
        self.config_structure["GRID"]["CIL_POWERX(3)"] = powertita3

    def set_grid_cil_titazone_4(self, titazone4):
        self.config_structure["GRID"]["CIL_XZONE(4)"] = titazone4

    def set_grid_cil_ncvtita_4(self, ncvtita4):
        self.config_structure["GRID"]["CIL_NCVX(4)"] = ncvtita4

    def set_grid_cil_powertita_4(self, powertita4):
        self.config_structure["GRID"]["CIL_POWERX(4)"] = powertita4

    def set_grid_cil_titazone_5(self, titazone5):
        self.config_structure["GRID"]["CIL_XZONE(5)"] = titazone5

    def set_grid_cil_ncvtita_5(self, ncvtita5):
        self.config_structure["GRID"]["CIL_NCVX(5)"] = ncvtita5

    def set_grid_cil_powertita_5(self, powertita5):
        self.config_structure["GRID"]["CIL_POWERX(5)"] = powertita5

    def set_grid_cil_titazone_6(self, titazone6):
        self.config_structure["GRID"]["CIL_XZONE(6)"] = titazone6

    def set_grid_cil_ncvtita_6(self, ncvtita6):
        self.config_structure["GRID"]["CIL_NCVX(6)"] = ncvtita6

    def set_grid_cil_powertita_6(self, powertita6):
        self.config_structure["GRID"]["CIL_POWERX(6)"] = powertita6

    def set_grid_cil_titazone_7(self, titazone7):
        self.config_structure["GRID"]["CIL_XZONE(7)"] = titazone7

    def set_grid_cil_ncvtita_7(self, ncvtita7):
        self.config_structure["GRID"]["CIL_NCVX(7)"] = ncvtita7

    def set_grid_cil_powertita_7(self, powertita7):
        self.config_structure["GRID"]["CIL_POWERX(7)"] = powertita7

    def set_grid_cil_titazone_8(self, titazone8):
        self.config_structure["GRID"]["CIL_XZONE(8)"] = titazone8

    def set_grid_cil_ncvtita_8(self, ncvtita8):
        self.config_structure["GRID"]["CIL_NCVX(8)"] = ncvtita8

    def set_grid_cil_powertita_8(self, powertita8):
        self.config_structure["GRID"]["CIL_POWERX(8)"] = powertita8

    def set_grid_cil_titazone_9(self, titazone9):
        self.config_structure["GRID"]["CIL_XZONE(9)"] = titazone9

    def set_grid_cil_ncvtita_9(self, ncvtita9):
        self.config_structure["GRID"]["CIL_NCVX(9)"] = ncvtita9

    def set_grid_cil_powertita_9(self, powertita9):
        self.config_structure["GRID"]["CIL_POWERX(9)"] = powertita9

    def set_grid_cil_titazone_10(self, titazone10):
        self.config_structure["GRID"]["CIL_XZONE(10)"] = titazone10

    def set_grid_cil_ncvtita_10(self, ncvtita10):
        self.config_structure["GRID"]["CIL_NCVX(10)"] = ncvtita10

    def set_grid_cil_powertita_10(self, powertita10):
        self.config_structure["GRID"]["CIL_POWERX(10)"] = powertita10

    # -COORDENADA R (CILINDRICA) - VARIAS ZONAS

    def set_grid_cil_nzr(self, cil_nzr):
        self.config_structure["GRID"]["CIL_NZY"] = cil_nzr

    def set_grid_cil_rini_vz(self, cil_rini_vz):
        self.config_structure["GRID"]["CIL_R(1)_VZ"] = cil_rini_vz

    def set_grid_cil_rzone_1(self, rzone1):
        self.config_structure["GRID"]["CIL_YZONE(1)"] = rzone1

    def set_grid_cil_ncvr_1(self, ncvr1):
        self.config_structure["GRID"]["CIL_NCVY(1)"] = ncvr1

    def set_grid_cil_powerr_1(self, powerr1):
        self.config_structure["GRID"]["CIL_POWERY(1)"] = powerr1

    def set_grid_cil_rzone_2(self, rzone2):
        self.config_structure["GRID"]["CIL_YZONE(2)"] = rzone2

    def set_grid_cil_ncvr_2(self, ncvr2):
        self.config_structure["GRID"]["CIL_NCVY(2)"] = ncvr2

    def set_grid_cil_powerr_2(self, powerr2):
        self.config_structure["GRID"]["CIL_POWERY(2)"] = powerr2

    def set_grid_cil_rzone_3(self, rzone3):
        self.config_structure["GRID"]["CIL_YZONE(3)"] = rzone3

    def set_grid_cil_ncvr_3(self, ncvr3):
        self.config_structure["GRID"]["CIL_NCVY(3)"] = ncvr3

    def set_grid_cil_powerr_3(self, powerr3):
        self.config_structure["GRID"]["CIL_POWERY(3)"] = powerr3

    def set_grid_cil_rzone_4(self, rzone4):
        self.config_structure["GRID"]["CIL_YZONE(4)"] = rzone4

    def set_grid_cil_ncvr_4(self, ncvr4):
        self.config_structure["GRID"]["CIL_NCVY(4)"] = ncvr4

    def set_grid_cil_powerr_4(self, powerr4):
        self.config_structure["GRID"]["CIL_POWERY(4)"] = powerr4

    def set_grid_cil_rzone_5(self, rzone5):
        self.config_structure["GRID"]["CIL_YZONE(5)"] = rzone5

    def set_grid_cil_ncvr_5(self, ncvr5):
        self.config_structure["GRID"]["CIL_NCVY(5)"] = ncvr5

    def set_grid_cil_powerr_5(self, powerr5):
        self.config_structure["GRID"]["CIL_POWERY(5)"] = powerr5

    def set_grid_cil_rzone_6(self, rzone6):
        self.config_structure["GRID"]["CIL_YZONE(6)"] = rzone6

    def set_grid_cil_ncvr_6(self, ncvr6):
        self.config_structure["GRID"]["CIL_NCVY(6)"] = ncvr6

    def set_grid_cil_powerr_6(self, powerr6):
        self.config_structure["GRID"]["CIL_POWERY(6)"] = powerr6

    def set_grid_cil_rzone_7(self, rzone7):
        self.config_structure["GRID"]["CIL_YZONE(7)"] = rzone7

    def set_grid_cil_ncvr_7(self, ncvr7):
        self.config_structure["GRID"]["CIL_NCVY(7)"] = ncvr7

    def set_grid_cil_powerr_7(self, powerr7):
        self.config_structure["GRID"]["CIL_POWERY(7)"] = powerr7

    def set_grid_cil_rzone_8(self, rzone8):
        self.config_structure["GRID"]["CIL_YZONE(8)"] = rzone8

    def set_grid_cil_ncvr_8(self, ncvr8):
        self.config_structure["GRID"]["CIL_NCVY(8)"] = ncvr8

    def set_grid_cil_powerr_8(self, powerr8):
        self.config_structure["GRID"]["CIL_POWERY(8)"] = powerr8

    def set_grid_cil_rzone_9(self, rzone9):
        self.config_structure["GRID"]["CIL_YZONE(9)"] = rzone9

    def set_grid_cil_ncvr_9(self, ncvr9):
        self.config_structure["GRID"]["CIL_NCVY(9)"] = ncvr9

    def set_grid_cil_powerr_9(self, powerr9):
        self.config_structure["GRID"]["CIL_POWERY(9)"] = powerr9

    def set_grid_cil_rzone_10(self, rzone10):
        self.config_structure["GRID"]["CIL_YZONE(10)"] = rzone10

    def set_grid_cil_ncvr_10(self, ncvr10):
        self.config_structure["GRID"]["CIL_NCVY(10)"] = ncvr10

    def set_grid_cil_powerr_10(self, powerr10):
        self.config_structure["GRID"]["CIL_POWERY(10)"] = powerr10

    # -COORDENADA Z (CILINDRICA) - VARIAS ZONAS

    def set_grid_cil_vz_nzz(self, cil_nzz_vz):
        self.config_structure["GRID"]["CIL_VZ_NZZ"] = cil_nzz_vz

    def set_grid_cil_vz_zzone_1(self, zzone1_vz):
        self.config_structure["GRID"]["CIL_VZ_ZZONE(1)"] = zzone1_vz

    def set_grid_cil_vz_ncvz_1(self, ncvz1_vz):
        self.config_structure["GRID"]["CIL_VZ_NCVZ(1)"] = ncvz1_vz

    def set_grid_cil_vz_powerz_1(self, powerz1_vz):
        self.config_structure["GRID"]["CIL_VZ_POWERZ(1)"] = powerz1_vz

    def set_grid_cil_vz_zzone_2(self, zzone2_vz):
        self.config_structure["GRID"]["CIL_VZ_ZZONE(2)"] = zzone2_vz

    def set_grid_cil_vz_ncvz_2(self, ncvz2_vz):
        self.config_structure["GRID"]["CIL_VZ_NCVZ(2)"] = ncvz2_vz

    def set_grid_cil_vz_powerz_2(self, powerz2_vz):
        self.config_structure["GRID"]["CIL_VZ_POWERZ(2)"] = powerz2_vz

    def set_grid_cil_vz_zzone_3(self, zzone3_vz):
        self.config_structure["GRID"]["CIL_VZ_ZZONE(3)"] = zzone3_vz

    def set_grid_cil_vz_ncvz_3(self, ncvz3_vz):
        self.config_structure["GRID"]["CIL_VZ_NCVZ(3)"] = ncvz3_vz

    def set_grid_cil_vz_powerz_3(self, powerz3_vz):
        self.config_structure["GRID"]["CIL_VZ_POWERZ(3)"] = powerz3_vz

    def set_grid_cil_vz_zzone_4(self, zzone4_vz):
        self.config_structure["GRID"]["CIL_VZ_ZZONE(4)"] = zzone4_vz

    def set_grid_cil_vz_ncvz_4(self, ncvz4_vz):
        self.config_structure["GRID"]["CIL_VZ_NCVZ(4)"] = ncvz4_vz

    def set_grid_cil_vz_powerz_4(self, powerz4_vz):
        self.config_structure["GRID"]["CIL_VZ_POWERZ(4)"] = powerz4_vz

    def set_grid_cil_vz_zzone_5(self, zzone5_vz):
        self.config_structure["GRID"]["CIL_VZ_ZZONE(5)"] = zzone5_vz

    def set_grid_cil_vz_ncvz_5(self, ncvz5_vz):
        self.config_structure["GRID"]["CIL_VZ_NCVZ(5)"] = ncvz5_vz

    def set_grid_cil_vz_powerz_5(self, powerz5_vz):
        self.config_structure["GRID"]["CIL_VZ_POWERZ(5)"] = powerz5_vz

    def set_grid_cil_vz_zzone_6(self, zzone6_vz):
        self.config_structure["GRID"]["CIL_VZ_ZZONE(6)"] = zzone6_vz

    def set_grid_cil_vz_ncvz_6(self, ncvz6_vz):
        self.config_structure["GRID"]["CIL_VZ_NCVZ(6)"] = ncvz6_vz

    def set_grid_cil_vz_powerz_6(self, powerz6_vz):
        self.config_structure["GRID"]["CIL_VZ_POWERZ(6)"] = powerz6_vz

    def set_grid_cil_vz_zzone_7(self, zzone7_vz):
        self.config_structure["GRID"]["CIL_VZ_ZZONE(7)"] = zzone7_vz

    def set_grid_cil_vz_ncvz_7(self, ncvz7_vz):
        self.config_structure["GRID"]["CIL_VZ_NCVZ(7)"] = ncvz7_vz

    def set_grid_cil_vz_powerz_7(self, powerz7_vz):
        self.config_structure["GRID"]["CIL_VZ_POWERZ(7)"] = powerz7_vz

    def set_grid_cil_vz_zzone_8(self, zzone8_vz):
        self.config_structure["GRID"]["CIL_VZ_ZZONE(8)"] = zzone8_vz

    def set_grid_cil_vz_ncvz_8(self, ncvz8_vz):
        self.config_structure["GRID"]["CIL_VZ_NCVZ(8)"] = ncvz8_vz

    def set_grid_cil_vz_powerz_8(self, powerz8_vz):
        self.config_structure["GRID"]["CIL_VZ_POWERZ(8)"] = powerz8_vz

    def set_grid_cil_vz_zzone_9(self, zzone9_vz):
        self.config_structure["GRID"]["CIL_VZ_ZZONE(9)"] = zzone9_vz

    def set_grid_cil_vz_ncvz_9(self, ncvz9_vz):
        self.config_structure["GRID"]["CIL_VZ_NCVZ(9)"] = ncvz9_vz

    def set_grid_cil_vz_powerz_9(self, powerz9_vz):
        self.config_structure["GRID"]["CIL_VZ_POWERZ(9)"] = powerz9_vz

    def set_grid_cil_vz_zzone_10(self, zzone10_vz):
        self.config_structure["GRID"]["CIL_VZ_ZZONE(10)"] = zzone10_vz

    def set_grid_cil_vz_ncvz_10(self, ncvz10_vz):
        self.config_structure["GRID"]["CIL_VZ_NCVZ(10)"] = ncvz10_vz

    def set_grid_cil_vz_powerz_10(self, powerz10_vz):
        self.config_structure["GRID"]["CIL_VZ_POWERZ(10)"] = powerz10_vz

    ######################################################################################

    def save_to_json(self, filename):
        # Guardar la configuración en un archivo JSON
        with open(filename, "w") as f:
            json.dump(self.config_structure, f, indent=4)

    def load_from_json(self, filename):
        # Cargar la configuración desde un archivo JSON
        with open(filename, "r") as f:
            self.config_structure = json.load(f, object_pairs_hook=OrderedDict)
