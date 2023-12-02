# -*- coding: utf-8 -*-
# @Time : 2023/11/24 15:27
# @Author : 另外我
# @File : test_fixtrue.py
# @Software: 装饰器

import pytest


@pytest.fixture(scope='function')
# scope='function':设置作用域, autouse=True设置为自动应用
def login():
    print("登录操作")


def test_ss():
    print("搜索商品")


def test_gwc(login):
    print("添加购物车")


def test_xd(login):
    print("下单操作")
