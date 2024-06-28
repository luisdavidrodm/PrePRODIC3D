from PySide2 import QtWidgets as qtw

from densidad_window.ui.densidad_window_ui import Ui_densidad_window


class DensidadWindow(qtw.QDialog, Ui_densidad_window):

    def __init__(self, config_manager):
        # fmt: off
        super().__init__()
        self.setupUi(self)
        self.config_manager = config_manager
        self.config_name = "DENSE"

        self.cb_condition.currentTextChanged.connect(self.condition_change)

        self.pb_add_region.clicked.connect(self.add_region)
        self.pb_remove_region.clicked.connect(self.remove_region)
        self.pb_add_volume.clicked.connect(self.add_volume)
        self.pb_remove_volume.clicked.connect(self.remove_volume)

        self.lw_regions.currentRowChanged.connect(self.load_volume_config)
        self.lw_volumes.currentRowChanged.connect(self.load_current_config)

        self.region_widgets = [
            "cb_condition", "le_local_value", "le_ref_rho", "le_ref_temp"
        ]
        self.volume_widgets = [
            "le_x_start", "le_x_end", "le_y_start", "le_y_end", "le_z_start", "le_z_end", 
            "chb_exclude_borders", "cb_ex_x_start", "cb_ex_x_end", "cb_ex_y_start", 
            "cb_ex_y_end", "cb_ex_z_start", "cb_ex_z_end"]
        self.widgets = self.region_widgets + self.volume_widgets

        self.config_manager.connect_config(self)
        self.lw_regions.setCurrentItem(self.lw_regions.item(0))
        self.lw_volumes.setCurrentItem(self.lw_volumes.item(0))
        # fmt: on

    def get_configured_widgets(self, region, volume):
        """"""
        # Esta función busca en la configuración y recoge todos los widgets configurados
        config = self.config_manager.dense
        configured_widgets = set()
        if region:
            region_config = config[region.text()]
            configured_widgets.update(key for key, value in region_config.items() if not isinstance(value, dict))
            if volume:
                volume_config = region_config[volume.text()]
                configured_widgets.update(key for key in volume_config.keys())
        return configured_widgets

    def load_current_config(self):
        """"""
        region = self.lw_regions.currentItem()
        volume = self.lw_volumes.currentItem()
        configured_widgets = self.get_configured_widgets(region, volume)
        not_configured_widgets = [widget for widget in self.widgets if widget not in configured_widgets]
        self.toggle_widget_list(not_configured_widgets, False)
        if "cb_condition" not in configured_widgets:
            self.cb_condition.setCurrentText("Valor constante")
        config = self.config_manager.dense
        # Seleccionada una region
        if region is not None:
            self.lw_volumes.setEnabled(True)
            self.pb_add_volume.setEnabled(True)
            self.pb_remove_volume.setEnabled(True)
            # Seleccionado un volumen
            if volume is not None:
                self.toggle_widget_list(self.region_widgets, True)
                self.config_manager.load_config(self, config[region.text()])
                self.condition_change(self.cb_condition.currentText())
                self.toggle_widget_list(self.volume_widgets, True)
                self.config_manager.load_config(self, config[region.text()][volume.text()])
                if self.config_manager.is_mesh_info_complete:
                    volume_data = self.initialize_volume_data()
                    # Verificar si alguno de los valores ya está definido
                    keys = ["le_x_start", "le_x_end", "le_y_start", "le_y_end", "le_z_start", "le_z_end"]
                    if not any(key in config[region.text()][volume.text()] for key in keys):
                        self.le_x_start.setText(volume_data["le_x_start"])
                        self.le_x_end.setText(volume_data["le_x_end"])
                        self.le_y_start.setText(volume_data["le_y_start"])
                        self.le_y_end.setText(volume_data["le_y_end"])
                        self.le_z_start.setText(volume_data["le_z_start"])
                        self.le_z_end.setText(volume_data["le_z_end"])
            else:
                self.toggle_widget_list(self.region_widgets + self.volume_widgets, False)
        else:
            self.toggle_widget_list(self.region_widgets + self.volume_widgets, False)
            self.lw_volumes.setEnabled(False)
            self.lw_volumes.clear()
            self.pb_add_volume.setEnabled(False)
            self.pb_remove_volume.setEnabled(False)

    def load_volume_config(self):
        """"""
        region = self.lw_regions.currentItem()
        if region is not None:
            self.lw_volumes.clear()
            config = self.config_manager.dense[region.text()]
            for key, value in config.items():
                if isinstance(value, dict):
                    self.lw_volumes.addItem(key)
            self.load_current_config()

    def toggle_widget_list(self, widgets, toggle):
        """"""
        for widget_name in widgets:
            widget = getattr(self, widget_name, None)
            if widget:
                widget.setEnabled(toggle)
                if not toggle:
                    if isinstance(widget, qtw.QLineEdit):
                        widget.clear()
                    elif isinstance(widget, qtw.QComboBox):
                        widget.setCurrentText(None)
                    elif isinstance(widget, qtw.QCheckBox):
                        widget.setChecked(toggle)
            else:
                print(f"ERROR AL LIMPIAR: {widget_name} en {widgets}")

    def value_changed(self, value):
        """
        Maneja cambios en los valores de los widgets y actualiza el diccionario de configuraciones.

        Parameters:
        value: El nuevo valor del widget que ha cambiado.
        """
        # fmt: off
        sender = self.sender()
        region = self.lw_regions.currentItem()
        volume = self.lw_volumes.currentItem()
        if value is not None and value != "":
            if region and volume:
                if sender.objectName() in self.volume_widgets:
                    if region.text() not in self.config_manager.dense:
                        self.config_manager.dense[region.text()] = {}
                    if volume.text() not in self.config_manager.dense[region.text()]:
                        self.config_manager.dense[region.text()][volume.text()] = {}
                    self.config_manager.dense[region.text()][volume.text()][sender.objectName()] = value
                elif sender.objectName() in self.region_widgets:
                    if region.text() not in self.config_manager.dense:
                        self.config_manager.dense[region.text()] = {}
                    self.config_manager.dense[region.text()][sender.objectName()] = value
        else:
            if region and volume:
                if sender.objectName() in self.volume_widgets:
                    self.config_manager.dense[region.text()][volume.text()].pop(sender.objectName(), None)
                elif sender.objectName() in self.region_widgets:
                    self.config_manager.dense[region.text()].pop(sender.objectName(), None)

    def add_region(self):
        """"""
        region_number = self.lw_regions.count() + 1
        self.lw_regions.addItem(f"Región {region_number}")
        if f"Región {region_number}" not in self.config_manager.dense:
            self.config_manager.dense[f"Región {region_number}"] = {}
        self.config_manager.dense[f"Región {region_number}"]["Volumen 1"] = {}

    def remove_region(self):
        """"""
        region_count = self.lw_regions.count()
        if region_count > 1:
            last_region = self.lw_regions.item(region_count - 1)
            self.lw_regions.takeItem(region_count - 1)
            self.config_manager.dense.pop(last_region.text(), None)

    def add_volume(self):
        volume_number = self.lw_volumes.count() + 1
        self.lw_volumes.addItem(f"Volumen {volume_number}")
        region = self.lw_regions.currentItem()
        if region is not None:
            volume_key = f"Volumen {volume_number}"
            self.config_manager.dense[region.text()][volume_key] = {}

    def remove_volume(self):
        """"""
        volume_count = self.lw_volumes.count()
        if volume_count > 1:
            last_volume = self.lw_volumes.item(volume_count - 1)
            self.lw_volumes.takeItem(volume_count - 1)
            region = self.lw_regions.currentItem()
            if region is not None:
                self.config_manager.dense[region.text()].pop(last_volume.text(), None)

    def condition_change(self, text):
        if text == "Dependiente de la temperatura":
            self.le_ref_rho.setEnabled(True)
            self.le_ref_temp.setEnabled(True)
            self.le_local_value.setEnabled(False)
            self.le_local_value.clear()
        else:  # if text == "Valor constante":
            self.le_ref_rho.setEnabled(False)
            self.le_ref_temp.setEnabled(False)
            self.le_local_value.setEnabled(True)
            self.le_ref_rho.clear()
            self.le_ref_temp.clear()

    def initialize_volume_data(self):
        """Inicializa los valores de malla para un volumen nuevo"""
        if self.config_manager.is_cartesian and self.config_manager.is_ezgrid:
            volume_data = {
                "le_x_start": "0",
                "le_x_end": self.config_manager.grid["le_xlon"],
                "le_y_start": "0",
                "le_y_end": self.config_manager.grid["le_ylon"],
                "le_z_start": "0",
                "le_z_end": self.config_manager.grid["le_zlon"],
            }
        elif not self.config_manager.is_cartesian and self.config_manager.is_ezgrid:
            volume_data = {
                "le_x_start": "0",
                "le_x_end": self.config_manager.grid["le_titalon"],
                "le_y_start": self.config_manager.grid["le_rini"],
                "le_y_end": self.config_manager.grid["le_rlon"],
                "le_z_start": "0",
                "le_z_end": self.config_manager.grid["le_zloncil"],
            }
        elif self.config_manager.is_cartesian and not self.config_manager.is_ezgrid:
            x_end = sum(
                float(self.config_manager.grid.get(f"le_dirx_lon_zon{i}", 0))
                for i in range(1, self.config_manager.grid["sb_dirx_numz"] + 1)
            )
            y_end = sum(
                float(self.config_manager.grid.get(f"le_diry_lon_zon{i}", 0))
                for i in range(1, self.config_manager.grid["sb_diry_numz"] + 1)
            )
            z_end = sum(
                float(self.config_manager.grid.get(f"le_dirz_lon_zon{i}", 0))
                for i in range(1, self.config_manager.grid["sb_dirz_numz"] + 1)
            )
            volume_data = {
                "le_x_start": "0",
                "le_x_end": str(x_end),
                "le_y_start": "0",
                "le_y_end": str(y_end),
                "le_z_start": "0",
                "le_z_end": str(z_end),
            }
        else:  # if not self.config_manager.is_cartesian and not self.config_manager.is_ezgrid
            x_end = sum(
                float(self.config_manager.grid.get(f"le_dirtita_lon_zon{i}", 0))
                for i in range(1, self.config_manager.grid["sb_dirtita_numz"] + 1)
            )
            y_end = sum(
                float(self.config_manager.grid.get(f"le_dirr_lon_zon{i}", 0))
                for i in range(1, self.config_manager.grid["sb_dirr_numz"] + 1)
            )
            z_end = sum(
                float(self.config_manager.grid.get(f"le_dirzcil_lon_zon{i}", 0))
                for i in range(1, self.config_manager.grid["sb_dirzcil_numz"] + 1)
            )
            y_start = self.config_manager.grid.get("le_dirr_inidom", 0)
            volume_data = {
                "le_x_start": "0",
                "le_x_end": str(x_end),
                "le_y_start": str(y_start),
                "le_y_end": str(y_end),
                "le_z_start": "0",
                "le_z_end": str(z_end),
            }
        return volume_data
