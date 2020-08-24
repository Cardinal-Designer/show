# -*- coding:utf-8 -*-
from window_graphics import *
import sys
argv = sys.argv

if len(argv) < 2:
    print("emm")
else:
    Path = argv[1]

    app = QtWidgets.QApplication(sys.argv)
    #app.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)



    config_file = dir_mix(Path, 'config.json')

    # 合并多段数据 组成config文件的目录数据

    with open(config_file, 'r', encoding='utf-8') as f:
        graphics = window_graphics(json.loads(f.read()), Path,app)
    graphics.show()

    sys.exit(app.exec_())
