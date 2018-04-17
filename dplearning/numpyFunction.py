# coding=utf-8
import numpy as np
from numpy import pi

print(np.arange(15))
a = np.arange(15).reshape(3, 5)
print a
print(a.shape)
# 矩阵维度dimensions
print(a.ndim)
print(a.dtype.name)

# 初始化0矩阵，入参要求元组
b = np.zeros((3, 4))
print(b)
b = np.zeros((3, 4), dtype=np.int32)
print(b)

# 构造序列 右开区间
c = np.arange(10, 30, 5)
print(c)
c = np.arange(0, 2, 0.2)
print(c)

a = np.arange(12).reshape(4, 3)
print(a)

"""
随机模块
"""
# np.random 模块，然后是进入random函数 值在(-1,1)
d = np.random.random((2, 3))
print(d)

"""
平均取100个值
"""
e = np.linspace(0, 2 * pi, 100)
print(e)

a = np.array([20, 30, 40, 50])
b = np.arange(4)
print a
print b
c = a - b
print c
c = c - 1
print c

d = b ** 2
print  d

"""
矩阵乘法
"""

A = np.array([[1, 1], [0, 1]])
B = np.array([[2, 0], [3, 4]])
# 对应位置相乘
print (A * B)
print (A.dot(B))
print(np.dot(A, B))
