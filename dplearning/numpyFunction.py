# coding=utf-8
import numpy as np

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