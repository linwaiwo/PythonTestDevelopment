# -*- coding: utf-8 -*-
# @Time : 2023/08/04 1:51
# @Author : 另外我
# @File : test_case_compile_rule.py
# @Software: 用例编写规则

"""
类型	        规则
文件	        test_开头 或者 _test 结尾
类	        Test 开头
方法/函数	    test_开头
"""


# 定义测试类
class TestDemo:
    # 定义测试方法/函数
    def test_demo(self):
        print('case1')


if __name__ == '__main__':
    TestDemo.test_demo()
