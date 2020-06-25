from DataUnCopy import Add,Space
from PyQt5 import QtCore
from PyQt5.QtCore import pyqtSignal
import Share_fun
class User(QtCore.QThread):
    ResetWindowFlag = pyqtSignal()

    def __init__(self):
        super().__init__()
        Add('WindowFlags')
        Space['WindowFlags'] = set()
        Space['WindowFlags'].add(int(QtCore.Qt.FramelessWindowHint))
        Share_fun.WindowStaysOnTopHint(True)
        Share_fun.Tool(True)


