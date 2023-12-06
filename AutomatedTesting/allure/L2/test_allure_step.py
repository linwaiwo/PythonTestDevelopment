# -*- coding: utf-8 -*-
# @Time : 2023/8/5 21:10 05
# @Author : 另外我
# @File : test_allure_step.py
# @Software: Allure2 报告中添加用例步骤

"""
应用场景：
编写自动化测试用例的时候经常会遇到需要编写流程性测试用例的场景，一般流程性的测试用例的测试步骤比较多，我们在测试用例中添加详细的步骤会提高测试用例的可阅读性。
Allure 支持两种方法：
方法一：使用装饰器定义一个测试步骤，在测试用例中使用。
方法二：使用with allure.step():添加测试步骤。
"""
import allure


# 方法二：使用 with allure.step(): 添加测试步骤。

@allure.title('搜索用例')
def test_allure_step():
    with allure.step('测试步骤一'):
        print('操作一')
        print('操作二')

    with allure.step('测试步骤二'):
        print('操作三')
        print('操作四')
