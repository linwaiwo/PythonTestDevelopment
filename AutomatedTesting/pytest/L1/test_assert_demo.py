# -*- coding: utf-8 -*-
# @Time : 2023/08/04 2:10 04
# @Author : 另外我
# @File : test_assert_demo.py
# @Software: Pytest用例断言--assert

"""
断言(assert)，是一种在程序中的一阶逻辑（如：一个结果为真或假的逻辑判断式），
目的是为了表示与验证软件开发者预期的结果，当程序执行到断言位置时，对应的断言应该为真，若断言不为真时，程序会中止执行，并给出错误信息（AssertionError）

断言写法：
assert	表达式
assert	表达式，描述
"""

class TestAssert:
    def test_assert(self):
        a = 5
        b = 10
        assert a < b ,f"a小于b"