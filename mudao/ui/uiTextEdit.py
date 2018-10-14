from PyQt5.QtWidgets import *

from mudao.ui.pannel.edit import Ui_Form


class TextPannel(QPlainTextEdit, Ui_Form):

    def __init__(self, path='test', newfile=False, editable=True, parent=None):
        super(TextPannel, self).__init__(parent)
        self.setupUi(self)
        # Get filepannel operation
        self.fpannel = parent
        self.pathEdit.setText(path)
        if not newfile:
            self.load_file()
        else:
            self.textEdit.setText('')
        self.editable = editable
        self.pushButtonSave.setDisabled(not self.editable)
        self.textEdit.setReadOnly(not self.editable)
        self.pushButtonSave.clicked.connect(self.save_file)
        self.pushButtonLoad.clicked.connect(self.load_file)

    def save_file(self):
        print('save file')
        if self.textEdit.document():
            self.fpannel.save_file(self.pathEdit.text(), self.textEdit.toPlainText())

    def load_file(self):
        print('load file')
        self.textEdit.clear()
        content = self.fpannel.view_file(self.pathEdit.text())
        self.textEdit.setText(content)
