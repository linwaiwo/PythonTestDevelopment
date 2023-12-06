# -*- coding: utf-8 -*-
# @Time : 2023/08/03 23:55
# @Author : 另外我
# @File : logical_operator.py
# @Software: 逻辑运算符
"""
逻辑运算符一般用来解决当前有多个关系条件需要判断时使用，运算结果为布尔值

Python中提供的逻辑运算符有：
逻辑与运算符（and）：逻辑运算符（and）用来连接多个条件运算，只有多个条件同时满足时，结果为真（True）,否则为假（False）
逻辑或运算符（or）：逻辑或运算（or）用来连接多个关系运算，只有当多个条件同时不能满足时，结果为假（False），只有一个结果为真时，结果为真（True）
逻辑非运算符（not）：逻辑非运算（not）用来对表达式结果进行取反运算，如果表达式结果为真（True），则取反结果为假（False），如果表达式结果为假（False），结果即为真（True）
"""


def logical_operator():
    # 逻辑与运算符（ and ）
    print(1 < 9 and 9 > 1)
    # 输出结果为True
    # print(1 > 8 and 9 > 1)
    print(8 < 1 < 9)
    # 输出结果为False

    # 逻辑或运算符（ or ）
    print(1 < 5 or 5 < 1)
    # 输出结果为True
    print(1 < 5 or 5 < 9)
    # 输出结果为True
    print(9 < 5 or 5 < 1)
    # 输出结果为False

    # 逻辑非运算符（not）
    print(not (3 < 1))
    # 输出结果为True
    print(not (3 < 8))
    # 输出结果为False


logical_operator()
