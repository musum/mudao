import sys

import os
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from mudao.ui.pannel.MainWindow import Ui_MainWindow
from mudao.ui.uiFile import FilePannel
from mudao.ui.uiTextEdit import TextPannel
from mudao.ui.uiCmd import CmdPannel

from mudao.model.filemanager import FileManager
from mudao.utils.sqlite import sqlite as db

from mudao.utils.tool import CONF
from mudao.utils.logger import logger as log
log.setLevel('DEBUG')


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.action_quit.triggered.connect(self.on_exit)

        self.action_add.triggered.connect(self.add_shell)
        self.action_edit.triggered.connect(self.edit_shell)
        self.action_del.triggered.connect(self.delete_shell)

        self.action_cmd.triggered.connect(self.show_cmd)
        self.action_file.triggered.connect(self.show_file)
        self.action_data.triggered.connect(self.show_database)

        self.mainTable.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.mainTable.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.mainTable.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.mainTable.customContextMenuRequested.connect(self._right_menu)

        self.tabWidget.removeTab(1)
        self.tabWidget.currentChanged.connect(self.current_tab_changed)
        self.tabWidget.setTabsClosable(True)
        self.tabWidget.tabCloseRequested.connect(self.close_current_tab)

        # QtGui.QTabWidget.tabBar().setTabButton(0, QtGui.QTabBar.RightSide,None)

        # XStream.stdout().messageWritten.connect(self._system_output)
        # XStream.stderr().messageWritten.connect(self._system_output)

        self.db = self.init_db()

    def init_db(self, dbf='mudao.db'):
        if not os.path.exists(dbf):
            sqlList = ["""\
            CREATE TABLE 'box' (
            'id' INTEGER PRIMARY KEY AUTOINCREMENT,
            'url' VARCHAR(128),
            'pwd' VARCHAR(8),
            'type' VARCHAR(4),
            's_group' VARCHAR(32),
            'sql_con' TEXT,
            'comment' TEXT,
            'geo' VARCHAR(4),
            'status' VARCHAR(4),
            'c_time' TIMESTAMP not null default (datetime('now','localtime')),
            'e_time' TIMESTAMP not null default (datetime('now','localtime'))
            );
            """,
            """\
            CREATE TABLE 'group_list' (
            'group_id' INTEGER PRIMARY KEY,
            'group_name' VARCHAR(64),
            'counting' INT
            );
            
            """,
            """\
            CREATE TABLE 'box_cache' (
            'id' INTEGER PRIMARY KEY AUTOINCREMENT,
            'sid' INTEGER,
            'cache_name' TEXT,
            'cache_content' BLOB
            );
            
            """,
            """\
            create trigger box_Update before update on box
            for each row
            begin
            update box set e_time = datetime('now','localtime') where id=old.id;
            end;
            """
            ]
            database = db(dbf)
            for sql in sqlList:
                database.execute(sql)
        else:
            database = db(dbf)

        return database

    def add_shell(self):
        pass

    def edit_shell(self):
        pass

    def delete_shell(self):
        pass

    # Terminal execute action
    def show_cmd(self):
        cp = CmdPannel(self)
        self.add_new_tab(cp, 'CMD')

    # File manage action
    def show_file(self):
        try:
            f = FilePannel('http://172.17.0.2/test.php', 'a', 'php', coder='gbk', parent=self)
            f.init()
            f.sig_edit.connect(lambda f, p: self.show_textEdit(f, p, newfile=False, editable=True))
            f.sig_newFile.connect(lambda f, p: self.show_textEdit(f, p, newfile=True, editable=True))
            self.add_new_tab(f, 'File')
        except Exception as e:
            print(e)

    def show_textEdit(self, fm, path, newfile=True, editable=False):
        textEditor = TextPannel(path, newfile, editable, fm)
        self.add_new_tab(textEditor, 'TextEdit')

    # Database manage action
    def show_database(self):
        pass

    def _right_menu(self, point):
        menu = QMenu()
        menu.addAction(self.action_file)
        menu.addAction(self.action_cmd)
        menu.addAction(self.action_data)
        menu.addSeparator()
        menu.addAction(self.action_add)
        menu.addAction(self.action_edit)
        menu.addAction(self.action_del)
        menu.exec_(self.mainTable.viewport().mapToGlobal(point))

    def on_exit(self):
        btn = QMessageBox.question(self, "退出", "是否确定退出？",
                                   QMessageBox.Ok | QMessageBox.Cancel)
        if btn == QMessageBox.Ok:
            qApp.quit()

    # def _add_tab(self, widget, title):
    #     num = self.tabWidget.count()
    #     self.tabWidget.addTab(QWidget(), 'test')
    #     # QtGui.QTabWidget.tabBar().setTabButton(0, QtGui.QTabBar.RightSide,None)
    #     self.tabWidget.tabBar().setTabButton(num+1, QTabBar.RightSide, )

    def add_new_tab(self, widget, title='Tab'):
        i = self.tabWidget.addTab(widget, title)
        self.tabWidget.setCurrentIndex(i)

    # def tab_open_doubleclick(self, i):
    #     if i == -1:  # No tab under the click
    #         self.add_new_tab()

    def current_tab_changed(self, i):
        print('tab change to %s' % i)
        # title = self.tabWidget.currentWidget().title
        # print(title)

    def close_current_tab(self, i):
        if self.tabWidget.count() < 2:
            self.on_exit()

        self.tabWidget.removeTab(i)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())
