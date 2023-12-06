# -*- coding: utf-8 -*-
# @Time : 2023/08/03 17:17
# @Author : 另外我
# @File : request_put.py
# @Software: 发起put请求


"""
构造HTTP协议中的Put请求

requests.put(url, data=None, **kwargs)

url: 接口 url。
data：表单格式请求体。
**kwargs：更多底层支持的参数。
"""

# 导入requests库
import requests


def update_pet():
    # 设置url
    url = 'https://petstore.swagger.io/v2/pet'
    # 设置请求参数
    body = {
        "id": 1234,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    }
    # 发起put请求
    result = requests.put(url=url, json=body)
    # 打印请求结果，格式为文本
    print(result.text)


update_pet()
