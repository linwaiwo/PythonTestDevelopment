# -*- coding: utf-8 -*-
# @Time : 2023/08/04 16:58 04
# @Author : 另外我
# @File : test_fixtrue_aotuuse.py
# @Software: Fixture 在自动化中的应用 - 自动应用

"""
场景：
不想原测试⽅法有任何改动，或全部都⾃动实现⾃动应⽤，
没特例，也都不需要返回值时可以选择⾃动应⽤

解决：
使⽤ fixture 中参数 aotuuse=True 实现

步骤：
在⽅法上⾯加 @pytest.fixture(aotuuse=True)
"""
import pytest


#
@pytest.fixture(autouse=True)
# 定义了登录的fixture，尽量避免一test_开头
def login():
    print("登录操作")
    token = '123'
    yield
    print("退出登录操作")


def test_ss():
    print("搜索商品")


def test_gwc():
    print("添加购物车")
    print(f"token{login}")


def test_xd():
    print("下单操作")
