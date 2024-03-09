from PySide6 import QtWidgets as qtw
from PySide6.QtCore import Signal

from variables_window.ui.variables_window_ui import Ui_variables_window


class VariablesWindow(qtw.QDialog, Ui_variables_window):
    tipo_flujo_cambio_signal = Signal(bool)
    variables_signal = Signal(list)

    def __init__(self, config_manager):
        super().__init__()
        self.setupUi(self)
        self.config_manager = config_manager

        self.cb_tsimu.currentTextChanged.connect(self.changeTipoSimu)
        self.le_iptm.textChanged.connect(lambda text: self.update_config("IPTM", text))
        self.le_dt.textChanged.connect(lambda text: self.update_config("DT", text))
        self.cb_tipoflujo.currentTextChanged.connect(self.handle_tipo_flujo_cambio)
        self.cb_trataborde.currentTextChanged.connect(self.update_variables_kord)
        self.le_var_title5.textChanged.connect(self.enviar_datos_variables)
        self.le_var_title6.textChanged.connect(self.enviar_datos_variables)
        self.le_var_title7.textChanged.connect(self.enviar_datos_variables)
        self.le_var_title8.textChanged.connect(self.enviar_datos_variables)
        self.le_var_title9.textChanged.connect(self.enviar_datos_variables)
        self.le_var_title10.textChanged.connect(self.enviar_datos_variables)
        self.le_var_title11.textChanged.connect(self.enviar_datos_variables)
        self.le_var_title12.textChanged.connect(self.enviar_datos_variables)

        self.le_var_title5.setText("Temperatura")

        for i in range(1, 13):
            getattr(self, f"le_var_title{i}").textChanged.connect(
                lambda text, i=i: self.update_config(f"TITLE({i})", text)
            )
            getattr(self, f"chb_ksolve{i}").stateChanged.connect(
                lambda state, i=i: self.update_config_ksolve(f"KSOLVE({i})", state)
            )
            getattr(self, f"chb_kprint{i}").stateChanged.connect(
                lambda state, i=i: self.update_config_kprint(f"KPRINT({i})", state)
            )
            getattr(self, f"le_relax{i}").textChanged.connect(lambda text, i=i: self.update_config(f"RELAX({i})", text))

    def changeTipoSimu(self):
        current_text_simu = self.cb_tsimu.currentText()

        if current_text_simu == "Permanente":
            self.sw_tsimu.setCurrentIndex(0)
        elif current_text_simu == "Transitorio":
            self.sw_tsimu.setCurrentIndex(1)

    def update_variables_kord(self, selection):
        kord = 1 if selection == "Esquema de bajo orden" else 2
        self.config_manager.config_structure["VARIABLES"]["KORD"] = kord

    def update_config(self, config_key, text):
        # Actualiza el valor de la configuración en el ConfigManager
        self.config_manager.config_structure["VARIABLES"][config_key] = text

    def update_config_ksolve(self, config_key, state):
        value = 1 if state == 2 else 0
        self.config_manager.config_structure["VARIABLES"][config_key] = value

    def update_config_kprint(self, config_key, state):
        value = 1 if state == 2 else 0
        self.config_manager.config_structure["VARIABLES"][config_key] = value

    def handle_tipo_flujo_cambio(self, text):
        # Emitir 'True' si es "Difusivo", de lo contrario 'False'
        print(f"Cambiando tipo de flujo a: {text}")  # Impresión de depuración
        self.tipo_flujo_cambio_signal.emit(text == "Difusivo")

    def enviar_datos_variables(self):
        datos_variables = [
            self.le_var_title5.text(),
            self.le_var_title6.text(),
            self.le_var_title7.text(),
            self.le_var_title8.text(),
            self.le_var_title9.text(),
            self.le_var_title10.text(),
            self.le_var_title11.text(),
            self.le_var_title12.text(),
        ]
        self.variables_signal.emit(datos_variables)
