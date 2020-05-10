from .imports import *
from UI.graphics import Ui_Form as graphics_window
from Environment import path, dir_mix, next_
from .Find import Find


class Special_Label(QtWidgets.QLabel):
    LeftButton_release = pyqtSignal(int, int)
    RightButton_Move = pyqtSignal(int, int)
    RightButton_release = pyqtSignal()
    RightButton_JustClick = pyqtSignal()
    RightMove = False
    RightOn = False


    def mousePressEvent(self, QMouseEvent):  ##重载一下鼠标点击事件
        if QMouseEvent.button() == QtCore.Qt.LeftButton:
            self.RightOn = False
            # 获取左键时的相对窗口坐标
        if QMouseEvent.button() == QtCore.Qt.RightButton:
            self.Now_x = QMouseEvent.windowPos().x()
            self.Now_y = QMouseEvent.windowPos().y()
            self.RightOn = True

            # 获取右键时的相对窗口坐标

    def mouseReleaseEvent(self, QMouseEvent):
        if QMouseEvent.button() == QtCore.Qt.LeftButton:
            mE = QMouseEvent.windowPos()
            self.LeftButton_release.emit(mE.x(), mE.y())
            # 左键事件 [松开]
        if QMouseEvent.button() == QtCore.Qt.RightButton:

            if self.RightMove == True:

                self.RightMove = False
                self.RightButton_release.emit()
                # 右键移动且松开
            elif self.RightOn == True:

                self.RightButton_JustClick.emit()
                # 仅仅按下右键

            # 右键事件 [松开]

    def mouseMoveEvent(self, QMouseEvent):
        self.RightMove = True
        if self.RightOn == True:
            globalPos = QMouseEvent.globalPos()
            self.RightButton_Move.emit(globalPos.x() - self.Now_x, globalPos.y() - self.Now_y)
            # 判断右键移动，将计算好的参数返回


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

        self.init()

    def init(self):

        playSet = self.playActions[self.Action]
        self.child_path = ''
        self.path = playSet["path"]
        self.turns = playSet["turns"]
        for i in self.path:
            self.child_path += i + next_
        self.child_path = self.child_path[:-1]

    def run(self):
        def In_Play():
            for i in range(self.turns["first"], self.turns["last"] + 1):
                if self.stop == True:
                    return 'Jump'

                name = self.turns["front"] + str(i) + self.turns["end"]  # 拼合图片名称
                self.play.emit(dir_mix(self.root, self.child_path, name))  # 发出图片显示指令

                time.sleep(1 / self.turns["fps"])  # 等待1/fps秒
            return 'PlayOver'

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


class window_graphics(QtWidgets.QMainWindow, graphics_window):
    def __init__(self, config, root):
        super().__init__()
        self.config = config
        self.root = root
        # 保存传入的初始化数据
        with open(dir_mix(root, config['Script']), 'r', encoding='utf-8') as f:
            self.Script = json.loads(f.read())  # 获取Script的参数
        self.Setting = self.Script["Setting"]  # 获取Setting的数据集合

        self.ImageSize = self.Setting["ImageSize"]
        self.Change = self.Setting["Change"]
        self.usualy_play = self.Setting["usualy_play"]

        self.play_Actions = self.Script["play"]

        self.Find = Find(self.Script) #实例化指令查询插件
        self.Find.play.connect(self.PlayNew)

        self.setupUi(self)  # 创建标准窗口
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)  # 去掉窗口标题栏和按钮
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)  # 设置窗口背景透明
        self.setWindowTitle(self.config['Name'])  # 把窗口名称设置成config.json中的Name键的值

        self.label = Special_Label(self)  # 创建特殊的Label
        self.label.LeftButton_release.connect(self.LeftButton_release)  # 绑定鼠标左键点击事件[松开左键]
        self.label.RightButton_release.connect(self.RightButton_release)  # 绑定鼠标右键点击事件[松开右键]
        self.label.RightButton_Move.connect(self.RightButton_Move)
        self.label.RightButton_JustClick.connect(self.RightButton_JustClick)

        self.ChangeSize()  # 设置窗口初始大小

    def RightButton_JustClick(self):
        print('RightButton_JustClick')
        # +++++++++++++++++++++++++++++未实现+++++++++++++++++++++++++++++++++++++++++

    def RightButton_release(self):
        self.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))

    def RightButton_Move(self, x, y):
        self.move(x, y)
        self.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))

    def LeftButton_release(self, x, y):
        try:
            OnClick = self.Script["OnClick"]
            if OnClick["Use_xy"] == True:
                pass
            else:
                for i in OnClick["Action"]:
                    self.Find.Find(i)
        except:
            pass
        print(x, y)
        # self.PlayBoard.stop = True

    def PlayNew(self,name): # 播放新的动作
        self.PlayBoard.Action = name
        self.PlayBoard.stop = True

    def ChangeSize(self):
        # self.Change:图片缩放系数，>0 [理论是多大都可以，但是你改100看我不打死你]
        width = int(self.ImageSize[0] * self.Change)
        height = int(self.ImageSize[1] * self.Change)
        print('ChangeSize', width, height)
        self.resize(width, height)
        self.label.setGeometry(0, 0, width, height)

    def show(self) -> None:
        super().show()

        self.PlayBoard = PlayBoard(self.play_Actions, self.root, self.usualy_play)  # 把要播放的 动画参数 和动画文件的 根路径 传入
        self.PlayBoard.play.connect(self.graph)
        self.PlayBoard.start()

    def graph(self, paths):
        # print(paths)
        self.label.setPixmap(QtGui.QPixmap(paths).scaled(self.label.width(), self.label.height()))
