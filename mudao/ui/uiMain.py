import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from ui.pannel.MainWindow import Ui_MainWindow


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

        # QtGui.QTabWidget.tabBar().setTabButton(0, QtGui.QTabBar.RightSide,None)

        # XStream.stdout().messageWritten.connect(self._system_output)
        # XStream.stderr().messageWritten.connect(self._system_output)

    def add_shell(self):
        pass

    def edit_shell(self):
        pass

    def delete_shell(self):
        pass

    def show_cmd(self):
        pass

    def show_file(self):
        pass

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

    def _add_tab(self, widget, title):
        num = self.tabWidget.count()
        self.tabWidget.addTab(QWidget(), 'test')
        # QtGui.QTabWidget.tabBar().setTabButton(0, QtGui.QTabBar.RightSide,None)
        self.tabWidget.tabBar().setTabButton(num+1, QTabBar.RightSide, )


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())
