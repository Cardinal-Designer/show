# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\Codes\独立项目\Cardinal\UI\MainWindow.ui'
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
        self.centralwidget.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setStyleSheet("")
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 763, 1000))
        self.scrollAreaWidgetContents.setMinimumSize(QtCore.QSize(760, 1000))
        self.scrollAreaWidgetContents.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.scrollAreaWidgetContents.setStyleSheet("")
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.scrollArea, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 23))
        self.menubar.setObjectName("menubar")
        self.menuMenu = QtWidgets.QMenu(self.menubar)
        self.menuMenu.setTearOffEnabled(False)
        self.menuMenu.setObjectName("menuMenu")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.action_about = QtWidgets.QAction(MainWindow)
        self.action_about.setCheckable(False)
        self.action_about.setAutoRepeat(True)
        self.action_about.setVisible(True)
        self.action_about.setIconVisibleInMenu(True)
        self.action_about.setObjectName("action_about")
        self.action_play_selected = QtWidgets.QAction(MainWindow)
        self.action_play_selected.setObjectName("action_play_selected")
        self.action_play_all = QtWidgets.QAction(MainWindow)
        self.action_play_all.setObjectName("action_play_all")
        self.menuMenu.addAction(self.action_about)
        self.menu.addAction(self.action_play_selected)
        self.menu.addAction(self.action_play_all)
        self.menubar.addAction(self.menuMenu.menuAction())
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)
        self.action_about.triggered.connect(MainWindow.About_Window)
        self.action_play_selected.triggered.connect(MainWindow.Play_selected)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Cardinal"))
        self.menuMenu.setTitle(_translate("MainWindow", "属性"))
        self.menu.setTitle(_translate("MainWindow", "播放"))
        self.action_about.setText(_translate("MainWindow", "关于"))
        self.action_play_selected.setText(_translate("MainWindow", "播放所选"))
        self.action_play_all.setText(_translate("MainWindow", "播放所有"))
import Share_rc
