#-*- coding:utf-8 -*-
# 不同的组件数据交换要复制多份数据，于是做了一个空间来数据共享
Space = {}
def Add(Name):
    Space[Name] = None
def Del(Name):
    del Space[Name]
def LookUpUse(Name):
    try:
        if Space[Name] == None:
            return False
        else:
            return True
    except KeyError:
        return('Space is not created')
