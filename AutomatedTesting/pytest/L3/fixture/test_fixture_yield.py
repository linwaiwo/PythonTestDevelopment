# -*- coding: utf-8 -*-
# @Time : 2023/08/04 15:43 04
# @Author : 另外我
# @File : test_fixture_yield.py
# @Software: 装饰器--Fixture--yield关键字

"""
场景：
你已经可以将测试⽅法【前要执⾏的或依赖的】解决了，测试⽅法后销毁清除数据的要如何进⾏呢？

解决：
通过在 fixture 函数中加⼊ yield 关键字，yield 是调⽤第⼀次返回结果，第⼆次执⾏它下⾯的语句返回。

步骤：
在@pytest.fixture(scope=module)。
在登陆的⽅法中加 yield，之后加销毁清除的步骤

格式：
@pytest.fixture()
def fixture_name():
    setup操作
    yield 返回值1,返回值2
    teardown操作
"""
import pytest


@pytest.fixture(scope="class")
#定义了登录的fixture，尽量避免一test_开头
def login():
    print("登录操作")
    token = '123'
    yield
    print("退出登录操作")


def test_ss():
    print("搜索商品")


def test_gwc(login):
    print("添加购物车")
    print(f"token{login}")


def test_xd(login):
    print("下单操作")
