# coding=utf-8
import os
import xlrd
from numpy import *
import xlwt

title = ["A", "B", "C"]

# 在哪里搜索多个表格
filelocation = "C://Users//lenovo//Desktop//excel"
# 当前文件夹下搜索的文件名后缀
fileform = ".xlsx"
# 将合并后的表格存放到的位置
filedestination = "C://Users//lenovo//Desktop//"
# 合并后的表格命名为file
file = "Finance_All"

# 首先查找默认文件夹下有多少文档需要整合
filearray = []
f_list = os.listdir(filelocation)
for fileName in f_list:
    # os.path.splitext():分离文件名与扩展名
    if os.path.splitext(fileName)[1] == '.xlsx':
        filearray.append(filelocation+"//"+fileName)

print("在默认文件夹下有%d个文档" % len(filearray))
ge = len(filearray)
matrix = [None] * ge

# 下面是将所有文件读数据到三维列表cell[][][]中（不包含表头）
for i in range(ge):
    fname = filearray[i]
    bk = xlrd.open_workbook(fname)
    try:
        sh = bk.sheet_by_name("Sheet1")
    except:
        print("在文件%s中没有找到sheet，读取文件数据失败" % fname)
    nrows = sh.nrows
    matrix[i] = [0] * (nrows - 1)

    ncols = sh.ncols
    for m in range(nrows - 1):
        matrix[i][m] = ["0"] * ncols

    for j in range(1, nrows):
        for k in range(0, ncols):
            matrix[i][j - 1][k] = sh.cell(j, k).value
            # 下面是写数据到新的表格test.xls

# 是把表头写上
filename = xlwt.Workbook()
sheet = filename.add_sheet("hel")

for i in range(0, len(title)):
    if title[i][-1] == "*":
        crs = 1
        sheet.write_merge(0, 0, i, crs + i, title[i])
        # sheet.write(0, i, title[i][-2])
    elif i >= 4:
        merge_leng = i + 1
        sheet.write(0, merge_leng, title[i])
    else:
        sheet.write(0, i, title[i])

# 求和前面的文件一共写了多少行
zh = 1
for i in range(ge):
    for j in range(len(matrix[i])):
        for k in range(len(matrix[i][j])):
            sheet.write(zh, k, matrix[i][j][k])
        zh = zh + 1
print("我已经将%d个文件合并成1个文件，并命名为%s.xls." % (ge, file))
filename.save(filedestination + file + ".xls")
