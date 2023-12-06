# -*- coding: utf-8 -*-
# @Time : 2023/08/20 16:58
# @Author : 另外我
# @File : loop_while.py
# @Software: 逻辑结构-while循环

def while_loop():
    # 三次内输入正确的密码
    passwd = "passwd"
    input_passwd = ""
    n = 0
    while input_passwd != passwd and n < 3:
        input_password = input("请输入密码: ")
        n += 1
        if input_password == passwd:
            print("密码正确，登录成功！")
        elif n == 3:
            print("三次输入密码错误")


def loop_a3():
    # 1-10之间的乘积
    n = 1
    res = 1
    while n <= 10:
        res *= n
        n += 1
        print(res)


# 打印100内7的倍数以及包含7的数字
def loop_func():
    n = 1
    while n <= 100:
        if n % 7 == 0 or "7" in str(n):
            print(n)
        n += 1


if __name__ == '__main__':
    loop_a3()
