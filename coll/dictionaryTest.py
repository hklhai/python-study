# coding=utf-8

a = {"a":1,"b":2}
print a
print type(a)

if a.has_key("b"):
    print(a["b"])

for o in a.iteritems():
    print(o)

for o in a.iteritems():
    print(o[0])
    print(o[1])

# 26