# -*- coding: utf-8 -*-
# @Time : 2023/8/5 16:11 05
# @Author : 另外我
# @File : test_allure_demo.py
# @Software: allure报告生成 --alluredir方法（在线报告）

"""

在测试执行期间收集结果
pytest [测试用例/模块/包] --alluredir=./result/  (—alluredir这个选项 用于指定存储测试结果的路径)

生成在线的测试报告
allure serve ./result
"""


def test_allure1():
    print('case 1')


def test_allure2():
    print('case 2')


def test_allure3():
    print('case 3')
