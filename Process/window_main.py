from .imports import *
from UI.MainWindow import Ui_MainWindow as Main_window
class window_main(QtWidgets.QMainWindow, Main_window):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def About_Window(self):
        pass
