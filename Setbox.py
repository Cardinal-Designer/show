# -*- coding:utf-8 -*-
from UI.Setbox import Ui_Setbox
from PySide2 import QtGui, QtWidgets
from PySide2.QtCore import Signal
from DataUnCopy import Space
from Process import Special_Control
from Debug.Debug_Animation import Debug_Animation

class Setbox(QtWidgets.QMainWindow, Ui_Setbox,Debug_Animation):
    MovePeson = Signal()
    ResetWindowFlag = Signal(bool)

    def ReSetFont(self,PixelSize):
        font = QtGui.QFont()
        font.setPixelSize(PixelSize)
        # Key = ["Widget", "checkBox"]
        for i in self.__dict__:
            # for key in Key:
            #     if key in i:
            try:
                getattr(self, i).setFont(font)
            except:
                pass
        self.setFont(font)

    def __init__(self, parent=None):
        super(Setbox, self).__init__(parent)
        self.setupUi(self)

        self.ReSetFont(12)
        # 界面初始化 =========================================================

        self.Name_show.setText(Space['config']['Name'])
        self.Introduction_show.setPlainText(Space['config']['Description'])

        self.SyncChange()

    def SyncChange(self):
        # 同步CommonSet

        self.SetBox_Go_with_Person_checkBox.setChecked(Space['CommonSet']['MoveWithPerson']) # 设置是否与人物一同移动
        self.TopWindow_checkBox.setChecked(Space['CommonSet']['WindowStaysOnTopHint']) # 设置人物是否置顶
        self.WindowIconbox_checkBox.setChecked(not Space['CommonSet']['Tool']) # 设置是否显示应用栏图标
        self.MoveWithPerson = Space['CommonSet']['MoveWithPerson']

        if Space['CommonSet']["Change"] == None:
            Change = Space['Script']['Setting']['Change']
        else:
            Change = Space['CommonSet']["Change"]
        self.ImgSize_text_percent.setText(str(Change))
        self.ImgSize_control.setValue(Change * 20)
        # 人物缩放系数

        self.Animation_Cache_checkBox.setChecked(Space["CommonSet"]["Cache"]) # 图像缓存的checkBox

        self.Skip_frame_lineEdit.setText(str(Space["CommonSet"]["Skip_frame"])) # 动画跳帧的lineEdit

        self.Animation_Mirror_checkBox.setChecked(Space["CommonSet"]["mirrored"]) # 人物镜像的checkBox

    def show(self):
        super().show()
        self.move(Space['Info']["Move"]["Window"]['PersonX'] - 800, Space['Info']["Move"]["Window"]['PersonY'])
        # print(Space['Info']["Move"]["Window"]['PersonX'] - 800, Space['Info']["Move"]["Window"]['PersonY'])

    def moveEvent(self, Get: QtGui.QMouseEvent) -> None:
        if not self.isVisible():
            return
        # 窗口show()的时候会触发moveEvent，这一句判断是否已经show(),如果没有，则表明不是鼠标拖动触发，此时不改变PersonX/Y

        if self.MoveWithPerson:
            Space["CoreControl"].stopAllAction.emit()

            Space['Info']["Move"]["Window"]['PersonX'] = self.pos().x() + 800
            Space['Info']["Move"]["Window"]['PersonY'] = self.pos().y()
            # PersonX/Y 更新策略是人物拖动时更新，如果不用这种实现方法，就要为了同步数据而进行二次更新，降低效率

            self.MovePeson.emit()  # 控制是否为

    def ImgSize_control_valueChange(self):
        # Change 的值从0 - 5
        Change = self.ImgSize_control.value() / 20
        self.ImgSize_text_percent.setText(str(Change))
        Space['Change'] = Change
        Space['CommonSet']["Change"] = Change
        Space["CoreControl"].ChangeSize.emit()

    def TopWindow_checkBox_valueChange(self):
        Special_Control.WindowStaysOnTopHint(self.TopWindow_checkBox.isChecked())

        self.ResetWindowFlag.emit(False)

    def WindowIconbox_checkBox_valueChange(self):
        Special_Control.Tool(not self.WindowIconbox_checkBox.isChecked())

        self.ResetWindowFlag.emit(False)

    def SetBox_Go_with_Person_checkBox_valueChange(self):
        if self.SetBox_Go_with_Person_checkBox.isChecked():
            self.MoveWithPerson = True
        else:
            self.MoveWithPerson = False

    def Change_Skip_frame(self):
        try:
            Skip = int(self.Skip_frame_lineEdit.text())
            Space["CommonSet"]['Skip_frame'] = Skip
        except:
            pass

    def Mirror_Image(self):
        Space["CommonSet"]['mirrored'] = self.Animation_Mirror_checkBox.isChecked()

    def Skip_frame_GetBestConfig(self):
        usualy_play = Space["Script"]["Setting"]["usualy_play"]
        fps = Space["Script"]["play"][usualy_play]["turns"]["fps"]
        # 默认使用usualy_play动画fps作为全局fps
        suitable = int(fps/24)
        self.Skip_frame_lineEdit.setText(str(suitable)) # 会触发Change_Skip_frame

    def Cache_Image(self):
        Space["CommonSet"]["Cache"] = self.Animation_Cache_checkBox.isChecked()
