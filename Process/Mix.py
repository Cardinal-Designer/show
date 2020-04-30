from .imports import *
from .window_about import window_about
from .window_loading import window_loading
from .window_main import window_main


class window_loading_(window_loading):
    def run(self):
        main.show()
        self.close()
        # 开启动画后加载主界面


class window_about_(window_about):
    pass


class window_main_(window_main):
    def About_Window(self):
        about.show()


app = QtWidgets.QApplication(sys.argv)

main = window_main_()
about = window_about_()

loading = window_loading_()
loading.show()

sys.exit(app.exec_())
