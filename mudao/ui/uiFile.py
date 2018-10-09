import os
import sys

from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt, QVariant
from PyQt5.QtCore import pyqtSignal as Signal

from mudao.ui.pannel.file import Ui_Form
from mudao.model.filemanager import FileManager


class Delegate(QItemDelegate):

    def __init__(self, parent=None):
        super(QItemDelegate, self).__init__(parent)
        self.closeEditor.connect(self.emit_data)

    # def createEditor(self, parent, option, index):
    #     # Create editor object of QLineEdit
    #     if index.column() == 0:
    #         editor = QLineEdit(parent)
    #         editor.setMaximumWidth(100)
    #         editor.returnPressed.connect(self.commitAndCloseEditor)
    #         # self.connect(editor, SIGNAL("returnPressed()"), self.commitAndCloseEditor)
    #         return editor
    #     else:
    #         return QItemDelegate.createEditor(self, parent, option, index)
    #
    def emit_data(self, editor):
        # print('emit data')
        print(editor.text())
    #
    # def commitAndCloseEditor(self):
    #     editor = self.sender()
    #     if isinstance(editor, (QLineEdit)):
    #
    #         # call to commitData is essential in Qt5
    #         self.commitData.emit(editor)
    #         self.closeEditor.emit(editor)
    #         # self.emit_data(editor.text())
    #
    # def setEditorData(self, editor, index):
    #     # text = index.model().data(index, Qt.DisplayRole).value()
    #     text = index.model().data(index, Qt.DisplayRole)
    #     if index.column() == 0:
    #         editor.setText(text)
    #     else:
    #         QItemDelegate.setEditorData(self, editor, index)
    #
    # def setModelData(self, editor, model, index):
    #     # Method uses model.setData()!
    #     # Make sure that you implemented setData() method
    #     if index.column() == 0:
    #         model.setData(index, QVariant(editor.text()))
    #     else:
    #         QItemDelegate.setModelData(self, editor, model, index)


