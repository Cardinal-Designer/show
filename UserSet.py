#-*- coding:utf-8 -*-
from DataUnCopy import Add,Space
from PySide2 import QtCore
from PySide2.QtCore import Signal
from Process import Special_Control
class User(QtCore.QObject):
    ResetWindowFlag = Signal()

    def __init__(self):
        super().__init__()
        Add('CommonSet')
        Space['CommonSet'] = {
            "Change":None,
            "MoveWithPerson": True,
            "WindowStaysOnTopHint":True,
            "Tool":True, # 反向设置，如果要工具栏图标消失需要设置true
            "Skip_frame":1,
            "mirrored":False,
            "Cache":False
        }

        Add('WindowFlags')
        Space['WindowFlags'] = set()
        Space['WindowFlags'].add(int(QtCore.Qt.FramelessWindowHint))
        Special_Control.WindowStaysOnTopHint(Space['CommonSet']['WindowStaysOnTopHint'])
        Special_Control.Tool(Space['CommonSet']['Tool'])



