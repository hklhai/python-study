# coding=utf-8

def f1(a):
    def f2(b):
        return a + b

    return f2


q = f1(2)
p = f1(3)
print(q)
print(p)

print(q(3))
print(p(23))
