from Process.Api.Get import Get
import time

class Special():
    def __init__(self):
        self.Get = Get()
    def Play_wait(self,Action,key = False):
        if key:
            while(self.Get.Get_Play_complete(Action) == 1):
                time.sleep(0.05)

