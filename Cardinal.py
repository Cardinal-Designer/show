from PyQt5 import QtCore, QtGui, QtWidgets
from UI.MainWindow import Ui_MainWindow as Main_window
from UI.About import Ui_MainWindow as About_window

import sys

class window_main(QtWidgets.QMainWindow, Main_window):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def About_Window(self):
        about.show()


class window_about(QtWidgets.QMainWindow, About_window):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    main = window_main()
    main.show()

    about = window_about()
    sys.exit(app.exec_())
