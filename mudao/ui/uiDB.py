from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QWidget, QTreeWidgetItem, QTreeWidget
from PyQt5.QtCore import pyqtSignal as Signal

from mudao.ui.pannel.dbm import Ui_Form
from mudao.ui.uiDBConf import DBConfig
from mudao.utils.tool import chk_data


class DBManagerPannel(QWidget, Ui_Form):
    sig_db_conf_submit = Signal(dict)

    def __init__(self, shell, parent=None):
        super().__init__(parent=parent)
        self.setupUi(self)
        self.btn_config.clicked.connect(self.on_config_clicked)
        self.btn_execute.clicked.connect(self.on_execute_clicked)

        self.leftView.itemDoubleClicked.connect(self.on_left_doubleclicked)
        self.leftView.itemPressed.connect(self.on_select)

        self.mw = self.parentWidget()
        self.dbm = shell
        self.encoding = shell.encoding
        self.conf = shell.sqlconf or ''
        if self.conf:
            self.get_database()

        self.select = None
        self.current_obj = None

    def on_config_clicked(self):
        dlg = DBConfig(self.conf, self)
        dlg.sig_conf_submit.connect(self.db_config_edit)
        dlg.show()

    def on_execute_clicked(self):
        print(self.current_obj)
        sql = self.cbo_sql.currentText()
        data = chk_data(self.dbm.execute(self.conf, sql, self.current_obj.split('.')[0]), self.mw.statusbar)
        self.add_item_right(data)

    # def execute(self, conn, action, sql=None):
    #     return chk_data(self.dbm.get_data(conn, action, sql), self.mw.statusbar)

    def db_config_edit(self, conf):
        self.conf = conf
        self.get_database()
        self.sig_db_conf_submit.emit(dict(sqlconf=self.conf))

    def get_database(self):
        # clean tree view
        self.leftView.clear()
        self.reset_right_view()

        dbs = chk_data(self.dbm.database(self.conf), self.mw.statusbar)
        if dbs:
            for db in dbs.split('\t'):
                if db:
                    self.add_item_left(db, 'database')

    def add_tables(self, tbls):
        for tbl in tbls:
            if tbl:
                self.add_item_left(tbl, 'table', self.select)

    def add_columns(self, cols):
        for col in cols:
            if col:
                self.add_item_left(col, 'column', self.select)

    def on_select(self, it, idx):
        self.select = it
        self.current_obj = self.make_path(it)

    def on_left_doubleclicked(self, it, idx):
        self.select = it
        self.current_obj = self.make_path(it)
        if len(self.current_obj.split('.')) == 1:
            db = self.current_obj
            self.cbo_sql.setCurrentText('SHOW TABLES FROM `mysql`')
            tbls = chk_data(self.dbm.tables(self.conf, db), self.mw.statusbar)
            self.add_tables(tbls.split('\t'))
        elif len(self.current_obj.split('.')) == 2:
            db, tbl = self.current_obj.split('.')
            self.cbo_sql.setCurrentText('SELECT * FROM %s ORDER BY 1 DESC LIMIT 0,20' % tbl)
            cols = chk_data(self.dbm.columns(self.conf, tbl, db), self.mw.statusbar)
            self.add_columns(cols.split('\t'))

    @staticmethod
    def make_path(it):
        path = it.text(0)
        parent = it.parent()
        while parent:
            path = '.'.join((parent.text(0), path))
            parent = parent.parent()
        return path

    def add_item_left(self, name, type, root=None):
        item = None
        if type == 'database':
            item = self.make_item(name, 'database')
            self.leftView.addTopLevelItem(item)
        elif type == 'table':
            item = self.exist_item(name, root)
            if not item:
                item = self.make_item(name, 'table')
                root.addChild(item)
        elif type == 'column':
            item = self.exist_item(name, root)
            if not item:
                item = self.make_item(name, 'column')
                root.addChild(item)
        return item

    def add_item_right(self, data):
        self.reset_right_view()
        data = data.split('\n')
        header = data[0].split('\t|\t')
        self.rightView.setHeaderLabels(header)
        for d in data[1:]:
            item = self.make_item(d.split('\t|\t'))
            self.rightView.addTopLevelItem(item)

    def reset_right_view(self):
        self.rightView.clear()
        self.rightView.setColumnCount(0)

    @staticmethod
    def exist_item(name, root):
        for i in range(root.childCount()):
            if name == root.child(i).text(0):
                item = root.child(i)
                return item
        return None

    @staticmethod
    def empty_child(root):
        if root.childCount > 0:
            for i in range(root.childCount()):
                root.takechild(i)

    @staticmethod
    def make_item(it, icon=None):
        if icon in ('database', 'table', 'column'):
            icon_path = './images/db_icons/%s.png' % icon
        else:
            icon_path = None

        item = QTreeWidgetItem()
        if isinstance(it, (tuple, list)):
            for k, v in enumerate(it):
                item.setText(k, v)
        else:
            it = str(it)
            item.setText(0, it)
        if icon_path:
            item.setIcon(0, QIcon(icon_path))

        return item
