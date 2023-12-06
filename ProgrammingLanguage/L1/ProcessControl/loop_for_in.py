# -*- coding: utf-8 -*-
# @Time : 2023/08/21 14:45
# @Author : 另外我
# @Software: 逻辑结构-for-in循环

def loop_for_in():
    # 遍历字符串
    c = "hello"
    for c in c:
        print(c)
    s = "Hello !"

    # 输出前面示例中每个字符对应的ASCII码值。
    for c in s:
        print(f"字符【 {c} 】的ASCII码为：【 {ord(c)} 】")

    # 遍历元组
    t = (1, 2, 3, 4, 5)
    for n in t:
        print(n)

    # 输出前面示例元组中每个数字的立方值
    t = (1, 2, 3, 4, 5)
    for n in t:
        print(f"数字【 {n} 】的立方值为：【 {n * 3} 】")

    # 遍历列表
    requestMethods = ["get", "post", "put", "delete", "patch", "header", "options", 'trace']
    for method in requestMethods:
        print(f"method[{method.upper()}]")

if __name__ == '__main__':
    loop_for_in()

# 定义字典
requestMethods = {
    "get": "用于获取服务器上的资源，通过在URL中传递参数来发送请求。",
    "post": "用于向服务器提交数据，一般用于创建新的资源或进行修改操作。",
    "put": "用于更新服务器上的资源，一般用于修改已存在的资源的全部内容。",
    "delete": "用于删除服务器上的资源。"
}

# 遍历字典-keys
for method in requestMethods.keys():
    print(method)

# 遍历字典-vulues
for method in requestMethods.values():
    print(method)

# 遍历字典-键值对
for item in requestMethods.items():
    print(f"请求方式【 {item[0]} 】的作用为：【 {item[1]} 】")
    # print(item)
