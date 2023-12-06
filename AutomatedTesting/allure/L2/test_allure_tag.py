# -*- coding: utf-8 -*-
# @Time : 2023/8/6 2:38 06
# @Author : 另外我
# @File : test_allure_tag.py
# @Software: 添加用例标签-xfail、skipif、fixture

"""
应用场景
Allure 报告支持的一些常见 Pytest 特性包括 xfail、skipif、fixture 等。测试结果会展示特定的标识在用例详情页面。

标签-fixture
应用场景：fixture 和 finalizer 是分别在测试开始之前和测试结束之后由 Pytest 调用的实用程序函数。Allure 跟踪每个 fixture 的调用，并详细显示调用了哪些方法以及哪些参数，从而保持了调用的正确顺序。
"""

import pytest


# 当用例通过时标注为 xfail
@pytest.mark.xfail(reason='这是一个预期失败的用例')
def test_xfail_expected_failure():
    """this test is an xfail that will be marked as expected failure"""
    assert False


# 当用例通过时标注为 xpass
@pytest.mark.xfail
def test_xfail_unexpected_pass():
    """this test is an xfail that will be marked as unexpected success"""
    assert True


# 跳过用例
@pytest.mark.skipif('2 + 2 != 5', reason='当条件触发时这个用例被跳过 @pytest.mark.skipif')
def test_skip_by_triggered_condition():
    pass


# 添加 fixture 标签

@pytest.fixture()
def func1():
    print('前置动作')
    yield
    print('后置动作')


@pytest.fixture()
def func(request):
    # 前置动作，相当于setup
    print("这是一个fixture方法")

    # 后置动作，相当于teardown

    # 定义一个终结器，teardown动作放在终结器中
    def over():
        print("session级别终结器")

    # 添加终结器，在执行完测试用例之后执行终结器的内容
    request.addfinalizer(over)


class TestClass(object):
    def test_with_scoped_finalizers(self, func, func1):
        print("测试用例")
