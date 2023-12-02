# -*- coding: utf-8 -*-
# @Time : 2023/08/20 16:58
# @Author : 另外我
# @File : loop_while.py
# @Software: 逻辑结构-集合、集合运算

def set_demo():
    a = {1, 2, 3}
    a1 = {4, 5, 6}
    a2 = {4, 5, 6, 7}

    print(a.isdisjoint(a1))
    print(a1.isdisjoint(a2))
    print(a1.issubset(a2))
    print(a2.issuperset(a1))

    s = {1, 2, 3}
    s1 = {4, 5, 6}
    s2 = {7, 8, 9}
    res = s.union(s1)
    print(res)
    result = s.union(s1, s2)
    print(result)

    s1 = {1, 2, 3, 4}
    s2 = {3, 4, 5, 6}
    res = s1.intersection(s2)
    print(res)
    result = s1.difference(s2)
    print(result)
    result_one = s1.symmetric_difference(s2)
    print(result_one)


if __name__ == '__main__':
    set_demo()
