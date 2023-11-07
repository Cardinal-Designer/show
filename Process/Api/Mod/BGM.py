from Environment import dir_mix,path_read
from PySide2 import QtMultimedia,QtCore
from DataUnCopy import Add,Space

class BGM():
    def __init__(self):
        self.OnlyThis = QtMultimedia.QMediaPlaylist.CurrentItemOnce
        self.OnlyThisLoop = QtMultimedia.QMediaPlaylist.CurrentItemInLoop
        self.PlayTheList = QtMultimedia.QMediaPlaylist.Sequential
        self.PlayTheListLoop = QtMultimedia.QMediaPlaylist.Loop
        self.Random = QtMultimedia.QMediaPlaylist.Random

    def Set_List(self,IsSound,Content,Cycle = QtMultimedia.QMediaPlaylist.Loop):
        """IsSound : 标注音频是否来自Sound事件组 Content : 标注音频（传入音频位置数据或Sound事件组中别名 Cycle : 是否循环）"""
        Music = []

        for i in Content:
            if IsSound:
                Music.append(dir_mix(Space["root"], path_read(Space["Script"]["sound"][i]["path"])))
            else:
                Music.append(dir_mix(Space["root"], path_read(i)))
        if len(Music) >1:
            for i in Music:
                url = QtCore.QUrl.fromLocalFile(i)
                Space['BGMPlaylist'].addMedia(QtMultimedia.QMediaContent(url))
                Space['BGMPlayer'].setPlaylist(Space['BGMPlaylist'])
        else:
            url = QtCore.QUrl.fromLocalFile(Music[0])
            Space['BGMPlayer'].setMedia(QtMultimedia.QMediaContent(url))

        Space['BGMPlaylist'].setPlaybackMode(Cycle)

        # Constant	Value	Description
        # QMediaPlaylist::CurrentItemOnce	0	The current item is played only once.
        # QMediaPlaylist::CurrentItemInLoop	1	The current item is played repeatedly in a loop.
        # QMediaPlaylist::Sequential	2	Playback starts from the current and moves through each successive item until the last is reached and then stops. The next item is a null item when the last one is currently playing.
        # QMediaPlaylist::Loop	3	Playback restarts at the first item after the last has finished playing.
        # QMediaPlaylist::Random	4	Play items in random order.

    def setCurrentIndex(self,Id):
        Space['BGMPlaylist'].setCurrentIndex(Id)

    def setVolume(self,Volume):
        Space['BGMPlayer'].setVolume(Volume)

    def play(self):
        Space['BGMPlayer'].play()

    def pause(self):
        Space['BGMPlayer'].pause()

    def stop(self):
        Space['BGMPlayer'].stop()
