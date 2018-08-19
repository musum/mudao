import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import pyqtSignal as Signal

from mudao.ui.pannel.edit import Ui_Form


class TextPannel(QWidget, Ui_Form):
    # sig_fileSave = Signal(str)

    def __init__(self, parent=None, fm=None, path='test', editable=False):
        super(TextPannel, self).__init__(parent)
        self.setupUi(self)
        self.fileManger = fm
        self.pathEdit.setText(path)
        self.editable = editable
        self.pushButton.setDisabled(not self.editable)
        self.textEdit.setReadOnly(not self.editable)
        self.pushButton.clicked.connect(self.save_file)
        # self.action_save.triggered.connect(self.save_file)

    def save_file(self):
        print('save file')
        self.fileManger.save(self.pathEdit.text())
