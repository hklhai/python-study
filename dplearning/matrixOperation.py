# coding=utf-8

import numpy as np

B = np.arange(3)
print(B)
print(np.exp(B))
print(np.sqrt(B))

# floor 向下取整
a = np.floor(10 * np.random.random((3, 4)))
print(a)
# flatten the array
print(a.ravel())
a.shape = (6, 2)
print(a)
print(a.T)
# shape中如果指定-1，其它维度会自动计算
a.shape = (3, -1)
print(a)

"""
矩阵拼接
"""

a = np.floor(10 * np.random.random((2, 2)))
b = np.floor(10 * np.random.random((2, 2)))
print(a)
print(b)
# 增加特征
print(np.hstack((a, b)))
# 增加样本
print(np.vstack((a, b)))

"""
矩阵切分
"""
a = np.floor(10 * np.random.random((2, 12)))
print(a)
# 切分后得到3个 2 * 4的矩阵
print(np.hsplit(a, 3))

print(np.vsplit(a, 2))
# 指定位置切分 split a after the third and the fourth column
a = np.floor(10 * np.random.random((2, 12)))
print(a)

print(np.hsplit(a, (3, 4)))

a = np.floor(10 * np.random.random((12, 2)))
print(a)

print(np.vsplit(a, 3))
