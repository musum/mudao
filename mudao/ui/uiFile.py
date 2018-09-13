import sys

import os
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QDir, QModelIndex
from PyQt5.QtCore import pyqtSignal as Signal

from mudao.ui.pannel.file import Ui_Form


class FilePannel(QWidget, Ui_Form):
    sig_newFile = Signal(object, str)
    sig_newFolder = Signal(str)
    sig_edit = Signal(object, str)
    sig_upload = Signal(str)
    sig_download = Signal(str)
    sig_wget = Signal(str)

    def __init__(self, parent=None):
        super(FilePannel, self).__init__(parent)
        self.setupUi(self)
        self.action_upload.triggered.connect(self.upload)
        self.action_download.triggered.connect(self.download)
        self.action_wget.triggered.connect(self.wget)
        self.action_edit.triggered.connect(self.edit_file)
        self.action_fileAdd.triggered.connect(self.new_file)
        self.action_folderAdd.triggered.connect(self.new_folder)
        self.rightView.customContextMenuRequested.connect(self._right_menu)

        self.rootl = QTreeWidgetItem(self.leftView)
        self.rootr = QTreeWidgetItem(self.rightView)

        # self.folder_model = QFileSystemModel(self)
        # self.file_model = QFileSystemModel(self)
        # self.config_model()

    def _add_row(self, data, view, root=None):
        if view.topLevelItemCount() == 0:
            for d in data:
                item = self.make_item(d)
                root.addChild(item)
                # view.addTopLevelItem(item)
            return

        for d in data:
            item = self.make_item(d)
            root.addChild(item)

    def make_item(self, it, icon='folder'):
        item = QTreeWidgetItem()
        if isinstance(it, (list, tuple)):
            for k, v in enumerate(it):
                item.setText(k, v)
            item.setIcon(0, QIcon("./images/%s.png" % it[1]))
        elif isinstance(it, str):
            item.setText(0, it)
            item.setIcon(0, QIcon("./images/%s.png" % icon))

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
