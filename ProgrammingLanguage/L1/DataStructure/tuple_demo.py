# -*- coding: utf-8 -*-
# @Time : 2023/08/04 1:20
# @Author : 另外我
# @File : tuple_demo.py
# @Software: 元组

"""
元组是一种数据类型，在python中用于存储多个元素，元组可以容纳多个值
元组是有序的数据结构，意味着元组中的元素按照它们的顺序存储，并且可以通过索引进行访问和引用
元组是不可变的，一旦定义后，元组的数据不可以进行添加，修改和删除等操作
元组是异构的，可以包含不同类型的元素，例如整数、浮点数、字符串等，这使得元组成为一种有效的数据结构，用于存储多种不同类型的元素

元组的字面量定义
(1)元组使用小括号 （） 来定义，将元组的元素括在小括号中
(2)元组中的元素通过逗号 , 来进行分隔，每个元素都可以是不同的数据类型
(3)定义元组时，逗号是必须的，即使元组只包含一个元素，也需要在元素后面加上逗号，以区分它是一个元组，而不是其他数据类型

由于元组的不可变特性，所以元组提供的操作方法非常少
"""


def tuple_demo():
    # 定义一个元组
    tuple_1 = (1, 2, 3)
    print(type(tuple_1))

    # len()
    # 获取元组的元素个数
    tuple_1 = (1, 2, 3)
    print(len(tuple_1))

    # count(value)
    # 统计元组中的参数，value指定值的个数
    tuple_1 = (1, 2, 3, 3, 5, 2, 4)
    print(tuple_1.count(3))

    # index(value, start, step)
    # 在元组中查找value第一次出现的下标，如果指定了范围，则仅在范围内查找。如果查找的数据在元组中不存在，会抛出一个错误
    tuple_1 = (1, 2, 3, 3, 5, 2, 4)
    # 第一个3的下标
    print(tuple_1.index(3))
    # 从下标3开始查找
    print(tuple_1.index(2, 3))


tuple_demo()