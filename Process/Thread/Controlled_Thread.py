from functools import wraps
from PySide2 import QtCore
import time,random

__En__ = ['z', 'y', 'x', 'w', 'v', 'u', 't', 's', 'r', 'q', 'p', 'o', 'n', 'm', 'l', 'k', 'j', 'i', 'h', 'g', 'f', 'e', 'd',
      'c', 'b', 'a', 'Z', 'Y', 'X', 'W', 'V', 'U', 'T', 'S', 'R', 'Q', 'P', 'O', 'N', 'M', 'L', 'K', 'J', 'I', 'H', 'G',
      'F', 'E', 'D', 'C', 'B', 'A']

class __Signal__():
    def __init__(self):
        self.slot = []

    def emit(self, *arg, **kw):
        for Func in self.slot:
            Func(*arg, **kw)

    def connect(self, func):
        self.slot.append(func)

__StopChildThread__ = __Signal__()
__StopAllThread__ = __Signal__()



class __Thread__(QtCore.QThread):
    def __init__(self,function,*args,**kwargs):
        super().__init__()
        self.function = function
        self.kwargs = kwargs
        self.args = args

    def run(self):
        self.function(*self.args,**self.kwargs)

class Reasonable_termination(QtCore.QThread):
    def __init__(self, key=False,AfterDeath = None):

        super().__init__()

        self.key = key # 线程上锁开关，True表示函数执行线程唯一，只允许唯一的一个函数线程执行

        self.Extra = {}  # 创建多开线程存储字典，顺便随时垃圾回收
        self.BeginId = self.randomNew()
        self.AfterDeath = AfterDeath # 获取死亡函数
        self.start()

        self.alive = False

        __StopChildThread__.connect(self.FullClean)

        if not self.AfterDeath == None:
            __StopChildThread__.connect(self.AfterFunc) # 死亡函数，用于结束线程时收尾

        __StopAllThread__.connect(self.FullClean)
        __StopAllThread__.connect(self.terminate)

    def AfterFunc(self):
        if self.alive:
            self.alive = False
            self.AfterDeath()

    def Get_id(self):
        if not self.key:
            self.BeginId = self.randomNew()
        return self.BeginId

    def terminate_child(self,i):
        try:
            self.Extra[i].terminate()
        except:
            pass

    def FullClean(self):
        for i in self.Extra:  # 回收
            self.terminate_child(i)
        self.Extra = {}

    def run(self):
        while(not self.key):
            time.sleep(1)
            try:
                rubbish = []
                for i in self.Extra:  # 线程垃圾回收
                    if not self.Extra[i].isRunning():
                        rubbish.append(i)
                for r in rubbish:
                    del self.Extra[r]
            except:
                pass

    def randomNew(self):
        Str = ''.join(random.sample(__En__, random.randint(1, 10)))
        while (Str in self.Extra):
            Str = ''.join(random.sample(__En__, random.randint(1, 10)))
        return Str

    def __call__(self, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                if self.key and self.Extra[self.Get_id()].isRunning():
                    return
            except:
                pass

            id = self.Get_id()
            # print(id)
            self.Extra[id] = __Thread__(function = func,*args, **kwargs)
            self.Extra[id].start()
            self.alive = True
            return self.Extra[id]
        # 调用包装器后返回特殊线程线程对象
        return wrapper

