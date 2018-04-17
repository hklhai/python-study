# coding=utf-8
import numpy

world_alcohol = numpy.genfromtxt("D:\python-study\world_alcohol.txt", delimiter=",", dtype=str)
print(type(world_alcohol))
print(world_alcohol)

vector = numpy.array([1, 2, 3, 4])
print(vector.shape)

matrix = numpy.array([[5, 10, 15], [23, 33, 44], [45, 67, 77]])
print(matrix.shape)

print(vector)
print (matrix)

"""
NumPy
"""
# Each value in a NumPy has to the same data type
numbers = numpy.array([1, 2, 3, 4])
print(numbers)
print(numbers.dtype)

numbers = numpy.array([1, 2, 3, 4.0])
print(numbers)
print(numbers.dtype)

"""
读取数据
"""
world_alcohol = numpy.genfromtxt("D:\python-study\world_alcohol.txt", delimiter=",", dtype=str, skip_header=1)
print(world_alcohol)
a25 = world_alcohol[1, 4]
a33 = world_alcohol[2, 2]
print(a25)
print(a33)

"""
左闭右开 
[1 2 3]
"""
vector = numpy.array([1, 2, 3, 4])
print(vector[0:3])

matrix = numpy.array([[5, 10, 15], [23, 33, 44], [45, 67, 77]])
# 第一行
print(matrix[:1])
# 第一列
print(matrix[:, 1])

# 第0列和第一列
print(matrix[:, 0:2])
print(matrix[1:3, 0:2])

numbers = numpy.array([1, 2, 3, 4])
print(2 == numbers)
print(15 == matrix)

"""
将bool值当做索引传入NumPy
"""

bo = 2 == numbers
print (numbers[bo])

matrix = numpy.array([[5, 10, 15], [23, 33, 44], [45, 67, 77]])
# 第二列是否包含25
second_col = matrix[:, 1] == 33
print(second_col)
print(matrix[second_col, :])

"""
矩阵基础
"""
numbers = numpy.array([1, 2, 3, 4])
bool_numbers = (numbers == 2) & (numbers == 3)
print(bool_numbers)

numbers = numpy.array([1, 2, 3, 4])
bool_numbers = (numbers == 1) | (numbers == 2)
print(bool_numbers)

numbers = numpy.array([1, 2, 3, 4])
bool_numbers = (numbers == 1) | (numbers == 2)
numbers[bool_numbers] = 20
print(numbers)

numbers = numpy.array(["1", "2", "3", "4"])
print(numbers.dtype)
numbers = numbers.astype(float)
print(numbers.dtype)
print(numbers)

numbers = numpy.array([1, 2, 3, 4])
print(numbers.min())

"""按照行求和"""
matrix = numpy.array([[5, 10, 15], [23, 33, 44], [45, 67, 77]])
# 1 each row，0 each column
print(matrix.sum(axis=1))
print(matrix.sum(axis=0))

