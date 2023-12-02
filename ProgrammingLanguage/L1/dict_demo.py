# -*- coding: utf-8 -*-
# @Time : 2023/08/24 15:27
# @Author : 另外我
# @Software: 字典

def dict_demo():
    # d = {}
    # d1 = {"name" : "Tom","age": 15}
    # print(type(d))
    # print(type(d1))

    # d1 = dict(one=1, two=2, three=3)
    # d2 = dict([('two', 2), ('one', 1), ('three', 3)])
    # #列表中包含多个元组
    # d3 = dict((('two', 2), ('one', 1), ('three', 3)))
    # #元组中包含多个元组
    # d4 = dict([('two', 2), ['one', 1], ('three', 3)])
    # #列表中包含元组和列表
    # d5 = dict({'one': 1, 'two': 2, 'three': 3})
    # d6 = dict({'one': 1, 'three': 3}, two=2)
    #
    # key = ["name","age","address"]
    # values = ("xiaoliu",18,"Beihai")
    # d7 = dict(zip(key,values))
    #
    # print(d1)
    # print(d2)
    # print(d3)
    # print(d4)
    # print(d5)
    # print(d6)
    # print(d7)

    d = {"name": "xiaoliu", "age": 18, "address": "Beihai"}
    print(d["age"])

    d = {"name": "xiaoliu", "age": 18, "address": "Beihai"}
    print(d["name"])
    # 修改值
    d["name"] = "xiaoli"
    print(d)
    # 增加键值对
    d["gender"] = "male"
    print(d)

    print('*' * 15)

    d1 = {"name": "xiaoyang", "age": 18, "address": "Beihai"}
    print(d1)
    del [d1["address"]]
    print(d1)


dict_demo()
