from UI.Setbox import Ui_Setbox
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSignal

class Setbox(QtWidgets.QMainWindow,Ui_Setbox):
    ChangeSize = pyqtSignal(float)
    def __init__(self,parent = None):
        super(Setbox,self).__init__(parent)
        self.setupUi(self)
        self.config = None
        self.Script = None
        # self.show()
    def init(self):
        self.Name_show.setText(self.config['Name'])
        self.Introduction_show.setPlainText(self.config['Description'])

        Setting = self.Script['Setting']
        print(str(Setting['Change']))
        self.ImgSize_text_percent.setText(str(Setting['Change']))
        self.ImgSize_control.setValue(Setting['Change']*20)
    def ImgSize_control_valueChange(self):
        # Change 的值从0 - 5
        Change = self.ImgSize_control.value()/20
        self.ImgSize_text_percent.setText(str(Change))
        self.ChangeSize.emit(Change)
