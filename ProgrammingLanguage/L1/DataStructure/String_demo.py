# -*- coding: utf-8 -*-
# @Time : 2023/08/20 16:58
# @Author : 另外我
# @File : string_demo.py
# @Software: 字符串

# def string_demo():
#     # 获取字符串个数 len()
#     a = "hello"
#     print(len(a))
#
#     # 检查字符串出现的次数 count()
#     a = "helloworld"
#     print(a.count("o"))
#     print(a.count("o", 6))
#
#     # 检查字符串中是否包含某个字符 indedx()
#     a = "helloworld"
#     print(a.index("o"))
#     print(a.index("o", 6))
#
#     # 检查字符串中是否包含某个字符(从右侧开始查找) rindedx()
#     a = "helloworld"
#     print(a.rindex("o"))
#     print(a.index("o", 1))
#
#     ##检查字符串中是否包含某个字符 find()
#     a = "helloworld"
#     print(a.find("l"))
#     print(a.find("l", 7))
#     print(a.find("k"))
#
#     # 检查字符串中是否包含某个字符(从右侧开始查找) rfind()
#     a = "helloworld"
#     print(a.rfind("l"))
#     print(a.rfind("l", 1, 6))
#     print(a.rfind("k"))
#
#     # 把string中的old替换成new replace()
#     a = "helloworld"
#     print(a.replace("l", "L"))
#     print(a.replace("l", "L", 2))
#
#     # 检查字符串是否以sub开头 startwith()
#     url = 'https://www.baidu.com/'
#     print(url.startswith("https://"))
#     print(url.startswith("https://", 2))
#     print(url.startswith("http://"))
#
#     # 检查字符串是否以sub结束 endwith()
#     url = 'https://www.baidu.com/'
#     print(url.endswith(".com/"))
#     print(url.endswith(".com/", 1, 5))
#     print(url.endswith(".com"))
#
#     # 判断string中至少有一个字符并且所有字符都是字母 isalpha()
#     B = "QWE"
#     print("*" * 10)
#     print("abc".isalpha())
#     print(B.isalpha())
#     print("ZXC".isalpha())
#     print("zxc1".isalpha())
#     print("ZXC1".isalpha())
#     print("123".isalpha())
#     print("#".isalpha())
#     print("#".isalpha())
#
#     #判断string中至少有一个字符并且所有字符都是数字 isdigiti()
#     print("*" * 10)
#     print("123".isdigit())
#     print("a1".isdigit())
#     print("a".isdigit())
#     print("A".isdigit())
#     print("#".isdigit())
#     print("#".isdigit())
#
#     #判断string中是否至少有一个字符并且所有字符都是数字或字母  isalnum()
#     print("*" * 10)
#     print("QWE".isalnum())
#     print("qwe".isalnum())
#     print("123".isalnum())
#     print("A1".isalnum())
#     print("a1".isalnum())
#     print("1A".isalnum())
#     print("1a".isalnum())
#     print("#$".isalnum())
#     print("".isalnum())
#
#     #判断string中是否包含空格  ispace()
#     print("*" * 10)
#     print(" ".isspace())
#     print("  ".isspace())
#     print("     ".isspace())
#     print("\t".isspace())
#     print("\n".isspace())
#     print("qwe".isspace())
#     print("123".isspace())
#     print("#".isspace())
#
#     #判断string中是否全是大写字母   isupper()
#     print('=' * 10)
#     print('QWE'.isupper())
#     print('QW1'.isupper())
#     print('QWe'.isupper())
#     print('QW#'.isupper())
#     print('qwe'.isupper())
#     print('123'.isupper())
#     print('#'.isupper())
#     print(''.isupper())
#
#     #islower()是判断dtring中是否全是小写字母
#     print("+"* 10)
#     print("qwe".islower())
#     print("QWE".islower())
#     print("qw1".islower())
#     print("qw#".islower())
#     print("123".islower())
#     print("#".islower())
#     print("".islower())
#
#     #istitle()是判断string中的单词是否标题化（单词首字母大写）
#     print('+'* 10)
#     print('Hello Wolrd'.istitle())
#     print('Hello_Wolrd'.istitle())
#     print('Hello wolrd'.istitle())
#     print('hello_Wolrd'.istitle())
#     print('hello_wolrd'.istitle())
#     print('Helloworld'.istitle())
#     print('HelloWorld'.istitle())
# string()


# def string():
# str = "测试"
# print(str.encode("gbk"))
# print(str.encode("utf-8"))
# str_a = b'\xe6\xb5\x8b\xe8\xaf\x95'
# print(str_a.decode('utf-8'))

# a = b'\xb2\xe2\xca\xd4'
# b = b'\xe6\xb5\x8b\xe8\xaf\x95'
# print(a.decode('gbk'))
# print(b.decode('utf-8'))


# a = 'hello'
# b = 'world'
# print(a+b)

# string()


# def string():
#     # a = "abcdefg"
#     # b = ['a','b','c','d','e','f']
#     # print(' '.join(a))
#     # print('+'.join(a))
#     # print('-'.join(a))
#     # print('->'.join(a))
#     # print(' '.join(b))
#     # print('-'.join(b))
#     # print('->'.join(b))
#
#     # print("a-b-c-d".split("-"))
#     # print("a-b-c-d".split("-", 2))
#     # print("a--b-c-d".split("-"))
#     # print("a-+b-c-d".split("-+"))
#     # print("a b\tc\nd\re".split())
#     # print("a b c d e".split(" ", 3))
#
#     # print("a\nb\nc".splitlines())
#     # print("a\nb\nc".splitlines(True))
#
#     # a = "1234567890"
#     # print(a[:])
#     # print(a[2:7])  # 指定2-7下标范围
#     # print(a[2])  # 下标为2的元素
#     # print(a[2:])  # 从2下标开始
#     # print(a[::-1])  # 倒序
#
#     # t = (1, 2, 2, 3.1, 1, 1, 1, 1, 1)
#     # print(t.index(1))
#     # print(t.index(1,3,9))
#     #
#     # l1 = [1, 2, 3.2, 1, 2, 555, 123, 1, 2]
#     # l1.append(456)
#     # print(l1)
#
#
#
# string()

d = {'name': "xiaolu", 'age': 15, 'address': 'beihai'}
print(d['age'])


def set_demo():
    s = {1, 2, 3}
    s1 = {4, 5, 6}
    s2 = {7, 8, 9, 10}
    res = s.union(s1)
    print(res)
    # 输出结果：{1, 2, 3, 4, 5, 6}
    result = s.union(s1, s2)
    print(result)
    # 输出结果:{1, 2, 3, 4, 5, 6, 7, 8, 9, 10}


set_demo()
