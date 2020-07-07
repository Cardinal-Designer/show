#-*- coding:utf-8 -*-
import os

path = Workpath = os.path.dirname(os.path.abspath(__file__))
# 工程根目录

next_ = None
if os.name == 'nt':
    next_ = '\\'
else:
    next_ = '/'
# 针对 Linux 和 windows 的不同，更改路径中的 反斜杠(\) 或 斜杠(/)

def dir_mix(*dirs):
    mix = ''
    for i in dirs:
        mix += i+next_
    return mix[:-1]
# 路径拼合函数


def path_read(path):
    child_path = ''
    for i in path:
        child_path += i + next_
    return child_path[:-1]
# 读取path数据，合成子路径
