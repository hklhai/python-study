# coding=utf-8

if __name__ == "__main__":
    print("hello ")

a = 1
if a == 1:
    print(1)
elif a == 2:
    print(2)
else:
    print(3)

a = "你好"
print(a)

b = u"你好"
print(b)

a = ('a', 1, 2, 3, "sss")
for o in a:
    print(o)

import os

# files = os.listdir("C:\\Users\\lenovo\\Desktop\\excel")
# for ele in files:
#     print(ele)
path = "C:\\Users\\lenovo\\Desktop\\excel"
file_list = os.listdir(path)
file_path = [os.path.join(path, filename) for filename in file_list if filename.endswith('xlsx')]
for path in file_path:
    path = path.replace('\\', '\\\\')
    print(path)
