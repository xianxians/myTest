"""
语法： 文件对象.seek(偏移量, 起始位置)  0开头1当前2结尾
目标：
    1. r 改变文件指针位置：改变读取数据开始位置或把文件指针放结尾(无法读取数据)
    2. a 改变文件指针位置，做到可以读取出来数据
"""
# f = open('test.txt', 'r+')
f = open('test.txt', 'a+')

# 1. 改变读取数据开始位置
f.seek(0, 0)
# 1. 把文件指针放结尾(无法读取数据)
# f.seek(0, 2)

# 2. a 改变文件指针位置，做到可以读取出来数据
# f.seek(0, 0)
# f.seek(0)

con = f.read()
print(con)

f.close()

# tell() 函数用于判断文件指针当前所处的位置
f = open("test.txt",'r')
print(f.tell())
print(f.read(3))
print(f.tell())
print(f.read(3))
print(f.tell())
print(f.read(3))
print(f.tell())