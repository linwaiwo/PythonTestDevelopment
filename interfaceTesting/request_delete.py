# -*- coding: utf-8 -*-
# @Time : 2023/08/03 17:37
# @Author : 另外我
# @File : request_delete.py
# @Software: 发起delete请求

"""
构造HTTP协议中的DELETE请求

requests.delete(url, **kwargs)
url: 接口 url。
**kwargs：更多底层支持的参数。
"""
# 导入requests库
import requests


def del_pet():
    # 设置请求地址及删除宠物的id
    url = 'https://petstore.swagger.io/v2/pet/1234'
    # 发起delete请求
    result = requests.delete(url=url)
    # 打印请求结果，格式为json
    print(result.json())


del_pet()
