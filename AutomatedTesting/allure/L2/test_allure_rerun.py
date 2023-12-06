# -*- coding: utf-8 -*-
# @Time : 2023/8/6 3:00 06
# @Author : 另外我
# @File : test_allure_rerun.py
# @Software: 用例失败重试

"""
Allure 可以收集用例运行期间，重试的用例的结果，以及这段时间重试的历史记录。
方法
重试功能可以使用 pytest 相关的插件，例如pytest-rerunfailures。
重试的结果信息，会展示在详情页面的”Retries” 选项卡中。
安装方法：pip install pytest-rerunfailures
"""

import pytest

#reruns:重试次数，reruns_delay：间隔时间
@pytest.mark.flaky(reruns=5, reruns_delay=3)
def test_rerun2():
    assert False
