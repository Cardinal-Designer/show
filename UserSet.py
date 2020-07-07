#-*- coding:utf-8 -*-
from DataUnCopy import Add,Space
from PySide2 import QtCore
from PySide2.QtCore import Signal
import Share_fun
class User(QtCore.QThread):
    ResetWindowFlag = Signal()

    def __init__(self):
        super().__init__()
        Add('CommonSet')
        Space['CommonSet'] = {
            "MoveWithPerson": True,
            "WindowStaysOnTopHint":True,
            "Tool":True, # 反向设置，如果要工具栏图标消失需要设置true
        }

        Add('WindowFlags')
        Space['WindowFlags'] = set()
        Space['WindowFlags'].add(int(QtCore.Qt.FramelessWindowHint))
        Share_fun.WindowStaysOnTopHint(Space['CommonSet']['WindowStaysOnTopHint'])
        Share_fun.Tool(Space['CommonSet']['Tool'])


