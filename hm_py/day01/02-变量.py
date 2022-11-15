"""
1. 定义变量
    语法：变量名 = 值

2. 使用变量
3. 看变量的特点
"""

# 定义变量：存储数据TOM
my_name = 'TOM'
print(my_name)

# 定义变量：存储数据 黑马程序员
schoolName = '我是黑马程序员，我爱Python'
print(schoolName)

'''
Python数据类型
- Number 数字
- String 字符串
- List 列表
- Tuple 元组
- set 集合
- Dictionary 字
'''

a = 1
print(a)
print(type(a)) # <class 'int'> -- 整型
b = 1.1
print(type(b)) # <class 'float'> -- 浮点型
c = True
print(type(c)) # <class 'bool'> -- 布尔型
d = '12345'
print(type(d)) # <class 'str'> -- 字符串
e = [10, 20, 30]
print(type(e)) # <class 'list'> -- 列表
f = (10, 20, 30)
print(type(f)) # <class 'tuple'> -- 元组
h = {10, 20, 30}
print(type(h)) # <class 'set'> -- 集合
g = {'name': 'TOM', 'age': 20}
print(type(g)) # <class 'dict'> -- 字典
