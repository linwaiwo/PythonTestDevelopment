# -*- coding: utf-8 -*-
# @Time : 2023/08/03 17:07
# @Author : 另外我
# @File : request_post.py
# @Software: 发起post请求


"""
构造HTTP协议中的post请求

requests.post(url, data=None, json=None, **kwargs)

url: 接口 url。
data：表单格式请求体。
json：JSON 格式请求体。
**kwargs：更多底层支持的参数。
"""

# 引用requests库
import requests


def new_pet():
    # 设置json请求参数
    body = {
        "id": 1234,
        "category": {
            "id": 0,
            "name": ""
        },
        "name": "x",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": ""
    }
    # 设置请求Url
    url = "https://petstore.swagger.io/v2/pet"
    # 发起post请求
    result = requests.post(url=url, json=body)
    # 打印请求结果，格式为json
    print(result.json())


new_pet()
