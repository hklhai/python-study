# coding=utf-8

def f1():
    print 1


f1()


def f1(a=1, b=2, c=3):
    print a
    print b
    print c
    return a, b


print f1()

f2 = lambda x, y: x + y
print(f2(1, 2))
