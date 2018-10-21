import os
import sys
import time

from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt
from PyQt5.QtCore import pyqtSignal as Signal

from mudao.ui.pannel.file import Ui_Form
from mudao.ui.uiWget import DlgWget
from mudao.utils.tool import add_item, human_size
from mudao.utils.logger import logger as log


class FilePannel(QWidget, Ui_Form):
    sig_newFile = Signal(object, str)
    sig_edit = Signal(object, str)
    sig_rename = Signal(object, int)

    def __init__(self, shell, parent=None):
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

        self.sig_rename.connect(self.rename)

        self.rightView.customContextMenuRequested.connect(self._right_menu)

        self.pushButton.clicked.connect(self.on_path_enter)

        self.leftView.itemDoubleClicked['QTreeWidgetItem*', 'int'].connect(self.on_left_double_clicked)
        # self.leftView.itemSelectionChanged.connect(self.on_select_changed)
        self.leftView.itemPressed['QTreeWidgetItem*', 'int'].connect(self.on_select)

        delegate = QItemDelegate()
        delegate.closeEditor.connect(self._emit_rename)
        self.leftView.setItemDelegate(delegate)

        self.rightView.itemDoubleClicked['QTreeWidgetItem*', 'int'].connect(self.on_right_double_clicked)
        self.rightView.itemPressed['QTreeWidgetItem*', 'int'].connect(self.on_select)
        setattr(self.rightView, 'mousePressEvent', lambda v: self.mousePressEvent(v, self.rightView))
        setattr(self.leftView, 'mousePressEvent', lambda v: self.mousePressEvent(v, self.leftView))
        # self.rightView.itemSelectionChanged.connect(self.on_select_changed)
        # delegate1 = QItemDelegate()
        # delegate1.closeEditor.connect(self._emit_rename_file)
        self.rightView.setItemDelegate(delegate)

        self.leftView.clear()
        self.rightView.clear()
        self.rightView.setColumnWidth(0, 200)
        self.rightView.setColumnWidth(1, 200)

        self.current_folder = None
        self.current_file = None
        self.last_select = None
        self.current_select = None
        self.click_tick = 0
        self.action = None

        self.filemanager = shell
        self.coder = self.filemanager.encoding
        self.webRoot = self.path = self.tmpAttr = self.os = self.sep = self.file2paste = None
        self.mw = self.parentWidget()

        self.menu_small = self.menu_full = None
        self.init_menu()
        self.menu = self.menu_small

    def mousePressEvent(self, evt, view):
        view.clearSelection()
        self.menu = self.menu_small
        QTreeWidget.mousePressEvent(view, evt)

    def init_menu(self):
        self.menu_small = QMenu()
        self.menu_small.addAction(self.action_upload)
        # self.menu_small.addAction(self.action_download)
        self.menu_small.addAction(self.action_wget)
        self.menu_small.addSeparator()
        subMenu = self.menu_small.addMenu('新建')
        subMenu.addAction(self.action_fileAdd)
        subMenu.addAction(self.action_folderAdd)
        self.menu_small.addSeparator()
        self.menu_small.addAction(self.action_paste)

        self.menu_full = QMenu()
        # self.menu_full.addAction(self.action_upload)
        self.menu_full.addAction(self.action_download)
        # self.menu_full.addAction(self.action_wget)
        # self.menu_full.addSeparator()
        # subMenu = self.menu_full.addMenu('新建')
        # subMenu.addAction(self.action_fileAdd)
        # subMenu.addAction(self.action_folderAdd)
        # self.menu_full.addSeparator()
        self.menu_full.addAction(self.action_view)
        self.menu_full.addAction(self.action_edit)
        self.menu_full.addAction(self.action_delete)
        self.menu_full.addAction(self.action_rename)
        self.menu_full.addAction(self.action_chstamp)
        self.menu_full.addSeparator()
        self.menu_full.addAction(self.action_copy)
        self.menu_full.addAction(self.action_cut)
        # self.menu_full.addAction(self.action_paste)

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
                log.exception(e)
        else:
            self.comboBox.setCurrentText('ERR :(')
            self.mw.statusbar.showMessage('Get server info ERR :(')

    def chk_data(self, ret):
        log.debug(ret)
        data = ''
        if ret[0] != 200:
            QMessageBox.information(self, ret[1], str(ret[2]))
            return data
        try:
            data = ret[2]       # .decode(self.coder)
            log.info('Get data:\n%s' % data)
            if data == '1':
                self.mw.statusbar.showMessage('Operation finished :)')
            else:
                self.mw.statusbar.showMessage('Operation failed :(')
        except Exception as e:
            QMessageBox.information(self, 'ERR', str(e))
            log.exception(e)
        return data

    def do_action(self, *args):
        action = getattr(self.filemanager, self.action, None)
        if action:
            return self.chk_data(action(*args))

    def list_dir(self, path):
        # todo check data in database
        self.mw.statusbar.showMessage('Get %s files...' % path)
        files = self.chk_data(self.filemanager.showfolder(path))
        if files:
            # sep = '/' if path.startswith('/') else '\\'
            self.mw.statusbar.showMessage('Get %s OK :)' % path)
            files = [f.split('\t') for f in files.split('\n') if f and './' not in f]
            folders = [f for f in files if f[0].endswith('/')]
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

    def on_select(self, item, idx):
        self.last_select = self.current_select
        self.current_select = item
        if item.treeWidget() is self.leftView:
            self.current_folder = self.get_path(item, 0)
            self.comboBox.setCurrentText(self.current_folder)
        elif item.treeWidget() is self.rightView:
            self.current_file = self.sep.join((self.current_folder, item.text(0)))
            self.comboBox.setCurrentText(self.current_file)

        if qApp.mouseButtons() & Qt.RightButton:
            self.menu = self.menu_full

        elif qApp.mouseButtons() & Qt.LeftButton:
            # print('left button')
            tick = time.time()
            # action_rename: check item equal last_select and time delta in rang (0.5, 1) sec
            if self.last_select and item == self.last_select and 0.5 < (tick - self.click_tick) < 1:
                # print('rename')
                if item.treeWidget() is self.leftView:
                    self.action = 'newfolder'
                elif item.treeWidget() is self.rightView and idx == 0:
                    self.action = 'rename'
                elif item.treeWidget() is self.rightView and idx == 1:
                    self.action = 'settime'
                self.sig_rename.emit(self.last_select, idx)
            self.click_tick = tick

    def on_left_double_clicked(self, it, idx):
        path = self.get_path(it, idx)
        self.comboBox.setCurrentText(path)
        self.list_dir(path)

    def on_right_double_clicked(self, it, idx):
        # print('double clicked')
        file = it.text(0)
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
        #         add_item(d[0], it)
        # self.make_right(data)

    # def get_file(self, it, idx):
    #     # self.current_file = tuple([it.text(i) for i in range(it.columnCount())])
    #     return it.text(0)

    def make_left(self, fullpath):
        # sep = '/' if fullpath.startswith('/') else '\\'
        fullpath = fullpath.split(self.sep)
        if fullpath[0] == '':
            fullpath[0] = '/'
        root = add_item(fullpath[0], self.leftView)
        for p in fullpath[1:]:
            p = p[:-1] if p.endswith('/') else p
            root = add_item(p, root)
        return root

    def make_right(self, data):
        self.rightView.clear()
        for d in data:
            if d[0] in ('./', '../'):
                continue
            add_item(d, self.rightView)

    # def add_item(self, data, root):
    #     NEW = True
    #     item = None
    #     name = data[0] if isinstance(data, (tuple, list)) else str(data)
    # 
    #     if isinstance(root, QTreeWidget):
    #         for i in range(root.topLevelItemCount()):
    #             if name == root.topLevelItem(i).text(0):
    #                 item = root.topLevelItem(i)
    #                 NEW = False
    #                 break
    #         if NEW:
    #             item = self.make_item(data, 'disk')
    #             root.addTopLevelItem(item)
    #         item.setExpanded(True)
    #     elif isinstance(root, QTreeWidgetItem):
    #         for i in range(root.childCount()):
    #             if name == root.child(i).text(0):
    #                 item = root.child(i)
    #                 NEW = False
    #                 break
    #         if NEW:
    #             item = self.make_item(data)
    #             root.addChild(item)
    #         item.setExpanded(True)
    #     return item
    # 
    # @staticmethod
    # def make_item(it, icon='folder'):
    #     if isinstance(it, (tuple, list)):
    #         if it[0].endswith('/'):
    #             icon = 'folder'
    #         elif '.' in it[0]:
    #             icon = 'file'
    #         else:
    #             icon = 'binary'
    # 
    #     if icon not in ('disk', 'folder', 'file', 'image'):
    #         icon = 'binary'
    # 
    #     item = QTreeWidgetItem()
    #     if isinstance(it, (tuple, list)):
    #         for k, v in enumerate(it):
    #             v = v[:-1] if v.endswith('/') else v
    #             item.setText(k, v)
    #     else:
    #         it = str(it)
    #         it = it[:-1] if it.endswith('/') else it
    #         item.setText(0, it)
    #     item.setIcon(0, QIcon("./images/file_icons/%s_24px.png" % icon))
    # 
    #     return item

    def _right_menu(self, point):
        # init right menu
        self.menu.exec_(self.rightView.viewport().mapToGlobal(point))

    def upload(self):
        path, _ = QFileDialog.getOpenFileName(self, "Open file", "", "All files (*.*)")
        rpath = self.sep.join((self.current_folder, os.path.split(path)[1]))
        log.debug('Upload file to %s' % rpath)
        if not path:
            return
        with open(path, 'rb') as f:
            self.chk_data(self.filemanager.uploadfile(rpath, f.read().hex()))
        self.list_dir(self.current_folder)

    def download(self):
        path, _ = QFileDialog.getSaveFileName(self, "Save file", "", "All files (*.*)")
        current = self.rightView.currentItem()
        if not path or not current:
            return

        # data = self.chk_data(self.filemanager.downfile(self.current_file))
        log.debug('Download file %s' % self.current_file)
        ret = self.filemanager.downfile(self.sep.join((self.current_folder, current.text(0))))
        log.debug(ret)
        if ret[0] == 200:
            with open(path, 'wb') as f:
                f.write(ret[2].encode(self.coder))
            self.mw.statusbar.showMessage('Save data success :)')
        else:
            self.mw.statusbar.showMessage('Download failed :(')

    def wget(self):
        # def _wget(url, path):
        #     self.chk_data(self.filemanager.wget(url, path))

        dlg = DlgWget(self)
        # dlg.sig_wget.connect(_wget)
        dlg.show()

    def new_file(self):
        path = self.sep.join((self.current_folder, 'New text.txt'))
        self.sig_newFile.emit(self, path)

    def delete_file(self):
        # path = self.get_path(self.rightView.currentItem(), 0)
        log.debug('del %s' % self.current_file)
        self.chk_data(self.filemanager.deletefile(self.current_file))

    def edit_file(self):
        path = self.get_path(self.rightView.currentItem(), 0)
        self.sig_edit.emit(self, path)

    def view_file(self, path):
        return self.chk_data(self.filemanager.showtxt(path))

    def save_file(self, path, data):
        self.chk_data(self.filemanager.savefile(path, data))
        # ret = self.filemanager.savefile(path, data)
        # if ret[0] == 200:
        #     self.mw.statusbar.showMessage('Save file OK :)')
        # else:
        #     self.mw.statusbar.showMessage('ERR :(')
        # return self

    def rename(self, item, idx):
        self.oldname = self.get_path(item, idx)
        view = item.treeWidget()
        if view is self.rightView and idx == 0:
            self.oldname = self.sep.join((self.current_folder, self.oldname))
        item.setFlags(item.flags() | Qt.ItemIsEditable)
        view.editItem(item, idx)

    def rename_file(self):
        self.action = 'rename'
        # item = self.rightView.currentItem()
        self.sig_rename.emit(self.current_select, 0)

    def change_stamp(self):
        self.action = 'settime'
        self.sig_rename.emit(self.current_select, 1)

    def _emit_rename(self, editor):
        if self.action is 'rename':
            new_name = self.sep.join((self.current_folder, editor.text()))
            if new_name == self.oldname:
                return
            self.mw.statusbar.showMessage('rename %s to %s' % (self.oldname, new_name))
            # self.chk_data(self.filemanager.rename(self.oldname, new_name))
            self.do_action(*(self.oldname, new_name))

        elif self.action is 'newfolder':
            new_name = self.sep.join((self.current_folder, editor.text()))
            self.mw.statusbar.showMessage('Create folder %s' % new_name)
            # self.chk_data(self.filemanager.newfolder(newname))
            self.do_action(*(new_name,))

        elif self.action is 'settime':
            newtime = editor.text()
            fname = self.sep.join((self.current_folder, self.last_select.text(0)))
            self.mw.statusbar.showMessage('Change time from %s to %s' % (self.oldname, newtime))
            # self.chk_data(self.filemanager.newfolder(newname))
            self.do_action(*(fname, newtime))

    def new_folder(self):
        self.action = 'newfolder'
        path = self.sep.join((self.current_folder, "newfolder"))
        self.oldname = path
        item = self.make_left(path)
        item.setFlags(item.flags() | Qt.ItemIsEditable)
        self.leftView.editItem(item, 0)

    # def _emit_rename_folder(self, editor):
    #     path = self.sep.join((self.current_folder, editor.text()))
    #     self.filemanager.newfolder(path)

    def copy_file(self):
        self.action = 'copy'
        self.file2paste = self.current_file

    def move_file(self):
        self.action = 'move'
        self.file2paste = self.current_file

    def paste_file(self):
        if self.action in ('copy', 'move'):
            self.action = 'pastefile'
            path = self.current_folder
            dst = self.sep.join((path, self.file2paste))
            self.do_action(*(self.file2paste, dst))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = FilePannel()
    win.show()
    sys.exit(app.exec_())
