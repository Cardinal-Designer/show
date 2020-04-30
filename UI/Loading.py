# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\Codes\独立项目\Cardinal\UI\Loading.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setWindowModality(QtCore.Qt.NonModal)
        Form.resize(300, 300)
        Form.setMinimumSize(QtCore.QSize(300, 300))
        Form.setMaximumSize(QtCore.QSize(300, 300))
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(0, 0, 300, 300))
        self.label.setStyleSheet("image: url(:/Logo/Share/Cardinal.png);\n"
"background-color: rgb(0, 0, 0);")
        self.label.setText("")
        self.label.setObjectName("label")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Loading"))
import Share_rc
