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
        self.cb_tipoflujo.currentTextChanged.connect(self.changeTipoFlujo)

        self.le_var_title1.textChanged.connect(self.update_variables_title_1)
        self.le_var_title2.textChanged.connect(self.update_variables_title_2)
        self.le_var_title3.textChanged.connect(self.update_variables_title_3)
        self.le_var_title4.textChanged.connect(self.update_variables_title_4)
        self.le_var_title5.textChanged.connect(self.update_variables_title_5)
        self.le_var_title6.textChanged.connect(self.update_variables_title_6)
        self.le_var_title7.textChanged.connect(self.update_variables_title_7)
        self.le_var_title8.textChanged.connect(self.update_variables_title_8)
        self.le_var_title9.textChanged.connect(self.update_variables_title_9)
        self.le_var_title10.textChanged.connect(self.update_variables_title_10)
        self.le_var_title11.textChanged.connect(self.update_variables_title_11)
        self.le_var_title12.textChanged.connect(self.update_variables_title_12)

        self.chb_ksolve1.stateChanged.connect(self.update_variables_ksolve_1)
        self.chb_ksolve2.stateChanged.connect(self.update_variables_ksolve_2)
        self.chb_ksolve3.stateChanged.connect(self.update_variables_ksolve_3)
        self.chb_ksolve4.stateChanged.connect(self.update_variables_ksolve_4)
        self.chb_ksolve5.stateChanged.connect(self.update_variables_ksolve_5)
        self.chb_ksolve6.stateChanged.connect(self.update_variables_ksolve_6)
        self.chb_ksolve7.stateChanged.connect(self.update_variables_ksolve_7)
        self.chb_ksolve8.stateChanged.connect(self.update_variables_ksolve_8)
        self.chb_ksolve9.stateChanged.connect(self.update_variables_ksolve_9)
        self.chb_ksolve10.stateChanged.connect(self.update_variables_ksolve_10)
        self.chb_ksolve11.stateChanged.connect(self.update_variables_ksolve_11)
        self.chb_ksolve12.stateChanged.connect(self.update_variables_ksolve_12)

        self.chb_kprint1.stateChanged.connect(self.update_variables_kprint_1)
        self.chb_kprint2.stateChanged.connect(self.update_variables_kprint_2)
        self.chb_kprint3.stateChanged.connect(self.update_variables_kprint_3)
        self.chb_kprint4.stateChanged.connect(self.update_variables_kprint_4)
        self.chb_kprint5.stateChanged.connect(self.update_variables_kprint_5)
        self.chb_kprint6.stateChanged.connect(self.update_variables_kprint_6)
        self.chb_kprint7.stateChanged.connect(self.update_variables_kprint_7)
        self.chb_kprint8.stateChanged.connect(self.update_variables_kprint_8)
        self.chb_kprint9.stateChanged.connect(self.update_variables_kprint_9)
        self.chb_kprint10.stateChanged.connect(self.update_variables_kprint_10)
        self.chb_kprint11.stateChanged.connect(self.update_variables_kprint_11)
        self.chb_kprint12.stateChanged.connect(self.update_variables_kprint_12)

        self.le_relax1.textChanged.connect(self.update_variables_relax_1)
        self.le_relax2.textChanged.connect(self.update_variables_relax_2)
        self.le_relax3.textChanged.connect(self.update_variables_relax_3)
        self.le_relax4.textChanged.connect(self.update_variables_relax_4)
        self.le_relax5.textChanged.connect(self.update_variables_relax_5)
        self.le_relax6.textChanged.connect(self.update_variables_relax_6)
        self.le_relax7.textChanged.connect(self.update_variables_relax_7)
        self.le_relax8.textChanged.connect(self.update_variables_relax_8)
        self.le_relax9.textChanged.connect(self.update_variables_relax_9)
        self.le_relax10.textChanged.connect(self.update_variables_relax_10)
        self.le_relax11.textChanged.connect(self.update_variables_relax_11)
        self.le_relax12.textChanged.connect(self.update_variables_relax_12)

    def changeTipoSimu(self):
        current_text_simu = self.cb_tsimu.currentText()

        if current_text_simu == "Permanente":
            self.sw_tsimu.setCurrentIndex(0)
        elif current_text_simu == "Transitorio":
            self.sw_tsimu.setCurrentIndex(1)

    def changeTipoFlujo(self):
        current_text_flujo = self.cb_tipoflujo.currentText()

        if current_text_flujo == "Difusivo":
            return "Difusivo"
        elif current_text_flujo == "Flujo Laminar":
            return "Flujo Laminar"

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

    def update_variables_ksolve_2(self, state):
        ksolve2 = 1 if state == 2 else 0
        self.config_manager.config_structure["VARIABLES"]["KSOLVE(2)"] = ksolve2

    def update_variables_ksolve_3(self, state):
        ksolve3 = 1 if state == 3 else 0
        self.config_manager.config_structure["VARIABLES"]["KSOLVE(3)"] = ksolve3

    def update_variables_ksolve_4(self, state):
        ksolve4 = 1 if state == 4 else 0
        self.config_manager.config_structure["VARIABLES"]["KSOLVE(4)"] = ksolve4

    def update_variables_ksolve_5(self, state):
        ksolve5 = 1 if state == 5 else 0
        self.config_manager.config_structure["VARIABLES"]["KSOLVE(5)"] = ksolve5

    def update_variables_ksolve_6(self, state):
        ksolve6 = 1 if state == 6 else 0
        self.config_manager.config_structure["VARIABLES"]["KSOLVE(6)"] = ksolve6

    def update_variables_ksolve_7(self, state):
        ksolve7 = 1 if state == 7 else 0
        self.config_manager.config_structure["VARIABLES"]["KSOLVE(7)"] = ksolve7

    def update_variables_ksolve_8(self, state):
        ksolve8 = 1 if state == 8 else 0
        self.config_manager.config_structure["VARIABLES"]["KSOLVE(8)"] = ksolve8

    def update_variables_ksolve_9(self, state):
        ksolve9 = 1 if state == 9 else 0
        self.config_manager.config_structure["VARIABLES"]["KSOLVE(9)"] = ksolve9

    def update_variables_ksolve_10(self, state):
        ksolve10 = 1 if state == 10 else 0
        self.config_manager.config_structure["VARIABLES"]["KSOLVE(10)"] = ksolve10

    def update_variables_ksolve_11(self, state):
        ksolve11 = 1 if state == 11 else 0
        self.config_manager.config_structure["VARIABLES"]["KSOLVE(11)"] = ksolve11

    def update_variables_ksolve_12(self, state):
        ksolve12 = 1 if state == 12 else 0
        self.config_manager.config_structure["VARIABLES"]["KSOLVE(12)"] = ksolve12

    def update_variables_kprint_1(self, state):
        kprint1 = 1 if state == 1 else 0
        self.config_manager.config_structure["VARIABLES"]["KPRINT(1)"] = kprint1

    def update_variables_kprint_2(self, state):
        kprint2 = 1 if state == 2 else 0
        self.config_manager.config_structure["VARIABLES"]["KPRINT(2)"] = kprint2

    def update_variables_kprint_3(self, state):
        kprint3 = 1 if state == 3 else 0
        self.config_manager.config_structure["VARIABLES"]["KPRINT(3)"] = kprint3

    def update_variables_kprint_4(self, state):
        kprint4 = 1 if state == 4 else 0
        self.config_manager.config_structure["VARIABLES"]["KPRINT(4)"] = kprint4

    def update_variables_kprint_5(self, state):
        kprint5 = 1 if state == 5 else 0
        self.config_manager.config_structure["VARIABLES"]["KPRINT(5)"] = kprint5

    def update_variables_kprint_6(self, state):
        kprint6 = 1 if state == 6 else 0
        self.config_manager.config_structure["VARIABLES"]["KPRINT(6)"] = kprint6

    def update_variables_kprint_7(self, state):
        kprint7 = 1 if state == 7 else 0
        self.config_manager.config_structure["VARIABLES"]["KPRINT(7)"] = kprint7

    def update_variables_kprint_8(self, state):
        kprint8 = 1 if state == 8 else 0
        self.config_manager.config_structure["VARIABLES"]["KPRINT(8)"] = kprint8

    def update_variables_kprint_9(self, state):
        kprint9 = 1 if state == 9 else 0
        self.config_manager.config_structure["VARIABLES"]["KPRINT(9)"] = kprint9

    def update_variables_kprint_10(self, state):
        kprint10 = 1 if state == 10 else 0
        self.config_manager.config_structure["VARIABLES"]["KPRINT(10)"] = kprint10

    def update_variables_kprint_11(self, state):
        kprint11 = 1 if state == 11 else 0
        self.config_manager.config_structure["VARIABLES"]["KPRINT(11)"] = kprint11

    def update_variables_kprint_12(self, state):
        kprint12 = 1 if state == 12 else 0
        self.config_manager.config_structure["VARIABLES"]["KPRINT(12)"] = kprint12

    # - Pendiente agregar el resto de ksolve y kprint

    def update_variables_relax_1(self, text):
        self.config_manager.config_structure["VARIABLES"]["RELAX(1)"] = text

    def update_variables_relax_2(self, text):
        self.config_manager.config_structure["VARIABLES"]["RELAX(2)"] = text

    def update_variables_relax_3(self, text):
        self.config_manager.config_structure["VARIABLES"]["RELAX(3)"] = text

    def update_variables_relax_4(self, text):
        self.config_manager.config_structure["VARIABLES"]["RELAX(4)"] = text

    def update_variables_relax_5(self, text):
        self.config_manager.config_structure["VARIABLES"]["RELAX(5)"] = text

    def update_variables_relax_6(self, text):
        self.config_manager.config_structure["VARIABLES"]["RELAX(6)"] = text

    def update_variables_relax_7(self, text):
        self.config_manager.config_structure["VARIABLES"]["RELAX(7)"] = text

    def update_variables_relax_8(self, text):
        self.config_manager.config_structure["VARIABLES"]["RELAX(8)"] = text

    def update_variables_relax_9(self, text):
        self.config_manager.config_structure["VARIABLES"]["RELAX(9)"] = text

    def update_variables_relax_10(self, text):
        self.config_manager.config_structure["VARIABLES"]["RELAX(10)"] = text

    def update_variables_relax_11(self, text):
        self.config_manager.config_structure["VARIABLES"]["RELAX(11)"] = text

    def update_variables_relax_12(self, text):
        self.config_manager.config_structure["VARIABLES"]["RELAX(12)"] = text


if __name__ == "__main__":
    app = qtw.QApplication(sys.argv)
    config_manager = ConfigManager()
    form = VariablesWindow(config_manager)
    form.open()
    sys.exit(app.exec())
