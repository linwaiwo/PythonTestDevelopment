# -*- coding: utf-8 -*-
# @Time : 2023/08/04 0:26
# @Author : 另外我
# @File : identity_operator.py
# @Software: 身份运算符

"""
身份运算符用来判断两个对象的引用是否为同一个，就是用来比较两个对象的内存地址是否相同

#is        是判断两个标识符是不是引用同一个对象
#is not    是判断两个标识符是不是引用自不同的对象
"""


def identity_operator():
    # is
    # 判断两个标识符是不是引用同一个对象
    # is not
    # 判断两个标识符是不是引用自不同的对象
    a1 = "hello"
    a2 = "hello"
    print(a1 is a2)
    # 输出结果为True
    print(a1 is not a2)
    # 输出结果为False

    q1 = "python"
    q2 = "pytest"
    print(q1 is q2)
    # 输出结果为False
    print(q1 is not q2)
    # 输出结果为True


identity_operator()
