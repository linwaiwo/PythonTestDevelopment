# -*- coding: utf-8 -*-
# @Time : 2023/08/04 14:29 04
# @Author : 另外我
# @File : test_raise.py
# @Software: pytest异常处理
"""
异常处理方法 try …except
try:
    可能产生异常的代码块
except [ (Error1, Error2, ... ) [as e] ]:
    处理异常的代码块1
except [ (Error3, Error4, ... ) [as e] ]:
    处理异常的代码块2
except  [Exception]:
    处理其它异常

异常处理方法 pytest.raise()
可以捕获特定的异常
获取捕获的异常的细节（异常类型，异常信息）
发生异常，后面的代码将不会被执行

"""
import pytest


def test_raise():
    with pytest.raises(ValueError, match='must be 0 or None'):
        raise ValueError("must be 0 or None")  # 执行成功
        # raise ZeroDivisionError("除数为0") #执行失败，因为捕获和抛出的类型不一致


def test_raise1():
    # 同时抛出多个异常
    with pytest.raises((ValueError, ZeroDivisionError)):
        raise ZeroDivisionError("除数为0")


def test_raise2():
    with pytest.raises(ValueError) as e:
        raise ValueError("value must be 10")
    # 获取异常类型和信息
    assert e.type is ValueError
    assert e.value.args[0] == "value must be 10"
