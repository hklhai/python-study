# coding=utf-8


# %matplotlib inline jupyter
import seaborn as sns
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats, integrate
import pandas as pd

sns.set(style="whitegrid", color_codes=True)
np.random.seed(sum(map(ord, "categorical")))
titanic = sns.load_dataset("titanic")
tips = sns.load_dataset("tips")
iris = sns.load_dataset("iris")

sns.stripplot(x="day", y="total_bill", data=tips)
sns.stripplot(x="day", y="total_bill", data=tips, jitter=True)

sns.swarmplot(x="day", y="total_bill", data=tips)
sns.swarmplot(x="day", y="total_bill", hue="sex", data=tips)

# 盒图
sns.boxplot(x="day", y="total_bill", hue="time", data=tips)

# 小提琴图
sns.violinplot(x="day", y="total_bill", hue="time", data=tips)

sns.violinplot(x="total_bill", y="day", hue="time", data=tips, split=True)
