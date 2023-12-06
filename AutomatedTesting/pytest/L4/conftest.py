# -*- coding: utf-8 -*-
# @Time : 2023/8/5 2:09 05
# @Author : 另外我
# @File : conftest.py
# @Software:内置函数--hook 改写

"""
1、hook 函数名字固定
2、hook 函数会被自动执行
3、执行是有先后顺序的
4、pytest 定义了很多 hook 函数，可以在不同阶段实现不同的功能
"""
from typing import Optional


# def pytest_runtest_setup(item: "Item") -> None:
#     print("hook : setup")
#
#
# def pytest_runtest_teardown(item: "Item", nextitem: Optional["Item"]) -> None:
#     print("teardown")

# 含有中文的测试用例名称，改写编码格式：
def pytest_collection_modifyitems(session, config, items):
    for item in items:
        item.name = item.name.encode('utf-8').decode('unicode-escape')
        item._nodeid = item.nodeid.encode('utf-8').decode('unicode-escape')
