from DataUnCopy import Add,Space
import time,traceback
class Do():
    def Do_PersonMove(self,x_add,y_add,time_Move = 0,wait = False):
        """x_add: x轴变化量 | y_add: y轴变化量 | time: 完成变化需要的时间 | wait: 播放动作是否阻塞 [播放后立即设置]"""
        Space['Control_Api']["Move"].Move({'x_add': x_add, 'y_add': y_add, 'time': time_Move})
        if wait:
            time.sleep(time_Move)
    def Do_mirror(self,key):
        Space['CommonSet']["mirrored"] = key

