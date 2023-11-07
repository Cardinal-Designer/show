from PyQt5 import QtCore, QtGui, QtWidgets,QtMultimedia
from UI.graphics import Ui_Form as graphics_window
from Environment import dir_mix,path_read
from Find import Find
from PlayBoard import PlayBoard
from Special_Label import Special_Label
import json

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

        try:
            self.sound_Actions = self.Script["sound"]
        except:
            pass

        # Find组件 ============================================
        self.Find = Find(self.Script) #实例化指令查询插件
        self.Find.play.connect(self.PlayNew)
        self.Find.soundPlay.connect(self.soundPlay)

        self.setupUi(self)  # 创建标准窗口
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)  # 去掉窗口标题栏和按钮
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)  # 设置窗口背景透明
        self.setWindowTitle(self.config['Name'])  # 把窗口名称设置成config.json中的Name键的值


        # Special_Label组件 ============================================
        self.label = Special_Label(self)  # 创建特殊的Label
        self.label.LeftButton_release.connect(self.LeftButton_release)  # 绑定鼠标左键点击事件[松开左键]
        self.label.LeftButton_click.connect(self.LeftButton_click)  # 绑定鼠标左键点击事件[松开左键]

        self.label.RightButton_release.connect(self.RightButton_release)  # 绑定鼠标右键点击事件[松开右键]
        self.label.RightButton_Move.connect(self.RightButton_Move)
        self.label.RightButton_JustClick.connect(self.RightButton_JustClick)


        self.sound = QtMultimedia.QMediaPlayer() # 创立音频播放组件

        self.PlayBoard = PlayBoard(self.play_Actions, self.root, self.usualy_play)  # 把要播放的 动画参数 和动画文件的 根路径 传入
        self.PlayBoard.play.connect(self.graph)
        self.PlayBoard.start()

        self.ChangeSize()  # 设置窗口初始大小
    def soundPlay(self,sound_name):
        path = dir_mix(self.root,path_read(self.sound_Actions[sound_name]["path"]))

        url = QtCore.QUrl.fromLocalFile(path)
        self.sound.setMedia(QtMultimedia.QMediaContent(url))
        self.sound.play()

    def RightButton_JustClick(self):
        print('RightButton_JustClick')

        # +++++++++++++++++++++++++++++未实现+++++++++++++++++++++++++++++++++++++++++

    def RightButton_release(self):
        self.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))

    def RightButton_Move(self, x, y):
        self.move(x, y)
        self.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
    def LeftButton_click(self,x, y):
        self.Find.LeftClick(x,y,self.Change)
    def LeftButton_release(self, x, y):
        self.Find.LeftRelease(x, y,self.Change)
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


    def graph(self, paths):
        # print(paths)
        self.label.setPixmap(QtGui.QPixmap(paths).scaled(self.label.width(), self.label.height()))
