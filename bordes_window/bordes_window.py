from collections import OrderedDict

from PySide6 import QtWidgets as qtw
from PySide6.QtCore import Slot

from bordes_window.ui.bordes_window_ui import Ui_bordes_window


class BordesWindow(qtw.QDialog, Ui_bordes_window):
    def __init__(self, config_manager):
        super().__init__()
        self.setupUi(self)
        self.config_manager = config_manager

        self.pb_addpatch_xmax.clicked.connect(self.add_patch_x_max)
        self.pb_rempatch_xmax.clicked.connect(self.remove_patch_x_max)

        self.pb_addpatch_xmin.clicked.connect(self.add_patch_x_min)
        self.pb_rempatch_xmin.clicked.connect(self.remove_patch_x_min)

        self.pb_addpatch_ymax.clicked.connect(self.add_patch_y_max)
        self.pb_rempatch_ymax.clicked.connect(self.remove_patch_y_max)

        self.pb_addpatch_ymin.clicked.connect(self.add_patch_y_min)
        self.pb_rempatch_ymin.clicked.connect(self.remove_patch_y_min)

        self.pb_addpatch_zmax.clicked.connect(self.add_patch_z_max)
        self.pb_rempatch_zmax.clicked.connect(self.remove_patch_z_max)

        self.pb_addpatch_zmin.clicked.connect(self.add_patch_z_min)
        self.pb_rempatch_zmin.clicked.connect(self.remove_patch_z_min)

        self.lw_bordes.currentRowChanged.connect(self.change_patch_list)

        self.lw_patchlist_xmax.currentRowChanged.connect(self.update_line_edit)
        self.lw_patchlist_xmin.currentRowChanged.connect(self.update_line_edit)
        self.lw_patchlist_ymax.currentRowChanged.connect(self.update_line_edit)
        self.lw_patchlist_ymin.currentRowChanged.connect(self.update_line_edit)
        self.lw_patchlist_zmax.currentRowChanged.connect(self.update_line_edit)
        self.lw_patchlist_zmin.currentRowChanged.connect(self.update_line_edit)

        self.patch_count_xmax = 1
        self.patch_count_xmin = 1
        self.patch_count_ymax = 1
        self.patch_count_ymin = 1
        self.patch_count_zmax = 1
        self.patch_count_zmin = 1

        self.chb_wall.stateChanged.connect(self.handle_chb_state_changed)
        self.chb_inmass.stateChanged.connect(self.handle_chb_state_changed)
        self.chb_outmass.stateChanged.connect(self.handle_chb_state_changed)

        self.chb_value.stateChanged.connect(self.handle_chb_valuefluxconvec_changed)
        self.chb_flux.stateChanged.connect(self.handle_chb_valuefluxconvec_changed)
        self.chb_convec.stateChanged.connect(self.handle_chb_valuefluxconvec_changed)

        self.le_value.textChanged.connect(self.on_le_value_changed)

    ################################################################################
    ##
    ## Funciones de Connect
    ##
    ################################################################################

    def change_patch_list(self):
        """Actualiza la lista de segmentos segun el borde seleccionado"""
        current_text_bordes = self.lw_bordes.currentItem().text()

        if current_text_bordes == "X Max":
            self.sw_patchlist.setCurrentIndex(0)
            self.sw_patch_addremove.setCurrentIndex(0)

        elif current_text_bordes == "X Min":
            self.sw_patchlist.setCurrentIndex(1)
            self.sw_patch_addremove.setCurrentIndex(1)

        elif current_text_bordes == "Y Max":
            self.sw_patchlist.setCurrentIndex(2)
            self.sw_patch_addremove.setCurrentIndex(2)

        elif current_text_bordes == "Y Min":
            self.sw_patchlist.setCurrentIndex(3)
            self.sw_patch_addremove.setCurrentIndex(3)

        elif current_text_bordes == "Z Max":
            self.sw_patchlist.setCurrentIndex(4)
            self.sw_patch_addremove.setCurrentIndex(4)

        elif current_text_bordes == "Z Min":
            self.sw_patchlist.setCurrentIndex(5)
            self.sw_patch_addremove.setCurrentIndex(5)

        self.update_line_edit()

    def update_line_edit(self):
        """Actualiza los campos de longitudes de segmentos segun la seleccion"""
        current_text_patch_list = self.get_current_patch_list()
        current_patch = current_text_patch_list.currentItem().text() if current_text_patch_list.currentItem() else ""

        m = self.sw_patchlist.currentIndex() * 5
        patch_to_index = {
            "Borde base": 0,
            "Parche 2": 1,
            "Parche 3": 2,
            "Parche 4": 3,
            "Parche 5": 4,
        }
        base_index = patch_to_index.get(current_patch, 0)
        self.sw_lon_patch.setCurrentIndex(base_index + m)

    def get_current_patch_list(self) -> qtw.QListWidget:
        """Devuelve la lista de segmentos dependiendo del borde seleccionado"""
        if self.sw_patchlist.currentIndex() == 0:
            result = self.lw_patchlist_xmax
        elif self.sw_patchlist.currentIndex() == 1:
            result = self.lw_patchlist_xmin
        elif self.sw_patchlist.currentIndex() == 2:
            result = self.lw_patchlist_ymax
        elif self.sw_patchlist.currentIndex() == 3:
            result = self.lw_patchlist_ymin
        elif self.sw_patchlist.currentIndex() == 4:
            result = self.lw_patchlist_zmax
        elif self.sw_patchlist.currentIndex() == 5:
            result = self.lw_patchlist_zmin
        print(result)
        for index in range(result.count()):
            item = result.item(index)
            print(index, item.text())
        return result

    def handle_chb_state_changed(self, state: int):
        """Permite solo seleccionar un tipo de segmento"""
        sender = self.sender()
        if state == 2:
            if sender == self.chb_wall:
                self.chb_inmass.setChecked(False)
                self.chb_outmass.setChecked(False)
            elif sender == self.chb_inmass:
                self.chb_wall.setChecked(False)
                self.chb_outmass.setChecked(False)
            elif sender == self.chb_outmass:
                self.chb_wall.setChecked(False)
                self.chb_inmass.setChecked(False)

    def handle_chb_valuefluxconvec_changed(self, state: int):
        """Permite solo seleccionar un tipo de variable escalar"""
        sender = self.sender()
        if state == 2:
            if sender == self.chb_value:
                self.chb_flux.setChecked(False)
                self.chb_convec.setChecked(False)
            elif sender == self.chb_flux:
                self.chb_value.setChecked(False)
                self.chb_convec.setChecked(False)
            elif sender == self.chb_convec:
                self.chb_value.setChecked(False)
                self.chb_flux.setChecked(False)

    def on_le_value_changed(self, new_value: str):
        current_index = self.sw_patchlist.currentIndex()
        current_borde = self.lw_bordes.currentItem().text().replace(" ", "_").lower()
        segment_name = f"Parche {current_index + 1}"

        # Actualiza el valor en el ConfigManager
        self.config_manager.update_patch_config(current_borde, segment_name, "value", new_value)

        if current_borde not in self.config_structure:
            self.config_structure[current_borde] = OrderedDict()
        if segment_name not in self.config_structure[current_borde]:
            self.config_structure[current_borde][segment_name] = OrderedDict()

        # Actualiza el valor específico
        self.config_structure[current_borde][segment_name][key] = value

    def load_segment_config(self, borde, segment_name):
        # Carga la configuración para el segmento dado y actualiza los campos de la UI
        segment_config = self.config_manager.config_structure.get(borde, {}).get(segment_name, {})
        value = segment_config.get("value", "")  # Usa un valor predeterminado si no se encuentra
        self.le_value.setText(value)

    def add_patch_x_max(self):
        if self.patch_count_xmax < 5:
            self.patch_count_xmax += 1
            self.lw_patchlist_xmax.addItem(f"Parche {self.patch_count_xmax}")

    def remove_patch_x_max(self):
        count_xmax = self.lw_patchlist_xmax.count()
        if count_xmax > 1:
            self.lw_patchlist_xmax.takeItem(count_xmax - 1)
            self.patch_count_xmax -= 1

    def add_patch_x_min(self):
        if self.patch_count_xmin < 5:
            self.patch_count_xmin += 1
            self.lw_patchlist_xmin.addItem(f"Parche {self.patch_count_xmin}")

    def remove_patch_x_min(self):
        count_xmin = self.lw_patchlist_xmin.count()
        if count_xmin > 1:
            self.lw_patchlist_xmin.takeItem(count_xmin - 1)
            self.patch_count_xmin -= 1

    def add_patch_y_max(self):
        if self.patch_count_ymax < 5:
            self.patch_count_ymax += 1
            self.lw_patchlist_ymax.addItem(f"Parche {self.patch_count_ymax}")

    def remove_patch_y_max(self):
        count_ymax = self.lw_patchlist_ymax.count()
        if count_ymax > 1:
            self.lw_patchlist_ymax.takeItem(count_ymax - 1)
            self.patch_count_ymax -= 1

    def add_patch_y_min(self):
        if self.patch_count_ymin < 5:
            self.patch_count_ymin += 1
            self.lw_patchlist_ymin.addItem(f"Parche {self.patch_count_ymin}")

    def remove_patch_y_min(self):
        count_ymin = self.lw_patchlist_ymin.count()
        if count_ymin > 1:
            self.lw_patchlist_ymin.takeItem(count_ymin - 1)
            self.patch_count_ymin -= 1

    def add_patch_z_max(self):
        if self.patch_count_zmax < 5:
            self.patch_count_zmax += 1
            self.lw_patchlist_zmax.addItem(f"Parche {self.patch_count_zmax}")

    def remove_patch_z_max(self):
        count_zmax = self.lw_patchlist_zmax.count()
        if count_zmax > 1:
            self.lw_patchlist_zmax.takeItem(count_zmax - 1)
            self.patch_count_zmax -= 1

    def add_patch_z_min(self):
        if self.patch_count_zmin < 5:
            self.patch_count_zmin += 1
            self.lw_patchlist_zmin.addItem(f"Parche {self.patch_count_zmin}")

    def remove_patch_z_min(self):
        count_zmin = self.lw_patchlist_zmin.count()
        if count_zmin > 1:
            self.lw_patchlist_zmin.takeItem(count_zmin - 1)
            self.patch_count_zmin -= 1

    ################################################################################
    ##
    ## Funciones de Señales
    ##
    ################################################################################

    @Slot()
    def update_entrada_masa(self, es_difusivo: bool):
        print(f"Actualizando Entrada de Masa, es_difusivo: {es_difusivo}")

        # Estado de los checkboxes
        # state_wall = self.chb_wall.isChecked()
        state_inmass = self.chb_inmass.isChecked()
        state_outmass = self.chb_outmass.isChecked()
        # state_value = self.chb_value.isChecked()
        state_flux = self.chb_flux.isChecked()
        state_convec = self.chb_convec.isChecked()

        # Deshabilitar o habilitar controles basados en condiciones específicas
        velocidades_habilitadas = not es_difusivo and state_inmass
        fracmass_habilitada = not es_difusivo and state_outmass
        flux_convec_deshabilitado = es_difusivo and state_inmass
        temamb_habilitada = state_convec

        # Manejo de condiciones especiales para resetear checkboxes
        if es_difusivo or not (state_inmass or state_outmass):
            self.chb_inmass.setChecked(False)
            self.chb_outmass.setChecked(False)
        if state_inmass or state_outmass:
            self.chb_wall.setChecked(False)

        if not (state_flux or state_convec):
            self.chb_convec.setChecked(False)
            self.chb_flux.setChecked(False)
        if state_flux or state_convec:
            self.chb_value.setChecked(False)

        # Aplicar estados directamente con condiciones
        self.chb_inmass.setDisabled(es_difusivo)
        self.chb_outmass.setDisabled(es_difusivo)
        self.le_value_veloc_u.setDisabled(
            (not velocidades_habilitadas and (self.sw_patchlist.currentIndex() in [0, 1])) or state_outmass
        )
        self.le_value_veloc_v.setDisabled(
            (not velocidades_habilitadas and (self.sw_patchlist.currentIndex() in [2, 3])) or state_outmass
        )
        self.le_value_veloc_w.setDisabled(
            (not velocidades_habilitadas and (self.sw_patchlist.currentIndex() in [4, 5])) or state_outmass
        )

        self.le_fracmass.setDisabled(not fracmass_habilitada)
        self.le_tempamb.setDisabled(not temamb_habilitada)
        self.le_value.setDisabled(state_outmass)
        self.chb_value.setDisabled(state_outmass)
        self.chb_flux.setDisabled(flux_convec_deshabilitado or state_outmass)
        self.chb_convec.setDisabled(flux_convec_deshabilitado or state_outmass)

    @Slot()
    def agregar_variables_lista(self, variables: list):
        print(f"Actualizando Lista de variables: {variables}")
        self.lw_variables.clear()
        self.lw_variables.addItems(variables)

    @Slot()
    def actualizar_longitudes(self, longitudes: list):
        self.le_xmax_bb_ylon.setText(str(longitudes[1]))
        self.le_xmax_bb_zlon.setText(str(longitudes[2]))
        self.le_xmax_bb_ystart.setText(str(longitudes[3]))
        self.le_xmin_bb_ylon.setText(str(longitudes[1]))
        self.le_xmin_bb_zlon.setText(str(longitudes[2]))
        self.le_xmin_bb_ystart.setText(str(longitudes[3]))
        self.le_ymax_bb_xlon.setText(str(longitudes[0]))
        self.le_ymax_bb_zlon.setText(str(longitudes[2]))
        self.le_ymin_bb_xlon.setText(str(longitudes[0]))
        self.le_ymin_bb_zlon.setText(str(longitudes[2]))
        self.le_zmax_bb_xlon.setText(str(longitudes[0]))
        self.le_zmax_bb_ylon.setText(str(longitudes[1]))
        self.le_zmax_bb_ystart.setText(str(longitudes[3]))
        self.le_zmin_bb_xlon.setText(str(longitudes[0]))
        self.le_zmin_bb_ylon.setText(str(longitudes[1]))
        self.le_zmin_bb_ystart.setText(str(longitudes[3]))
