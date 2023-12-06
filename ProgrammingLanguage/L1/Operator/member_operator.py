# -*- coding: utf-8 -*-
# @Time : 2023/08/04 0:09
# @Author : 另外我
# @File : member_operator.py
# @Software: 成员运算符

"""
python提供了成员运算符，用于判断实例中是否包含了一系列的成员，包括字符串、列表和元组

in        如果在指定序列里找到值，返回True，否则返回False
not in    如果在指定序列里没有找到值，返回True，否则返回False
"""


def member_operator():
    # in
    # 如果在指定序列里找到值，返回True，否则返回False
    print("w" in "qwerty")
    # 输出结果为True
    print("z" in "qwerty")
    # 输出结果为False

    # not in
    # 如果在指定序列里没有找到值，返回True，否则返回False
    print("z" not in "qwerty")
    # 输出结果为True
    print("w" not in "qwerty")
    # 输出结果为False


member_operator()
