# -*- coding: utf-8 -*-
# @Time : 2023/08/04 13:38 04
# @Author : 另外我
# @File : test_command_parameter.py
# @Software:Python 代码执行 pytest


"""
使用 main 函数
使用 python -m pytest 调用 pytest（jenkins 持续集成用到）

if __name__ == '__main__':
1、运行当前目录下所有符合规则的用例，包括子目录（test_*.py 和 *_test.py）
pytest.main()

2、运行test_mark.py::test_模块中的某一条用例
pytest.main(['test_mark.py::test_','-vs'])

3、运行某个 标签
pytest.main(['test_mark.py','-vs','-m','str'])

运行方式
  `python test_*.py `

--lf（--last-failed） 只重新运行故障。
--ff（--failed-first） 先运行故障然后再运行其余的测试
"""
import pytest


class TestDemo:
    @pytest.mark.str_demo
    def test_demo_str(self):
        print("case1")

    @pytest.mark.list_demo
    def test_demo_list(self):
        print("case2")

    @pytest.mark.set_demo
    def test_demo_set(self):
        print("case3")


if __name__ == '__main__':
    # 运行当前目录下所有符合规则的用例
    # pytest.main()

    # 运行模块中的test_demo_str用例
    # pytest.main(['test_command_parameter.py::TestDemo::test_demo_str','-vs'])

    # 运行list_demo标签的用例
    pytest.main(['test_command_parameter.py::TestDemo', '-vs', '-m', 'list_demo'])
