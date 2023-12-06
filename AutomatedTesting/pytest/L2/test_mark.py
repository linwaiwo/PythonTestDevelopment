# -*- coding: utf-8 -*-
# @Time : 2023/08/04 14:19 04
# @Author : 另外我
# @File : test_mark.py
# @Software: 测试用例打标签

"""
场景:只执行符合要求的某一部分用例
解决: 在测试用例方法上加 @pytest.mark.标签名

执行: -m 执行自定义标记的相关用例
pytest -s test_mark.py -m=str
pytest -s test_mark.py -m str
pytest -s test_mark.py -m "not ios"
"""

import pytest


class TestDemo:
    # 给test_demo_str函数标记一个标签为：str_demo
    @pytest.mark.str_demo
    def test_demo_str(self):
        print("case1")

    # 给test_demo_list函数标记一个标签为：list_demo
    @pytest.mark.list_demo
    def test_demo_list(self):
        print("case2")
