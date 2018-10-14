import sys
from PyQt5 import QtGui

from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
# from PyQt5.QtCore import pyqtSignal as Signal

from mudao.ui.pannel.cmd import Ui_Terminal


class CmdPannel(QPlainTextEdit, Ui_Terminal):
    def __init__(self, shell, path=None, parent=None):
        super(CmdPannel, self).__init__(parent)
        self.cursor = self.textCursor()
        self.cursor.movePosition(self.cursor.End)
        self.ensureCursorVisible()

        self.shell = shell

        self.zoomsize = 2
        self.ctrlPressed = False

    def wheelEvent(self, event):
        if self.ctrlPressed:
            delta = event.angleDelta()
            oriention = delta.y()/8
            self.zoomsize = 0
            if oriention > 0:
                self.zoomsize += 1
            else:
                self.zoomsize -= 1
            self.zoomIn(self.zoomsize)
            print(self.zoomsize)
        else:
            return super().wheelEvent(event)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Control:
            self.ctrlPressed = True
            print("The ctrl key is holding down")
            return super().keyPressEvent(event)
        self.insertText(event.text())

    def keyReleaseEvent(self, event):
        # print(event.text())
        if event.key() in (Qt.Key_Enter, Qt.Key_Return):
            print('execute cmd')
            print(self.get_lastline())

        if event.key() == Qt.Key_Control:
            self.ctrlPressed = False
            return super().keyReleaseEvent(event)

    def get_lastline(self):
        # print(self.toPlainText())
        # print(self.toPlainText().split('\n')[-2])
        return self.toPlainText().split('\n')[-2]

    def insertText(self, text):
        self.cursor.movePosition(QtGui.QTextCursor.End)
        self.cursor.insertText(text)
        self.setTextCursor(self.cursor)
        self.ensureCursorVisible()
