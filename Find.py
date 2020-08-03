#-*- coding:utf-8 -*-
from PySide2 import QtCore
from DataUnCopy import Space

class Find(QtCore.QObject):
    def __init__(self):
        super().__init__()
        self.OnClick = None

        self.Image_Width = Space["Script"]["Setting"]["ImageSize"][0]

        self.control_api = {
        'play': Space["CoreControl"].play.emit,
        'sound': Space["CoreControl"].sound.emit,
        'PushMsg':self.PushMsg,
        'ActionGroup':self.ActionGroup
    }

    def ActionGroup(self,Action):
        Actions = Space["Script"]["ActionGroup"][Action]
        for Order in Actions:
            if(Order["From"] == "ActionGroup" and Order["Action"] == Action):
                continue
                # 防止有人嵌套ActionGroup同名Action,使程序进入死循环,
            self.control_api[Order["From"]](Order["Action"])

    def PushMsg(self,Action):
        try:
            Title = Action["Title"]
        except:
            Title = ''
        try:
            Msg = Action["Msg"]
        except:
            Msg = ''
        Space["CoreControl"].MsgPush.emit(Title,Msg)


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
        Centre_Image_Width = self.Image_Width/2

        locate = Action["locate"]

        if locate[0]:
            locate_tmp = []
            for i in locate[1:]:
                locate_tmp.append(i*Change)

            left = locate_tmp[0]
            right = locate_tmp[1]

            if(Space['CommonSet']["mirrored"]):
                left = 2*Centre_Image_Width*Change - locate_tmp[1] # 左x坐标
                right = 2*Centre_Image_Width*Change - locate_tmp[0] # 右x坐标
            # print(left,right) # 输出左、右限制的x坐标
            if not (left <= x <= right and locate_tmp[2] <= y <= locate_tmp[3]):
                return 'Your mouse is not in place [play]'
        self.control_api[Action["From"]](Action["Action"])
