# -*- coding: utf-8 -*-
# @Time : 2023/08/22 14:34
# @Author : 另外我
# @File : var_scope_demo.py
# @Software: 变量作用域


"""
变量的作用域决定了在哪一部分程序可以访问哪个特定的变量名称。Python 的作用域一共有4种，分别是：
有四种作用域：
L（Local）：最内层，包含局部变量，比如一个函数/方法内部。
E（Enclosing）：包含了非局部(non-local)也非全局(non-global)的变量，一般在闭包中出现。
G（Global）：当前脚本的最外层，比如当前模块的全局变量。
B（Built-in）： 包含了内建的变量/关键字等，最后被搜索。
查找规则顺序：L –> E –> G –> B。
"""

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
