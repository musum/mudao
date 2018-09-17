from PyQt5.QtWidgets import *

from mudao.model.shellbase import Shell
from mudao.ui.uiFile import FilePannel


class FileManager(FilePannel):
    def __init__(self, shell_url, shell_pass, shell_type, encoder=None, parent=None):
        super(FileManager, self).__init__(parent)
        self.shell = Shell(shell_url, shell_pass, shell_type, encoder)
        self.sig_edit.connect(lambda f, p: self.edit_file(f, p))
        self.sig_newFile.connect(lambda f, p: self.new_file(f, p))
        self.sig_double_clicked.connect(lambda p: self.list_dir(p))

        for i in ['C:', 'D:']:
            self.add_item(i, self.leftView)

        # self._add_row(['folder', 'file'], self.leftView, self.leftView.topLevelItem(0))

        self.make_left('D:\\a\\b\\c')
        self.make_left('D:\\a\\c')

        for r in [('folder', 'folder', '', ''), ('file', 'file', '', '')]:
            self.add_item(r, self.rightView)

    def list_dir(self, path):
        data = self.shell.showfolder(path)
        if data[0] != 200:
            QMessageBox.information(self, data[1], data[2])
            return
        if data[2]:
            files = data[2].split('\t')
            print(files)

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
