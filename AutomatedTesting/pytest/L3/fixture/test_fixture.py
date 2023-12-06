# -*- coding: utf-8 -*-
# @Time : 2023/08/24 15:27
# @Author : 另外我
# @File : test_fixtrue.py
# @Software: 装饰器--fixture

"""
测试⽤例执⾏时，有的⽤例需要登陆才能执⾏，有些⽤例不需要登陆。setup 和 teardown ⽆法满⾜。fixture 可以。默认 scope（范围）function

步骤：
1.导⼊ pytest
2.在登陆的函数上⾯加@pytest.fixture()
3.在要使⽤的测试⽅法中传⼊（登陆函数名称），就先登陆
4.不传⼊的就不登陆直接执⾏测试⽅法。
"""

import pytest


@pytest.fixture(autouse=True, scope='function')
# scope='function':设置作用域, autouse=True设置为自动应用
def login():
    print("登录操作")


def test_ss():
    print("搜索商品")


def test_gwc(login):
    print("添加购物车")


def test_xd(login):
    print("下单操作")
