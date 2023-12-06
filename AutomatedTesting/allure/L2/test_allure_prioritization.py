# -*- coding: utf-8 -*-
# @Time : 2023/8/6 2:15 06
# @Author : 另外我
# @File : test_allure_prioritization.py
# @Software: 用例优先级

"""


Allure 对严重级别的定义分为 5 个级别：
Blocker级别：中断缺陷（客户端程序无响应，无法执行下一步操作）。
Critical级别：临界缺陷（ 功能点缺失）。
Normal级别：普通缺陷（数值计算错误）。
Minor级别：次要缺陷（界面错误与UI需求不符）。
Trivial级别：轻微缺陷（必输项无提示，或者提示不规范）。

使用装饰器添加用例方法/类的级别。
类上添加的级别，对类中没有添加级别的方法生效。
运行时添加命令行参数 --allure-severities： pytest --alluredir ./results --clean-alluredir --allure-severities normal,blocker
"""

import allure


# 未设置级别，默认为 Normal级别：普通缺陷（数值计算错误）。
# 未加级别标签的用例，在运行指定级别的时候，是不会被收集的
def test_with_no_severity_label():
    pass


# 给方法设置了 Trivial级别：轻微缺陷（必输项无提示，或者提示不规范）。
@allure.severity(allure.severity_level.TRIVIAL)
def test_with_trivial_severity():
    pass


# 给方法设置了 Normal级别：普通缺陷（数值计算错误）。
@allure.severity(allure.severity_level.NORMAL)
def test_with_normal_severity():
    pass


# 给一个类#设置了 Normal级别：普通缺陷（数值计算错误）。
@allure.severity(allure.severity_level.NORMAL)
class TestClassWithNormalSeverity(object):
    # 类里面的方法未设置级别的话，会默认继承父级类的 Normal级别：普通缺陷（数值计算错误）。
    def test_inside_the_normal(self):
        pass

    # 设置了Critical级别：临界缺陷（ 功能点缺失）
    @allure.severity(allure.severity_level.CRITICAL)
    def test_critical_severity(self):
        pass

    # 设置了 Blocker级别：中断缺陷（客户端程序无响应，无法执行下一步操作）。
    @allure.severity(allure.severity_level.BLOCKER)
    def test_blocker_severity(self):
        pass
