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

        self.connect_signals()
        self.load_variable_config()

        # Conexion de Variables con ventana Bordes
        self.le_var_title5.textChanged.connect(self.enviar_datos_variables)
        self.le_var_title6.textChanged.connect(self.enviar_datos_variables)
        self.le_var_title7.textChanged.connect(self.enviar_datos_variables)
        self.le_var_title8.textChanged.connect(self.enviar_datos_variables)
        self.le_var_title9.textChanged.connect(self.enviar_datos_variables)
        self.le_var_title10.textChanged.connect(self.enviar_datos_variables)
        self.le_var_title11.textChanged.connect(self.enviar_datos_variables)
        self.le_var_title12.textChanged.connect(self.enviar_datos_variables)

        # Nombre de Variable Temperatura enviado a Bordes
        self.le_var_title5.setText("Temperatura")

        for i in range(6, 11):  # Para le_var_title6 hasta le_var_title10
            getattr(self, f"le_var_title{i}").textChanged.connect(self.controlar_widgets_titles)
        # fmt: off
        self.widgets = [
            "le_xlon", "le_nvcx", "le_potenciax", "le_ylon", "le_nvcy",
            "le_potenciay", "le_zlon", "le_nvcz", "le_potenciaz", "le_titalon",
            "le_nvctita", "le_potenciatita", "le_rini", "le_rlon", "le_nvcr",
            "le_potenciar", "le_zloncil", "le_nvczcil", "le_potenciazcil",
            "sb_dirx_numz", "sb_diry_numz", "sb_dirz_numz", "sb_dirtita_numz",
            "sb_dirr_numz", "le_dirr_inidom", "sb_dirzcil_numz",
        ]

        self.widgets_to_extend = [
            "le_dirx_lon_zon{0}", "le_dirx_nvcx_zon{0}", "le_dirx_poten_zon{0}",
            "le_diry_lon_zon{0}", "le_diry_nvcy_zon{0}", "le_diry_poten_zon{0}",
            "le_dirz_lon_zon{0}", "le_dirz_nvcz_zon{0}", "le_dirz_poten_zon{0}",
            "le_dirr_lon_zon{0}", "le_dirr_nvcr_zon{0}", "le_dirr_poten_zon{0}",
            "le_dirtita_lon_zon{0}", "le_dirtita_nvctita_zon{0}", "le_dirtita_poten_zon{0}",
            "le_dirzcil_lon_zon{0}", "le_dirzcil_nvczcil_zon{0}", "le_dirzcil_poten_zon{0}"
        ]
        # fmt: on
        for widget_name in self.widgets:
            widget = getattr(self, widget_name)
            if isinstance(widget, QComboBox):
                signal = widget.currentTextChanged
            elif isinstance(widget, QSpinBox):
                signal = widget.valueChanged
            elif isinstance(widget, QLineEdit):
                signal = widget.textChanged
            else:
                continue
            signal.connect(self.value_changed)

    def connect_signals(self):
        self.cb_tsimu.currentTextChanged.connect(self.change_tipo_simu)
        self.cb_tipoflujo.currentTextChanged.connect(self.handle_tipo_flujo_cambio)
        self.cb_trataborde.currentTextChanged.connect(self.update_variables_kord)
        self.cb_tipoflujo.currentIndexChanged.connect(self.handle_flujo_change)

        self.cb_tsimu.currentTextChanged.connect(lambda value: self.update_config("TSIMU", value))
        self.cb_tipoflujo.currentTextChanged.connect(lambda value: self.update_config("TIPOFLUJO", value))
        self.cb_trataborde.currentTextChanged.connect(lambda value: self.update_config("TRATABORDE", value))

        self.le_iptm.textChanged.connect(lambda text: self.update_config("IPTM", text))
        self.le_dt.textChanged.connect(lambda text: self.update_config("DT", text))

        # Conexiones para le_var_titleX y otros QLineEdits específicos
        for i in range(1, 13):
            if hasattr(self, f"le_var_title{i}"):
                getattr(self, f"le_var_title{i}").textChanged.connect(
                    lambda text, i=i: self.value_changed(text, f"TITLE({i})")
                )
            if hasattr(self, f"le_relax{i}"):
                getattr(self, f"le_relax{i}").textChanged.connect(
                    lambda text, i=i: self.value_changed(text, f"RELAX({i})")
                )

        # Conectar cambios de estado en CheckBoxes a value_changed
        for i in range(1, 13):
            if hasattr(self, f"chb_ksolve{i}"):
                getattr(self, f"chb_ksolve{i}").stateChanged.connect(
                    lambda state, i=i: self.value_changed(1 if state > 0 else 0, f"KSOLVE({i})")
                )
            if hasattr(self, f"chb_kprint{i}"):
                getattr(self, f"chb_kprint{i}").stateChanged.connect(
                    lambda state, i=i: self.value_changed(1 if state > 0 else 0, f"KPRINT({i})")
                )

    def change_tipo_simu(self):
        current_text_simu = self.cb_tsimu.currentText()

        if current_text_simu == "Permanente":
            self.sw_tsimu.setCurrentIndex(0)
        elif current_text_simu == "Transitorio":
            self.sw_tsimu.setCurrentIndex(1)

    def update_variables_kord(self, selection):
        kord = 1 if selection == "Esquema de bajo orden" else 2
        self.config_manager.config_structure["VARIABLES"]["KORD"] = kord

    def update_config(self, config_key, value):
        # Actualiza el valor de la configuración en el ConfigManager
        self.config_manager.config_structure["VARIABLES"][config_key] = value

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

    def controlar_widgets_titles(self):
        # Comprueba todos los LineEdits a partir del 5 hasta el 10 (incluyendo el 10)
        ultimoConTexto = 5  # Asume que al menos el primer LineEdit debe tener texto (Temperatura)
        for i in range(5, 11):  # Cambio aquí para limitar hasta el 10
            le_var = getattr(self, f"le_var_title{i}", None)
            if le_var and le_var.text().strip():
                # Habilita y configura los componentes para este LineEdit
                self.activar_componentes_para(i)
                ultimoConTexto = i
            else:
                # Encuentra el primer LineEdit vacío y detiene el bucle
                break

        # Desactiva los componentes desde el siguiente al último con texto, si es necesario
        if ultimoConTexto < 10:  # Si no todos tienen texto y se ajusta el límite a 10
            self.desactivar_componentes_desde(ultimoConTexto + 1)

        # Asegura que el siguiente al último con texto esté habilitado para continuar la entrada
        if ultimoConTexto < 10:  # Si no estamos en el último (10), ajuste aquí
            siguienteLE = getattr(self, f"le_var_title{ultimoConTexto + 1}", None)
            if siguienteLE:
                siguienteLE.setEnabled(True)

    def activar_componentes_para(self, indice):
        # Solo activa componentes si el índice está entre 5 y 10
        if 5 <= indice <= 10:
            if hasattr(self, f"chb_ksolve{indice}"):
                getattr(self, f"chb_ksolve{indice}").setEnabled(True)
                getattr(self, f"chb_ksolve{indice}").setChecked(True)
            if hasattr(self, f"chb_kprint{indice}"):
                getattr(self, f"chb_kprint{indice}").setEnabled(True)
                getattr(self, f"chb_kprint{indice}").setChecked(True)
            if hasattr(self, f"le_relax{indice}"):
                getattr(self, f"le_relax{indice}").setEnabled(True)
                getattr(self, f"le_relax{indice}").setText("1")

    def desactivar_componentes_desde(self, indice):
        # Asegúrate de que la desactivación se limite desde el 6 al 11
        for j in range(indice, 11):  # Desactiva solo hasta el 10, incluyendo desde el que se indica
            if 5 <= j <= 10:  # Asegúrate de operar solo en el rango deseado
                le_var_title = getattr(self, f"le_var_title{j}", None)
                if le_var_title:
                    le_var_title.setEnabled(False)
                    le_var_title.setText("")
                chb_ksolve = getattr(self, f"chb_ksolve{j}", None)
                if chb_ksolve:
                    chb_ksolve.setEnabled(False)
                    chb_ksolve.setChecked(False)
                chb_kprint = getattr(self, f"chb_kprint{j}", None)
                if chb_kprint:
                    chb_kprint.setEnabled(False)
                    chb_kprint.setChecked(False)
                le_relax = getattr(self, f"le_relax{j}", None)
                if le_relax:
                    le_relax.setEnabled(False)
                    le_relax.setText("")

    def value_changed(self, value, config_key):
        # Actualizar la configuración con el nuevo valor
        self.config_manager.config_structure["VARIABLES"][config_key] = value

    def load_variable_config(self):
        config = self.config_manager.config_structure["VARIABLES"]

        self.le_iptm.setText(config.get("IPTM", ""))
        self.le_dt.setText(config.get("DT", ""))

        for i in range(1, 13):
            if hasattr(self, f"le_var_title{i}"):
                getattr(self, f"le_var_title{i}").setText(config.get(f"TITLE({i})", ""))

            if hasattr(self, f"chb_ksolve{i}"):
                state = config.get(f"KSOLVE({i})", 0)
                getattr(self, f"chb_ksolve{i}").setChecked(state == 1)

            if hasattr(self, f"chb_kprint{i}"):
                state = config.get(f"KPRINT({i})", 0)
                getattr(self, f"chb_kprint{i}").setChecked(state == 1)

            if hasattr(self, f"le_relax{i}"):
                getattr(self, f"le_relax{i}").setText(config.get(f"RELAX({i})", ""))

            self.controlar_widgets_titles()  # Llama a esta función al final para ajustar los controles

            # Cargar configuración para QComboBox
            tsimu = config.get("TSIMU", "Permanente")  # Asume un valor predeterminado si no está definido
            self.cb_tsimu.setCurrentText(tsimu)

            tipoflujo = config.get("TIPOFLUJO", "Difusivo")  # Asume un valor predeterminado
            self.cb_tipoflujo.setCurrentText(tipoflujo)

            trataborde = config.get("TRATABORDE", "Esquema de bajo orden")  # Asume un valor predeterminado
            self.cb_trataborde.setCurrentText(trataborde)

        # Añade aquí la lógica para cargar otros valores específicos que manejes en tu ventana de variables
