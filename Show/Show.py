from window_graphics import *
import sys

app = QtWidgets.QApplication(sys.argv)

Path = 'E:\\Codes\\独立项目\\Cardinal\\Data\\白金_站立_互动 - 语音'

config_file = dir_mix(Path,'config.json')
# 合并多段数据 组成config文件的目录数据

with open(config_file, 'r', encoding='utf-8') as f:
    graphics = window_graphics(json.loads(f.read()),Path)
graphics.show()

sys.exit(app.exec_())
