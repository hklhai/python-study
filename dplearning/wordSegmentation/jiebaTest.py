# coding=utf-8

import jieba

"""
https://blog.csdn.net/fontthrone/article/details/72782499#commentBox
"""

seg_list = jieba.cut("我来到北京清华大学", cut_all=True, HMM=False)
print("Full Mode: " + "/ ".join(seg_list))  # 全模式

seg_list = jieba.cut("我来到北京清华大学", cut_all=False, HMM=True)
print("Default Mode: " + "/ ".join(seg_list))  # 默认模式

seg_list = jieba.cut("他来到了网易杭研大厦", HMM=False)
print(", ".join(seg_list))

seg_list = jieba.cut_for_search("小明硕士毕业于中国科学院计算所，后在日本京都大学深造", HMM=False)  # 搜索引擎模式
print(", ".join(seg_list))
