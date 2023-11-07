#-*- coding:utf-8 -*-
from DataUnCopy import Space
from PySide2 import QtCore

def WindowStaysOnTopHint(Choose=False):
    """ Choose: 是否选择使用Tool这个选项 """
    if Choose:
        Space['WindowFlags'].add(int(QtCore.Qt.WindowStaysOnTopHint))
    else:
        Space['WindowFlags'].remove(int(QtCore.Qt.WindowStaysOnTopHint))


def Tool(Choose=False):
    """ Choose: 是否选择使用Tool这个选项 """
    if Choose:
        Space['WindowFlags'].add(int(QtCore.Qt.Tool))
    else:
        Space['WindowFlags'].remove(int(QtCore.Qt.Tool))
