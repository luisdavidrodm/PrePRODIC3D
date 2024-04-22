from typing import Union

from PySide6 import QtWidgets as qtw
from PySide6.QtCore import Slot

from bordes_window.ui.bordes_window_ui import Ui_bordes_window


class BordesWindow(qtw.QDialog, Ui_bordes_window):

    def __init__(self, config_manager):
        # fmt: off
        super().__init__()
        self.setupUi(self)
        self.config_manager = config_manager
        self.config_name = "BOUND"

        self.lw_bordes.currentRowChanged.connect(self.select_border)

        for axis in ['x', 'y', 'z']:
            for direction in ['min', 'max']:
                getattr(self, f'pb_addpatch_{axis}{direction}').clicked.connect(getattr(self, f'add_patch_{axis}_{direction}'))
                getattr(self, f'pb_rempatch_{axis}{direction}').clicked.connect(getattr(self, f'remove_patch_{axis}_{direction}'))
                getattr(self, f'lw_patchlist_{axis}{direction}').currentRowChanged.connect(self.select_patch)
                setattr(self, f'patch_count_{axis}{direction}', 1)

        # Conexion con ConfigManager
        self.widgets = [
            "le_value", "le_tempamb", "chb_value", "lw_variables", "le_value_veloc_u",
            "le_value_veloc_v", "le_value_veloc_w", "le_fracmass", "le_transversal_lon",
            "le_transversal_start", "le_vertical_lon", "le_vertical_start"
        ]

        for chb_name in ['wall', 'inmass', 'outmass']:
            getattr(self, f'chb_{chb_name}').stateChanged.connect(self.handle_chb_state_changed)
            self.widgets.append(f'chb_{chb_name}')

        for chb_name in ['value', 'flux', 'convec']:
            getattr(self, f'chb_{chb_name}').stateChanged.connect(self.handle_chb_valuefluxconvec_changed)
            self.widgets.append(f'chb_{chb_name}')

        self.config_manager.connect_config(self)
        # Cargar configuración inicial
        self.clear_and_disable_fields()
        # fmt: on

    ################################################################################
    ##
    ## Funciones de Connect
    ##
    ################################################################################

    def select_border(self):
        """Actualiza la lista de parches segun el borde seleccionado"""
        border_to_index = {"X Max": 0, "X Min": 1, "Y Max": 2, "Y Min": 3, "Z Max": 4, "Z Min": 5}
        current_text_bordes = self.lw_bordes.currentItem().text()
        new_index = border_to_index.get(current_text_bordes, None)

        if new_index is not None:
            # Cambiar al QListWidget correspondiente en el QStackedWidget
            self.sw_patchlist.setCurrentIndex(new_index)
            self.sw_patch_addremove.setCurrentIndex(new_index)
            # Llamar a select_patch para verificar el parche seleccionado
            self.select_patch()
        else:
            # Si no hay un borde seleccionado, limpia y deshabilita los campos relevantes
            self.clear_and_disable_fields()

    def select_patch(self):
        """Actualiza los campos de longitudes de parches segun la seleccion"""
        patch_to_index = {
            "Borde base": 0,
            "Parche 2": 1,
            "Parche 3": 2,
            "Parche 4": 3,
            "Parche 5": 4,
        }
        current_patch_list = self.get_current_patch_list()
        if current_patch_list:
            current_patch = current_patch_list.currentItem().text() if current_patch_list.currentItem() else None
            if current_patch:
                self.load_patch_config()
                return None
        self.clear_and_disable_fields()

    def get_current_patch_list(self) -> Union[qtw.QListWidget, None]:
        """Devuelve la lista de parches dependiendo del borde seleccionado"""
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
        else:
            result = None
        return result

    def get_current_border_and_patch_name(self) -> Union[tuple[str, str], None]:
        """Devuelve el tuple con borde y parche actual en formato ("X Max", "Parche 1")"""
        current_border_item = self.lw_bordes.currentItem()
        if current_border_item is not None:
            current_border = current_border_item.text()
            # Obtiene el parche actualmente seleccionado desde la lista de parches para el borde seleccionado
            current_patch_list = self.get_current_patch_list()
            current_patch_item = current_patch_list.currentItem()
            if current_patch_item is not None:
                current_patch = current_patch_item.text()
                return current_border, current_patch
        return None

    def handle_chb_state_changed(self, state: int):
        """Permite solo seleccionar un tipo de parche"""
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
            self.le_tempamb.setEnabled(sender == self.chb_convec)
            if sender == self.chb_value:
                self.chb_flux.setChecked(False)
                self.chb_convec.setChecked(False)
            elif sender == self.chb_flux:
                self.chb_value.setChecked(False)
                self.chb_convec.setChecked(False)
            elif sender == self.chb_convec:
                self.chb_value.setChecked(False)
                self.chb_flux.setChecked(False)
            if sender != self.chb_convec:
                self.le_tempamb.clear()
                border_and_patch_name = self.get_current_border_and_patch_name()
                if border_and_patch_name:
                    self.config_manager.set_patch_config(
                        border=border_and_patch_name[0], patch=border_and_patch_name[1], key="le_tempamb", value=None
                    )

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
    ## Funciones de Carga
    ##
    ################################################################################

    def value_changed(self, value):
        sender = self.sender()
        # print(sender, sender.objectName())
        border_and_patch_name = self.get_current_border_and_patch_name()
        if border_and_patch_name:
            # Actualiza la configuración para el parche seleccionado
            self.config_manager.set_patch_config(
                border=border_and_patch_name[0], patch=border_and_patch_name[1], key=sender.objectName(), value=value
            )

    def load_patch_config(self):
        """
        Carga la configuración para el borde y parche actualmente seleccionados y
        actualiza la interfaz de usuario con estos valores.
        """
        border_and_patch_name = self.get_current_border_and_patch_name()
        if border_and_patch_name:
            # Habilita los campos si esta seleccionado un parche
            self.le_value.setEnabled(True)
            self.chb_value.setEnabled(True)
            self.chb_value.setChecked(True)
            self.chb_convec.setEnabled(True)
            self.chb_flux.setEnabled(True)
            # Carga la configuración para el parche dado
            patch_config = (
                self.config_manager.config_structure[self.config_name]
                .get(border_and_patch_name[0], {})
                .get(border_and_patch_name[1], None)
            )
            print(patch_config)
            # Actualiza los campos de la UI
            if patch_config:
                self.le_value.setText(patch_config.get("le_value", ""))
                self.le_tempamb.setText(patch_config.get("le_tempamb", ""))
                self.le_value_veloc_u.setText(patch_config.get("le_value_veloc_u", ""))
                self.le_value_veloc_v.setText(patch_config.get("le_value_veloc_v", ""))
                self.le_value_veloc_w.setText(patch_config.get("le_value_veloc_w", ""))
                self.le_fracmass.setText(patch_config.get("le_fracmass", ""))
            else:
                self.chb_value.setChecked(True)
                self.chb_convec.setChecked(False)
                self.chb_flux.setChecked(False)
                self.le_value.clear()
                self.le_tempamb.clear()
                self.le_value_veloc_u.clear()
                self.le_value_veloc_v.clear()
                self.le_value_veloc_w.clear()
                self.le_fracmass.clear()
            self.le_tempamb.setEnabled(self.chb_convec.isChecked())

    def clear_and_disable_fields(self):
        """Limpia y deshabilita los campos si es necesario."""
        self.chb_value.setChecked(False)
        self.chb_convec.setChecked(False)
        self.chb_flux.setChecked(False)
        self.chb_value.setEnabled(False)
        self.chb_convec.setEnabled(False)
        self.chb_flux.setEnabled(False)
        self.le_value.setEnabled(False)
        self.le_tempamb.setEnabled(False)
        # self.le_value_veloc_u.setEnabled(False)
        # self.le_value_veloc_v.setEnabled(False)
        # self.le_value_veloc_w.setEnabled(False)
        if self.le_value.text():
            self.le_value.clear()
        if self.le_tempamb.text():
            self.le_tempamb.clear()
        # if self.le_value_veloc_u.text():
        #     self.le_value_veloc_u.text()
        # if self.le_value_veloc_v.text():
        #     self.le_value_veloc_v.text()
        # if self.le_value_veloc_w.text():
        #     self.le_value_veloc_w.text()

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

        # self.le_fracmass.setDisabled(not fracmass_habilitada)
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
