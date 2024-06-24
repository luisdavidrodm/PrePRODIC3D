from PySide6 import QtWidgets as qtw

from variables_window.ui.variables_window_ui import Ui_variables_window


class VariablesWindow(qtw.QDialog, Ui_variables_window):

    def __init__(self, config_manager):
        super().__init__()
        self.setupUi(self)
        self.config_manager = config_manager
        self.config_name = "VARIABLES"

        self.widgets = ["cb_tsimu", "cb_tipoflujo", "cb_trataborde", "le_iptm", "le_dt", "le_tol", "checkBox"]
        for i in range(1, 13):
            self.widgets.extend([f"le_var_title{i}", f"chb_kprint{i}"])
        for i in range(1, 12):
            self.widgets.extend([f"le_relax{i}", f"chb_ksolve{i}"])

        self.cb_tsimu.currentTextChanged.connect(self.simulation_type_change)
        self.cb_tipoflujo.currentTextChanged.connect(self.flow_type_change)
        for widget_name in [f"le_var_title{i}" for i in range(1, 12)]:
            getattr(self, widget_name).textChanged.connect(self.le_var_title_changed)

        self.config_manager.connect_config(self)
        self.config_manager.load_config(self)
        for index in range(5, 11):
            if getattr(self, f"le_var_title{index}").text().strip():
                getattr(self, f"le_var_title{index}").setEnabled(True)
                getattr(self, f"chb_ksolve{index}").setEnabled(True)
                getattr(self, f"chb_kprint{index}").setEnabled(True)
                getattr(self, f"le_relax{index}").setEnabled(True)
                if index != 10:
                    getattr(self, f"le_var_title{index + 1}").setEnabled(True)

    def value_changed(self, value):
        sender = self.sender()
        if value is None or value == "":
            self.config_manager.variables.pop(sender.objectName(), None)
        else:
            self.config_manager.variables[sender.objectName()] = value

    def simulation_type_change(self):
        current_text_simu = self.cb_tsimu.currentText()
        if current_text_simu == "Permanente":
            self.sw_tsimu.setCurrentIndex(0)
        elif current_text_simu == "Transitorio":
            self.sw_tsimu.setCurrentIndex(1)

    def flow_type_change(self, text):
        if text == "Flujo Laminar":
            # fmt: off
            for chb_name in [
                "chb_kprint1", "chb_kprint2", "chb_kprint3", "chb_kprint11", "chb_kprint12",
                "chb_ksolve1", "chb_ksolve2", "chb_ksolve3", "chb_ksolve4", "chb_ksolve11",
            ]:  # fmt: on
                getattr(self, chb_name).setChecked(True)
            for le_name in ["le_relax1", "le_relax2", "le_relax3"]:
                getattr(self, le_name).setEnabled(True)
            self.chb_kprint11.setEnabled(True)
        else:  # if text == "Difusivo":
            # fmt: off
            for chb_name in [
                "chb_kprint1", "chb_kprint2", "chb_kprint3", "chb_ksolve1", "chb_ksolve2", 
                "chb_ksolve3", "chb_ksolve4", "chb_ksolve11", "chb_kprint11", "chb_kprint12",
            ]:  # fmt: on
                getattr(self, chb_name).setChecked(False)
            for le_name in ["le_relax1", "le_relax2", "le_relax3"]:
                le_widget = getattr(self, le_name)
                le_widget.setEnabled(False)
                le_widget.setText("")
            self.chb_kprint11.setEnabled(False)

    def le_var_title_changed(self, _):
        """Actualiza el config_structure en el ConfigManager basado en el texto del LineEdit."""
        sender = self.sender()
        le_name = sender.objectName()
        index = int(sender.objectName()[sender.objectName().rfind("e") + 1 :])
        if sender.text().strip():
            if not le_name in self.config_manager.variables:
                getattr(self, f"chb_ksolve{index}").setEnabled(True)
                getattr(self, f"chb_ksolve{index}").setChecked(True)
                getattr(self, f"chb_kprint{index}").setEnabled(True)
                getattr(self, f"chb_kprint{index}").setChecked(True)
                getattr(self, f"le_relax{index}").setEnabled(True)
                if le_name != "le_var_title10":
                    getattr(self, f"le_var_title{index + 1}").setEnabled(True)
            # Modificaciones en otras ventanas
            if le_name in self.config_manager.values:
                self.config_manager.values[le_name]["name"] = sender.text()
            else:
                self.config_manager.values[le_name] = {
                    "name": sender.text(),
                    "Región 1": {"Volumen 1": {}},
                }
            if le_name in self.config_manager.output:
                self.config_manager.output[le_name]["name"] = sender.text()
            else:
                self.config_manager.output[le_name] = {"name": sender.text()}
        else:
            for i in range(index, 11):
                if i != index:
                    getattr(self, f"le_var_title{i}").setEnabled(False)
                    getattr(self, f"le_var_title{i}").setText("")
                getattr(self, f"chb_ksolve{i}").setEnabled(False)
                getattr(self, f"chb_ksolve{i}").setChecked(False)
                getattr(self, f"chb_kprint{i}").setEnabled(False)
                getattr(self, f"chb_kprint{i}").setChecked(False)
                getattr(self, f"le_relax{i}").setEnabled(False)
                getattr(self, f"le_relax{i}").setText("")
            # Modificaciones en otras ventanas
            if le_name in self.config_manager.values:
                del self.config_manager.values[le_name]
            if le_name in self.config_manager.output:
                del self.config_manager.output[le_name]
