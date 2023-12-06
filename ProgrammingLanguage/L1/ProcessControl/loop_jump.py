# -*- coding: utf-8 -*-
# @Time : 2023/08/20 16:58
# @Author : 另外我
# @File : loop_jump.py
# @Software: 逻辑结构-循环跳出  continue break


def loop_cont():
    n = 1
    while n <= 5:
        print(f"hello,world{n}")
        n += 1
        # 跳出当次循环，进入下一循环
        # continue
        print("hello")
    else:
        print("end")


def loop_cont_onr():
    n = 1
    while n <= 5:
        print(f"hello,world{n}")
        n += 1
        # 跳出整体循环
        break
    else:
        print("end")


loop_cont_onr()
