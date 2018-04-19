# coding=utf-8

a = {"a": 1, "b": 2}
print(a)
print(type(a))

if a.has_key("b"):
    print(a["b"])

for o in a.iteritems():
    print(o)

for o in a.iteritems():
    print(o[0])
    print(o[1])

b = [x for x in a.iterkeys()]
print(type(a.iterkeys()))
print(b)

b = [x for x in a.itervalues()]
print(type(a.itervalues()))
print(b)

print(a.values())

# 排序
a = {"d": 2, "a": 1}
e = sorted(a, key=lambda x: x[0])
print(e)
print(a)
