# -*- coding:utf-8 -*-
from DataUnCopy import Space
from PySide2 import QtCore
from PySide2.QtCore import Signal

def WindowStaysOnTopHint(Choose=False):
    """ Choose: 是否选择使用Tool这个选项 """
    try:
        if Choose:
            Space['WindowFlags'].add(int(QtCore.Qt.WindowStaysOnTopHint))
        else:
            Space['WindowFlags'].remove(int(QtCore.Qt.WindowStaysOnTopHint))
    except:
        pass


def Tool(Choose=False):
    """ Choose: 是否选择使用Tool这个选项 """
    try:
        if Choose:
            Space['WindowFlags'].add(int(QtCore.Qt.Tool))
        else:
            Space['WindowFlags'].remove(int(QtCore.Qt.Tool))
    except:
        pass

class CoreControl(QtCore.QObject):
    # 通过全局实例化提供全局的播放控制接口
    play = Signal(str)
    sound = Signal(str)
    ChangeSize = Signal()
    MsgPush = Signal(str,str)
    Move = Signal()
    clean = Signal()
    stopAllAction = Signal()
