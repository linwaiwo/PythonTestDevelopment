# -*- coding: utf-8 -*-
# @Time : 2023/8/5 21:45 05
# @Author : 另外我
# @File : test_allure_link.py
# @Software:报告中添加连接

"""
应用场景：
将报告与 bug 管理系统或测试用例管理系统集成，
可以添加链接装饰器:
 @allure.link、@allure.issue 和@allure.testcase。

 格式：
格式 1：@allure.link(url, name) 添加一个普通的 link 链接。
格式 2：@allure.testcase(url, name) 添加一个用例管理系统链接。
格式 3：@allure.issue(url, name)，添加 bug 管理系统链接。
"""
import allure


# 方法一:
# 使用name给链接起别名
@allure.link('http://www.baidu.com/', name='百度')
@allure.title('方法一：')
def test_with_link():
    print('报告中添加链接')


# 方法二:
test_link = 'http://www.baidu.com/'


@allure.title('方法二：')
@allure.testcase(test_link, '百度')
def test_with_link2():
    print('报告中添加链接')


# 方法三：
# 格式3：添加bug管理系统链接
# 这个装饰器在展示的时候会带 bug 图标的链接。可以在运行时通过参数 `--allure-link-pattern` 指定一个模板链接，以便将其与提供的问题链接类型链接模板一起使用。
# 执行命令需要指定模板链接：`--allure-link-pattern=issue:https://ceshiren.com/t/topic/{}`
@allure.title('方法三：')
@allure.issue("15860", 'bug管理系统')
def test_with_issue():
    print('报告中添加链接')
