import sys
from PySide6 import QtCore as qtc
from PySide6 import QtWidgets as qtw
from PySide6 import QtGui as qtg


from variables_window.ui.variables_window_ui import Ui_variables_window
from config_manager import ConfigManager


class VariablesWindow(qtw.QDialog, Ui_variables_window):
    def __init__(self, config_manager):
        super().__init__()
        self.setupUi(self)
        self.config_manager = config_manager

        self.cb_tsimu.currentTextChanged.connect(self.changeTipoSimu)
        self.le_iptm.textChanged.connect(self.update_variables_iptm)
        self.le_dt.textChanged.connect(self.update_variables_dt)
        self.cb_trataborde.currentTextChanged.connect(self.update_variables_kord)

        self.le_dt.textChanged.connect(self.update_variables_title_1)
        self.le_dt.textChanged.connect(self.update_variables_title_2)
        self.le_dt.textChanged.connect(self.update_variables_title_3)
        self.le_dt.textChanged.connect(self.update_variables_title_4)
        self.le_dt.textChanged.connect(self.update_variables_title_5)
        self.le_dt.textChanged.connect(self.update_variables_title_6)
        self.le_dt.textChanged.connect(self.update_variables_title_7)
        self.le_dt.textChanged.connect(self.update_variables_title_8)
        self.le_dt.textChanged.connect(self.update_variables_title_9)
        self.le_dt.textChanged.connect(self.update_variables_title_10)
        self.le_dt.textChanged.connect(self.update_variables_title_11)
        self.le_dt.textChanged.connect(self.update_variables_title_12)

        self.chb_ksolve1.stateChanged.connect(self.update_variables_ksolve_1)

    def changeTipoSimu(self):
        current_text_simu = self.cb_tsimu.currentText()

        if current_text_simu == "Permanente":
            self.sw_tsimu.setCurrentIndex(0)
        elif current_text_simu == "Transitorio":
            self.sw_tsimu.setCurrentIndex(1)

    def update_variables_iptm(self, text):
        self.config_manager.config_structure["VARIABLES"]["IPTM"] = text

    def update_variables_dt(self, text):
        self.config_manager.config_structure["VARIABLES"]["DT"] = text

    def update_variables_kord(self, selection):
        kord = 1 if selection == "Esquema de bajo orden" else 2
        self.config_manager.config_structure["VARIABLES"]["KORD"] = kord

    def update_variables_title_1(self, text):
        self.config_manager.config_structure["VARIABLES"]["TITLE(1)"] = text

    def update_variables_title_2(self, text):
        self.config_manager.config_structure["VARIABLES"]["TITLE(2)"] = text

    def update_variables_title_3(self, text):
        self.config_manager.config_structure["VARIABLES"]["TITLE(3)"] = text

    def update_variables_title_4(self, text):
        self.config_manager.config_structure["VARIABLES"]["TITLE(4)"] = text

    def update_variables_title_5(self, text):
        self.config_manager.config_structure["VARIABLES"]["TITLE(5)"] = text

    def update_variables_title_6(self, text):
        self.config_manager.config_structure["VARIABLES"]["TITLE(6)"] = text

    def update_variables_title_7(self, text):
        self.config_manager.config_structure["VARIABLES"]["TITLE(7)"] = text

    def update_variables_title_8(self, text):
        self.config_manager.config_structure["VARIABLES"]["TITLE(8)"] = text

    def update_variables_title_9(self, text):
        self.config_manager.config_structure["VARIABLES"]["TITLE(9)"] = text

    def update_variables_title_10(self, text):
        self.config_manager.config_structure["VARIABLES"]["TITLE(10)"] = text

    def update_variables_title_11(self, text):
        self.config_manager.config_structure["VARIABLES"]["TITLE(11)"] = text

    def update_variables_title_12(self, text):
        self.config_manager.config_structure["VARIABLES"]["TITLE(12)"] = text

    def update_variables_ksolve_1(self, state):
        ksolve1 = 1 if state == 2 else 0
        self.config_manager.config_structure["VARIABLES"]["KSOLVE(1)"] = ksolve1


if __name__ == "__main__":
    app = qtw.QApplication(sys.argv)
    config_manager = ConfigManager()
    form = VariablesWindow(config_manager)
    form.open()
    sys.exit(app.exec())
