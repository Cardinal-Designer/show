# -*- coding:utf-8 -*-

from PySide2 import QtCore, QtGui, QtWidgets, QtMultimedia
from UI.graphics import Ui_Form as graphics_window
from Environment import dir_mix, path_read
from Find import Find
from PlayBoard import PlayBoard
from Special_Label import Special_Label
from TrayIcon import TrayIcon
from Setbox import Setbox
from DataUnCopy import Add, Space
from UserSet import User
import json, sys


class window_graphics(QtWidgets.QMainWindow, graphics_window):
    def __init__(self, config, root):
        # mainwindow 初始化 ======================================================================
        super().__init__()
        Add('config')
        Space["config"] = config
        Add('root')
        Space["root"] = root

        # 保存传入的初始化数据
        TrayIcon_img = dir_mix(Space["root"], Space["config"]['cover'])  # 用人物预览图作为托盘图标 和 显示图标

        self.setWindowIcon(QtGui.QIcon(TrayIcon_img))

        with open(dir_mix(Space["root"], Space["config"]['Script']), 'r', encoding='utf-8') as f:
            Add('Script')
            Space["Script"] = json.loads(f.read())  # 获取Script的参数
        self.Setting = Space["Script"]["Setting"]  # 获取Setting的数据集合

        self.ImageSize = self.Setting["ImageSize"]
        Add('Change')
        Space['Change'] = self.Setting["Change"]

        self.usualy_play = Space["Script"]["Setting"]["usualy_play"]

        try:
            self.sound_Actions = Space["Script"]["sound"]
        except:
            pass

        # Find组件 ============================================
        self.Find = Find()  # 实例化指令查询插件
        self.Find.play.connect(self.PlayNew)
        self.Find.soundPlay.connect(self.soundPlay)
        ###############################################################################
        self.setupUi(self)  # 创建标准窗口

        # User组件 =======================================================
        self.User = User()
        self.ChangeWindowFlags(True)

        ####################################################################

        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)  # 设置窗口背景透明
        self.setWindowTitle(Space["config"]['Name'])  # 把窗口名称设置成config.json中的Name键的值

        # Special_Label组件 ============================================
        self.label = Special_Label(self)  # 创建特殊的Label

        self.label.LeftButton_release.connect(self.LeftButton_release)  # 绑定鼠标左键点击事件[松开左键]
        self.label.LeftButton_click.connect(self.LeftButton_click)  # 绑定鼠标左键点击事件[松开左键]

        self.label.RightButton_release.connect(self.RightButton_release)  # 绑定鼠标右键点击事件[松开右键]
        self.label.RightButton_Move.connect(self.RightButton_Move)

        # 设置 ===========================
        self.Setbox = Setbox(self)
        self.Setbox.ChangeSize.connect(self.ChangeSize)
        self.Setbox.MovePeson.connect(self.MovePeson)
        self.Setbox.ResetWindowFlag.connect(self.ChangeWindowFlags)
        # TrayIcon 组件 =====================================
        self.TrayIcon = TrayIcon(self)
        self.TrayIcon.setIcon(QtGui.QIcon(TrayIcon_img))
        self.TrayIcon.show()
        self.TrayIcon.AddActions("退出", self.close)
        self.TrayIcon.AddActions("设置", self.Setbox.show)

        self.sound = QtMultimedia.QMediaPlayer()  # 创立音频播放组件

        self.PlayBoard = PlayBoard()  # 把要播放的 动画参数 和动画文件的 根路径 传入
        self.PlayBoard.play.connect(self.graph)
        self.PlayBoard.start()

        self.ChangeSize()  # 设置窗口初始大小

    def ChangeWindowFlags(self, init=True):
        Flags = 0
        for i in Space['WindowFlags']:
            Flags = Flags | i
        self.setWindowFlags(QtCore.Qt.WindowType(Flags))
        if init:
            return
        if not self.isVisible():
            self.setVisible(True)

    def MovePeson(self):
        self.move(Space['PersonX'], Space['PersonY'])
        # 同步移动，拖动窗口时候同时移动人物

    def show(self):
        super().show()

        Add('PersonX')
        Add('PersonY')
        Space['PersonX'] = self.pos().x()
        Space['PersonY'] = self.pos().y()

        # 在标准窗口show()后才可以获取窗口的x,y坐标

    def PlayNew(self, name):  # 播放新的动作
        self.PlayBoard.Action = name
        self.PlayBoard.stop = True

    def close(self):
        super().close()

        sys.exit(0)

    def soundPlay(self, sound_name):
        path = dir_mix(Space["root"], path_read(self.sound_Actions[sound_name]["path"]))

        url = QtCore.QUrl.fromLocalFile(path)
        self.sound.setMedia(QtMultimedia.QMediaContent(url))
        self.sound.play()

    def RightButton_release(self):
        self.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        # 拖动完成必然松开右键才能操作别的，只同步最新拖动后的人物x，y数据，节省资源
        Space['PersonX'] = self.pos().x()
        Space['PersonY'] = self.pos().y()

    def RightButton_Move(self, x, y):
        self.move(x, y)
        self.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))

        if self.Setbox.MoveWithPerson:
            self.Setbox.move(x - 800, y)

    def LeftButton_click(self, x, y):
        self.Find.LeftClick(x, y, Space['Change'])

    def LeftButton_release(self, x, y):
        self.Find.LeftRelease(x, y, Space['Change'])
        # self.PlayBoard.stop = True

    def ChangeSize(self):
        # Space['Change']:图片缩放系数，>0 [理论是多大都可以，但是你改100看我不 *%*&%]
        width = int(self.ImageSize[0] * Space['Change'])
        height = int(self.ImageSize[1] * Space['Change'])
        self.resize(width, height)
        self.label.setGeometry(0, 0, width, height)

    def graph(self, paths):
        self.label.setPixmap(QtGui.QPixmap.fromImage(QtGui.QImage(paths).scaled(self.label.width(), self.label.height()).mirrored(Space['CommonSet']["mirrored"],False)))
