# -*- coding: utf-8 -*-
# @Time : 2023/08/03 17:01
# @Author : 另外我
# @File : request_get.py
# @Software: 发起GET请求


"""
Requests的优势
功能全面：HTTP、HTTPS支持全面
使用简单：简单易用，不用关心底层细节
定制性高：结合测试框架完成二次封装


构造HTTP协议中的GET请求
requests.get(url,params=None,**kwargs)
url=接口url
params=拼接在url的请求参数
kwargs=更多底层支持的参数

"""
# 导入requests库
import requests


def find_pet():
    # 设置请求地址&宠物id
    url = "https://petstore.swagger.io/v2/pet/1234"
    # 发起get请求
    result = requests.get(url=url)
    # 打印请求结果，格式为json
    print(result.json())


find_pet()
