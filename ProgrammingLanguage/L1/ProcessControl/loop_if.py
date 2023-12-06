# -*- coding: utf-8 -*-
# @Time : 2023/08/21 14:45
# @Author : 另外我
# @Software: 逻辑结构-if循环

from random import randint


def loop_info():
    age = 21
    res = int(input("猜猜我几岁了？："))
    if res < age:
        print("猜小了")
    elif res > age:
        print("猜大了")
    else:
        print("猜对了")


# loop_info()


def loop_fora():
    # 求1-100相加的值
    res = 0
    for x in range(1, 101):
        res += x
    print(res)


def if_demo():
    result = randint(1, 10)
    res = int(input("猜数字："))
    if res < result:
        print("猜小了")
    elif res > result:
        print("猜大了")
    else:
        print("猜对了")


if_demo()
