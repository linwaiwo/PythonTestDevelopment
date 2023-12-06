# -*- coding: utf-8 -*-
# @Time : 2023/08/20 16:58
# @Author : 另外我
# @File : loop_while.py
# @Software: 逻辑结构-集合、集合运算

"""
集合是一种数据类型，用于存储多个元素，并确保元素的唯一性
集合中的元素是无序的，不可通过索引或切片进行访问
集合的主要特点是元素不重复，相同的元素在集合只会出现一次

使用大括号  { }  或 set() 函数来定义和创建集合

判断两个集合是否不相交
isdisjoint(other)如果集合中没有于other共有的元素则返回True

"""


def set_demo():
    # 判断两个集合是否不相交
    # isdisjoint(other) 如果集合中没有于other共有的元素则返回True
    a = {1, 2, 3}
    a1 = {4, 5, 6}
    a2 = {4, 5, 6, 7}
    print(a.isdisjoint(a1))
    print(a1.isdisjoint(a2))

    # 判断集合是否是另一个集合的子集
    # issubset()检测是否集合中的每一个元素都在other中
    print(a1.issubset(a2))

    # 判断集合是否是另一个集合的超集
    # issuperset()检测是否other中的每一个元素都在集合之中
    print(a2.issuperset(a1))

    # 并集
    # union(other)返回一个新集合，其中包含来自原集合以及other指定的所有元素，other可以指定多个集合
    s = {1, 2, 3}
    s1 = {4, 5, 6}
    s2 = {7, 8, 9}
    res = s.union(s1)
    print(res)
    result = s.union(s1, s2)
    print(result)

    s1 = {1, 2, 3, 4}
    s2 = {3, 4, 5, 6}
    # 交集
    # intersection(other)返回一个新集合，其中包含原集合以及other指定的所有集合中共有的元素
    res = s1.intersection(s2)
    print(res)

    # 差集
    # difference(other)返回一个新集合，包含原集合中在other指定的其他集合中不存在的元素
    result = s1.difference(s2)
    print(result)

    # 对称差集
    # symmetric_difference(other)返回一个新集合，其中的元素属于原集合或属于other指定的集合，但不能同时属于两者
    result_one = s1.symmetric_difference(s2)
    print(result_one)


if __name__ == '__main__':
    set_demo()
