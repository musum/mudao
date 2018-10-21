from PyQt5.QtWidgets import QWidget, QTreeWidgetItem

from mudao.ui.pannel.dbm import Ui_Form
from mudao.ui.uiDBConf import DBConfig

from mudao.model import DBManager


class DBManagerPannel(QWidget, Ui_Form):

    def __init__(self, shell, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.btn_config.clicked.connect(self.on_config_clicked)
        self.btn_execute.clicked.connect(self.on_execute_clicked)

        self.leftView.itemDoubleClicked.connect(self.on_left_doubleclicked)

        self.dbm = shell
        self.encoding = shell.encoding

        self.sql_conf = ''
        self.sql_example = []

    def on_config_clicked(self):
        dlg = DBConfig(self)
        dlg.sig_conf_submit.connect(self.db_config_edit)
        dlg.show()

    def on_execute_clicked(self):
        sql = self.cbo_sql.currentText()
        self.execute('executesql', sql)

    def do_action(self, action, sql):
        return self.dbm.get_data(action, sql)

    def db_config_edit(self, conf):
        self.sql_conf = conf
