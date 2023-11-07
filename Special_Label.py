from PyQt5 import QtCore,QtWidgets
from PyQt5.QtCore import pyqtSignal

class Special_Label(QtWidgets.QLabel):
    LeftButton_release = pyqtSignal(int, int)
    LeftButton_click = pyqtSignal(int, int)

    RightButton_Move = pyqtSignal(int, int)
    RightButton_release = pyqtSignal()
    RightButton_JustClick = pyqtSignal()

    RightMove = False
    RightOn = False
    def __init__(self,window):
        super().__init__(window)


    def mousePressEvent(self, QMouseEvent):  ##重载一下鼠标点击事件
        if QMouseEvent.button() == QtCore.Qt.LeftButton:
            self.RightOn = False
            mE = QMouseEvent.windowPos()
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

            if self.RightMove == True:

                self.RightMove = False
                self.RightButton_release.emit()
                # 右键移动且松开
            elif self.RightOn == True:
                self.RightOn = False

            # 右键事件 [松开]

    def mouseMoveEvent(self, QMouseEvent):
        self.RightMove = True
        if self.RightOn == True:
            globalPos = QMouseEvent.globalPos()
            self.RightButton_Move.emit(globalPos.x() - self.Now_x, globalPos.y() - self.Now_y)
            # 判断右键移动，将计算好的参数返回
