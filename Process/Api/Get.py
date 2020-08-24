from DataUnCopy import Add,Space

class Get():
    def Get_Play_complete(self,Action):
        """Action: 动画的名称 默认动画未被播放返回2"""
        # 0 正在播放
        # 1 播放完成
        # 2 从未播放过
        if Action in Space['Info']["Play_complete"]:
            return Space['Info']["Play_complete"][Action]
        else:
            return 2
