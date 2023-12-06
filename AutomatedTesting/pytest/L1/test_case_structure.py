# -*- coding: utf-8 -*-
# @Time : 2023/08/04 1:54
# @Author : 另外我
# @File : test_case_structure.py
# @Software: 测试用结构

"""
用例结构：
三部分构成
-用例名称
-用例步骤
-用例断言

类级别用例示例：
class TestXXX:
    def setup(self):
        # 资源准备
        pass

    def teardown(self):
        # 资源销毁
        pass

    def test_XXX(self):
        # 测试步骤1
        # 测试步骤2
        # 断言  实际结果 对比 预期结果
        assert ActualResult == ExpectedResult
"""