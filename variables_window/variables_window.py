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

        self.cb_tsimu.currentTextChanged.connect(self.change_tipo_simu)
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
            if hasattr(self, f"le_var_title{i}"):
                getattr(self, f"le_var_title{i}").textChanged.connect(
                    lambda text, i=i: self.update_config(f"TITLE({i})", text)
                )

            if hasattr(self, f"chb_ksolve{i}"):
                getattr(self, f"chb_ksolve{i}").stateChanged.connect(
                    lambda state, i=i: self.update_config_ksolve(f"KSOLVE({i})", state)
                )

            if hasattr(self, f"chb_kprint{i}"):
                getattr(self, f"chb_kprint{i}").stateChanged.connect(
                    lambda state, i=i: self.update_config_kprint(f"KPRINT({i})", state)
                )

            if hasattr(self, f"le_relax{i}"):
                getattr(self, f"le_relax{i}").textChanged.connect(
                    lambda text, i=i: self.update_config(f"RELAX({i})", text)
                )

        self.cb_tipoflujo.currentIndexChanged.connect(self.handle_flujo_change)

        for i in range(6, 11):  # Para le_var_title6 hasta le_var_title10
            getattr(self, f"le_var_title{i}").textChanged.connect(lambda: self.controlarWidgetsTitles())

    def change_tipo_simu(self):
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

    def handle_flujo_change(self):
        flujo = self.cb_tipoflujo.currentText()

        # Si el flujo es Flujo Laminar, chequea los CheckBox y habilita/habilita y establece los QLineEdit
        if flujo == "Flujo Laminar":
            # Chequear CheckBoxes
            for chb_name in [
                "chb_kprint1",
                "chb_kprint2",
                "chb_kprint3",
                "chb_ksolve1",
                "chb_ksolve2",
                "chb_ksolve3",
                "chb_ksolve4",
                "chb_ksolve11",
                "chb_kprint11",
                "chb_kprint12",
            ]:
                getattr(self, chb_name).setChecked(True)

            # Habilitar widgets y establecer valor en LineEdits
            for le_name in ["le_relax1", "le_relax2", "le_relax3"]:
                getattr(self, le_name).setEnabled(True)
                getattr(self, le_name).setText("1")

            self.chb_kprint11.setEnabled(True)

        # Si el flujo es Difusivo, revierte las acciones
        elif flujo == "Difusivo":
            # Desmarcar CheckBoxes
            for chb_name in [
                "chb_kprint1",
                "chb_kprint2",
                "chb_kprint3",
                "chb_ksolve1",
                "chb_ksolve2",
                "chb_ksolve3",
                "chb_ksolve4",
                "chb_ksolve11",
                "chb_kprint11",
                "chb_kprint12",
            ]:
                getattr(self, chb_name).setChecked(False)

            # Deshabilitar LineEdits y borrar su contenido
            for le_name in ["le_relax1", "le_relax2", "le_relax3"]:
                le_widget = getattr(self, le_name)
                le_widget.setEnabled(False)
                le_widget.setText("")  # Asegúrate de borrar el texto para los QLineEdit

            # Asegúrate de que chb_kprint11 también se maneje adecuadamente
            self.chb_kprint11.setEnabled(False)

    def controlarWidgetsTitles(self):
        # Primero, maneja el caso especial para le_var_title6
        if not self.le_var_title6.text():
            self.desactivarComponentesDesde(6)

        for i in range(6, 11):  # Ahora incluye hasta le_var_title10 en el bucle
            current_le_var = getattr(self, f"le_var_title{i}")
            texto = current_le_var.text().strip()

            if texto:
                # Para todos los LineEdit con texto, habilita sus componentes asociados
                self.activarComponentesPara(i)
                # Si no es le_var_title10, habilita el siguiente LineEdit
                if i < 10:
                    getattr(self, f"le_var_title{i+1}").setEnabled(True)
            else:
                # Si se encuentra un LineEdit vacío, desactiva los componentes desde el siguiente
                self.desactivarComponentesDesde(i + 1)
                break

    def activarComponentesPara(self, indice):
        # Habilitar y chequear los componentes relacionados al índice proporcionado
        getattr(self, f"chb_ksolve{indice}").setEnabled(True)
        getattr(self, f"chb_kprint{indice}").setEnabled(True)
        getattr(self, f"le_relax{indice}").setEnabled(True)
        getattr(self, f"chb_ksolve{indice}").setChecked(True)
        getattr(self, f"chb_kprint{indice}").setChecked(True)
        getattr(self, f"le_relax{indice}").setText("1")

    def desactivarComponentesDesde(self, indice):
        # Desde el índice proporcionado, deshabilitar y limpiar los componentes asociados
        for j in range(indice, 11):
            getattr(self, f"le_var_title{j}").setEnabled(False)
            getattr(self, f"le_var_title{j}").setText("")
            getattr(self, f"chb_ksolve{j}", None).setEnabled(False)
            getattr(self, f"chb_kprint{j}", None).setEnabled(False)
            getattr(self, f"le_relax{j}", None).setEnabled(False)
            getattr(self, f"chb_ksolve{j}", None).setChecked(False)
            getattr(self, f"chb_kprint{j}", None).setChecked(False)
            getattr(self, f"le_relax{j}", None).setText("")
