# -*- coding: utf-8 -*-
# @Time : 2023/09/03 0:43
# @Author : 另外我
# @File : interface_testing_example.py
# @Software: 接口测试实例
import requests
import pytest


class InterfaceTestingExample:
    # 类初始化
    def __init__(self):
        self.body = {"content": {
            "epub_url": "xxx",
            "total_size": "1459.30", "is_watermark": 0, "type": 1}}
        self.url = "https://www.baidu/xxx/1.0.0"
        cookie = '1234'
        self.header = {
            "Cooike": cookie
        }

    def send_request(self):
        resp = requests.post(url=self.url, json=self.body, headers=self.header)
        return resp

    @pytest.mark.parametrize((1, 2, 4))
    def test_total_size_is_null(self):
        self.body['content']['total_size'] = ''
        self.send_request()

    @pytest.mark('1234')
    def test_set_total_size_is_negative(self):
        self.body['content']['total_size'] = '-1'
        self.send_request()
