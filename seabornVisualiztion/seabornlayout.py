# coding=utf-8


# %matplotlib inline jupyter
import seaborn as sns
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats, integrate
import pandas as pd

sns.set(color_codes=True)
np.random.seed(sum(map(ord, "distributions")))
x = np.random.normal(size=100)
sns.distplot(x, kde=False)

# 切分成20小块
sns.distplot(x, bins=20, kde=False)

# 数据分布状态
x = np.random.gamma(6, size=200)
sns.distplot(x, kde=False, fit=stats.gamma)

# 根据均值和协方差生成数据
mean, cov = [0, 1], [(1, .5), (.5, 1)]
data = np.random.multivariate_normal(mean, cov, 200)
df = pd.DataFrame(data, columns=["x", "y"])

# 观察俩个变量之间发分布关系最好选用散点图
sns.jointplot(x="x", y="y", data=df)

"""
生成蜂窝图
"""
x, y = np.random.multivariate_normal(mean, cov, 1000).T
with sns.axes_style("white"):
    sns.jointplot(x=x, y=y, kind="hex", color="k")
