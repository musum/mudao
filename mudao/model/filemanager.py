from PyQt5.QtWidgets import *

from mudao.model.shellbase import Shell
from mudao.ui.uiFile import FilePannel


class FileManager(object):
    def __init__(self, shell_url, shell_pass, shell_type, encoder=None, parent=None):
        self.parent = parent
        self.shell = Shell(shell_url, shell_pass, shell_type, encoder)

        self.pannel = FilePannel(parent)
        self.pannel.sig_edit.connect(lambda f, p: self.edit_file(f, p))
        self.pannel.sig_newFile.connect(lambda f, p: self.new_file(f, p))
        self.pannel.sig_double_clicked.connect(lambda p: self.list_dir(p))

        self.init()
        # for i in ['C:', 'D:']:
        #     self.add_item(i, self.leftView)
        #
        # # self._add_row(['folder', 'file'], self.leftView, self.leftView.topLevelItem(0))
        #
        # self.make_left('D:\\a\\b\\c')
        # self.make_left('D:\\a\\c')
        #
        # for r in [('folder', 'folder', '', ''), ('file', 'file', '', '')]:
        #     self.add_item(r, self.rightView)

    def init(self):
        # print(self.parent.db)
        info = self.shell.getinfo()
        print(info)
        info = self.get_data(info)
        self.pannel.comboBox.setCurrentText(info[0])
        self.pannel.make_left(info[0])
        files = self.list_dir(info[0])
        self.pannel.make_right([f for f in files if f not in ('./', '../')])

    def get_data(self, ret):
        if ret[0] != 200:
            QMessageBox.information(self, ret[1], ret[2])
            return ''
        return ret[2]

    def list_dir(self, path):
        data = self.shell.showfolder(path)
        return self.get_data(data)

    def edit_file(self, fm, path):
        print(path)
        self.show_textEdit(fm, path, 'test content', editable=True)

    def new_file(self, fm, path):
        print(path)
        self.show_textEdit(fm, path, '', editable=True)

    def save_file(self, path):
        self.self.save(path)


if __name__ == "__main__":
    f = FileManager('http://localhost/test.php', 'a', 'php')
    print(f.list_dir('.'))
