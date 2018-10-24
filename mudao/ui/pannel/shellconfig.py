# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'shellconfig.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(491, 119)
        Dialog.setMinimumSize(QtCore.QSize(491, 119))
        Dialog.setMaximumSize(QtCore.QSize(491, 119))
        self.cbo_category = QtWidgets.QComboBox(Dialog)
        self.cbo_category.setGeometry(QtCore.QRect(60, 80, 111, 22))
        self.cbo_category.setObjectName("cbo_category")
        self.cbo_category.addItem("")
        self.cbo_category.addItem("")
        self.cbo_category.addItem("")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 20, 41, 21))
        self.label.setObjectName("label")
        self.cbo_encoding = QtWidgets.QComboBox(Dialog)
        self.cbo_encoding.setGeometry(QtCore.QRect(290, 80, 101, 22))
        self.cbo_encoding.setObjectName("cbo_encoding")
        self.cbo_encoding.addItem("")
        self.cbo_encoding.addItem("")
        self.cbo_encoding.addItem("")
        self.cbo_encoding.addItem("")
        self.cbo_encoding.addItem("")
        self.cbo_encoding.addItem("")
        self.url = QtWidgets.QLineEdit(Dialog)
        self.url.setGeometry(QtCore.QRect(60, 20, 291, 21))
        self.url.setObjectName("url")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(360, 20, 41, 21))
        self.label_2.setObjectName("label_2")
        self.btnAdd = QtWidgets.QPushButton(Dialog)
        self.btnAdd.setGeometry(QtCore.QRect(400, 80, 61, 23))
        self.btnAdd.setObjectName("btnAdd")
        self.pwd = QtWidgets.QLineEdit(Dialog)
        self.pwd.setGeometry(QtCore.QRect(400, 20, 61, 21))
        self.pwd.setObjectName("pwd")
        self.cbo_shelltype = QtWidgets.QComboBox(Dialog)
        self.cbo_shelltype.setGeometry(QtCore.QRect(180, 80, 101, 22))
        self.cbo_shelltype.setObjectName("cbo_shelltype")
        self.cbo_shelltype.addItem("")
        self.cbo_shelltype.addItem("")
        self.cbo_shelltype.addItem("")
        self.cbo_shelltype.addItem("")
        self.cbo_shelltype.addItem("")
        self.edt_tag = QtWidgets.QLineEdit(Dialog)
        self.edt_tag.setGeometry(QtCore.QRect(60, 50, 401, 20))
        self.edt_tag.setObjectName("edt_tag")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(20, 50, 31, 21))
        self.label_4.setObjectName("label_4")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "ShellConfig"))
        self.cbo_category.setItemText(0, _translate("Dialog", "SiteGroup"))
        self.cbo_category.setItemText(1, _translate("Dialog", "default"))
        self.cbo_category.setItemText(2, _translate("Dialog", "group1"))
        self.label.setText(_translate("Dialog", "Url："))
        self.cbo_encoding.setItemText(0, _translate("Dialog", "Encoding"))
        self.cbo_encoding.setItemText(1, _translate("Dialog", "UTF-8"))
        self.cbo_encoding.setItemText(2, _translate("Dialog", "GBK"))
        self.cbo_encoding.setItemText(3, _translate("Dialog", "Euc-KR"))
        self.cbo_encoding.setItemText(4, _translate("Dialog", "Euc-JP"))
        self.cbo_encoding.setItemText(5, _translate("Dialog", "ISO-8859-1"))
        self.label_2.setText(_translate("Dialog", "Pass："))
        self.btnAdd.setText(_translate("Dialog", "ADD"))
        self.cbo_shelltype.setItemText(0, _translate("Dialog", "ShellType"))
        self.cbo_shelltype.setItemText(1, _translate("Dialog", "ASP"))
        self.cbo_shelltype.setItemText(2, _translate("Dialog", "ASPX"))
        self.cbo_shelltype.setItemText(3, _translate("Dialog", "PHP"))
        self.cbo_shelltype.setItemText(4, _translate("Dialog", "Custom"))
        self.label_4.setText(_translate("Dialog", "Tag："))

