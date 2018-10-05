import sys

import os
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QDir, QModelIndex
from PyQt5.QtCore import pyqtSignal as Signal

from mudao.ui.pannel.file import Ui_Form
from mudao.model.filemanager import FileManager


class FilePannel(QWidget, Ui_Form):
    sig_newFile = Signal(object, str)
    # sig_newFolder = Signal(str)
    sig_edit = Signal(object, str)
    # sig_upload = Signal(str)
    # sig_download = Signal(str)
    # sig_wget = Signal(str)
    # sig_double_clicked = Signal(str)
    # sig_path_enter = Signal(str)

    def __init__(self, url, pwd, type, coder='utf-8', parent=None):
        super(FilePannel, self).__init__(parent)
        self.setupUi(self)
        self.action_upload.triggered.connect(self.upload)
        self.action_download.triggered.connect(self.download)
        self.action_wget.triggered.connect(self.wget)
        self.action_edit.triggered.connect(self.edit_file)
        self.action_fileAdd.triggered.connect(self.new_file)
        self.action_folderAdd.triggered.connect(self.new_folder)
        self.rightView.customContextMenuRequested.connect(self._right_menu)

        self.pushButton.clicked.connect(self.on_path_enter)

        self.leftView.itemDoubleClicked['QTreeWidgetItem*', 'int'].connect(self.on_left_double_clicked)
        self.leftView.itemSelectionChanged.connect(self.on_select_folder)

        self.rightView.itemDoubleClicked['QTreeWidgetItem*', 'int'].connect(self.on_right_double_clicked)
        self.rightView.itemSelectionChanged.connect(self.on_select_file)

        self.leftView.clear()
        self.rightView.clear()

        self.current_folder = None
        self.current_file = None

        self.coder = coder
        self.filemanager = FileManager(url, pwd, type, coder)
        self.webRoot = self.path = self.tmpAttr = self.os = None
        self.mw = self.parentWidget()

        # self.folder_model = QFileSystemModel(self)
        # self.file_model = QFileSystemModel(self)
        # self.config_model()

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
        # add status to mainWindow
        self.mw.statusBar().showMessage('Get base info...')
        info = self.chk_data(self.filemanager.getinfo())
        if info:
            self.mw.statusBar().showMessage('Get base OK :)')
            self.webRoot, self.path, _ = info.split('\t')
            self.os = 'lnx' if self.webRoot.startswith('/') else 'win'
            self.comboBox.setCurrentText(self.webRoot)
            self.make_left(self.webRoot)
            # Get webRoot files and make right view
            try:
                self.list_dir(self.webRoot)
            except Exception as e:
                print(e)
        else:
            self.comboBox.setCurrentText('ERR :(')
            self.mw.statusBar().showMessage('Get base ERR :(')

    def chk_data(self, ret):
        data = ''
        if ret[0] != 200:
            QMessageBox.information(self, ret[1], str(ret[2]))
            return data
        try:
            data = ret[2].decode(self.coder)
        except Exception as e:
            QMessageBox.information(self, 'ERR', str(e))

        return data

    def list_dir(self, path):
        # todo check data in database
        self.mw.statusBar().showMessage('Get %s files...' % path)
        try:
            files = self.chk_data(self.filemanager.showfolder(path))
        except Exception as e:
            print(e)
        if files:
            sep = '/' if path.startswith('/') else '\\'
            self.mw.statusBar().showMessage('Get %s OK :)' % path)
            files = [f.split('\t') for f in files.split('\n') if f]
            folders = [f for f in files if f[0].endswith('/') and f[0] not in ('../', './')]
            files = [f for f in files if not f[0].endswith('/')]
            self.make_right(files)
            for f in folders:
                self.make_left(sep.join((path, f[0][:-1])))
        else:
            self.mw.statusBar().showMessage('Get %s ERR :(' % path)

    def save_file(self, path, data):
        ret = self.filemanager.savefile(path, data)
        if ret[0] == 200:
            self.mw.statusBar().showMessage('Save file OK :)')
        else:
            self.mw.statusBar().showMessage('ERR :(')
        return self

    def on_path_enter(self):
        path = self.comboBox.currentText()
        self.make_left(path)
        self.list_dir(path)

    def on_select_folder(self):
        current = self.leftView.currentItem()
        self.current_folder = self.get_path(current, 0)
        self.comboBox.setCurrentText(self.current_folder)
        self.list_dir(self.current_folder)

    def on_select_file(self):
        sep = '/' if self.current_folder.startswith('/') else '\\'
        current = self.rightView.currentItem()
        self.current_file = sep.join((self.current_folder, current.text(0)))
        self.comboBox.setCurrentText(self.current_file)

    def on_left_double_clicked(self, it, idx):
        path = self.get_path(it, idx)
        self.comboBox.setCurrentText(path)
        self.list_dir(path)

    def on_right_double_clicked(self, it, idx):
        print('double clicked')
        file = self.get_file(it, idx)
        sep = '/' if self.current_folder.startswith('/') else '\\'
        path = sep.join((self.current_folder, file))
        # self.comboBox.setCurrentText(path)
        self.sig_edit.emit(self, path)

    def get_path(self, it, idx, sep='\\'):
        path = it.text(idx)
        parent = it.parent()
        while parent:
            path = sep.join((parent.text(idx), path))
            parent = parent.parent()
        return path
        # self.sig_current_folder_changed.emit(path)
        # data = self.do_list(path)
        # for d in data:
        #     if d[1] == 'folder':
        #         self.add_item(d[0], it)
        # self.make_right(data)

    def get_file(self, it, idx):
        self.current_file = tuple([it.text(i) for i in range(it.columnCount())])
        return self.current_file

    def make_left(self, fullpath):
        sep = '/' if fullpath.startswith('/') else '\\'
        fullpath = fullpath.split(sep)
        if fullpath[0] == '':
            fullpath[0] = '/'
        root = self.add_item(fullpath[0], self.leftView)
        for p in fullpath[1:]:
            p = p[:-1] if p.endswith('/') else p
            root = self.add_item(p, root)

    def make_right(self, data):
        self.rightView.clear()
        for d in data:
            if d[0] in ('./', '../'):
                continue
            self.add_item(d, self.rightView)

    def add_item(self, data, root):
        NEW = True
        item = None
        name = data[0] if isinstance(data, (tuple, list)) else str(data)

        if isinstance(root, QTreeWidget):
            for i in range(root.topLevelItemCount()):
                if name == root.topLevelItem(i).text(0):
                    item = root.topLevelItem(i)
                    NEW = False
                    break
            if NEW:
                item = self.make_item(data, 'disk')
                root.addTopLevelItem(item)
            item.setExpanded(True)
        elif isinstance(root, QTreeWidgetItem):
            for i in range(root.childCount()):
                if name == root.child(i).text(0):
                    item = root.child(i)
                    NEW = False
                    break
            if NEW:
                item = self.make_item(data)
                root.addChild(item)
            item.setExpanded(True)
        return item

    @staticmethod
    def make_item(it, icon='folder'):
        if isinstance(it, (tuple, list)):
            if it[0].endswith('/'):
                icon = 'folder'
            elif '.' in it[0]:
                icon = 'file'
            else:
                icon = 'binary'

        if icon not in ('disk', 'folder', 'file', 'image'):
            icon = 'binary'

        item = QTreeWidgetItem()
        if isinstance(it, (tuple, list)):
            for k, v in enumerate(it):
                v = v[:-1] if v.endswith('/') else v
                item.setText(k, v)
        else:
            it = str(it)
            item.setText(0, it)
        item.setIcon(0, QIcon("./images/file_icons/%s_24px.png" % icon))

        return item

    # def config_model(self):
    #     self.folder_model.setRootPath(None)
    #     self.folder_model.setFilter(QDir.AllDirs | QDir.NoDotAndDotDot)
    #     self.leftView.setModel(self.folder_model)
    #     self.leftView.setRootIndex(self.folder_model.index(None))
    #     self.leftView.clicked[QModelIndex].connect(self.clicked_onfolder)
    #     self.leftView.hideColumn(1)
    #     self.leftView.hideColumn(2)
    #     self.leftView.hideColumn(3)
    #
    #     self.file_model.setFilter(QDir.Files)
    #     self.rightView.setModel(self.file_model)
    #     self.file_model.setReadOnly(False)
    #     self.rightView.setColumnWidth(0, 200)
    #     self.rightView.setSelectionMode(QAbstractItemView.ExtendedSelection)

    def _right_menu(self, point):
        menu = QMenu()
        menu.addAction(self.action_upload)
        menu.addAction(self.action_download)
        menu.addAction(self.action_wget)
        menu.addSeparator()
        menu.addAction(self.action_edit)
        menu.addAction(self.action_fileAdd)
        menu.addAction(self.action_folderAdd)
        menu.exec_(self.rightView.viewport().mapToGlobal(point))

    def new_folder(self):
        print('new folder')
        self.sig_newFolder.emit(self, 'test new folder')

    def upload(self):
        path, _ = QFileDialog.getOpenFileName(self, "Open file", "", "All files (*.*)")
        print(path)
        # self.sig_upload(path)

    def download(self):
        path, _ = QFileDialog.getSaveFileName(self, "Save file", "", "All files (*.*)")
        print(path)
        # self.sig_download(path)

    def edit_file(self):
        print('edit file')
        self.sig_edit.emit(self, 'test')

    def save(self, path):
        print(path)

    def wget(self):
        pass

    def clicked_onfolder(self, index):
        selection_model = self.leftView.selectionModel()
        index = selection_model.currentIndex()
        print(index)
        dir_path = self.folder_model.filePath(index)
        print(dir_path)
        self.file_model.setRootPath(dir_path)
        self.rightView.setRootIndex(self.file_model.index(dir_path))

    def open_file(self):
        index = self.rightView.selectedIndexes()
        if not index:
            return
        else:
            index = index[0]
        file_path = self.file_model.filePath(index).replace('/', '\\')
        print(file_path)
        extention = os.path.splitext(file_path)[-1]
        print(extention)
        # if extention in ['.txt', '.py']:
        #     text_editor.Application.main(file_path)
        self.rightView.update()

    def new_file(self):
        index = self.leftView.selectedIndexes()
        if len(index) > 0:
            path = self.folder_model.filePath(index[0])
            self.sig_newFile.emit(self, path + '/New text.txt')
        else:
            print("Please, select folder")

    def delete_file(self):
        indexes = self.rightView.selectedIndexes()
        for i in indexes:
            self.file_model.remove(i)

    def rename_file(self):
        index = self.rightView.selectedIndexes()
        if not index:
            return
        else:
            index = index[0]
        self.rightView.edit(index)

    def copy_file(self):
        print("COPY")
        ask = QFileDialog.getExistingDirectory(self, "Open Directory", "/home",
                                               QFileDialog.ShowDirsOnly |
                                               QFileDialog.DontResolveSymlinks)
        new_path = ask.replace('\\', '/')
        indexes = self.rightView.selectedIndexes()[::4]
        for i in indexes:
            new_filename = new_path + '/' + self.file_model.fileName(i)
            # shutil.copy2(self.file_model.filePath(i), new_filename)

    def colapse(self):
        self.leftView.collapseAll()

    def go_to(self):
        dir_path = self.goto_lineedit.text().replace('\\', '/')
        print(dir_path)
        self.file_model.setRootPath(dir_path)
        self.rightView.setRootIndex(self.file_model.index(dir_path))

        #self.file_model.setRootPath()

    def move_file(self):
        print("MOVE")
        ask = QFileDialog.getExistingDirectory(self, "Open Directory", "/home",
                                               QFileDialog.ShowDirsOnly |
                                               QFileDialog.DontResolveSymlinks)
        if ask == '':
            return
        new_path = ask.replace('\\', '/')
        indexes = self.rightView.selectedIndexes()[::4]
        for i in indexes:
            new_filename = new_path + '/' + self.file_model.fileName(i)
            # shutil.move(self.file_model.filePath(i), new_filename)

    def new_folder(self):
        index = self.leftView.selectedIndexes()
        if len(index) > 0:
            path = self.folder_model.filePath(index[0])
            for i in range(1, 9999999999999999):
                if not os.path.isdir(os.path.join(path, "newfolder{}".format(i))):
                    file_name = os.path.join(path, "newfolder{}".format(i))
                    break
            file_name = os.path.abspath(file_name)
            self.sig_newFolder.emit(self, file_name)
        else:
            print("Please, select folder")

    def delete_folder(self):
        indexes = self.leftView.selectedIndexes()
        for i in indexes:
            self.folder_model.remove(i)

    def rename_folder(self):
        index = self.leftView.selectedIndexes()
        if not index:
            return
        else:
            index = index[0]
        self.leftView.edit(index)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = FilePannel()
    win.show()
    sys.exit(app.exec_())
