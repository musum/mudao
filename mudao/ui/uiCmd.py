import sys
from PyQt5 import QtGui

from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from mudao.utils.logger import logger as log
from mudao.ui.pannel.cmd import Ui_Terminal
from mudao.utils.tool import chk_data


class CmdPannel(QPlainTextEdit, Ui_Terminal):
    def __init__(self, shell, cmd_path=None, parent=None, banner=None):
        super(CmdPannel, self).__init__(parent)
        self.cursor = self.textCursor()
        self.setUndoRedoEnabled(False)
        # Disable context menu
        # This menu is useful for undo/redo, cut/copy/paste, del, select all,
        self.setContextMenuPolicy(Qt.NoContextMenu)

        # Change font, colour of text entry box
        # text-decoration: underline;
        self.setStyleSheet(
            """QPlainTextEdit {background-color: #333;
                               color: #00FF00;
                               font-family: Courier;}""")

        self.mw = self.parentWidget()
        self.shell = shell
        self.cmd_path = cmd_path
        self.banner = banner
        self.prompt = self.promptParagraph = None
        self.isLock = False
        self.history = []
        self.webRoot = self.path = self.os = self.sep = None

        self.zoomsize = 2
        self.ctrlPressed = False
        self.get_script_path()
        self.reset(self.banner)
        self.setPrompt(self.webRoot + '> ')

    def reset(self, banner):
        self.clear()
        self.appendPlainText(banner)
        self.appendPlainText('')
        self.history = []

    def setPrompt(self, prompt, display=True):
        self.prompt = prompt
        if display:
            self.displayPrompt()

    def displayPrompt(self):
        self.setUndoRedoEnabled(False)
        self.appendPlainText('')
        self.insertText(self.prompt)
        self.promptParagraph = self.cursor.blockNumber()
        self.setUndoRedoEnabled(True)

    def get_script_path(self):
        self.mw.statusbar.showMessage('Get server info...')
        info = chk_data(self.shell.getinfo(), self.mw.statusbar)
        if info:
            self.mw.statusbar.showMessage('Get server info OK :)')
            self.webRoot, disk, _ = info.split('\t')
            self.os = 'lnx' if self.webRoot.startswith('/') else 'win'
            self.sep = '/' if self.os is 'lnx' else '\\'
            inf = ' '.join(('[ ', disk, _, ' ]'))
            self.banner = '\n'.join((self.banner, inf)) if self.banner else inf

        if not self.cmd_path:
            self.cmd_path = 'sh' if self.os is 'lnx' else 'cmd'

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
        # if event.key() == Qt.Key_Control:
        #     self.ctrlPressed = True
        #     print("The ctrl key is holding down")
            # return super().keyPressEvent(event)
        if event.key() == Qt.Key_Backspace:
            if self.handleBackspace() or not self.isSelectInEditionZone():
                return
            # return super().keyPressEvent(event)
        if event.key() in (Qt.Key_Enter, Qt.Key_Return):
            cmd = self.getCommand()
            # print('execute: %s' % cmd)
            if cmd:
                self.execute(cmd)
            else:
                self.appendPlainText('')
                self.cursor.movePosition(QtGui.QTextCursor.End)
            self.displayPrompt()
            return
        return super().keyPressEvent(event)
        # self.insertText(event.text())

    # def keyReleaseEvent(self, event):
    #     # print(event.text())
    #     if event.key() == Qt.Key_Control:
    #         self.ctrlPressed = False
    #         return super().keyReleaseEvent(event)

        # if event.key() in (Qt.Key_Enter, Qt.Key_Return):
        #     cmd = self.getCommand()
        #     print('execute: %s' % cmd)
        #     if cmd:
        #         self.execute(cmd)
        #     else:
        #         self.appendPlainText('')
        #         self.cursor.movePosition(QtGui.QTextCursor.End)
        #     self.displayPrompt()

    def handleBackspace(self):
        col = self.cursor.columnNumber()
        blk = self.cursor.blockNumber()
        if blk == self.promptParagraph and col == len(self.prompt):
            return True
        else:
            return False

    def getCommand(self):
        cur = self.textCursor()
        # self.cursor.movePosition(QtGui.QTextCursor.StartOfBlock)
        cur.movePosition(QtGui.QTextCursor.StartOfBlock)
        cur.movePosition(QtGui.QTextCursor.Right, QtGui.QTextCursor.MoveAnchor, len(self.prompt))
        cur.movePosition(QtGui.QTextCursor.EndOfBlock, QtGui.QTextCursor.KeepAnchor)
        # self.cursor.movePosition(QtGui.QTextCursor.EndOfBlock, QtGui.QTextCursor.KeepAnchor)
        cmd = cur.selectedText()
        cur.clearSelection()
        return cmd

    def replaceCommand(self, cmd):
        # cursor = self.textCursor()
        self.cursor.movePosition(QtGui.QTextCursor.StartOfLine)
        self.cursor.movePosition(QtGui.QTextCursor.Right, QtGui.QTextCursor.MoveAnchor, len(self.prompt))
        self.cursor.movePosition(QtGui.QTextCursor.EndOfBlock, QtGui.QTextCursor.KeepAnchor)
        self.cursor.insertText(cmd)

    def isInEditionZone(self, pos=None):
        if pos:
            self.cursor.setPosition(pos)
        pra = self.cursor.blockNumber()
        idx = self.cursor.columnNumber()
        return pra > self.promptParagraph or (pra == self.promptParagraph and idx > len(self.prompt))

    def isSelectInEditionZone(self):
        st = self.cursor.selectionStart()
        ed = self.cursor.selectionEnd()
        for i in (st, ed):
            self.cursor.setPosition(i)
            pra = self.cursor.blockNumber()
            idx = self.cursor.columnNumber()
            if pra < self.promptParagraph or (pra == self.promptParagraph and idx < len(self.prompt)):
                return False
        return True

    def get_lastline(self):
        # print(self.toPlainText())
        # print(self.toPlainText().split('\n')[-2])
        return self.toPlainText().split('\n')[-2]

    def insertText(self, text):
        self.cursor.movePosition(QtGui.QTextCursor.End)
        self.cursor.insertText(text)
        self.setTextCursor(self.cursor)
        self.ensureCursorVisible()

    def execute(self, cmd):
        ret = chk_data(self.shell.execute(self.cmd_path, cmd), self.mw.statusbar)
        self.appendPlainText(ret)
        return
