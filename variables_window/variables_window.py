from PySide6 import QtWidgets as qtw
from PySide6.QtCore import Signal

from variables_window.ui.variables_window_ui import Ui_variables_window


class VariablesWindow(qtw.QDialog, Ui_variables_window):

    flow_type_change_signal = Signal(bool)
    variables_signal = Signal(list)

    def __init__(self, config_manager):
        # fmt: off
        super().__init__()
        self.setupUi(self)
        self.config_manager = config_manager
        self.config_name = "VARIABLES"

        self.cb_tsimu.currentTextChanged.connect(self.change_simulation_type)
        self.cb_tipoflujo.currentTextChanged.connect(self.handle_flow_type_change)

        for i in range(5, 13):
            getattr(self, f"le_var_title{i}").textChanged.connect(self.send_variables_data)

        for i in range(6, 11):
            getattr(self, f"le_var_title{i}").textChanged.connect(self.control_widgets_titles)

        # Conexion con ConfigManager
        self.widgets = [
            "cb_tsimu", "cb_tipoflujo", "cb_trataborde", "le_iptm", "le_dt", "le_tol", "checkBox"
            ]

        for i in range(1, 13):
            self.widgets.extend([f"le_var_title{i}", f"chb_kprint{i}"])

        for i in range(1, 12):
            self.widgets.extend([f"le_relax{i}", f"chb_ksolve{i}"])

        self.config_manager.connect_config(self)

        self.chb_ksolve_widgets = [
            "chb_ksolve1", "chb_ksolve2", "chb_ksolve3", "chb_ksolve4", "chb_ksolve5", 
            "chb_ksolve6", "chb_ksolve7", "chb_ksolve8", "chb_ksolve9", "chb_ksolve10", "chb_ksolve11"
        ]
        # for widget_name in self.chb_ksolve_widgets:
        #     getattr(self, widget_name).stateChanged.connect(self.chb_ksolve_changed)

        self.le_var_title_widgets = [
            "le_var_title1", "le_var_title2", "le_var_title3", "le_var_title4", "le_var_title5", "le_var_title6", 
            "le_var_title7", "le_var_title8", "le_var_title9", "le_var_title10", "le_var_title11"
        ]
        for widget_name in self.le_var_title_widgets:
            getattr(self, widget_name).textChanged.connect(self.le_var_title_changed)

        # Cargar configuración inicial
        self.load_variable_config()
        # fmt: on

    def change_simulation_type(self):
        current_text_simu = self.cb_tsimu.currentText()
        if current_text_simu == "Permanente":
            self.sw_tsimu.setCurrentIndex(0)
        elif current_text_simu == "Transitorio":
            self.sw_tsimu.setCurrentIndex(1)

    def send_variables_data(self):
        # fmt: off
        datos_variables = [
            self.le_var_title5.text(), self.le_var_title6.text(), self.le_var_title7.text(), self.le_var_title8.text(),
            self.le_var_title9.text(), self.le_var_title10.text(), self.le_var_title11.text(), self.le_var_title12.text(),
        ]  # fmt: on
        self.variables_signal.emit(datos_variables)

    def handle_flow_type_change(self, text):
        # Emitir 'True' si es "Difusivo", de lo contrario 'False'
        print(f"Cambiando tipo de flujo a: {text}")  # Impresión de depuración
        self.flow_type_change_signal.emit(text == "Difusivo")
        # Si el flujo es Flujo Laminar, chequea los CheckBox y habilita/habilita y establece los QLineEdit
        if text == "Flujo Laminar":
            # Chequear CheckBoxes
            # fmt: off
            for chb_name in [
                "chb_kprint1", "chb_kprint2", "chb_kprint3", "chb_ksolve1", "chb_ksolve2", 
                "chb_ksolve3", "chb_ksolve4", "chb_ksolve11", "chb_kprint11", "chb_kprint12",
            ]:  # fmt: on
                getattr(self, chb_name).setChecked(True)
            # Habilitar widgets y establecer valor en LineEdits
            for le_name in ["le_relax1", "le_relax2", "le_relax3"]:
                getattr(self, le_name).setEnabled(True)
                # getattr(self, le_name).setText("1")
            self.chb_kprint11.setEnabled(True)
        # Si el flujo es Difusivo, revierte las acciones
        elif text == "Difusivo":
            # Desmarcar CheckBoxes
            # fmt: off
            for chb_name in [
                "chb_kprint1", "chb_kprint2", "chb_kprint3", "chb_ksolve1", "chb_ksolve2", 
                "chb_ksolve3", "chb_ksolve4", "chb_ksolve11", "chb_kprint11", "chb_kprint12",
            ]:  # fmt: on
                getattr(self, chb_name).setChecked(False)
            # Deshabilitar LineEdits y borrar su contenido
            for le_name in ["le_relax1", "le_relax2", "le_relax3"]:
                le_widget = getattr(self, le_name)
                le_widget.setEnabled(False)
                # le_widget.setText("")
            self.chb_kprint11.setEnabled(False)

    def control_widgets_titles(self):
        # Comprueba todos los LineEdits a partir del 5 hasta el 10 (incluyendo el 10)
        ultimoConTexto = 5  # Asume que al menos el primer LineEdit debe tener texto (Temperatura)
        for i in range(5, 11):  # Cambio aquí para limitar hasta el 10
            le_var = getattr(self, f"le_var_title{i}", None)
            if le_var and le_var.text().strip():
                # Habilita y configura los componentes para este LineEdit
                self.activate_components_for(i)
                ultimoConTexto = i
            else:
                # Encuentra el primer LineEdit vacío y detiene el bucle
                break
        # Desactiva los componentes desde el siguiente al último con texto, si es necesario
        if ultimoConTexto < 10:  # Si no todos tienen texto y se ajusta el límite a 10
            self.deactivate_components_from(ultimoConTexto + 1)
        # Asegura que el siguiente al último con texto esté habilitado para continuar la entrada
        if ultimoConTexto < 10:  # Si no estamos en el último (10), ajuste aquí
            siguienteLE = getattr(self, f"le_var_title{ultimoConTexto + 1}", None)
            if siguienteLE:
                siguienteLE.setEnabled(True)

    def activate_components_for(self, indice):
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

    def deactivate_components_from(self, indice):
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

    def value_changed(self, value):
        sender = self.sender()
        if value is None or value == "":
            self.config_manager.variables.pop(sender.objectName(), None)
        else:
            self.config_manager.variables[sender.objectName()] = value

    # def chb_ksolve_changed(self, state):
    #     """Actualiza el config_structure en el ConfigManager basado en el estado del CheckBox."""
    #     sender = self.sender()
    #     number = sender.objectName()[
    #         sender.objectName().rfind("e") + 1 :
    #     ]  # Esto obtiene todo después de la última 'e' en "ksolve"
    #     le_name = f"le_var_title{number}"
    #     if state == 2:
    #         widget = getattr(self, le_name)
    #         self.config_manager.values[le_name] = {
    #             "name": widget.text(),
    #             "Region 1": {"Volumen 1": {}},
    #         }
    #         self.config_manager.output[le_name] = {"name": widget.text()}
    #     else:
    #         # Si está desactivado, elimina de VALUES si existe
    #         if le_name in self.config_manager.values:
    #             del self.config_manager.values[le_name]
    #             del self.config_manager.output[le_name]

    def le_var_title_changed(self, _):
        """Actualiza el config_structure en el ConfigManager basado en el texto del LineEdit."""
        sender = self.sender()
        le_name = sender.objectName()
        if sender.text().strip():
            if le_name in self.config_manager.values:
                self.config_manager.values[le_name]["name"] = sender.text()
            else:
                self.config_manager.values[le_name] = {
                    "name": sender.text(),
                    "Region 1": {"Volumen 1": {}},
                }
            if le_name in self.config_manager.output:
                self.config_manager.output[le_name]["name"] = sender.text()
            else:
                self.config_manager.output[le_name] = {"name": sender.text()}
        else:
            if le_name in self.config_manager.values:
                del self.config_manager.values[le_name]
            if le_name in self.config_manager.output:
                del self.config_manager.output[le_name]

    def load_variable_config(self):
        self.config_manager.load_config(self)
        self.control_widgets_titles()  # Llama a esta función al final para ajustar los controles
