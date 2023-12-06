# -*- coding: utf-8 -*-
# @Time : 2023/12/5 1:51 05
# @Author : 另外我
# @File : test_hook.py
# @Software: 内置插件hook


"""
pytest hook 介绍：
是个函数，在系统消息触时被系统调用
是一个自动触发机制
Hook 函数的名称是确定的
pytest 有非常多的勾子函数
使用时直接编写函数体

pytest hook 的执行顺序：
pytest_addoption :添加命令行参数，运时会先读取命令行参数
pytest_collection_modifyitems : 收集测试用例，收集之后（改编码，改执行顺序）
pytest_collection_finish：收集之后的操作
pytest_runtest_setup：在调用 pytest_runtest_call 之前调用
pytest_runtest_call：调用执行测试的用例
pytest_runtest_makereport：运行测试用例，返回setup，call，teardown的执行结果

具体的执行顺序：
root
└── pytest_cmdline_main
├── pytest_plugin_registered
├── pytest_configure
│ └── pytest_plugin_registered
├── pytest_sessionstart
│ ├── pytest_plugin_registered
│ └── pytest_report_header
├── pytest_collection
│ ├── pytest_collectstart
│ ├── pytest_make_collect_report
│ │ ├── pytest_collect_file
│ │ │ └── pytest_pycollect_makemodule
│ │ └── pytest_pycollect_makeitem
│ │ └── pytest_generate_tests
│ │ └── pytest_make_parametrize_id
│ ├── pytest_collectreport
│ ├── pytest_itemcollected
│ ├── pytest_collection_modifyitems
│ └── pytest_collection_finish
│ └── pytest_report_collectionfinish
├── pytest_runtestloop
│ └── pytest_runtest_protocol
│ ├── pytest_runtest_logstart
│ ├── pytest_runtest_setup
│ │ └── pytest_fixture_setup
│ ├── pytest_runtest_makereport
│ ├── pytest_runtest_logreport
│ │ └── pytest_report_teststatus
│ ├── pytest_runtest_call
│ │ └── pytest_pyfunc_call
│ ├── pytest_runtest_teardown
│ │ └── pytest_fixture_post_finalizer
│ └── pytest_runtest_logfinish
├── pytest_sessionfinish
│ └── pytest_terminal_summary
└── pytest_unconfigure
"""


# hook配置见 conftest.py
def test_hook():
    print("hook")
