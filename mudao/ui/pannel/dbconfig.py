# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dbconfig.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(472, 162)
        Dialog.setMinimumSize(QtCore.QSize(472, 162))
        Dialog.setMaximumSize(QtCore.QSize(472, 162))
        self.cbo_example = QtWidgets.QComboBox(Dialog)
        self.cbo_example.setGeometry(QtCore.QRect(10, 10, 451, 22))
        self.cbo_example.setObjectName("cbo_example")
        self.cbo_example.addItem("")
        self.edt_conf = QtWidgets.QLineEdit(Dialog)
        self.edt_conf.setGeometry(QtCore.QRect(10, 40, 451, 81))
        self.edt_conf.setObjectName("edt_conf")
        self.btn_submit = QtWidgets.QPushButton(Dialog)
        self.btn_submit.setGeometry(QtCore.QRect(390, 130, 71, 23))
        self.btn_submit.setObjectName("btn_submit")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "DBConfig"))
        self.cbo_example.setItemText(0, _translate("Dialog", "Example:"))
        self.btn_submit.setText(_translate("Dialog", "Submit"))

