# -*- coding:utf-8 -*-
from Environment import dir_mix, path_read
from DataUnCopy import Add, Space
from PySide2 import QtCore
from queue import Queue
import sys, time
# 导入来自插件组件的特殊穿透控制信号
from Process.Thread.Controlled_Thread import __StopChildThread__, __StopAllThread__


def Importer():
    try:
        Imports = Space["Script"]["Import"]
        Add("Plugin")
        Space["Plugin"] = {}
    except:
        return
    for Action_name in Imports:
        Path = dir_mix(Space["root"], path_read(Imports[Action_name]["WorkPath"]))
        if Path not in sys.path:
            sys.path.append(Path)
            # 引入模块路径
        Space["Plugin"][Action_name] = Plugin(Imports[Action_name]["module_name"])
        Space["Plugin"][Action_name].start()
        try:
            Space["Plugin"][Action_name].Call(Imports[Action_name]['init']) # Plugin类提供的函数执行方法
        except:
            pass


class Plugin(QtCore.QThread):

    def __init__(self, name):
        self.name = name
        super().__init__()
        self.queue = Queue()
        self.Key = True

        Space["CoreControl"].clean.connect(self.terminate)
        Space["CoreControl"].clean.connect(__StopAllThread__.emit)
        Space["CoreControl"].stopAllAction.connect(__StopChildThread__.emit)

    def run(self):
        self.module = __import__(self.name)

        while (self.Key):

            if not self.queue.empty():
                Get = self.queue.get()
                Tmp = self.module
                for i in Get["Target"]:
                    Tmp = getattr(Tmp, i)
                Tmp(**Get["kwargs"])

            time.sleep(0.2)

    def Call(self, agrv):
        self.queue.put(agrv)
