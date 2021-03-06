# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'file.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1043, 618)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.iconPath = QtWidgets.QWidget(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.iconPath.sizePolicy().hasHeightForWidth())
        self.iconPath.setSizePolicy(sizePolicy)
        self.iconPath.setObjectName("iconPath")
        self.horizontalLayout.addWidget(self.iconPath)
        self.comboBox = QtWidgets.QComboBox(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox.sizePolicy().hasHeightForWidth())
        self.comboBox.setSizePolicy(sizePolicy)
        self.comboBox.setEditable(True)
        self.comboBox.setCurrentText("")
        self.comboBox.setObjectName("comboBox")
        self.horizontalLayout.addWidget(self.comboBox)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.splitter = QtWidgets.QSplitter(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.splitter.sizePolicy().hasHeightForWidth())
        self.splitter.setSizePolicy(sizePolicy)
        self.splitter.setMidLineWidth(2)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setChildrenCollapsible(False)
        self.splitter.setObjectName("splitter")
        self.leftView = QtWidgets.QTreeWidget(self.splitter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(25)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.leftView.sizePolicy().hasHeightForWidth())
        self.leftView.setSizePolicy(sizePolicy)
        self.leftView.setMinimumSize(QtCore.QSize(100, 0))
        self.leftView.setMouseTracking(True)
        self.leftView.setTabletTracking(True)
        self.leftView.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.leftView.setIconSize(QtCore.QSize(16, 16))
        self.leftView.setColumnCount(1)
        self.leftView.setObjectName("leftView")
        item_0 = QtWidgets.QTreeWidgetItem(self.leftView)
        self.leftView.header().setVisible(False)
        self.rightView = QtWidgets.QTreeWidget(self.splitter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(75)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rightView.sizePolicy().hasHeightForWidth())
        self.rightView.setSizePolicy(sizePolicy)
        self.rightView.setMinimumSize(QtCore.QSize(200, 0))
        self.rightView.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.rightView.setEditTriggers(QtWidgets.QAbstractItemView.SelectedClicked)
        self.rightView.setIconSize(QtCore.QSize(16, 16))
        self.rightView.setObjectName("rightView")
        item_0 = QtWidgets.QTreeWidgetItem(self.rightView)
        self.verticalLayout.addWidget(self.splitter)
        self.action_fileAdd = QtWidgets.QAction(Form)
        self.action_fileAdd.setObjectName("action_fileAdd")
        self.action_folderAdd = QtWidgets.QAction(Form)
        self.action_folderAdd.setObjectName("action_folderAdd")
        self.action_upload = QtWidgets.QAction(Form)
        self.action_upload.setObjectName("action_upload")
        self.action_download = QtWidgets.QAction(Form)
        self.action_download.setObjectName("action_download")
        self.action_wget = QtWidgets.QAction(Form)
        self.action_wget.setObjectName("action_wget")
        self.action_edit = QtWidgets.QAction(Form)
        self.action_edit.setObjectName("action_edit")
        self.action_rename = QtWidgets.QAction(Form)
        self.action_rename.setObjectName("action_rename")
        self.action_view = QtWidgets.QAction(Form)
        self.action_view.setObjectName("action_view")
        self.action_chstamp = QtWidgets.QAction(Form)
        self.action_chstamp.setObjectName("action_chstamp")
        self.action_delete = QtWidgets.QAction(Form)
        self.action_delete.setObjectName("action_delete")
        self.action_copy = QtWidgets.QAction(Form)
        self.action_copy.setObjectName("action_copy")
        self.action_paste = QtWidgets.QAction(Form)
        self.action_paste.setObjectName("action_paste")
        self.action_cut = QtWidgets.QAction(Form)
        self.action_cut.setObjectName("action_cut")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "FileManager"))
        self.pushButton.setText(_translate("Form", "Go"))
        self.splitter.setToolTip(_translate("Form", "文件管理"))
        self.splitter.setWhatsThis(_translate("Form", "文件管理"))
        self.leftView.headerItem().setText(0, _translate("Form", "Folder"))
        __sortingEnabled = self.leftView.isSortingEnabled()
        self.leftView.setSortingEnabled(False)
        self.leftView.topLevelItem(0).setText(0, _translate("Form", "/"))
        self.leftView.setSortingEnabled(__sortingEnabled)
        self.rightView.setSortingEnabled(True)
        self.rightView.headerItem().setText(0, _translate("Form", "Name"))
        self.rightView.headerItem().setText(1, _translate("Form", "Time"))
        self.rightView.headerItem().setText(2, _translate("Form", "Size"))
        self.rightView.headerItem().setText(3, _translate("Form", "Attribute"))
        __sortingEnabled = self.rightView.isSortingEnabled()
        self.rightView.setSortingEnabled(False)
        self.rightView.topLevelItem(0).setText(0, _translate("Form", "etc"))
        self.rightView.topLevelItem(0).setText(1, _translate("Form", "2018.09.12"))
        self.rightView.topLevelItem(0).setText(2, _translate("Form", "10K"))
        self.rightView.topLevelItem(0).setText(3, _translate("Form", "777"))
        self.rightView.setSortingEnabled(__sortingEnabled)
        self.action_fileAdd.setText(_translate("Form", "文件"))
        self.action_fileAdd.setToolTip(_translate("Form", "新建文件"))
        self.action_fileAdd.setShortcut(_translate("Form", "Ctrl+N"))
        self.action_folderAdd.setText(_translate("Form", "文件夹"))
        self.action_folderAdd.setToolTip(_translate("Form", "新建文件夹"))
        self.action_folderAdd.setShortcut(_translate("Form", "Ctrl+Shift+N"))
        self.action_upload.setText(_translate("Form", "上传"))
        self.action_upload.setToolTip(_translate("Form", "上传"))
        self.action_upload.setShortcut(_translate("Form", "Ctrl+U"))
        self.action_download.setText(_translate("Form", "下载"))
        self.action_download.setToolTip(_translate("Form", "下载"))
        self.action_download.setShortcut(_translate("Form", "Ctrl+D"))
        self.action_wget.setText(_translate("Form", "wget"))
        self.action_wget.setToolTip(_translate("Form", "wget"))
        self.action_wget.setShortcut(_translate("Form", "Ctrl+W"))
        self.action_edit.setText(_translate("Form", "编辑"))
        self.action_edit.setToolTip(_translate("Form", "编辑文件"))
        self.action_edit.setShortcut(_translate("Form", "Ctrl+E"))
        self.action_rename.setText(_translate("Form", "重命名"))
        self.action_rename.setToolTip(_translate("Form", "重命名文件"))
        self.action_view.setText(_translate("Form", "查看"))
        self.action_view.setToolTip(_translate("Form", "查看文件"))
        self.action_chstamp.setText(_translate("Form", "修改时间"))
        self.action_chstamp.setToolTip(_translate("Form", "修改文件时间"))
        self.action_delete.setText(_translate("Form", "删除"))
        self.action_delete.setToolTip(_translate("Form", "删除文件"))
        self.action_copy.setText(_translate("Form", "复制"))
        self.action_copy.setToolTip(_translate("Form", "复制文件"))
        self.action_paste.setText(_translate("Form", "粘贴"))
        self.action_paste.setToolTip(_translate("Form", "粘贴文件"))
        self.action_cut.setText(_translate("Form", "剪切"))
        self.action_cut.setToolTip(_translate("Form", "剪切文件"))

import mudao.resource_rc
