from PyQt5.QtWidgets import QDialog
from PyQt5.QtCore import pyqtSignal as Signal
from mudao.ui.pannel.dbconfig import Ui_Dialog


class DBConfig(QDialog, Ui_Dialog):
    sig_conf_submit = Signal(str)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.btn_submit.clicked.connect(self.on_submit_clicked)
        self.cbo_example.currentIndexChanged.connect(self.on_example_changed)
        self.edt_conf.setText('')

    def on_submit_clicked(self):
        if self.edt_conf:
            self.sig_dbconf_submit.emit(self.edt_conf.text())
            self.hide()

    def on_example_changed(self):
        self.edt_conf.setText(self.cbo_example.currentText())
