# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'cmd.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Terminal(object):
    def setupUi(self, Terminal):
        Terminal.setObjectName("Terminal")
        Terminal.resize(1175, 660)
        self.verticalLayout = QtWidgets.QVBoxLayout(Terminal)
        self.verticalLayout.setObjectName("verticalLayout")
        self.edt_text = QtWidgets.QPlainTextEdit(Terminal)
        self.edt_text.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.edt_text.setMouseTracking(True)
        self.edt_text.setTabletTracking(True)
        self.edt_text.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.edt_text.setStyleSheet("font-size: 18px ;")
        self.edt_text.setObjectName("edt_text")
        self.verticalLayout.addWidget(self.edt_text)

        self.retranslateUi(Terminal)
        QtCore.QMetaObject.connectSlotsByName(Terminal)

    def retranslateUi(self, Terminal):
        _translate = QtCore.QCoreApplication.translate
        Terminal.setWindowTitle(_translate("Terminal", "CMD"))

