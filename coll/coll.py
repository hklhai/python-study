# coding=utf-8
import sys

a = [1, 2, 3]
print type(a)

a = [1, "ss", [2, 3, "33"], 3]
print type(a)
print a

# 遍历循环
for o in a:
    print o

# 有序列表
a = [x for x in range(10)]
print a
print dir(a)

a.append(10)
print(a)

b = [11, 12, 13]
a.append(b)
print a

# 合并
a.extend(b)
print a

print a.count(13)
print a.count(90)

# 插入字符串
a.insert(1, "a")
print(a)

# inster使用场景，在开发模块时，将模块路径插入path中
print sys.path
sys.path.insert(0, "/usr/local/test")
print sys.path


s = a.pop()
print(s)
print(a)

# remove 没有返回值,仅remove第一个发现的元素；使用remove需要小心元素不存在，使用try catch
a.remove(3)
print a

a.reverse()
print(a)


a = [1,4,2,9]
a.sort()
print(a)

print a[2]
b = a[:3]
print b

a = [1,2,3,4,5]
print a[-1]
print a[-3:-1]
a = [1,2,3,4,5]
print a[:-2]