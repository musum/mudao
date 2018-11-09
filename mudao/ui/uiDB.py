from PyQt5.QtWidgets import QWidget, QTreeWidgetItem
from PyQt5.QtCore import pyqtSignal as Signal

from mudao.ui.pannel.dbm import Ui_Form
from mudao.ui.uiDBConf import DBConfig


class DBManagerPannel(QWidget, Ui_Form):
    sig_db_conf_submit = Signal(dict)

    def __init__(self, shell, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.btn_config.clicked.connect(self.on_config_clicked)
        self.btn_execute.clicked.connect(self.on_execute_clicked)

        self.leftView.itemDoubleClicked.connect(self.on_left_doubleclicked)

        self.dbm = shell
        self.encoding = shell.encoding
        self.conf = shell.sqlconf or ''

    def on_config_clicked(self):
        dlg = DBConfig(self.conf, self)
        dlg.sig_conf_submit.connect(self.db_config_edit)
        dlg.show()

    def on_execute_clicked(self):
        sql = self.cbo_sql.currentText()
        self.execute(self.conf, 'executesql', sql)

    def execute(self, conn, action, sql=None):
        return self.dbm.get_data(conn, action, sql)

    def db_config_edit(self, conf):
        print(conf)
        self.conf = conf
        print(self.execute(self.conf, 'DBLIST'))
        self.sig_db_conf_submit.emit(dict(sqlconf=self.conf))

    def on_left_doubleclicked(self, it, idx):
        pass
