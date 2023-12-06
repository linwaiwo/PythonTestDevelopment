# -*- coding: utf-8 -*-
# @Time : 2023/08/04 16:41 04
# @Author : 另外我
# @File : conftest.py
# @Software: Fixture 在自动化中的应用 - 数据共享
"""
场景：
你与其他测试⼯程师合作⼀起开发时，公共的模块要在不同⽂件中，要在⼤家都访问到的地⽅。

解决：
使⽤ conftest.py 这个⽂件进⾏数据共享，并且他可以放在不同位置起着不同的范围共享作⽤。

前提：
conftest ⽂件名是不能换的
放在项⽬下是全局的数据共享的地⽅

执⾏：
系统执⾏到参数 login 时先从本模块中查找是否有这个名字的变量什么的，
之后在 conftest.py 中找是否有。

步骤：
将登陆模块带@pytest.fixture 写在 conftest.py

"""

import pytest


@pytest.fixture()
# scope='function':设置作用域, autouse=True设置为自动应用
def login():
    print("登录操作")
    token = '123'
    yield
    print("退出登录操作")