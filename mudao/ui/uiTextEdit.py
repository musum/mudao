from PyQt5.QtWidgets import *

from mudao.ui.pannel.edit import Ui_Form


class TextPannel(QWidget, Ui_Form):

    def __init__(self, path='test', newfile=False, editable=True, parent=None):
        super(TextPannel, self).__init__(parent)
        self.setupUi(self)
        # Get filepannel operation
        self.fpannel = parent
        self.pathEdit.setText(path)
        if not newfile:
            self.textEdit.setText(self.get_content())
        else:
            self.textEdit.setText('')
        self.editable = editable
        self.pushButtonSave.setDisabled(not self.editable)
        self.textEdit.setReadOnly(not self.editable)
        self.pushButtonSave.clicked.connect(self.save_file)
        self.pushButtonLoad.clicked.connect(self.load_file)

    def get_content(self):
        return self.fpannel.chk_data(self.fpannel.filemanager.showtxt(self.pathEdit.text()))

    def save_file(self):
        print('save file')
        if self.textEdit.document():
            self.fpannel.save_file(self.pathEdit.text(), self.textEdit.toPlainText())

    def load_file(self):
        print('load file')
        content = self.get_content()
        self.textEdit.setText(content)
