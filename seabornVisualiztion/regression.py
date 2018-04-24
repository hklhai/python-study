# coding=utf-8

import seaborn as sns
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats, integrate
import pandas as pd

# 两两关系
iris = sns.load_dataset("iris")
sns.pairplot(iris)

# 回归
np.random.seed(sum(map(ord, "regression")))
tips = sns.load_dataset("tips")
tips.head()

sns.regplot(x="total_bill", y="tip", data=tips)

sns.lmplot(x="total_bill", y="tip", data=tips)

# x基本不是连续值
sns.regplot(data=tips, x="size", y="tip")
#  增加小范围浮动
sns.regplot(x="size", y="tip", data=tips, x_jitter=.05)
