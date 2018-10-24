import sys

from PyQt5.QtWidgets import *

from mudao.ui.pannel.MainWindow import Ui_MainWindow
from mudao.ui.uiShellConf import ShellConfPannel
from mudao.ui.uiFile import FilePannel
from mudao.ui.uiTextEdit import TextPannel
from mudao.ui.uiCmd import CmdPannel

from mudao.model.filemanager import FileManager
from mudao.model import Box, Shell
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
        self.mainTable.itemPressed.connect(self.on_shell_select)

        self.tabWidget.removeTab(1)
        self.tabWidget.currentChanged.connect(self.current_tab_changed)
        self.tabWidget.setTabsClosable(True)
        self.tabWidget.tabCloseRequested.connect(self.close_current_tab)

        # QtGui.QTabWidget.tabBar().setTabButton(0, QtGui.QTabBar.RightSide,None)

        # XStream.stdout().messageWritten.connect(self._system_output)
        # XStream.stderr().messageWritten.connect(self._system_output)

        self.db = Box()
        self.shell = None
        self.update_table()

    def update_table(self):
        # header = ['URL', 'PWD', 'TYPE', 'ENCODING', 'CATEGORY', 'SQLCONF', 'TAG', 'IPGEO', 'STATUS', 'CREATE', 'UPDATE']
        # self.mainTable.setHorizontalHeaderLabels(header)
        self.clear_table()
        shells = self.db.get_shell()
        for shell in shells:
            self.add_row(shell)

    def clear_table(self):
        for r in range(self.mainTable.rowCount()):
            self.mainTable.removeRow(r)

    def get_row(self):
        rdata = []
        for item in self.mainTable.selectedItems():
            rdata.append(item.text())
        return rdata

    def add_row(self, data):
        data.pop('id')
        cc = self.mainTable.columnCount()
        rc = self.mainTable.rowCount()
        self.mainTable.setColumnWidth(0, 400)
        self.mainTable.insertRow(rc)
        # self.mainTable.setRowCount(rc)
        for i in range(min(cc, len(data))):
            item = QTableWidgetItem(list(data.values())[i])
            self.mainTable.setItem(rc, i, item)
        self.mainTable.update()

    def on_shell_select(self, it):
        k = ['url', 'pwd', 'type', 'encoding', 'category', 'sqlconf', 'tag']
        v = self.get_row()[:-4]
        self.shell = Shell(**dict(zip(k, v)))

    def add_shell(self):
        pannel = ShellConfPannel(parent=self)
        pannel.sig_emit_shell.connect(self.on_shell_added)
        pannel.show()

    def on_shell_added(self, shell):
        self.db.add_shell(shell)
        self.update_table()

    def edit_shell(self, shell):
        pannel = ShellConfPannel(self.shell, self)
        pannel.sig_emit_shell.connect(self.on_shell_updated)
        pannel.show()

    def on_shell_updated(self, shell):
        self.db.update_shell(shell)
        self.update_table()

    def delete_shell(self):
        self.db.delete_shell(self.shell)
        self.update_table()

    # Terminal execute action
    def show_cmd(self):
        cp = CmdPannel(self)
        self.add_new_tab(cp, 'CMD')

    # File manage action
    def show_file(self):
        try:
            # f = FilePannel('http://172.17.0.2/test.php', 'a', 'php', coder='gbk', parent=self)
            shell = FileManager(url='http://localhost/test.php', pwd='a', type='php', encoding='gbk')
            f = FilePannel(shell, parent=self)
            f.init()
            f.sig_edit.connect(lambda fm, p: self.show_textEdit(fm, p, newfile=False, editable=True))
            f.sig_newFile.connect(lambda fm, p: self.show_textEdit(fm, p, newfile=True, editable=True))
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
