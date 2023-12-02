# -*- coding: utf-8 -*-
# @Time : 2023/08/22 14:34
# @Author : 另外我
# @File : var_scope_demo.py
# @Software: PyCharm


# #局部变量
# def aa():
#     num = 100
#     print(num)
#     #打印100
# aa()
#
# print(num)
# #会报Name Error错误

# 全局变量
num = 100


def show():
    global num
    num = 200
    print(num)


show()

print(num)
