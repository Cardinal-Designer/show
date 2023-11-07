from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys


class MyLabel(QLabel):
    def __init__(self, *args, **kw):
        super().__init__(*args, **kw)
        self.setContextMenuPolicy(Qt.CustomContextMenu)
        self.customContextMenuRequested.connect(self.rightMenuShow)  # 开放右键策略

    def rightMenuShow(self, pos):  # 添加右键菜单
        menu = QMenu(self)
        menu.addAction(QAction('动作1', menu))
        menu.addAction(QAction('动作2', menu))
        menu.addAction(QAction('动作3', menu))
        menu.triggered.connect(self.menuSlot)
        menu.exec_(QCursor.pos())

    def menuSlot(self, act):
        print(act.text())


class Demo(QWidget):
    def __init__(self, *args, **kw):
        super().__init__(*args, **kw)
        label = MyLabel('右击这里', self)
        label.setGeometry(0, 0, 60, 30)

        self.resize(100, 100)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ecs = Demo()
    sys.exit(app.exec_())
