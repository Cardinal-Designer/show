from PyQt5 import QtCore
from PyQt5.QtCore import pyqtSignal
from Environment import dir_mix,path_read
import time

class PlayBoard(QtCore.QThread):
    # 创建了一个子线程，用来渲染动画
    play = pyqtSignal(str)

    def __init__(self, playActions, root, ususly_play):
        super().__init__()
        self.ususly_play = ususly_play
        self.playActions = playActions  # playActions传入所有动作
        self.root = root  # self.root是图包的路径

        self.Action = ususly_play
        self.stop = False
        self.child_path = ''
        self.Speeds = 1 # 播放倍速控制

        self.init()

    def init(self):

        playSet = self.playActions[self.Action]

        self.turns = playSet["turns"]

        self.child_path = path_read(playSet["path"])

    def run(self):
        def In_Play():

            First_time = time.time()
            wait = 1/self.turns["fps"]
            Picture = 0
            while (self.stop == False):
                Now_time = time.time()
                Picture = int((Now_time - First_time) / wait )+ self.turns["first"] # 利用当前经过的时间来确定当前帧
                if Picture > self.turns["last"]:
                    break
                name = self.turns["front"] + str(Picture) + self.turns["end"]  # 拼合图片名称
                self.play.emit(dir_mix(self.root, self.child_path, name))  # 发出图片显示指令
                time.sleep(wait)

            if self.stop == True:
                return 'Jump'
            else:
                return 'PlayOver'
            # 把跳出检查集中到下方可以避免出现因为图片过少导致的忽略跳出 bug出现：v0.0.0.2

        while True:
            if self.stop == True:
                self.init()
                self.stop = False
            Playwell = In_Play()  # 获取播放状态

            if self.Action != self.ususly_play and Playwell == 'PlayOver':
                # 在跳出播放后 Playwell的值是Jump ，故本语句不执行，再播放完成一次特殊动画后 Playwell的值是PlayOver，本语句执行
                # 执行本语句会恢复播放常态动画：ususly_play
                self.Action = self.ususly_play
                self.init()
