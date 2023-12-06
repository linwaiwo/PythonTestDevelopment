# -*- coding: utf-8 -*-
# @Time : 2023/08/03 23:33
# @Author : 另外我
# @File : relational_operator.py
# @Software: 关系运算符

"""
关系运算符也成为比较运算符，用来对参与运算的两个操作数进行比较，运算结果会返回一个布尔值

==            等于
!=            不等于
>             大于
<             小于
>=            大于等于
<=            小于等于
"""


def relational_operator():
    # 等于（==）
    # 用来判断两个操作数是否相同，如果相同，结果为真 True，如果不同，结果为假 False。
    print(1 == 1)
    # 输出结果：True
    print(1 == 2)
    # 输出结果False

    # 不等于(!=)
    # 用来判断两个操作数是否不同，如果不同，结果为真 True，如果相同，结果为假 False。
    print(1 != 1)
    # 输出结果False
    print(1 != 2)
    # 输出结果True

    # 大于 （ > ）
    # 用来判断左操作数是否大于右操作数，如果大于，结果为真 True，否则，结果为假 False。
    print(1 > 2)
    # 输出结果False
    print(2 > 1)
    # 输出结果True

    # 小于 （ < ）
    # 用来判断左操作数是否小于右操作数，如果小于，结果为真 True，否则，结果为假 False。
    print(1 < 2)
    # 输出结果True
    print(1 < 1)
    # 输出结果False

    # 大于等于 （ >= ）
    # 用来判断左操作数是否大于或等于右操作数，如果大于或等于，结果为真 True，否则，结果为假 False。
    print(1 >= 1)
    # 输出结果True
    print(1 >= 2)
    # 输出结果False

    # 小于等于 （ <= ）
    # 用来判断左操作数是否小于或等于右操作数，如果小于或等于，结果为真 True，否则，结果为假 False。
    print(1 <= 1)
    # 输出结果True
    print(2 <= 1)
    # 输出结果False


relational_operator()
