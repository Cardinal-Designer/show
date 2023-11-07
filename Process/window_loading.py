from .imports import *
from UI.Loading import Ui_Form as Loading_window

class wait(QtCore.QThread):
    # 创建了一个子线程，用来防止等待带来的界面卡死
    comm = pyqtSignal()
    def __init__(self):
        super().__init__()
    def run(self):
        time.sleep(5)
        # 等待5秒
        self.comm.emit()

class window_loading(QtWidgets.QMainWindow,Loading_window):
    def __init__(self):
        super().__init__()
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setupUi(self)
        self.waits = wait()
        self.waits.comm.connect(self.run)
        self.waits.start()
        # 执行QThread子线程，进行等待，等待结束后回调run(self)函数
    def run(self):
        pass
