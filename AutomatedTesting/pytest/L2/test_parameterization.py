# -*- coding: utf-8 -*-
# @Time : 2023/08/24 15:27
# @Author : 另外我
# @Software: pytest-参数化

# def inc(x):
#     return x + 1
#
#
# def test_answer():
#     assert inc(3) == 5


import pytest
# 单参数
# key = ['xiaolu','xiaoyang','xiaoli','xiaoqin']
#
# @pytest.mark.parametrize('sea_key',['xiaolu','xiaoyang','xiaoqin','xiao'])
#
# def test_sea(sea_key):
#     assert sea_key in key


# 多参数
# @pytest.mark.parametrize("user,passwd",[["userone","passwdone"],
#                                         ["usertwo","passwdtwo"],
#                                         ["userthree","passwdthree"]
#                                         ])
#
# def test_user(user,passwd):
#     print(f"用户{user},密码{passwd}")


# #ids给用例重命名
# @pytest.mark.parametrize("user,passwd",[["userone","passwdone"],
#                                         ["usertwo","passwdtwo"],
#                                         ["userthree","passwdthree"]
#                                         ],
#                          ids=["用户1","用户2","用户3"])
#
# def test_user(user,passwd):
#     print(f"用户名{user},密码{passwd}")


# #笛卡尔积
# @pytest.mark.parametrize("b",["a","b","c"])
# @pytest.mark.parametrize("a",[1,2,3])
#
# def test_inc(a,b):
#     print(f"a={a},b={b}")
