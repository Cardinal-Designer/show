from PyQt5 import QtCore
from PyQt5.QtCore import pyqtSignal
from DataUnCopy import Space

class Find(QtCore.QThread):
    play = pyqtSignal(str)
    soundPlay = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self.OnClick = None

    def ClickCheck(self, types):
        try:
            self.OnClick = Space["Script"]["OnClick"]
            LeftWhat = self.OnClick[types]
            if not LeftWhat[0]:
                return False
        except:
            return False
        return True
        # 检查当前鼠标事件是否在Script中存在

    def LeftClick(self, x, y, Change):
        if self.ClickCheck("LeftClick"):
            for Actions in self.OnClick["LeftClick"][1:]:
                self.Action_run(x=x, y=y, Change=Change, Action=Actions)

    def LeftRelease(self, x, y, Change):
        if self.ClickCheck("LeftRelease"):
            for Actions in self.OnClick["LeftRelease"][1:]:
                self.Action_run(x=x, y=y, Change=Change, Action=Actions)

    def Action_run(self, Action, x, y, Change):
        if Action["From"] == "play":
            locate = Action["locate"]
            if locate[0]:
                locate_tmp = []
                for i in locate[1:]:
                    locate_tmp.append(i*Change)
                if not (locate_tmp[0] <= x <= locate_tmp[1] and locate_tmp[2] <= y <= locate_tmp[3]):
                    return 'Your mouse is not in place [play]'
            self.play.emit(Action["Action"])

        elif Action["From"] == "sound":
            locate = Action["locate"]
            if locate[0]:
                locate_tmp = []
                for i in locate[1:]:
                    locate_tmp.append(i * Change)
                if not (locate_tmp[0] <= x <= locate_tmp[1] and locate_tmp[2] <= y <= locate_tmp[3]):
                    return 'Your mouse is not in place [sound]'
            self.soundPlay.emit(Action["Action"])