class FilePannel(QWidget, Ui_Form):
    sig_newFile = Signal(object, str)
    sig_edit = Signal(object, str)

    def __init__(self, url, pwd, type, coder='utf-8', parent=None):
        super(FilePannel, self).__init__(parent)
        self.setupUi(self)
        self.action_upload.triggered.connect(self.upload)
        self.action_download.triggered.connect(self.download)
        self.action_wget.triggered.connect(self.wget)
        self.action_fileAdd.triggered.connect(self.new_file)
        self.action_folderAdd.triggered.connect(self.new_folder)
        self.action_edit.triggered.connect(self.edit_file)
        self.action_view.triggered.connect(self.view_file)
        self.action_delete.triggered.connect(self.delete_file)
        self.action_rename.triggered.connect(self.rename_file)
        self.action_chstamp.triggered.connect(self.change_stamp)
        self.action_copy.triggered.connect(self.copy_file)
        self.action_cut.triggered.connect(self.move_file)
        self.action_paste.triggered.connect(self.paste_file)

        self.rightView.customContextMenuRequested.connect(self._right_menu)

        self.pushButton.clicked.connect(self.on_path_enter)

        self.leftView.itemDoubleClicked['QTreeWidgetItem*', 'int'].connect(self.on_left_double_clicked)
        self.leftView.itemSelectionChanged.connect(self.on_select_folder)
        # self.leftView.itemPressed['QTreeWidgetItem*', 'int'].connect(self.on_left_data_handle)

        delegate = QItemDelegate()
        delegate.closeEditor.connect(self._emit_rename_folder)
        self.leftView.setItemDelegate(delegate)

        self.rightView.itemDoubleClicked['QTreeWidgetItem*', 'int'].connect(self.on_right_double_clicked)
        self.rightView.itemPressed['QTreeWidgetItem*', 'int'].connect(self.on_select_file)
        # self.rightView.itemSelectionChanged.connect(self.on_select_file)
        delegate1 = QItemDelegate()
        delegate1.closeEditor.connect(self._emit_rename_file)
        self.rightView.setItemDelegate(delegate1)

        self.leftView.clear()
        self.rightView.clear()

        self.current_folder = None
        self.current_file = None

        self.coder = coder
        self.filemanager = FileManager(url, pwd, type, coder)
        self.webRoot = self.path = self.tmpAttr = self.os = self.sep = None
        self.mw = self.parentWidget()

    def init(self):
        # add status to mainWindow
        self.mw.statusbar.showMessage('Get server info...')
        info = self.chk_data(self.filemanager.getinfo())
        if info:
            self.mw.statusbar.showMessage('Get server info OK :)')
            self.webRoot, self.path, _ = info.split('\t')
            self.os = 'lnx' if self.webRoot.startswith('/') else 'win'
            self.sep = '/' if self.os is 'lnx' else '\\'
            self.current_folder = self.webRoot
            self.comboBox.setCurrentText(self.webRoot)
            self.make_left(self.webRoot)
            # Get webRoot files and make right view
            try:
                self.list_dir(self.webRoot)
            except Exception as e:
                print(e)
        else:
            self.comboBox.setCurrentText('ERR :(')
            self.mw.statusbar.showMessage('Get server info ERR :(')

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
        self.mw.statusbar.showMessage('Get %s files...' % path)
        try:
            files = self.chk_data(self.filemanager.showfolder(path))
        except Exception as e:
            print(e)
        if files:
            # sep = '/' if path.startswith('/') else '\\'
            self.mw.statusbar.showMessage('Get %s OK :)' % path)
            files = [f.split('\t') for f in files.split('\n') if f]
            folders = [f for f in files if f[0].endswith('/') and f[0] not in ('../', './')]
            files = [f for f in files if not f[0].endswith('/')]
            self.make_right(files)
            for f in folders:
                self.make_left(self.sep.join((path, f[0][:-1])).replace('//', '/'))
        else:
            self.mw.statusbar.showMessage('Get %s ERR :(' % path)

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
        if qApp.mouseButtons() & Qt.RightButton:
            print('right button')
        elif qApp.mouseButtons() & Qt.LeftButton:
            print('left button')
            # tick = QTime.currentTime().msec()
            # while QTime.currentTime().msec() - tick < 500:
            #     if QTime.currentTime().msec() - tick > 300 and qApp.mouseButtons() & QtCore.Qt.LeftButton:
            #         print('edit name')
            #         break

        # sep = '/' if self.current_folder.startswith('/') else '\\'
        current = self.rightView.currentItem()
        self.current_file = self.sep.join((self.current_folder, current.text(0)))
        self.comboBox.setCurrentText(self.current_file)

    def on_left_double_clicked(self, it, idx):
        path = self.get_path(it, idx)
        self.comboBox.setCurrentText(path)
        self.list_dir(path)

    def on_right_double_clicked(self, it, idx):
        print('double clicked')
        file = self.get_file(it, idx)
        # sep = '/' if self.current_folder.startswith('/') else '\\'
        path = self.sep.join((self.current_folder, file))
        # self.comboBox.setCurrentText(path)
        self.sig_edit.emit(self, path)

    def get_path(self, it, idx):
        path = it.text(idx)
        parent = it.parent()
        while parent:
            path = self.sep.join((parent.text(idx), path))
            parent = parent.parent()
        if self.os is 'lnx':
            path = path.replace('//', '/')
        return path
        # self.sig_current_folder_changed.emit(path)
        # data = self.do_list(path)
        # for d in data:
        #     if d[1] == 'folder':
        #         self.add_item(d[0], it)
        # self.make_right(data)

    def get_file(self, it, idx):
        # self.current_file = tuple([it.text(i) for i in range(it.columnCount())])
        return it.text(0)

    def make_left(self, fullpath):
        # sep = '/' if fullpath.startswith('/') else '\\'
        fullpath = fullpath.split(self.sep)
        if fullpath[0] == '':
            fullpath[0] = '/'
        root = self.add_item(fullpath[0], self.leftView)
        for p in fullpath[1:]:
            p = p[:-1] if p.endswith('/') else p
            root = self.add_item(p, root)
        return root

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

    def _right_menu(self, point):
        # init right menu
        menu = QMenu()
        menu.addAction(self.action_upload)
        menu.addAction(self.action_download)
        menu.addAction(self.action_wget)
        menu.addSeparator()
        menu.addAction(self.action_fileAdd)
        menu.addAction(self.action_folderAdd)

        menu.addSeparator()
        menu.addAction(self.action_view)
        menu.addAction(self.action_edit)
        menu.addAction(self.action_delete)
        menu.addAction(self.action_rename)
        menu.addAction(self.action_chstamp)
        menu.addSeparator()
        menu.addAction(self.action_copy)
        menu.addAction(self.action_cut)
        menu.addAction(self.action_paste)
        menu.exec_(self.rightView.viewport().mapToGlobal(point))

    def upload(self):
        path, _ = QFileDialog.getOpenFileName(self, "Open file", "", "All files (*.*)")
        rpath = self.sep.join((self.current_folder, os.path.split(path)[1]))
        print(rpath)
        with open(path, 'rb') as f:
            self.filemanager.uploadfile(rpath, f.read().hex())
        print('ok')

    def download(self):
        path, _ = QFileDialog.getSaveFileName(self, "Save file", "", "All files (*.*)")
        print(path)
        with open(path, 'wb') as f:
            f.write(self.filemanager.downfile(self.current_file)[2])

    def wget(self):
        pass

    def new_file(self):
        path = self.sep.join((self.current_folder, 'New text.txt'))
        self.sig_newFile.emit(self, path)

    def delete_file(self):
        path = self.get_path(self.rightView.currentItem(), 0)
        print('del %s' % self.current_file)
        self.filemanager.deletefile(self.current_file)

    def edit_file(self):
        path = self.get_path(self.rightView.currentItem(), 0)
        self.sig_edit.emit(self, path)

    def view_file(self):
        self.edit_file()

    def save_file(self, path, data):
        ret = self.filemanager.savefile(path, data)
        if ret[0] == 200:
            self.mw.statusbar.showMessage('Save file OK :)')
        else:
            self.mw.statusbar.showMessage('ERR :(')
        return self

    def rename_file(self):
        item = self.rightView.currentItem()
        self.prename = self.get_path(item, 0)
        item.setFlags(item.flags() | Qt.ItemIsEditable)
        self.rightView.editItem(item, 0)

    def change_stamp(self):
        pass

    def _emit_rename_file(self, editor):
        newname = self.sep.join((self.current_folder, editor.text()))
        if newname == self.prename:
            self.prename = None
            return
        print('rename %s to %s' % (self.prename, newname))
        self.filemanager.rename(self.prename, newname)

    def new_folder(self):
        path = self.sep.join((self.current_folder, "newfolder"))
        item = self.make_left(path)
        item.setFlags(item.flags() | Qt.ItemIsEditable)
        self.leftView.editItem(item, 0)

    def _emit_rename_folder(self, editor):
        path = self.sep.join((self.current_folder, editor.text()))
        self.filemanager.newfolder(path)

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

    def paste_file(self):
        print('paste file')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = FilePannel()
    win.show()
    sys.exit(app.exec_())
