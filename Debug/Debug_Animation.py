from DataUnCopy import Space
from Environment import dir_mix, path_read
from PySide2.QtWidgets import QMessageBox

class Debug_Animation():
    ChooseItem = None

    def Debug_Animation_GetActions(self):
        Setting = Space["Script"]["Setting"]
        self.Debug_Animation_CoreInfo_Usualyplay_lineEdit.setText(str(Setting["usualy_play"]))
        self.Debug_Animation_CoreInfo_ImageSize_x_lineEdit.setText(str(Setting["ImageSize"][0]))
        self.Debug_Animation_CoreInfo_ImageSize_y_lineEdit.setText(str(Setting["ImageSize"][1]))
        self.Debug_Animation_CoreInfo_Change_lineEdit.setText(str(Setting["Change"]))
        # 获取参数并显示 [Debug_Animation_CoreInfo_groupBox] 的子项
        self.Debug_Animation_Actions_listWidget.clear()
        for content in Space["Script"]["play"]:
            self.Debug_Animation_Actions_listWidget.addItem(content)

    def Animation_Information_Get(self, Item):
        self.ChooseItem = Item.text()
        Info = Space["Script"]["play"][Item.text()]
        fullpath = dir_mix(Space["root"], path_read(Info["path"]))
        self.Animation_Information_path_lineEdit.setText(fullpath)
        self.Animation_Information_front_lineEdit.setText(Info["turns"]["front"])
        self.Animation_Information_end_lineEdit.setText(Info["turns"]["end"])
        self.Animation_Information_start_lineEdit.setText(str(Info["turns"]["first"]))
        self.Animation_Information_last_lineEdit.setText(str(Info["turns"]["last"]))
        self.Animation_Information_fps_lineEdit.setText(str(Info["turns"]["fps"]))

    def Animation_Test_Play(self):
        if self.ChooseItem == None:
            QMessageBox.question(self,"异常","没有选中任何动作或没有获取动作",QMessageBox.Close)
        else:
            Space["CoreControl"].play.emit(self.ChooseItem)

    def SetUsuallyPlay(self):
        if self.ChooseItem == None:
            QMessageBox.question(self,"异常","没有选中任何动作或没有获取动作",QMessageBox.Close)
        else:
            Space["Script"]["Setting"]["usualy_play"] = self.ChooseItem
            self.Debug_Animation_CoreInfo_Usualyplay_lineEdit.setText(self.ChooseItem)
