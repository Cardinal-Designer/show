# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\Codes\独立项目\Cardinal\UI\About.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 450)
        MainWindow.setMinimumSize(QtCore.QSize(800, 450))
        MainWindow.setMaximumSize(QtCore.QSize(800, 450))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/Logo/Share/Logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 80, 241, 251))
        self.label.setStyleSheet("image: url(:/Logo/Share/Logo.png);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(260, 0, 481, 451))
        self.label_2.setObjectName("label_2")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "About"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:36pt; font-weight:600;\">Cardinal</span></p><p align=\"center\"><br/><a href=\" http://www.github.com\"><span style=\" text-decoration: underline; color:#0000ff;\">http://www.github.com</span></a></p><p align=\"center\"><br/></p><p align=\"center\"><br/></p><p align=\"center\"><br/></p><p align=\"center\"><br/></p><p align=\"center\"><br/></p></body></html>"))
import Share_rc
