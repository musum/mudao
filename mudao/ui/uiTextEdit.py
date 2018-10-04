import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import pyqtSignal as Signal

from mudao.ui.pannel.edit import Ui_Form


class TextPannel(QWidget, Ui_Form):
    sig_fileSave = Signal(str, str)

    def __init__(self, path='test', content='', editable=True, parent=None):
        super(TextPannel, self).__init__(parent)
        self.setupUi(self)
        self.pathEdit.setText(path)
        self.textEdit.setText(content)
        self.editable = editable
        self.pushButton.setDisabled(not self.editable)
        self.textEdit.setReadOnly(not self.editable)
        self.pushButton.clicked.connect(self.save_file)
        # self.action_save.triggered.connect(self.save_file)

    def save_file(self):
        print('save file')
        print(self.textEdit.document())
        if self.textEdit.document():
            self.sig_fileSave.emit(self.pathEdit.text(), self.textEdit.document())
