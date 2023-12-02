# -*- coding: utf-8 -*-
# @Time : 2023/08/24 15:27
# @Author : 另外我
# @Software: pytest-mark打标签

import sys
import pytest

# 跳过
@pytest.mark.skipif(sys.platform == "darwin", reason="当前系统为windows")
def test_one():
    print("one")


def test_two():
    pytest.skip(reason="当前用例已知bug")
    print("two")


def test_three():
    print("three")

# 预期失败
@pytest.mark.xfail
def test_one():
    print("one")
    assert 1 == 2

def test_two():
    print("two")