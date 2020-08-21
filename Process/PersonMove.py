from PySide2 import QtCore
from DataUnCopy import Space
import time
class Move(QtCore.QThread):
    def __init__(self):
        super().__init__()
        self.x_add = 0
        self.y_add = 0
        self.time_ = 0
        Space["CoreControl"].clean.connect(self.terminate)
        Space["CoreControl"].stopAllAction.connect(self.terminate)
    def run(self):
        Unit_add_x = self.x_add/self.time_
        Unit_add_y = self.y_add / self.time_
        Start = time.time()
        X = Space['Info']["Move"]["Window"]['PersonX']
        Y = Space['Info']["Move"]["Window"]['PersonY']
        Go_pass = 0.0
        while(Go_pass<=self.time_):
            Space['Info']["Move"]["Window"]['PersonX'] = X+Unit_add_x*Go_pass
            Space['Info']["Move"]["Window"]['PersonY'] = Y+Unit_add_y*Go_pass
            Space["CoreControl"].Move.emit()
            Go_pass = time.time() - Start
            time.sleep(0.01)

    def Move(self,Action):
        if self.isRunning():
            self.terminate()

        self.x_add = Action["x_add"]
        self.y_add = Action["y_add"]
        self.time_ = Action["time"]

        self.start()
