import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from mudao.ui.pannel.MainWindow import Ui_MainWindow
from mudao.ui.uiFile import FilePannel
from mudao.ui.uiTextEdit import TextPannel
from mudao.ui.uiCmd import CmdPannel


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
        fileManager = FilePannel(self)
        fileManager.sig_edit.connect(lambda f, p: self.edit_file(f, p))
        fileManager.sig_newFile.connect(lambda f, p: self.new_file(f, p))
        self.add_new_tab(fileManager, 'File')

    def show_textEdit(self, fm, path, content, editable):
        textEditor = TextPannel(self, fm, path, editable)
        # textEditor.sig_fileSave.connect(lambda x: self.save_file(x))
        if content:
            textEditor.textEdit.setText(content)
        self.add_new_tab(textEditor, 'TextEdit')

    def edit_file(self, fm, path):
        print(path)
        self.show_textEdit(fm, path, 'test content', editable=True)

    def new_file(self, fm, path):
        print(path)
        self.show_textEdit(fm, path, '', editable=True)

    def save_file(self, path):
        self.fileManager.save(path)

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
