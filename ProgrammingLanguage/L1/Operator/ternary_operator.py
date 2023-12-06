# -*- coding: utf-8 -*-
# @Time : 2023/12/4 0:36
# @Author : 另外我
# @File : ternary_operator.py
# @Software: 三目运算符

"""
三目运算符也称三元运算符，是指运算符在使用时，需要三个操作数参与运算

语法格式：
【True】 if 【expression】 else 【False】
【True】是指条件为真时的结果
【False】是指条件为假时的结果
【expression】条件判断表达式

python会先判断【expression】条件表达式的结果，如果条件为真，则结果为【True】，条件为假，结果为【False】
"""


def ternary_operator():
    age = 10
    age_1 = 20
    # 条件判断表达式为True，执行 【True】 的结果
    result = "成年" if age >= 18 else "未成年"
    # 条件判断表达式为False，执行 【False】 的结果
    result_1 = "成年" if age_1 >= 18 else "未成年"
    print(result)
    # 输出结果：未成年
    print(result_1)
    # 输出结果：成年


ternary_operator()
