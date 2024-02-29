from PySide6 import QtWidgets as qtw
from PySide6.QtCore import Signal, Slot

from bordes_window.ui.bordes_window_ui import Ui_bordes_window


class BordesWindow(qtw.QDialog, Ui_bordes_window):
    def __init__(self, config_manager):
        super().__init__()
        self.setupUi(self)
        self.config_manager = config_manager

        self.pb_addsegment_xmax.clicked.connect(self.add_segment_x_max)
        self.pb_remsegment_xmax.clicked.connect(self.remove_segment_x_max)

        self.pb_addsegment_xmin.clicked.connect(self.add_segment_x_min)
        self.pb_remsegment_xmin.clicked.connect(self.remove_segment_x_min)

        self.pb_addsegment_ymax.clicked.connect(self.add_segment_y_max)
        self.pb_remsegment_ymax.clicked.connect(self.remove_segment_y_max)

        self.pb_addsegment_ymin.clicked.connect(self.add_segment_y_min)
        self.pb_remsegment_ymin.clicked.connect(self.remove_segment_y_min)

        self.pb_addsegment_zmax.clicked.connect(self.add_segment_z_max)
        self.pb_remsegment_zmax.clicked.connect(self.remove_segment_z_max)

        self.pb_addsegment_zmin.clicked.connect(self.add_segment_z_min)
        self.pb_remsegment_zmin.clicked.connect(self.remove_segment_z_min)

        self.lw_bordes.currentRowChanged.connect(self.change_segment_list)

        self.lw_segmentlist_xmax.currentRowChanged.connect(self.change_lon_segment)
        self.lw_segmentlist_xmin.currentRowChanged.connect(self.change_lon_segment)
        self.lw_segmentlist_ymax.currentRowChanged.connect(self.change_lon_segment)
        self.lw_segmentlist_ymin.currentRowChanged.connect(self.change_lon_segment)
        self.lw_segmentlist_zmax.currentRowChanged.connect(self.change_lon_segment)
        self.lw_segmentlist_zmin.currentRowChanged.connect(self.change_lon_segment)

        self.segment_count_xmax = 1
        self.segment_count_xmin = 1
        self.segment_count_ymax = 1
        self.segment_count_ymin = 1
        self.segment_count_zmax = 1
        self.segment_count_zmin = 1

        self.chb_wall.stateChanged.connect(self.handle_chb_state_changed)
        self.chb_inmass.stateChanged.connect(self.handle_chb_state_changed)
        self.chb_outmass.stateChanged.connect(self.handle_chb_state_changed)

        self.chb_value.stateChanged.connect(self.handle_chb_valuefluxconvec_changed)
        self.chb_flux.stateChanged.connect(self.handle_chb_valuefluxconvec_changed)
        self.chb_convec.stateChanged.connect(self.handle_chb_valuefluxconvec_changed)

    def change_segment_list(self):
        current_text_segment = self.lw_bordes.currentItem().text()

        if current_text_segment == "X Max":
            self.sw_segmentlist.setCurrentIndex(0)
            self.sw_segment_addremove.setCurrentIndex(0)

        elif current_text_segment == "X Min":
            self.sw_segmentlist.setCurrentIndex(1)
            self.sw_segment_addremove.setCurrentIndex(1)

        elif current_text_segment == "Y Max":
            self.sw_segmentlist.setCurrentIndex(2)
            self.sw_segment_addremove.setCurrentIndex(2)

        elif current_text_segment == "Y Min":
            self.sw_segmentlist.setCurrentIndex(3)
            self.sw_segment_addremove.setCurrentIndex(3)

        elif current_text_segment == "Z Max":
            self.sw_segmentlist.setCurrentIndex(4)
            self.sw_segment_addremove.setCurrentIndex(4)

        elif current_text_segment == "Z Min":
            self.sw_segmentlist.setCurrentIndex(5)
            self.sw_segment_addremove.setCurrentIndex(5)

        self.update_line_edit()

    def add_segment_x_max(self):
        if self.segment_count_xmax < 5:
            self.segment_count_xmax += 1
            self.lw_segmentlist_xmax.addItem(f"Segmento {self.segment_count_xmax}")

    def remove_segment_x_max(self):
        count_xmax = self.lw_segmentlist_xmax.count()
        if count_xmax > 1:
            self.lw_segmentlist_xmax.takeItem(count_xmax - 1)
            self.segment_count_xmax -= 1

    def add_segment_x_min(self):
        if self.segment_count_xmin < 5:
            self.segment_count_xmin += 1
            self.lw_segmentlist_xmin.addItem(f"Segmento {self.segment_count_xmin}")

    def remove_segment_x_min(self):
        count_xmin = self.lw_segmentlist_xmin.count()
        if count_xmin > 1:
            self.lw_segmentlist_xmin.takeItem(count_xmin - 1)
            self.segment_count_xmin -= 1

    def add_segment_y_max(self):
        if self.segment_count_ymax < 5:
            self.segment_count_ymax += 1
            self.lw_segmentlist_ymax.addItem(f"Segmento {self.segment_count_ymax}")

    def remove_segment_y_max(self):
        count_ymax = self.lw_segmentlist_ymax.count()
        if count_ymax > 1:
            self.lw_segmentlist_ymax.takeItem(count_ymax - 1)
            self.segment_count_ymax -= 1

    def add_segment_y_min(self):
        if self.segment_count_ymin < 5:
            self.segment_count_ymin += 1
            self.lw_segmentlist_ymin.addItem(f"Segmento {self.segment_count_ymin}")

    def remove_segment_y_min(self):
        count_ymin = self.lw_segmentlist_ymin.count()
        if count_ymin > 1:
            self.lw_segmentlist_ymin.takeItem(count_ymin - 1)
            self.segment_count_ymin -= 1

    def add_segment_z_max(self):
        if self.segment_count_zmax < 5:
            self.segment_count_zmax += 1
            self.lw_segmentlist_zmax.addItem(f"Segmento {self.segment_count_zmax}")

    def remove_segment_z_max(self):
        count_zmax = self.lw_segmentlist_zmax.count()
        if count_zmax > 1:
            self.lw_segmentlist_zmax.takeItem(count_zmax - 1)
            self.segment_count_zmax -= 1

    def add_segment_z_min(self):
        if self.segment_count_zmin < 5:
            self.segment_count_zmin += 1
            self.lw_segmentlist_zmin.addItem(f"Segmento {self.segment_count_zmin}")

    def remove_segment_z_min(self):
        count_zmin = self.lw_segmentlist_zmin.count()
        if count_zmin > 1:
            self.lw_segmentlist_zmin.takeItem(count_zmin - 1)
            self.segment_count_zmin -= 1

    def update_line_edit(self):
        current_text_segment_list = self.get_current_segment_list()
        current_segment = (
            current_text_segment_list.currentItem().text()
            if current_text_segment_list.currentItem()
            else ""
        )

        if self.sw_segmentlist.currentIndex() == 0:
            self.m = 0
        elif self.sw_segmentlist.currentIndex() == 1:
            self.m = 5
        if self.sw_segmentlist.currentIndex() == 2:
            self.m = 10
        elif self.sw_segmentlist.currentIndex() == 3:
            self.m = 15
        if self.sw_segmentlist.currentIndex() == 4:
            self.m = 20
        elif self.sw_segmentlist.currentIndex() == 5:
            self.m = 25

        if current_segment == "Segmento 1":
            self.sw_lon_segment.setCurrentIndex(0 + self.m)
        elif current_segment == "Segmento 2":
            self.sw_lon_segment.setCurrentIndex(1 + self.m)
        elif current_segment == "Segmento 3":
            self.sw_lon_segment.setCurrentIndex(2 + self.m)
        elif current_segment == "Segmento 4":
            self.sw_lon_segment.setCurrentIndex(3 + self.m)
        elif current_segment == "Segmento 5":
            self.sw_lon_segment.setCurrentIndex(4 + self.m)

    def change_lon_segment(self):
        self.update_line_edit()

    def get_current_segment_list(self):
        if self.sw_segmentlist.currentIndex() == 0:
            return self.lw_segmentlist_xmax
        elif self.sw_segmentlist.currentIndex() == 1:
            return self.lw_segmentlist_xmin
        elif self.sw_segmentlist.currentIndex() == 2:
            return self.lw_segmentlist_ymax
        elif self.sw_segmentlist.currentIndex() == 3:
            return self.lw_segmentlist_ymin
        elif self.sw_segmentlist.currentIndex() == 4:
            return self.lw_segmentlist_zmax
        elif self.sw_segmentlist.currentIndex() == 5:
            return self.lw_segmentlist_zmin

    def update_entrada_masa(self, es_difusivo):
        print(f"Actualizando Entrada de Masa, es_difusivo: {es_difusivo}")

        # Estado de los checkboxes
        state_wall = self.chb_wall.isChecked()
        state_inmass = self.chb_inmass.isChecked()
        state_outmass = self.chb_outmass.isChecked()
        state_value = self.chb_value.isChecked()
        state_flux = self.chb_flux.isChecked()
        state_convec = self.chb_convec.isChecked()

        # Deshabilitar o habilitar controles basados en condiciones específicas
        velocidades_habilitadas = not es_difusivo and (state_wall or state_inmass)
        fracmass_habilitada = not es_difusivo and state_outmass
        flux_convec_deshabilitado = state_inmass or state_outmass

        # Aplicar estados directamente con condiciones
        self.chb_inmass.setDisabled(es_difusivo)
        self.chb_outmass.setDisabled(es_difusivo)
        self.le_value_veloc_u.setDisabled(not velocidades_habilitadas)
        self.le_value_veloc_v.setDisabled(not velocidades_habilitadas)
        self.le_value_veloc_w.setDisabled(not velocidades_habilitadas)
        self.le_fracmass.setDisabled(not fracmass_habilitada)
        self.chb_value.setDisabled(state_outmass)
        self.chb_flux.setDisabled(flux_convec_deshabilitado)
        self.chb_convec.setDisabled(flux_convec_deshabilitado)

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

    @Slot()
    def handle_chb_state_changed(self, state):
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

    @Slot()
    def handle_chb_valuefluxconvec_changed(self, state):
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
