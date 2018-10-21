import sys
from PyQt5.QtWidgets import QDialog, QApplication, QInputDialog
from PyQt5.QtCore import pyqtSignal as Signal

from mudao.model import Shell
from mudao.ui.pannel.shellconfig import Ui_Dialog


class ShellConfPannel(QDialog, Ui_Dialog):
    sig_emit_shell = Signal(object)

    def __init__(self, shell=None, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.shell_default = dict(url='', pwd='', type='', category='default', encoding='utf-8',
                                  sqlconf='', tag='', status='', geo='')
        self.action = 'update' if shell else 'insert'
        self.shell = shell or Shell(**self.shell_default)
        self.init_view()
        self.btnAdd.clicked.connect(self.on_btn_clicked)
        self.cbo_category.currentTextChanged.connect(self.on_category_changed)
        self.cbo_encoding.currentTextChanged.connect(self.on_encoding_changed)
        self.cbo_shelltype.currentTextChanged.connect(self.on_type_changed)
        self.mw = parent

    def init_view(self):
        btn_text = 'ADD' if self.action is 'insert' else 'EDIT'
        self.btnAdd.setText(btn_text)
        self.url.setText(self.shell.url)
        self.pwd.setText(self.shell.pwd)
        self.cbo_shelltype.setCurrentText(self.shell.type)
        self.cbo_category.setCurrentText(self.shell.category)
        self.cbo_encoding.setCurrentText(self.shell.encoding)
        # self.dbconf.setText(self.shell.sqlconf)
        self.edt_tag.setText(self.shell.tag)

    def update_shell(self):
        self.shell.url = self.url.text()
        self.shell.pwd = self.pwd.text()
        # self.shell.type = self.cbo_shelltype.currentText()
        # self.shell.category = self.cbo_category.currentText()
        # self.shell.encoding = self.cbo_encoding.currentText()
        # self.shell.sqlconf = self.dbconf.toPlainText()
        self.shell.tag = self.edt_tag.text()

    def on_btn_clicked(self):
        self.update_shell()
        self.sig_emit_shell.emit(self.shell.to_dict())

    def on_category_changed(self):
        self.shell.category = self.cbo_category.currentText().lower()

    def on_type_changed(self):
        self.shell.type = self.cbo_shelltype.currentText().lower()

    def on_encoding_changed(self):
        self.shell.encoding = self.cbo_encoding.currentText()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = ShellConfPannel()
    win.show()
    sys.exit(app.exec_())
