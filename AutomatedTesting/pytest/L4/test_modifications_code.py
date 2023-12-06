# -*- coding: utf-8 -*-
# @Time : 2023/8/5 14:38 05
# @Author : 另外我
# @File : test_modifications_code.py
# @Software: 修改默认编码

""""
含有中文的测试用例名称，改写编码格式：
pytest_collection_modifyitems配置见 conftest.py
"""
import pytest


@pytest.fixture(params=['张三', '李四'])
def modifications_code(request):
    print(f"{request.param}")
    # return request.param


def test_demo(modifications_code):
    print({modifications_code})
