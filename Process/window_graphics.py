from .imports import *
from UI.graphics import Ui_Form as graphics_window
from Environment import path, dir_mix


class Special_Label(QtWidgets.QLabel):
    def __init__(self):
        super().__init__()

        def mousePressEvent(self, e):  ##重载一下鼠标点击事件
            print("you clicked the label")

        def mouseReleaseEvent(self, QMouseEvent):
            print('you have release the mouse')


class PlayBoard(QtCore.QThread):
    # 创建了一个子线程，用来渲染动画
    play = pyqtSignal(str)

    def __init__(self):
        super().__init__()

    def run(self):
        dirs = 'E:\\Codes\\独立项目\\Cardinal\\Data\\白金_站立_互动 - 语音\\resources\\R\\'
        while True:
            for i in range(1, 122):
                front = 'F ('
                end = ').png'
                name = front + str(i) + end
                print(name)
                print(dir_mix(dirs[:-1], name))
                time.sleep(1 / 64)
                self.play.emit(dir_mix(dirs[:-1], name))


class window_graphics(QtWidgets.QMainWindow, graphics_window):
    def __init__(self, config, root):
        super().__init__()
        self.config = config
        self.root = root
        # 保存传入的初始化数据
        with open(dir_mix(root,config['Script']),'r',encoding='utf-8') as f:
            print(json.loads(f.read()))
        self.setupUi(self)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)  # 去掉窗口标题栏和按钮
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)  # 设置窗口背景透明

        self.label = QtWidgets.QLabel(self)
        self.label.setObjectName("label")
        width = 711
        height = 496
        self.resize(width, height)

        self.label.setGeometry(0, 0, width, height)

    def show(self) -> None:
        super().show()
        self.PlayBoard = PlayBoard()
        self.PlayBoard.play.connect(self.graph)
        self.PlayBoard.start()

    def graph(self, paths):
        print(paths)
        pixmap = QtGui.QPixmap(paths).scaled(self.label.width(), self.label.height())
        self.label.setPixmap(pixmap)
