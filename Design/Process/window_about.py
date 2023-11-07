from .imports import *
from UI.About import Ui_MainWindow as About_window
class window_about(QtWidgets.QMainWindow, About_window):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
