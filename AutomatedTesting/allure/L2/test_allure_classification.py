# -*- coding: utf-8 -*-
# @Time : 2023/8/6 0:08 06
# @Author : 另外我
# @File : test_allure_classification.py
# @Software: 报告中添加用例分类epic-->feature-->story

"""
应用场景：可以为项目，以及项目下的不同模块对用例进行分类管理。也可以运行某个类别下的用例。
报告展示：类别会展示在测试报告的 Behaviors 栏目下。

Allure 提供了三个装饰器：
@allure.epic：敏捷里面的概念，定义史诗，往下是 feature。
@allure.feature：功能点的描述，理解成模块往下是 story。
@allure.story：故事 story 是 feature 的子集。

epic-->feature-->story

epic:需求				（登录）
feature：大的功能点	（QQ登录、微信登陆）
story：小的功能点		（登陆成功、登陆失败、特殊情况等）

"""
import allure


# 设置需求，例如：登录界面
@allure.epic('登录需求')
# 设置需求下的功能模块，例如：登陆成功
@allure.feature('功能模块')
class TestEpic:
    # 设置功能模块下的子功能，例如qq登录、微信登陆
    @allure.story('子功能一')
    @allure.title('用例一')
    def test_case1(self):
        print('case 1')

    @allure.story('子功能一')
    @allure.title('用例二')
    def test_case2(self):
        print('case 2')

    @allure.story('子功能二')
    @allure.title('用例三')
    def test_case3(self):
        print('case 3')

    @allure.story('子功能二')
    @allure.title('用例四')
    def test_case4(self):
        print('case 4')
