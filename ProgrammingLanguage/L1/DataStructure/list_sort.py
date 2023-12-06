# -*- coding: utf-8 -*-
# @Time : 2023/08/21 14:45
# @Author : 另外我
# @File : list_sort.py
# @Software: 列表去重并排序

def sort_data():
    data = [1, 34, 23, 2, 56, 78, 78, 9, 779, 9789, 1, 2, 0, 3, 4, 4]
    # 将列表装换成集合再转换成列表，利用集合的特性自动去重功能。
    new_data = list(set(data))
    # 对新的列表进行排序
    new_data.sort()
    print(new_data)
    print(type(new_data))
