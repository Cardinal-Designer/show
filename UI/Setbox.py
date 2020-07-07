# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Setbox.ui'
##
## Created by: Qt User Interface Compiler version 5.15.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient)
from PySide2.QtWidgets import *


class Ui_Setbox(object):
    def setupUi(self, Setbox):
        if not Setbox.objectName():
            Setbox.setObjectName(u"Setbox")
        Setbox.resize(800, 500)
        Setbox.setMinimumSize(QSize(800, 500))
        Setbox.setMaximumSize(QSize(800, 500))
        self.centralwidget = QWidget(Setbox)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.verticalLayout = QVBoxLayout(self.tab)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.groupBox = QGroupBox(self.tab)
        self.groupBox.setObjectName(u"groupBox")
        self.ImgSize_text = QLabel(self.groupBox)
        self.ImgSize_text.setObjectName(u"ImgSize_text")
        self.ImgSize_text.setGeometry(QRect(10, 20, 31, 21))
        self.ImgSize_control = QSlider(self.groupBox)
        self.ImgSize_control.setObjectName(u"ImgSize_control")
        self.ImgSize_control.setGeometry(QRect(40, 20, 191, 22))
        self.ImgSize_control.setMaximum(100)
        self.ImgSize_control.setPageStep(0)
        self.ImgSize_control.setValue(0)
        self.ImgSize_control.setSliderPosition(0)
        self.ImgSize_control.setOrientation(Qt.Horizontal)
        self.ImgSize_text_percent = QLabel(self.groupBox)
        self.ImgSize_text_percent.setObjectName(u"ImgSize_text_percent")
        self.ImgSize_text_percent.setGeometry(QRect(240, 20, 31, 21))
        self.TopWindow_checkBox = QCheckBox(self.groupBox)
        self.TopWindow_checkBox.setObjectName(u"TopWindow_checkBox")
        self.TopWindow_checkBox.setGeometry(QRect(10, 50, 71, 16))
        self.TopWindow_checkBox.setChecked(True)
        self.WindowIconbox_checkBox = QCheckBox(self.groupBox)
        self.WindowIconbox_checkBox.setObjectName(u"WindowIconbox_checkBox")
        self.WindowIconbox_checkBox.setGeometry(QRect(90, 50, 121, 16))
        self.WindowIconbox_checkBox.setChecked(False)
        self.SetBox_Go_with_Person_checkBox = QCheckBox(self.groupBox)
        self.SetBox_Go_with_Person_checkBox.setObjectName(u"SetBox_Go_with_Person_checkBox")
        self.SetBox_Go_with_Person_checkBox.setGeometry(QRect(10, 80, 181, 16))
        self.SetBox_Go_with_Person_checkBox.setChecked(True)

        self.verticalLayout.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(self.tab)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.Name_show = QLineEdit(self.groupBox_2)
        self.Name_show.setObjectName(u"Name_show")
        self.Name_show.setGeometry(QRect(40, 20, 241, 20))
        self.Name_text = QLabel(self.groupBox_2)
        self.Name_text.setObjectName(u"Name_text")
        self.Name_text.setGeometry(QRect(10, 21, 31, 21))
        self.Introduction_text = QLabel(self.groupBox_2)
        self.Introduction_text.setObjectName(u"Introduction_text")
        self.Introduction_text.setGeometry(QRect(10, 50, 31, 21))
        self.Introduction_show = QPlainTextEdit(self.groupBox_2)
        self.Introduction_show.setObjectName(u"Introduction_show")
        self.Introduction_show.setGeometry(QRect(40, 50, 241, 91))

        self.verticalLayout.addWidget(self.groupBox_2)

        self.tabWidget.addTab(self.tab, "")

        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)

        Setbox.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(Setbox)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 23))
        Setbox.setMenuBar(self.menubar)

        self.retranslateUi(Setbox)
        self.ImgSize_control.valueChanged.connect(Setbox.ImgSize_control_valueChange)
        self.TopWindow_checkBox.toggled.connect(Setbox.TopWindow_checkBox_valueChange)
        self.WindowIconbox_checkBox.toggled.connect(Setbox.WindowIconbox_checkBox_valueChange)
        self.SetBox_Go_with_Person_checkBox.toggled.connect(Setbox.SetBox_Go_with_Person_checkBox_valueChange)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Setbox)
    # setupUi

    def retranslateUi(self, Setbox):
        Setbox.setWindowTitle(QCoreApplication.translate("Setbox", u"\u4eba\u7269\u8bbe\u7f6e", None))
        self.groupBox.setTitle(QCoreApplication.translate("Setbox", u"\u663e\u793a", None))
        self.ImgSize_text.setText(QCoreApplication.translate("Setbox", u"\u7f29\u653e", None))
        self.ImgSize_text_percent.setText(QCoreApplication.translate("Setbox", u"0", None))
        self.TopWindow_checkBox.setText(QCoreApplication.translate("Setbox", u"\u7a97\u53e3\u7f6e\u9876", None))
        self.WindowIconbox_checkBox.setText(QCoreApplication.translate("Setbox", u"\u663e\u793a\u56fe\u6807\u680f\u56fe\u6807", None))
        self.SetBox_Go_with_Person_checkBox.setText(QCoreApplication.translate("Setbox", u"\u8bbe\u7f6e\u9762\u677f\u4e0e\u4eba\u7269\u4f4d\u7f6e\u7ed1\u5b9a", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("Setbox", u"\u57fa\u672c\u53c2\u6570", None))
        self.Name_text.setText(QCoreApplication.translate("Setbox", u"\u540d\u79f0", None))
        self.Introduction_text.setText(QCoreApplication.translate("Setbox", u"\u4ecb\u7ecd", None))
        self.Introduction_show.setPlainText("")
        self.Introduction_show.setPlaceholderText("")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("Setbox", u"\u57fa\u672c\u53c2\u6570", None))
    # retranslateUi

