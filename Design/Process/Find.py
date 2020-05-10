from .imports import *
class Find(QtCore.QThread):
    play = pyqtSignal(str)

    def __init__(self, Script):
        super().__init__()
        self.Script = Script
        self.ActionGroup = None

    def Find(self,Action):
        try:
            self.ActionGroup = self.Script["ActionGroup"]
            if Action in self.ActionGroup: # 检查动作是否在动作组
                Actions = self.ActionGroup[Action]
                for From in Actions: # 遍历动作组，获得相应定义的动作 类
                    if From == 'play':
                        for runs in Actions[From]: # 遍历动作 类 ，获得类中动作
                            print('PlayAction',runs)
                            self.play.emit(runs)

                return True

        except:
            if Action in self.Script["play"]:  # 检查动作是否在play组
                self.play.emit(Action)


