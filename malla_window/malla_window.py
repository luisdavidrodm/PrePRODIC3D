import sys
from PySide6 import QtWidgets as qtw

from malla_window.ui.malla_window_ui import Ui_malla_window
from config_manager import ConfigManager


class MallaWindow(qtw.QDialog, Ui_malla_window):
    def __init__(self, config_manager):
        super().__init__()
        self.setupUi(self)
        self.config_manager = config_manager

        self.cb_tipocoord.currentTextChanged.connect(self.changeZonas)
        self.cb_tipozonas.currentTextChanged.connect(self.changeZonas)

        self.cb_tipocoord.currentTextChanged.connect(self.on_coordinate_system_changed)

        self.cb_tipozonas.currentTextChanged.connect(self.on_zones_system_changed)

        ##############################################################################################
        # CONEXION DE WIDGETS ZONA UNICA - CARTESIANA

        self.le_xlon.textChanged.connect(self.update_cart_xl)

        self.le_nvcx.textChanged.connect(self.update_cart_nvcx)

        self.le_potenciax.textChanged.connect(self.update_cart_potenciax)

        self.le_ylon.textChanged.connect(self.update_cart_yl)

        self.le_nvcy.textChanged.connect(self.update_cart_nvcy)

        self.le_potenciay.textChanged.connect(self.update_cart_potenciay)

        self.le_zlon.textChanged.connect(self.update_cart_zl)

        self.le_nvcz.textChanged.connect(self.update_cart_nvcz)

        self.le_potenciaz.textChanged.connect(self.update_cart_potenciaz)

        ##############################################################################################
        # CONEXION DE WIDGETS ZONA UNICA - CILINDRICA

        self.le_titalon.textChanged.connect(self.update_cil_tital)

        self.le_nvctita.textChanged.connect(self.update_cil_nvctita)

        self.le_potenciatita.textChanged.connect(self.update_cil_potenciatita)

        self.le_rini.textChanged.connect(self.update_cil_rini)

        self.le_rlon.textChanged.connect(self.update_cil_rl)

        self.le_nvcr.textChanged.connect(self.update_cil_nvcr)

        self.le_potenciar.textChanged.connect(self.update_cil_potenciar)

        self.le_zloncil.textChanged.connect(self.update_cil_zl)

        self.le_nvczcil.textChanged.connect(self.update_cil_nvcz)

        self.le_potenciazcil.textChanged.connect(self.update_cil_potenciaz)

    #####################################################################################

    def changeZonas(self):
        current_text_coord = self.cb_tipocoord.currentText()
        current_text_zona = self.cb_tipozonas.currentText()

        if current_text_zona == "Zona única" and current_text_coord == "Cartesianas":
            self.gbsw_malla2.setCurrentIndex(0)
        elif current_text_zona == "Zona única" and current_text_coord == "Cilindricas":
            self.gbsw_malla2.setCurrentIndex(1)
        elif (
            current_text_zona == "Varias zonas" and current_text_coord == "Cartesianas"
        ):
            self.gbsw_malla2.setCurrentIndex(2)
        elif (
            current_text_zona == "Varias zonas" and current_text_coord == "Cilindricas"
        ):
            self.gbsw_malla2.setCurrentIndex(3)
            self.sb_dirx_numz.valueChanged.connect(self.changingNumBoxX)

    # AYUDAAA
    def changingNumBoxX(self):
        currentNumBox = self.sb_dirx_numz.value()
        if not getattr(
            self.gb_dirx_vz1, "le_dirx_lon_zon{}".format(currentNumBox)
        ).isEnabled():
            getattr(
                self.gb_dirx_vz1, "le_dirx_lon_zon{}".format(currentNumBox)
            ).setEnabled(True)
            getattr(
                self.gb_dirx_vz1, "le_dirx_nvcx_zon{}".format(currentNumBox)
            ).setEnabled(True)
            getattr(
                self.gb_dirx_vz1, "le_dirx_poten_zon{}".format(currentNumBox)
            ).setEnabled(True)
        else:
            try:
                getattr(
                    self.gb_dirx_vz1, "le_dirx_lon_zon{}".format(currentNumBox + 1)
                ).setEnabled(False)
                getattr(
                    self.gb_dirx_vz1, "le_dirx_nvcx_zon{}".format(currentNumBox + 1)
                ).setEnabled(False)
                getattr(
                    self.gb_dirx_vz1, "le_dirx_poten_zon{}".format(currentNumBox + 1)
                ).setEnabled(False)
            except:
                pass

    def on_coordinate_system_changed(self, selection):
        mode = 1 if selection == "Cartesianas" else 2
        self.config_manager.set_grid_mode(mode)

    def on_zones_system_changed(self, selection):
        zone = "zgrid" if selection == "Varias zonas" else "ezgrid"
        self.config_manager.set_grid_zgrid_ezgrid(zone)

    ##############################################################################################
    # METODOS PARA CONEXION DE WIDGETS ZONA UNICA - CARTESIANA

    def update_cart_xl(self, text):
        self.config_manager.set_grid_cart_xl(text)

    def update_cart_nvcx(self, text):
        self.config_manager.set_grid_cart_nvcx(text)

    def update_cart_potenciax(self, text):
        self.config_manager.set_grid_cart_potenciax(text)

    def update_cart_yl(self, text):
        self.config_manager.set_grid_cart_yl(text)

    def update_cart_nvcy(self, text):
        self.config_manager.set_grid_cart_nvcy(text)

    def update_cart_potenciay(self, text):
        self.config_manager.set_grid_cart_potenciay(text)

    def update_cart_zl(self, text):
        self.config_manager.set_grid_cart_zl(text)

    def update_cart_nvcz(self, text):
        self.config_manager.set_grid_cart_nvcz(text)

    def update_cart_potenciaz(self, text):
        self.config_manager.set_grid_cart_potenciaz(text)

    ##############################################################################################
    # METODOS PARA CONEXION DE WIDGETS ZONA UNICA - CILINDRICA

    def update_cil_tital(self, text):
        self.config_manager.set_grid_cil_tital(text)

    def update_cil_nvctita(self, text):
        self.config_manager.set_grid_cil_nvctita(text)

    def update_cil_potenciatita(self, text):
        self.config_manager.set_grid_cil_potenciatita(text)

    def update_cil_rini(self, text):
        self.config_manager.set_grid_cil_rini(text)

    def update_cil_rl(self, text):
        self.config_manager.set_grid_cil_rl(text)

    def update_cil_nvcr(self, text):
        self.config_manager.set_grid_cil_nvcr(text)

    def update_cil_potenciar(self, text):
        self.config_manager.set_grid_cil_potenciar(text)

    def update_cil_zl(self, text):
        self.config_manager.set_grid_cil_zl(text)

    def update_cil_nvcz(self, text):
        self.config_manager.set_grid_cil_nvcz(text)

    def update_cil_potenciaz(self, text):
        self.config_manager.set_grid_cil_potenciaz(text)

    ##############################################################################################


if __name__ == "__main__":
    app = qtw.QApplication(sys.argv)
    config_manager = ConfigManager()  # Crear una instancia del gestor de configuración
    form = MallaWindow(config_manager)
    form.open()
    sys.exit(app.exec())
