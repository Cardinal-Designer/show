#-*- coding:utf-8 -*-
from PySide2 import QtCore, QtWidgets
from PySide2.QtCore import Signal
from DataUnCopy import Space

class Special_Label(QtWidgets.QLabel):
    LeftButton_release = Signal(int, int)
    LeftButton_click = Signal(int, int)

    RightButton_Move = Signal(int, int)
    RightButton_release = Signal()
    RightButton_JustClick = Signal()

    RightMove = False
    RightOn = False

    def __init__(self, window):
        super().__init__(window)
        self.Now_x = None
        self.Now_y = None
        Space['Info']["Move"]["Click"] = {}
        Space['Info']["Move"]["Click"]["x"] = 0
        Space['Info']["Move"]["Click"]["y"] = 0

    def mousePressEvent(self, QMouseEvent):  ##重载一下鼠标点击事件
        if QMouseEvent.button() == QtCore.Qt.LeftButton:
            self.RightOn = False
            mE = QMouseEvent.windowPos()
            Mouse_info = Space['Info']["Move"]["Click"]
            Mouse_info["x"] = mE.x()
            Mouse_info["y"] = mE.y()

            self.LeftButton_click.emit(mE.x(), mE.y())
            # 获取左键时的相对窗口坐标
        if QMouseEvent.button() == QtCore.Qt.RightButton:
            self.Now_x = QMouseEvent.windowPos().x()
            self.Now_y = QMouseEvent.windowPos().y()
            self.RightOn = True

            # 获取右键时的相对窗口坐标

    def mouseReleaseEvent(self, QMouseEvent):
        if QMouseEvent.button() == QtCore.Qt.LeftButton:
            mE = QMouseEvent.windowPos()
            self.LeftButton_release.emit(mE.x(), mE.y())
            # 左键事件 [松开]
        if QMouseEvent.button() == QtCore.Qt.RightButton:

            if self.RightMove:

                self.RightMove = False
                self.RightButton_release.emit()
                # 右键移动且松开
            elif self.RightOn:
                self.RightOn = False

            # 右键事件 [松开]

    def mouseMoveEvent(self, QMouseEvent):
        self.RightMove = True
        if self.RightOn:
            globalPos = QMouseEvent.globalPos()
            self.RightButton_Move.emit(globalPos.x() - self.Now_x, globalPos.y() - self.Now_y)
            # 判断右键移动，将计算好的参数返回
