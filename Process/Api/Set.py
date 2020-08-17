from DataUnCopy import Add,Space
from Process.Api.Special import Special
class Set():
    def __init__(self):
        self.Special = Special()
    def Set_Ususlly_play(self,Action=str):
        """Action: 动画的名称 [立即设置，播放需等待到下个周期]"""
        Space["Script"]["Setting"]["usualy_play"] = Action

    def Set_Ususlly_play_mix(self,Action=str,wait=False):
        """Action: 动画的名称 | wait: 播放动作是否阻塞(阻塞时长等于动作时长)[播放后立即设置]"""
        Space["CoreControl"].play.emit(Action)
        Space["Script"]["Setting"]["usualy_play"] = Action
        self.Special.Play_wait(Action, wait)

    def Set_play(self,Action,wait = False):
        """Action: 动画的名称 | wait: 播放动作是否阻塞(阻塞时长等于动作时长) [立即播放]"""
        Space["CoreControl"].play.emit(Action)
        self.Special.Play_wait(Action,wait)

    def Set_position(self,x,y):
        """x: x坐标 | x: y坐标 [立即执行移动]"""
        Space['Info']["Move"]["Window"]['PersonX'] = x
        Space['Info']["Move"]["Window"]['PersonY'] = y
        Space["CoreControl"].Move.emit()
