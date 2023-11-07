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
from Process import Special_Control,plugin
import json, sys


class window_graphics(QtWidgets.QMainWindow, graphics_window):
    def __init__(self, config, root,app):
        # mainwindow 初始化 ======================================================================
        super().__init__()
        self.app = app
        # 保存传入的初始化数据
        Add('config')
        Space["config"] = config
        Add('root')
        Space["root"] = root



        TrayIcon_img = dir_mix(Space["root"], Space["config"]['cover'])  # 用人物预览图作为托盘图标 和 显示图标

        with open(dir_mix(Space["root"], Space["config"]['Script']), 'r', encoding='utf-8') as f:
            Add('Script')
            Space["Script"] = json.loads(f.read())  # 获取Script的参数
        Setting = Space["Script"]["Setting"]  # 获取Setting的数据集合

        self.ImageSize = Setting["ImageSize"]
        Add('Change')
        Space['Change'] = Setting["Change"]

        try:
            self.sound_Actions = Space["Script"]["sound"]
        except:
            pass

        Add('Info')
        Space['Info'] = {}
        Space['Info']["Play_complete"] = {}  # 播放组件是否播放完毕设置
        Space['Info']["Move"] = {}
        Space['Info']["Move"]["Window"] = {}

        Add('Control_Api')
        Space['Control_Api'] = {}

        # 核心控制器类
        Add("CoreControl")
        Space["CoreControl"] = Special_Control.CoreControl()



        self.setupUi(self)  # 创建标准窗口
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)  # 设置窗口背景透明
        self.setWindowTitle(Space["config"]['Name'])  # 把窗口名称设置成config.json中的Name键的值
        self.setWindowIcon(QtGui.QIcon(TrayIcon_img)) # 设置Icon

        self.Cache = {} # 图片缓存字典



        # 组件创建
        self.label = Special_Label(self)  # 创建特殊的Label
        self.PlayBoard = PlayBoard()  # 创建播放器
        self.PlayBoard.play.connect(self.graph)
        self.Find = Find()  # 实例化指令查询插件
        self.sound = QtMultimedia.QMediaPlayer()  # 创立音频播放组件

        Space['BGMPlayer'] = QtMultimedia.QMediaPlayer()
        Space['BGMPlaylist'] = QtMultimedia.QMediaPlaylist()

        self.User = User() # User组件 （会创建CommonSet，在Setbox前加载）

        self.Setbox = Setbox(self)



        self.ChangeWindowFlags(True)

        # 核心控制器绑定组件 ============================================
        Space["CoreControl"].play.connect(self.PlayNew)
        Space["CoreControl"].sound.connect(self.soundPlay)
        Space["CoreControl"].ChangeSize.connect(self.ChangeSize)
        Space["CoreControl"].Move.connect(self.MovePeson)

        Space["CoreControl"].clean.connect(self.PlayBoard.terminate)
        Space["CoreControl"].clean.connect(self.Setbox.close)
        Space["CoreControl"].clean.connect(self.close)
        Space["CoreControl"].clean.connect(self.app.exit)

        # Special_Label组件事件绑定 ============================================
        self.label.LeftButton_release.connect(self.LeftButton_release)  # 绑定鼠标左键点击事件[松开左键]
        self.label.LeftButton_click.connect(self.LeftButton_click)  # 绑定鼠标左键点击事件[松开左键]

        self.label.RightButton_release.connect(self.RightButton_release)  # 绑定鼠标右键点击事件[松开右键]
        self.label.RightButton_Move.connect(self.RightButton_Move)

        # 设置事件绑定 ===========================
        self.Setbox.MovePeson.connect(self.MovePeson)
        self.Setbox.ResetWindowFlag.connect(self.ChangeWindowFlags)
        # TrayIcon 组件 =====================================
        self.TrayIcon = TrayIcon(self)
        self.TrayIcon.setIcon(QtGui.QIcon(TrayIcon_img))
        self.TrayIcon.show()
        self.TrayIcon.AddActions("退出", self.close_)
        self.TrayIcon.AddActions("设置", self.Setbox.show)

        # 线程启动
        self.PlayBoard.start()

        if Space['CommonSet']["Change"] != None:
            Space['Change'] = Space['CommonSet']["Change"]
        self.ChangeSize()  # 设置窗口初始大小

        # Importer
        plugin.Importer()

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
        self.move(Space['Info']["Move"]["Window"]['PersonX'], Space['Info']["Move"]["Window"]['PersonY'])
        # 同步移动，拖动窗口时候同时移动人物

    def show(self):
        super().show()

        Space['Info']["Move"]["Window"]['PersonX'] = self.pos().x()
        Space['Info']["Move"]["Window"]['PersonY'] = self.pos().y()

        # 在标准窗口show()后才可以获取窗口的x,y坐标

    def PlayNew(self, name):  # 播放新的动作
        self.PlayBoard.Action = name
        self.PlayBoard.stop = True

    def close_(self):
        Space["CoreControl"].clean.emit()

    def soundPlay(self, sound_name):
        path = dir_mix(Space["root"], path_read(self.sound_Actions[sound_name]["path"]))

        url = QtCore.QUrl.fromLocalFile(path)
        self.sound.setMedia(QtMultimedia.QMediaContent(url))
        self.sound.play()

    def RightButton_release(self):
        self.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))

        # 拖动完成必然松开右键才能操作别的，只同步最新拖动后的人物x，y数据，节省资源
        Space['Info']["Move"]["Window"]['PersonX'] = self.pos().x()
        Space['Info']["Move"]["Window"]['PersonY'] = self.pos().y()

    def RightButton_Move(self, x, y):
        Space["CoreControl"].stopAllAction.emit()
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
        hash_ = hash(paths)
        if Space["CommonSet"]["Cache"]:
            if hash_ not in self.Cache.keys():
                #print(hash(paths))
                self.Cache[hash_] = QtGui.QImage(paths)
            self.label.setPixmap(QtGui.QPixmap.fromImage(self.Cache[hash_].scaled(self.label.width(), self.label.height()).mirrored(Space['CommonSet']["mirrored"],False)))
        else:
            self.Cache.clear()
            self.label.setPixmap(QtGui.QPixmap.fromImage(QtGui.QImage(paths).scaled(self.label.width(), self.label.height()).mirrored(Space['CommonSet']["mirrored"],False)))

