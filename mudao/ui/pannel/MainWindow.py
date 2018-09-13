# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(950, 600)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(950, 600))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setAutoFillBackground(True)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Triangular)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setTabBarAutoHide(False)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.tab)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.mainTable = QtWidgets.QTableWidget(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mainTable.sizePolicy().hasHeightForWidth())
        self.mainTable.setSizePolicy(sizePolicy)
        self.mainTable.setMinimumSize(QtCore.QSize(901, 501))
        self.mainTable.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.mainTable.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.mainTable.setObjectName("mainTable")
        self.mainTable.setColumnCount(4)
        self.mainTable.setRowCount(1)
        item = QtWidgets.QTableWidgetItem()
        self.mainTable.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.mainTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.mainTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.mainTable.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.mainTable.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.mainTable.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.mainTable.setItem(0, 1, item)
        self.mainTable.horizontalHeader().setCascadingSectionResizes(True)
        self.mainTable.horizontalHeader().setDefaultSectionSize(200)
        self.mainTable.horizontalHeader().setStretchLastSection(True)
        self.verticalLayout_2.addWidget(self.mainTable)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/test/ui/resources/img/process.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.tab, icon, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tabWidget.addTab(self.tab_2, "")
        self.verticalLayout.addWidget(self.tabWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar_file = QtWidgets.QToolBar(MainWindow)
        self.toolBar_file.setObjectName("toolBar_file")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar_file)
        self.toolBar_action = QtWidgets.QToolBar(MainWindow)
        self.toolBar_action.setObjectName("toolBar_action")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar_action)
        self.toolBar_about = QtWidgets.QToolBar(MainWindow)
        self.toolBar_about.setObjectName("toolBar_about")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar_about)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 950, 20))
        self.menubar.setObjectName("menubar")
        self.menu_file = QtWidgets.QMenu(self.menubar)
        self.menu_file.setObjectName("menu_file")
        self.menu_about = QtWidgets.QMenu(self.menubar)
        self.menu_about.setObjectName("menu_about")
        MainWindow.setMenuBar(self.menubar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.action_import = QtWidgets.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/test/ui/resources/img/import.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_import.setIcon(icon1)
        self.action_import.setObjectName("action_import")
        self.action_export = QtWidgets.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/test/ui/resources/img/export.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_export.setIcon(icon2)
        self.action_export.setObjectName("action_export")
        self.action_quit = QtWidgets.QAction(MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/test/ui/resources/img/power_exit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_quit.setIcon(icon3)
        self.action_quit.setObjectName("action_quit")
        self.action_file = QtWidgets.QAction(MainWindow)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/test/ui/resources/img/folder.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_file.setIcon(icon4)
        self.action_file.setObjectName("action_file")
        self.action_cmd = QtWidgets.QAction(MainWindow)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/test/ui/resources/img/terminal.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_cmd.setIcon(icon5)
        self.action_cmd.setObjectName("action_cmd")
        self.action_data = QtWidgets.QAction(MainWindow)
        self.action_data.setIcon(icon)
        self.action_data.setObjectName("action_data")
        self.action_about = QtWidgets.QAction(MainWindow)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/test/ui/resources/img/restart1.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_about.setIcon(icon6)
        self.action_about.setObjectName("action_about")
        self.action_add = QtWidgets.QAction(MainWindow)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/test/ui/resources/img/add.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_add.setIcon(icon7)
        self.action_add.setObjectName("action_add")
        self.action_edit = QtWidgets.QAction(MainWindow)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/test/ui/resources/img/edit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_edit.setIcon(icon8)
        self.action_edit.setObjectName("action_edit")
        self.action_del = QtWidgets.QAction(MainWindow)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(":/test/ui/resources/img/del.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_del.setIcon(icon9)
        self.action_del.setObjectName("action_del")
        self.toolBar_file.addAction(self.action_import)
        self.toolBar_file.addAction(self.action_export)
        self.toolBar_file.addAction(self.action_quit)
        self.toolBar_action.addAction(self.action_file)
        self.toolBar_action.addAction(self.action_cmd)
        self.toolBar_action.addAction(self.action_data)
        self.toolBar_about.addAction(self.action_about)
        self.menu_file.addAction(self.action_import)
        self.menu_file.addAction(self.action_export)
        self.menu_file.addSeparator()
        self.menu_file.addAction(self.action_quit)
        self.menu_about.addAction(self.action_about)
        self.menubar.addAction(self.menu_file.menuAction())
        self.menubar.addAction(self.menu_about.menuAction())
        self.toolBar.addAction(self.action_add)
        self.toolBar.addAction(self.action_edit)
        self.toolBar.addAction(self.action_del)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.mainTable.setSortingEnabled(True)
        item = self.mainTable.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "1"))
        item = self.mainTable.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "URL"))
        item = self.mainTable.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "IP"))
        item = self.mainTable.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "TIME"))
        item = self.mainTable.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "MARK"))
        __sortingEnabled = self.mainTable.isSortingEnabled()
        self.mainTable.setSortingEnabled(False)
        item = self.mainTable.item(0, 0)
        item.setText(_translate("MainWindow", "http://localhost/1.php"))
        self.mainTable.setSortingEnabled(__sortingEnabled)
        self.tabWidget.setTabToolTip(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Home"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Tab 2"))
        self.toolBar_file.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.toolBar_action.setWindowTitle(_translate("MainWindow", "toolBar_2"))
        self.toolBar_about.setWindowTitle(_translate("MainWindow", "toolBar_3"))
        self.menu_file.setTitle(_translate("MainWindow", "文件"))
        self.menu_about.setTitle(_translate("MainWindow", "关于"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.action_import.setText(_translate("MainWindow", "导入"))
        self.action_export.setText(_translate("MainWindow", "导出"))
        self.action_quit.setText(_translate("MainWindow", "退出"))
        self.action_file.setText(_translate("MainWindow", "文件管理"))
        self.action_file.setToolTip(_translate("MainWindow", "文件管理"))
        self.action_file.setShortcut(_translate("MainWindow", "Ctrl+Shift+F"))
        self.action_cmd.setText(_translate("MainWindow", "终端模拟"))
        self.action_cmd.setToolTip(_translate("MainWindow", "终端模拟"))
        self.action_cmd.setShortcut(_translate("MainWindow", "Ctrl+Shift+C"))
        self.action_data.setText(_translate("MainWindow", "数据库管理"))
        self.action_data.setToolTip(_translate("MainWindow", "数据库管理"))
        self.action_data.setShortcut(_translate("MainWindow", "Ctrl+Shift+D"))
        self.action_about.setText(_translate("MainWindow", " About"))
        self.action_about.setToolTip(_translate("MainWindow", "关于"))
        self.action_add.setText(_translate("MainWindow", "添加"))
        self.action_add.setToolTip(_translate("MainWindow", "添加Shell"))
        self.action_add.setShortcut(_translate("MainWindow", "Ctrl+Shift+A"))
        self.action_edit.setText(_translate("MainWindow", "编辑"))
        self.action_edit.setToolTip(_translate("MainWindow", "编辑Shell"))
        self.action_edit.setShortcut(_translate("MainWindow", "Ctrl+Shift+E"))
        self.action_del.setText(_translate("MainWindow", "删除"))
        self.action_del.setToolTip(_translate("MainWindow", "删除Shell"))
        self.action_del.setShortcut(_translate("MainWindow", "Ctrl+Shift+R"))

import resource_rc