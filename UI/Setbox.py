# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\Codes\独立项目\Cardinal\show\UI\Setbox.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Setbox(object):
    def setupUi(self, Setbox):
        Setbox.setObjectName("Setbox")
        Setbox.resize(800, 500)
        Setbox.setMinimumSize(QtCore.QSize(800, 500))
        Setbox.setMaximumSize(QtCore.QSize(800, 500))
        self.centralwidget = QtWidgets.QWidget(Setbox)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.tab)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox = QtWidgets.QGroupBox(self.tab)
        self.groupBox.setObjectName("groupBox")
        self.ImgSize_text = QtWidgets.QLabel(self.groupBox)
        self.ImgSize_text.setGeometry(QtCore.QRect(10, 20, 31, 21))
        self.ImgSize_text.setObjectName("ImgSize_text")
        self.ImgSize_control = QtWidgets.QSlider(self.groupBox)
        self.ImgSize_control.setGeometry(QtCore.QRect(40, 20, 191, 22))
        self.ImgSize_control.setMaximum(100)
        self.ImgSize_control.setPageStep(0)
        self.ImgSize_control.setProperty("value", 0)
        self.ImgSize_control.setSliderPosition(0)
        self.ImgSize_control.setOrientation(QtCore.Qt.Horizontal)
        self.ImgSize_control.setObjectName("ImgSize_control")
        self.ImgSize_text_percent = QtWidgets.QLabel(self.groupBox)
        self.ImgSize_text_percent.setGeometry(QtCore.QRect(240, 20, 31, 21))
        self.ImgSize_text_percent.setObjectName("ImgSize_text_percent")
        self.verticalLayout.addWidget(self.groupBox)
        self.groupBox_2 = QtWidgets.QGroupBox(self.tab)
        self.groupBox_2.setObjectName("groupBox_2")
        self.Name_show = QtWidgets.QLineEdit(self.groupBox_2)
        self.Name_show.setGeometry(QtCore.QRect(40, 20, 241, 20))
        self.Name_show.setObjectName("Name_show")
        self.Name_text = QtWidgets.QLabel(self.groupBox_2)
        self.Name_text.setGeometry(QtCore.QRect(10, 21, 31, 21))
        self.Name_text.setObjectName("Name_text")
        self.Introduction_text = QtWidgets.QLabel(self.groupBox_2)
        self.Introduction_text.setGeometry(QtCore.QRect(10, 50, 31, 21))
        self.Introduction_text.setObjectName("Introduction_text")
        self.Introduction_show = QtWidgets.QPlainTextEdit(self.groupBox_2)
        self.Introduction_show.setGeometry(QtCore.QRect(40, 50, 241, 91))
        self.Introduction_show.setPlainText("")
        self.Introduction_show.setPlaceholderText("")
        self.Introduction_show.setObjectName("Introduction_show")
        self.verticalLayout.addWidget(self.groupBox_2)
        self.tabWidget.addTab(self.tab, "")
        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)
        Setbox.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Setbox)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 23))
        self.menubar.setObjectName("menubar")
        Setbox.setMenuBar(self.menubar)

        self.retranslateUi(Setbox)
        self.tabWidget.setCurrentIndex(0)
        self.ImgSize_control.valueChanged['int'].connect(Setbox.ImgSize_control_valueChange)
        QtCore.QMetaObject.connectSlotsByName(Setbox)

    def retranslateUi(self, Setbox):
        _translate = QtCore.QCoreApplication.translate
        Setbox.setWindowTitle(_translate("Setbox", "MainWindow"))
        self.groupBox.setTitle(_translate("Setbox", "显示"))
        self.ImgSize_text.setText(_translate("Setbox", "缩放"))
        self.ImgSize_text_percent.setText(_translate("Setbox", "0"))
        self.groupBox_2.setTitle(_translate("Setbox", "基本参数"))
        self.Name_text.setText(_translate("Setbox", "名称"))
        self.Introduction_text.setText(_translate("Setbox", "介绍"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Setbox", "基本参数"))
