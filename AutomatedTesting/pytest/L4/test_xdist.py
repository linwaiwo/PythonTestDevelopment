# -*- coding: utf-8 -*-
# @Time : 2023/8/5 0:02 05
# @Author : 另外我
# @File : test_xdist.py
# @Software: 用例并行与分布式执行

"""
场景1：
当测试用例非常多的时候，一条条按顺序执行，是非常浪费时间的
这时候就可以使用pytest-xdist分布式执行用例，这就是一种分布式场景。

场景2 ：
假设有个报名系统，对报名总数统计，数据同时进行修改操作的时候有可能出现问题，
需要模拟这个场景，需要多用户并发请求数据。

解决:
使用分布式并发执行测试用例。分布式插件：pytest-xdist
安装及运行:pip install pytest-xdist

注意： 用例多的时候效果明显，多进程并发执行，同时支持 allure

运行方式：
命令行输入：pytest -n cpu数量
         pytest -n auto(自动识别空闲cou)
"""


def test_demo1():
    print('demo 1')


def test_demo2():
    print('demo 2')


def test_demo3():
    print('demo 3')


def test_demo4():
    print('demo 4')


def test_demo5():
    print('demo 5')
