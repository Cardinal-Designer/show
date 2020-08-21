# -*- coding:utf-8 -*-
from PySide2 import QtCore
from PySide2.QtCore import Signal
from Environment import dir_mix, path_read
from DataUnCopy import Space

import time


class PlayBoard(QtCore.QThread):
    # 创建了一个子线程，用来渲染动画
    play = Signal(str)

    def __init__(self):
        super().__init__()
        self.playActions = Space["Script"]["play"]  # playActions传入所有动作
        try:
            self.Action = Space["Script"]["Setting"]["Start_play"]
        except:
            self.Action = Space["Script"]["Setting"]["usualy_play"]  # 第一次播放的一定是常动作 / 或起始动画
        self.stop = False
        self.child_path = ''

        self.turns = None

        self.init()

    def init(self):

        playSet = self.playActions[self.Action]

        self.turns = playSet["turns"]

        self.child_path = path_read(playSet["path"])

    def run(self):
        def In_Play():

            First_time = time.time()
            wait = 1 / self.turns["fps"]

            while not self.stop:
                Now_time = time.time()
                Picture = int((Now_time - First_time) / wait) + self.turns["first"]  # 利用当前经过的时间来确定当前帧
                if Picture > self.turns["last"]:
                    break
                name = self.turns["front"] + str(Picture) + self.turns["end"]  # 拼合图片名称
                self.play.emit(dir_mix(Space['root'], self.child_path, name))  # 发出图片显示指令
                time.sleep(wait * Space["CommonSet"]['Skip_frame'])

            if self.stop:
                return 'Jump'
            else:
                return 'PlayOver'
            # 把跳出检查集中到下方可以避免出现因为图片过少导致的忽略跳出 bug出现：v0.0.0.2

        while True:

            if self.stop:
                self.init()
                self.stop = False

            Space['Info']["Play_complete"][self.Action] = 0

            Playwell = In_Play()  # 获取播放状态

            Space['Info']["Play_complete"][self.Action] = 1

            if self.Action != Space["Script"]["Setting"]["usualy_play"] and Playwell == 'PlayOver':
                # 在跳出播放后 Playwell的值是Jump ，故本语句不执行，再播放完成一次特殊动画后 Playwell的值是PlayOver，本语句执行
                # 执行本语句会恢复播放常态动画：ususly_play
                self.Action = Space["Script"]["Setting"]["usualy_play"]
                self.init()
