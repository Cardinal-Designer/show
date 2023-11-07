#-*- coding:utf-8 -*-
from UI.Setbox import Ui_Setbox
from PySide2 import QtGui, QtWidgets
from PySide2.QtCore import Signal
from DataUnCopy import Space
import Share_fun


class Setbox(QtWidgets.QMainWindow, Ui_Setbox):
    ChangeSize = Signal()
    MovePeson = Signal()
    ResetWindowFlag = Signal(bool)

    def __init__(self, parent=None):
        super(Setbox, self).__init__(parent)
        self.setupUi(self)
        self.init()

        self.Name_show.setText(Space['config']['Name'])
        self.Introduction_show.setPlainText(Space['config']['Description'])

        Setting = Space['Script']['Setting']
        self.ImgSize_text_percent.setText(str(Setting['Change']))
        self.ImgSize_control.setValue(Setting['Change'] * 20)
    def init(self):
        # 界面初始化 =========================================================
        CommonSet = Space['CommonSet']
        self.MoveWithPerson = CommonSet['MoveWithPerson']
        self.SetBox_Go_with_Person_checkBox.setChecked(CommonSet['MoveWithPerson'])
        self.TopWindow_checkBox.setChecked(CommonSet['WindowStaysOnTopHint'])
        self.WindowIconbox_checkBox.setChecked(not CommonSet['Tool'])

    def show(self):
        super().show()
        self.move(Space['PersonX'] - 800, Space['PersonY'])
        print(Space['PersonX'] - 800, Space['PersonY'])

    def moveEvent(self, Get: QtGui.QMouseEvent) -> None:
        if not self.isVisible():
            return
        # 窗口show()的时候会触发moveEvent，这一句判断是否已经show(),如果没有，则表明不是鼠标拖动触发，此时不改变PersonX/Y
        Space['PersonX'] = self.pos().x() + 800
        Space['PersonY'] = self.pos().y()
        # PersonX/Y 更新策略是人物拖动时更新，如果不用这种实现方法，就要为了同步数据而进行二次更新，降低效率

        if self.MoveWithPerson:
            self.MovePeson.emit() # 控制是否为

    def ImgSize_control_valueChange(self):
        # Change 的值从0 - 5
        Change = self.ImgSize_control.value() / 20
        self.ImgSize_text_percent.setText(str(Change))
        Space['Change'] = Change
        self.ChangeSize.emit()

    def TopWindow_checkBox_valueChange(self):
        Share_fun.WindowStaysOnTopHint(self.TopWindow_checkBox.isChecked())

        self.ResetWindowFlag.emit(False)

    def WindowIconbox_checkBox_valueChange(self):
        Share_fun.Tool(not self.WindowIconbox_checkBox.isChecked())

        self.ResetWindowFlag.emit(False)

    def SetBox_Go_with_Person_checkBox_valueChange(self):
        if self.SetBox_Go_with_Person_checkBox.isChecked():
            self.MoveWithPerson = True
        else:
            self.MoveWithPerson = False
