# -*- coding: utf-8 -*-
import os
import sys
from subprocess import *

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from PyQt5 import QtGui
from PyQt5 import QtCore
from PyQt5.QtCore import QThreadPool, QProcess, Qt
from PyQt5.QtWidgets import *

from ui import *
from config import Config
from logger import logger
# from utils import XStream





class ConsoleLog(QTextEdit):
    def __init__(self, parent=None):
        super().__init__(parent)

    def keyReleaseEvent(self, e):
        if e.key() == Qt.Key_Enter:
            print(self.toPlainText())


class DialogFile(QDialog, Ui_File):
    def __init__(self, parent=None):
        super(DialogFile, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle('File')

        self.treeView.customContextMenuRequested.connect(self.open_right_menu)
        self.action_upload.triggered.connect(self.upload_file)
        self.action_download.triggered.connect(self.download_file)

    def open_right_menu(self, po):
        popMenu = QMenu(self)
        popMenu.addAction(self.action_newfile)
        popMenu.addAction(self.action_newfolder)
        popMenu.addAction(self.action_upload)
        popMenu.addAction(self.action_download)
        popMenu.addSeparator()
        popMenu.addAction(self.action_refresh)
        popMenu.exec_(self.treeView.viewport().mapToGlobal(po))

    def new_file(self, fname='New Text.txt'):
        pass

    def new_folder(self, name='New Folder'):
        pass

    def upload_file(self):
        filename, _ = QFileDialog.getOpenFileName(self, "打开文件", "",
                                                  "All files (*.*)")
        print(filename)
        print(_)
        # with open(filename, 'r') as f:
        #     f.read()

    def download_file(self):
        savename, _ = QFileDialog.getSaveFileName(self, "保存文件", "", "All files (*.*)")
        print(savename)

    def refresh(self):
        pass


class DialogCmd(QDialog, Ui_Cmd):

    class EmittingStream(QtCore.QObject):
        textWritten = QtCore.pyqtSignal(str)  # 定义一个发送str的信号

        def write(self, text):
            self.textWritten.emit(str(text))

    def __init__(self, parent=None):
        super(DialogCmd, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle('Cmd')
        # self.textEdit.setReadOnly(True)
        # 将输出重定向到textEdit中
        sys.stdout = self.EmittingStream(textWritten=self.outputWritten)
        sys.stderr = self.EmittingStream(textWritten=self.outputWritten)

    # 接收信号str的信号槽
    def outputWritten(self, text):
        cursor = self.textEdit.textCursor()
        cursor.movePosition(QtGui.QTextCursor.End)
        cursor.insertText(text)
        self.textEdit.setTextCursor(cursor)
        self.textEdit.ensureCursorVisible()


class DialogProcess(QDialog, Ui_Process):
    def __init__(self, parent=None):
        super(DialogProcess, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle('Process Manager')
        self.listView.customContextMenuRequested.connect(self._right_menu)
        self.action_refresh.triggered.connect(self.on_refresh)
        self.action_kill.triggered.connect(self.on_kill)

    def _right_menu(self, point):
        menu = QMenu()
        menu.addAction(self.action_kill)
        menu.addSeparator()
        menu.addAction(self.action_refresh)
        menu.exec_(self.listView.viewport().mapToGlobal(point))

    def on_kill(self):
        print('kill process')

    def on_refresh(self):
        print('refresh process')


class DialogSvrSettings(QDialog, Ui_svrSettings):
    def __init__(self, parent=None, conf=None):
        super(DialogSvrSettings, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("Server Setting")
        if conf:
            self.url.setText(conf.get('server', 'config_url'))
        self.buttonBox.accepted.connect(lambda: self.save_settings(conf))

    def save_settings(self, conf):
        conf.set('server', 'config_url', self.url.text())
        conf.save()


class DialogCtlSettings(QDialog, Ui_ctlSettings):
    def __init__(self, parent=None, conf=None):
        super(DialogCtlSettings, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle('Controller Setting')
        if conf:
            self.port.setText(conf.get('controller', 'port'))
            self.password.setText(conf.get('controller', 'password'))
            self.git_user.setText(conf.get('github', 'user'))
            self.git_pass.setText(conf.get('github', 'password'))
            self.token_full.setText(conf.get('github', 'token_full'))
            self.token_limit.setText(conf.get('github', 'token_limit'))
        self.buttonBox.accepted.connect(lambda: self.save_settings(conf))

    def save_settings(self, conf):
        conf.set('controller', 'port', self.port.text())
        conf.set('controller', 'password', self.password.text())
        conf.set('github', 'user', self.git_user.text())
        conf.set('github', 'password', self.git_pass.text())
        conf.set('github', 'token_full', self.token_full.text())
        conf.set('github', 'token_limit', self.token_limit.text())
        conf.save()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())
