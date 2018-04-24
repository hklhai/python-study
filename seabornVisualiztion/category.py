# coding=utf-8


# %matplotlib inline jupyter
import seaborn as sns
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats, integrate
import pandas as pd

titanic = sns.load_dataset("titanic")
sns.barplot(x="sex", y="survived", hue="class", data=titanic)

# 点图描述不同类别变化差异
sns.pointplot(x="sex", y="survived", hue="class", data=titanic)
