# coding=utf-8

import re

# r表示原生字符串，字符串内容出现\n不转义
p = re.compile(r"abc")
print(type(p))

m = p.match("abcdef")
print(m)
print(m.group())  # 返回SRE_Match对象

m = p.match("abddef")
print(m)  # 返回None

# . 除换行符的任意字符 DOTALL
m2 = re.compile(".")
p2 = m2.match("abb")
print(p2.group())

#  转义字符
m2 = re.compile("\.")
p2 = m2.match("bac.aa")
print(p2
)

m2 = re.compile("\.")
p2 = m2.match(".")
print(p2.group())


p2 = m2.findall("bac.bsb.sss")
print(p2)


# 字符集合
m3 = re.compile("[abc]")
p3 = m3.findall("abcderf")
print(p3)


p3 = m3.match("abcderf")
print(p3.group())


regular_v1 = re.findall(r"docs", "https://docs.python.org/3/whatsnew/3.6.html")
print(regular_v1)
