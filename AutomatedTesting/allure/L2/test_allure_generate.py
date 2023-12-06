# -*- coding: utf-8 -*-
# @Time : 2023/8/5 16:43 05
# @Author : 另外我
# @File : test_allure_generate.py
# @Software: allure报告生成 --generate方法

"""
应用场景：如果希望随时打开报告，可以生成一个静态资源文件报告，将这个报告布署到 web 服务器上，启动 web 服务，即可随时随地打开报告。
解决方案：使用allure generate生成带有 index.html 的结果报告。这种方式需要两个步骤：
第一步：生成报告。
第二步：打开报告。

生成报告
allure generate ./result
打开报告
allure open ./report/

常用参数：
allure generate 可以指定输出路径，也可以清理上次的报告记录。
-o / –output 输出报告的路径。 （需要分析的中间结果文件也需要加上去，在-o之前）
-c / –clean 如果报告路径重复。
allure open 打开报告。
-h / –host 主机 IP 地址，此主机将用于启动报表的 web 服务器。
-p / –port 主机端口，此端口将用于启动报表的 web 服务器，默认值：0。

生成报告，指定输出路径，清理报告。
allure generate ./result -o ./report --clean

打开报告，指定IP地址和端口。
allure open -h 127.0.0.1 -p 8883 ./report/
"""


def test_allure1():
    print('case 1')


def test_allure2():
    print('case 2')


def test_allure3():
    print('case 3')
