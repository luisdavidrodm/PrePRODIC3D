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

    def update_variables_iptm(self, text):
        self.config_manager.set_variables_iptm(text)

    def update_variables_dt(self, text):
        self.config_manager.set_variables_dt(text)

    def update_variables_kord(self, selection):
        kord = 1 if selection == "Esquema de bajo orden" else 2
        self.config_manager.set_variables_kord(kord)

    def update_variables_title_1(self, text):
        self.config_manager.set_variables_title_1(text)

    def update_variables_title_2(self, text):
        self.config_manager.set_variables_title_2(text)

    def update_variables_title_3(self, text):
        self.config_manager.set_variables_title_3(text)

    def update_variables_title_4(self, text):
        self.config_manager.set_variables_title_4(text)

    def update_variables_title_5(self, text):
        self.config_manager.set_variables_title_5(text)

    def update_variables_title_6(self, text):
        self.config_manager.set_variables_title_6(text)

    def update_variables_title_7(self, text):
        self.config_manager.set_variables_title_7(text)

    def update_variables_title_8(self, text):
        self.config_manager.set_variables_title_8(text)

    def update_variables_title_9(self, text):
        self.config_manager.set_variables_title_9(text)

    def update_variables_title_10(self, text):
        self.config_manager.set_variables_title_10(text)

    def update_variables_title_11(self, text):
        self.config_manager.set_variables_title_11(text)

    def update_variables_title_12(self, text):
        self.config_manager.set_variables_title_12(text)

    ####DUDA

    def update_variables_ksolve_1(self, state):
        if state == qtc.Qt.CheckState.Checked:
            ksolve1 = 0
        else:
            ksolve1 = 1
        self.config_manager.set_variables_ksolve_1(ksolve1)

    # - Pendiente agregar el resto de ksolve y kprint

    def update_variables_relax_1(self, text):
        self.config_manager.set_variables_relax_1(text)

    def update_variables_relax_2(self, text):
        self.config_manager.set_variables_relax_2(text)

    def update_variables_relax_3(self, text):
        self.config_manager.set_variables_relax_3(text)

    def update_variables_relax_4(self, text):
        self.config_manager.set_variables_relax_4(text)

    def update_variables_relax_5(self, text):
        self.config_manager.set_variables_relax_5(text)

    def update_variables_relax_6(self, text):
        self.config_manager.set_variables_relax_6(text)

    def update_variables_relax_7(self, text):
        self.config_manager.set_variables_relax_7(text)

    def update_variables_relax_8(self, text):
        self.config_manager.set_variables_relax_8(text)

    def update_variables_relax_9(self, text):
        self.config_manager.set_variables_relax_9(text)

    def update_variables_relax_10(self, text):
        self.config_manager.set_variables_relax_10(text)

    def update_variables_relax_11(self, text):
        self.config_manager.set_variables_relax_11(text)

    def update_variables_relax_12(self, text):
        self.config_manager.set_variables_relax_12(text)


if __name__ == "__main__":
    app = qtw.QApplication(sys.argv)
    config_manager = ConfigManager()
    form = VariablesWindow(config_manager)
    form.open()
    sys.exit(app.exec())
