# -*- coding: utf-8 -*-
# @Time : 2023/08/20 16:58
# @Author : 另外我
# @File : loop_nest.py
# @Software: 逻辑结构-循环嵌套


def loop_nest():
    data = [
        [1,2,3,4,5,6,7,8,9],
        ["A","B","C","D","E","F"],
        ["hello","python","pytest"]
    ]
    # for item in data:
    #     for i in item:
    #         print(i)

    l1 = len(data)
    i = 0
    while i < l1:
        item = data[i]
        l2 = len(item)
        j = 0
        while (j < l2):
            el = item[j]
            print(el)
            j += 1
        i += 1

def loop_nests():
    for i in range(1,10):
        for j in range(1,i+1):
            print(f"{j}*{i}={j*i:<3}",end=" ")
        print()

if __name__ == '__main__':
    # loop_nest()
    loop_nests()