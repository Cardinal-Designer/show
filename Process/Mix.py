from .imports import *
from .window_about import window_about
from .window_loading import window_loading
from .window_main import window_main
from .window_graphics import window_graphics


class window_graphics_(window_graphics):
    pass


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

    def Play_selected(self):
        super().selected()
        for select in self.selected:
            graphics[select] = window_graphics_(config=self.configs[select], root=self.pkg_root[select])
            graphics[select].show()


debug = 2
app = QtWidgets.QApplication(sys.argv)

main = window_main_()
about = window_about_()
graphics = {}
loading = window_loading_()
# 加载各个窗体
if debug == 1:
    loading.show()
elif debug == 2:
    main.show()
sys.exit(app.exec_())
