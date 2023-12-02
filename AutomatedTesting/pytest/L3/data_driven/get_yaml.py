# -*- coding: utf-8 -*-
# @Time : 2023/11/24 22:42
# @Author : 另外我
# @File : get_yaml.py
# @Software: PyCharm

import yaml


# 获取yaml文件数据
def get_yaml():
    with open('data/123.yaml', 'r')as file:
        data = yaml.safe_load(file)
        print(data)
