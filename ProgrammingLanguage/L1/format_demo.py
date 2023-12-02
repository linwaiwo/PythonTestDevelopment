# -*- coding: utf-8 -*-
# @Time : 2023/08/29 17:33
# @Author : 另外我
# @File : format_demo.py
# @Software:格式化


def mymess():
    # format基本方法
    mess = "我叫{}，{}岁了".format('小刘', '12')
    print(mess)

    # format位置参数方法
    name = 'xiaoyang'
    age = 18
    mess = 'my name is {0},I {1} years old'.format(name, age)
    print(mess)
    mess = 'I {1} years old，my name is {0}'.format(name, age)
    print(mess)

    # format关键字方法
    username = 'xiaoliu'
    age = 18
    mess = 'my name is {name},I {age} years old'.format(name=username, age=age)
    print(mess)


def ifon():
    # 字符串对齐
    print("The value is ljust: |{:5}|".format("abc"))
    print("The value is rjust: |{:<5}|".format("abc"))
    print("The value is rjust: |{:>5}|".format("abc"))
    # 数字对齐
    print("The value is rjust: |{:5}|".format(11))
    print("The value is rjust: |{:<5}|".format(11))
    print("The value is rjust: |{:>5}|".format(11))


def fstring():
    name = 'xiaoli'
    age = 15
    print(f"name:{name},age:{age}")


fstring()
