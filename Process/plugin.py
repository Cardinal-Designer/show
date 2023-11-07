# -*- coding:utf-8 -*-
from Environment import dir_mix, path_read
from DataUnCopy import Add, Space
from PySide2 import QtCore
from queue import Queue
from Process.All_Api import Api
import sys, time, random

En = ['z', 'y', 'x', 'w', 'v', 'u', 't', 's', 'r', 'q', 'p', 'o', 'n', 'm', 'l', 'k', 'j', 'i', 'h', 'g', 'f', 'e', 'd',
      'c', 'b', 'a', 'Z', 'Y', 'X', 'W', 'V', 'U', 'T', 'S', 'R', 'Q', 'P', 'O', 'N', 'M', 'L', 'K', 'J', 'I', 'H', 'G',
      'F', 'E', 'D', 'C', 'B', 'A']

Plugin_Runtime = None


def Importer():
    # print('Importer')
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
            Space["Plugin"][Action_name].Call(Imports[Action_name]['init'])
        except:
            pass

class Thread(QtCore.QThread):
    def __init__(self,function,kwargs):
        super().__init__()
        self.function = function
        self.kwargs = kwargs
    def run(self):
        self.function(**self.kwargs)

class Plugin(QtCore.QThread):

    def __init__(self, name):
        self.name = name
        super().__init__()
        self.queue = Queue()
        self.Key = True
        Space["CoreControl"].clean.connect(self.FullClean)

    def FullClean(self):
        self.Key = False
        # 下方代码功能为强制结束线程并清空对象
        del_RunList = []
        for i in self.RunList:
            self.RunList[i].terminate()
            del_RunList.append(i)

        for i in del_RunList:
            del self.RunList[i]

        del_Extra = []
        for j in self.Extra:
            self.Extra[j].terminate()
            del_Extra.append(j)

        for j in del_Extra:
            del self.Extra[j]

        self.terminate()

    def run(self):
        self.module = __import__(self.name)

        try:
            self.module.Api = Api()
        except:
            pass

        try:
            self.module.Space = Space
        except:
            pass

        self.RunList = {}  # 创建线程表，保证每一个函数的驱动都只能有一个线程（设置了非锁死不算）
        self.Extra = {}  # 创建多开线程，顺便随时垃圾回收

        def randomNew():
            Str = ''.join(random.sample(En, random.randint(1, 10)))
            while (Str in self.Extra):
                Str = ''.join(random.sample(En, random.randint(1, 10)))
            return Str


        def Clean():
            if len(self.Extra) == 0 or self.Key == False:
                return
            rubbish = []
            for i in self.Extra:  # 线程垃圾回收
                if not self.Extra[i].isRunning():
                    rubbish.append(i)
            for r in rubbish:
                del self.Extra[r]

        while (self.Key):

            if not self.queue.empty():
                Get = self.queue.get()
                if Get["Target"] not in self.RunList or not self.RunList[Get["Target"]].isRunning():
                    self.RunList[Get["Target"]] = Thread(function = getattr(self.module, Get["Target"]),kwargs=Get["kwargs"])
                    # 单函数单线程，如果设置多开，会在临时线程里面开启
                    self.RunList[Get["Target"]].start()
                else:
                    try:
                        if ((not Get["lock"]) and self.RunList[Get["Target"]].isRunning()):
                            Str = randomNew()
                            # 获取一个随机不重复的字符串作为临时多开线程的 key [key: str value: Thread_classb]
                            # 在需要全局释放资源的时候可以迅速定位并释放
                            self.Extra[Str] = Thread(function=getattr(self.module, Get["Target"]), kwargs=Get["kwargs"])
                            self.Extra[Str].start()
                    except:
                        pass
            time.sleep(0.2)
            Clean() # 每个时间单位执行一次垃圾清理

    def Call(self, agrv):
        self.queue.put(agrv)
