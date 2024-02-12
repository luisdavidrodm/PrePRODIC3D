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


if __name__ == "__main__":
    app = qtw.QApplication(sys.argv)
    config_manager = ConfigManager()  # Crear una instancia del gestor de configuración
    form = MallaWindow(config_manager)
    form.open()
    sys.exit(app.exec())
