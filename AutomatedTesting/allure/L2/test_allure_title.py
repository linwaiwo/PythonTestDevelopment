# -*- coding: utf-8 -*-
# @Time : 2023/8/5 19:48 05
# @Author : 另外我
# @File : test_allure_title.py
# @Software: Allure2报告中添加用例标题

"""
应用场景：
为了让生成的测试报告便于阅读，可以为每条用例添加一个便于阅读的标题（可以使用中文标题）。生成的报告展示用例时，就会以设置的标题名展示出来。
通过使用装饰器@allure.title可以为测试用例自定义一个可阅读性的标题。

allure.title的三种使用方式：
1、直接使用@allure.title为测试用例自定义标题。

2、@allure.title支持通过占位符的方式传递参数，可以实现测试用例标题参数化，动态生成测试用例标题。

3、allure.dynamic.title动态更新测试用例标题。
"""

import allure


# 方法一：直接使用@allure.title为测试用例自定义标题。
# @allure.title("这是 allure报告 标题 1")
# def test_title():
#     print('title')


# 方法二:@allure.title支持通过占位符的方式传递参数，可以实现测试用例标题参数化，动态生成测试用例标题。
# 参数化用例标题
# @allure.title("方法二参数化用例标题：{param1},{param2}")
# @pytest.mark.parametrize("param1,param2",
#                          ['张三',
#                           '李四']
#                          )
# def test_demo(param1, param2):
#     print(f'{param1}{param2}')


# 方法三：动态更新测试用例标题
# 使用allure.dynamic.title

@allure.title('方法三：这是原始标题')
def test_allure_title():
    print('动态更新测试用例标题')
    # allure.dynamic.title('方法三：这是更新后的测试用例标题')
