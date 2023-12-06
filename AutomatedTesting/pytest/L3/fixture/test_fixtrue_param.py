# -*- coding: utf-8 -*-
# @Time : 2023/08/04 17:11 04
# @Author : 另外我
# @File : test_fixtrue_param.py
# @Software: Fixture 在自动化中的应用 - 参数化

"""
场景：
测试离不开数据，为了数据灵活，⼀般数据都是通过参数传的

解决：
fixture 通过固定参数 request 传递

步骤：
在 fixture 中增加@pytest.fixture(params=[1, 2, 3, ‘zhangsan’])
在⽅法参数写 request，方法体里面使用 request.param 接收参数
"""
import pytest


# 设置参数化数据
@pytest.fixture(params=['zahngsan', 'lisi'])
def login(request):
    # 使用request.param接受参数
    print(f"{request.param}")
    return request.param


def test_login1(login):
    print(f"{login}")
