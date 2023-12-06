# -*- coding: utf-8 -*-
# @Time : 2023/08/04 23:37 04
# @Author : 另外我
# @File : test_ordering.py
# @Software: 测试用例执行顺序自定义
"""
给用例打执行顺序标签
@pytest.mark.run(order=1)

执行顺序：小的正数-->大的正数-->未定义的数-->小的负数-->大的负数
"""

import pytest


@pytest.mark.run(order=2)
def test_ordering():
    print('case0')


@pytest.mark.run(order=1)
def test_ordering1():
    print('case1')

@pytest.mark.run(order=-1)
def test_ordering2():
    print('case2')


@pytest.mark.run(order=-2)
def test_ordering3():
    print('case3')


@pytest.mark.run()
def test_ordering4():
    print('case4')
