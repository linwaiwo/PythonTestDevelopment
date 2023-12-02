# -*- coding: utf-8 -*-
# @Time : 2023/11/24 14:19
# @Author : 另外我
# @File : getcsv.py
# @Software: 数据驱动-csv

import csv


def get_csv():
    # 获取csv文件
    with open('data/123.csv', 'r') as file:
        res = csv.reader(file)
        data = []
        for i in res:
            data.append(i)
        print(data)


get_csv()
