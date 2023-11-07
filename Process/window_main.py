from .imports import *
from UI.MainWindow import Ui_MainWindow as Main_window
from Environment import path, dir_mix

configs = []
pkg_root = []


def message_info(type, title, msgs):
    msg = {
        'type': type,
        'title': title,
        'msg': msgs
    }
    return json.dumps(msg)
    # 包装message数据


class ReadConfig(QtCore.QThread):
    message = pyqtSignal(str)
    model_add = pyqtSignal(int, int, int)

    # 传参（传出）：x,y,ID

    def __init__(self):
        super().__init__()

    def run(self) -> None:
        Path = None  # 图包父目录
        Child_path = None  # 图包文件夹目录名[list]
        # 遍历图包目录
        for paths, child_path, j in os.walk(path + '\\Data'):
            Path = paths
            Child_path = child_path
            break

        now_Process = None
        try:
            for pkg_name in Child_path:
                now_Process = pkg_name
                config_file = dir_mix(
                    Path,
                    pkg_name,
                    'config.json'
                )
                # 合并多段数据 组成config文件的目录数据

                with open(config_file, 'r', encoding='utf-8') as f:
                    configs.append(json.loads(f.read()))

                    pkg_root.append(dir_mix(
                        Path,
                        pkg_name,
                    ))
        except:
            self.message.emit(message_info(type='wrong', title='error', msgs='包：[' + now_Process + ']异常'))
            # 回调，发送出错的包的名称
        All_model_count = len(configs)

        count = 0
        print(int(All_model_count / 5))
        for y in range(1, 6):
            for x in range(1, 6):
                if count == All_model_count:
                    break
                # print(x,y,configs[count]["Name"],configs[count]["Description"])
                self.model_add.emit(x, y, count)
                count += 1


class window_main(QtWidgets.QMainWindow, Main_window):
    def __init__(self):
        super().__init__()
        self.checkBox = []
        self.label = []
        self.pixmap = []

        self.setupUi(self)
        self.scrollArea.setFrameShape(QtWidgets.QFrame.NoFrame)
        # 设置滚动区域无边框

    def show(self) -> None:
        super().show()
        self.Add = ReadConfig()
        self.Add.message.connect(self.message)  # 绑定事件: message事件
        self.Add.model_add.connect(self.Create_model)
        self.Add.start()  # 启动图包加载线程

        # #人物计数器归零
        # for y in range(1,30):
        #     for x in range(1,6):
        #         self.Create_model(x,y)

    def message(self, msg):
        data = json.loads(msg)
        if data["type"] == "wrong":
            QtWidgets.QMessageBox.warning(self, data["title"], data["msg"], QtWidgets.QMessageBox.Yes)

    def Create_model(self, x, y, ID):
        name = configs[ID]["Name"]
        Description = configs[ID]["Description"]
        cover = dir_mix(pkg_root[ID], configs[ID]["cover"])
        list_length = 10 + 176 * y
        self.scrollAreaWidgetContents.setMinimumSize(QtCore.QSize(760, list_length))
        x_label = 10 + 150 * (x - 1)
        y_label = 10 + 176 * (y - 1)

        self.label.append(QtWidgets.QLabel(self.scrollAreaWidgetContents))
        self.label[ID].setGeometry(QtCore.QRect(x_label, y_label, 140, 140))
        self.label[ID].setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label[ID].setToolTip(Description)

        print(cover)
        self.pixmap.append(QtGui.QPixmap(cover).scaled(140, 140))
        self.label[ID].setPixmap(self.pixmap[ID])

        x_checkBox = 10 + 150 * (x - 1)
        y_checkBox = 10 + 150 * y + 26 * (y - 1)
        self.checkBox.append(QtWidgets.QCheckBox(self.scrollAreaWidgetContents))
        self.checkBox[ID].setGeometry(QtCore.QRect(x_checkBox, y_checkBox, 140, 16))

        self.checkBox[ID].setText(name)
        self.checkBox[ID].setToolTip(Description)

        self.label[ID].show()
        self.checkBox[ID].show()

    def About_Window(self):
        pass

    def Play_selected(self):
        self.configs = configs
        self.pkg_root = pkg_root
        self.selected = []  # 记录被选择的ID
        for i in range(0, len(configs)):
            if self.checkBox[i].checkState() == 2:
                self.selected.append(i)
