# coding=utf-8

# 元组是不可变对象,元组支持嵌套
# 列表使用场景频繁修改的情况，元组对于不修改仅查询使用，查询效率高
a = (1, 2, "22")
print(type(a))

for e in a:
    print(e)

b = [x for x in a]
print(b)

# 生成器
b = (x for x in a)
print(b)
print(b.next())
print(b.next())
print(b.next())

# 元组的索引操作
print(a[1])

# 格式化输出字符串
print('abcd %d and %s' % (66, "hello"))

b = ([1, 2, 3], 2)
print(type(b))
print(b)

# 修改元组内的嵌套列表
a = b[0]
a.append("s")
print(b)
