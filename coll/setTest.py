# coding=utf-8

a = [1, 1, 2, 3, 3, 4, 4, 5]
b = set(a)
print(type(b))
print(b)

# map
a = [1, 2, 3, 4]
b = map(lambda x: x * 2, a)
print(b)

# reduce
c = reduce(lambda x, y: x + y, a)
print(c)

# filter
d = filter(lambda e: e > 2, a)
print(d)
d = filter(lambda e: e % 2, a)
print(d)
d = filter(lambda e: e % 2 + 1, a)
print(d)
d = filter(lambda e: not e % 2, a)
print(d)

import os

b = os.walk(".")
print(b)

print([e for e in b])


# StopIteration
# b.next()


def fab(m):
    a, b = 1, 1
    while a < m:
        yield a
        a, b = b, a + b


def f(m):
    print(m)


b = fab(6)
print(type(b))

print(type(f))

print(b.next())
