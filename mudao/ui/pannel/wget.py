# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'wget.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setWindowModality(QtCore.Qt.NonModal)
        Dialog.resize(433, 114)
        Dialog.setMinimumSize(QtCore.QSize(433, 114))
        Dialog.setMaximumSize(QtCore.QSize(433, 114))
        self.edt_url = QtWidgets.QLineEdit(Dialog)
        self.edt_url.setGeometry(QtCore.QRect(50, 20, 361, 20))
        self.edt_url.setObjectName("edt_url")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 20, 31, 21))
        self.label.setObjectName("label")
        self.edt_path = QtWidgets.QLineEdit(Dialog)
        self.edt_path.setGeometry(QtCore.QRect(50, 50, 361, 20))
        self.edt_path.setObjectName("edt_path")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(20, 50, 31, 21))
        self.label_2.setObjectName("label_2")
        self.btn_wget = QtWidgets.QPushButton(Dialog)
        self.btn_wget.setGeometry(QtCore.QRect(340, 80, 61, 23))
        self.btn_wget.setObjectName("btn_wget")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "WGET FILE"))
        self.label.setText(_translate("Dialog", "URL :"))
        self.label_2.setText(_translate("Dialog", "SAVE:"))
        self.btn_wget.setText(_translate("Dialog", "WGET"))

