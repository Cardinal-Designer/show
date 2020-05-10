from PyQt5 import QtCore
from PyQt5.QtCore import pyqtSignal


class Find(QtCore.QThread):
    play = pyqtSignal(str)

    def __init__(self, Script):
        super().__init__()
        self.Script = Script
        self.OnClick = None

    def ClickCheck(self, types):
        try:
            self.OnClick = self.Script["OnClick"]
            LeftWhat = self.OnClick[types]
            if LeftWhat[0] == False:
                return False
        except:
            return False
        return True
        # 检查当前鼠标事件是否在Script中存在

    def LeftClick(self, x, y, Change):
        if self.ClickCheck("LeftClick"):
            for Actions in self.OnClick["LeftClick"][1:]:
                self.Action_run(x=x,y=y,Change=Change,Action=Actions)

    def LeftRelease(self, x, y, Change):
        if self.ClickCheck("LeftRelease"):
            print(22222)

    def Action_run(self,Action,x,y,Change):
        if Action["From"] == "play":
            locate = Action["locate"]
            if locate[0] == True:
                if (x >= locate[1]*Change and x <= locate[2]*Change and y >= locate[3]*Change and y <= locate[4]*Change)!= True:
                    return 'Your mouse is not in place'
            self.play.emit(Action["Action"])



    def Find(self, Action):
        try:
            self.ActionGroup = self.Script["ActionGroup"]
            if Action in self.ActionGroup:  # 检查动作是否在动作组
                Actions = self.ActionGroup[Action]
                for From in Actions:  # 遍历动作组，获得相应定义的动作 类
                    if From == 'play':
                        for runs in Actions[From]:  # 遍历动作 类 ，获得类中动作
                            print('PlayAction', runs)
                            self.play.emit(runs)

                return True

        except:
            if Action in self.Script["play"]:  # 检查动作是否在play组
                self.play.emit(Action)
