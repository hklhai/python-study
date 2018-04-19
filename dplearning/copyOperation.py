# coding=utf-8
import numpy as np

a = np.arange(12)
print(a)
# a and b are two names for the same nparray object
b = a
print(b is a)
b.shape = (3, 4)
print(a.shape)
print(id(a))
print(id(b))

"""
The view method creates a new array object that looks at same data. 
指向不一样，但是公用相同的值
"""
c = a.view()
print(c is a)
c.shape = 2, 6
print(a.shape)
c[0, 4] = 123
print(a)
print(id(a))
print(id(c))

"""
the copy method makes a complete copy of array and its data.
指向不一样，值也不一样
"""
d = a.copy()
print(d is a)
d[0, 0] = 9999
print(a)
print(d)

"""
排序及索引
"""
data = np.sin(np.arange(20)).reshape(5, 4)
print(data)

# 取出每列最大的值
ind = data.argmax(axis=0)
# 2 0 3 1
print(ind)

# print range(data.shape[1]) 0,1,2,3 指定0~3列
data_max = data[ind, range(data.shape[1])]
print(data_max)

"""
扩展
"""
a = np.arange(0, 40, 10)
print(a)
# 扩展
b = np.tile(a, (3, 5))
print(b)

"""
排序
"""
a = np.array([[4, 3, 5], [1, 2, 1]])
print(a)
# 按照行排序
b = np.sort(a, axis=1)
print(b)

a = np.array([4, 3, 1, 2])
# 排序后的下标
b = np.argsort(a)
print(b)
print(a[b])
