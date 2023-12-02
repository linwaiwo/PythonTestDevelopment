# -*- coding: utf-8 -*-
# @Time : 2023/11/24 14:46
# @Author : 另外我
# @File : get_json.py
# @Software: PyCharm

import json


def get_json():
    # 获取json文件数据
    with open('data/123.json', 'r') as file:
        data = json.loads(file.read())
        print(list(data.values()))
        return data.values()


get_json()
