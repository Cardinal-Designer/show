# -*- coding:utf-8 -*-
from PySide2 import QtGui, QtWidgets
from DataUnCopy import Add,Space

class TrayIcon(QtWidgets.QSystemTrayIcon):
    def __init__(self, parent=None):
        super(TrayIcon, self).__init__(parent)

        self.popMenu = QtWidgets.QMenu()
        self.MenuActions = {}
        self.popMenu.show()
        self.popMenu.setVisible(False)

        self.activated.connect(self.Click)
        Space["CoreControl"].MsgPush.connect(self.MsgPush)

    def AddActions(self, name, job):
        self.MenuActions[name] = QtWidgets.QAction(name, self)
        self.MenuActions[name].triggered.connect(job)
        self.popMenu.addAction(self.MenuActions[name])

    def Click(self):
        self.popMenu.move(QtGui.QCursor.pos())
        self.popMenu.setVisible(True)
    def MsgPush(self,tip,msg):
        self.showMessage(tip, msg, self.icon())
