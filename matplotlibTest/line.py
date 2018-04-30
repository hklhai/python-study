# coding=utf-8

import pandas as pd
import matplotlib.pyplot as plt

unrate = pd.read_csv("D://python-study//matpltlib//UNRATE.csv")
# 转换时间格式函数to_datetime
unrate["DATE"] = pd.to_datetime(unrate["DATE"])
print(unrate.head(12))

"""
matplotlibTest 使用
"""
first_twelve = unrate[0:12]
plt.plot(first_twelve["DATE"], first_twelve["VALUE"])
plt.xticks(rotation=45)
plt.xlabel("Month")
plt.ylabel("Unemployment Rate")
plt.title("Title")
plt.show()

"""
双颜色作图
"""
unrate["MONTH"] = unrate["DATE"].dt.month
fig = plt.figure(figsize=(6, 3))
plt.plot(unrate[0:12]["MONTH"], unrate[0:12]["VALUE"], c="red")
plt.plot(unrate[12:24]["MONTH"], unrate[12:24]["VALUE"], c="blue")

plt.show()
