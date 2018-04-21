# coding=utf-8

import pandas as pd
import numpy as np

titanic_train = pd.read_csv("D://python-study//titanic_train.csv")
print(titanic_train.head())
# SibSp兄弟姐数量，Parch 父母孩子数量 Fare船票价格，Cabin船舱编号，Embaeked，登船地点
age = titanic_train["Age"]
print(age.loc[0:10])
age_is_null = pd.isnull(age)
print(age_is_null)
age_null_true = age[age_is_null]
print(age_null_true)
age_null_count = len(age_null_true)
print(age_null_count)

"""
平均年龄计算，总年龄除以总人数
"""
mean_age = sum(titanic_train["Age"]) / len(titanic_train["Age"])
print(mean_age)

# filter out the missing values before we calculate the mean
good_age = titanic_train["Age"][age_is_null == False]
mean_age = sum(good_age) / len(good_age)
print(mean_age)

# 通常缺失值以平均值、或中位数代替
print(titanic_train["Age"].mean())

"""
index tells the method which column to group by 
values is the column that we want to apply the calculation to
aggfunc specifies the calculation we want to perform
"""
passenger_fare = titanic_train.pivot_table(index="Pclass", values="Fare", aggfunc=np.mean)
print(passenger_fare)

passenger_survival = titanic_train.pivot_table(index="Pclass", values="Survived", aggfunc=np.mean)
print(passenger_survival)
#  aggfunc=np.mean不指定，默认求均值操作
passenger_age = titanic_train.pivot_table(index="Pclass", values="Age")
print(passenger_age)

# 登船地点的总费用和总存活人数
passenger_stat = titanic_train.pivot_table(index="Embarked", values=["Fare", "Survived"], aggfunc=np.sum)
print(passenger_stat)

"""
丢失缺失值
"""
# specifying axis=1 or axis='columns' will drop any columns that have null values
drop_na_columns = titanic_train.dropna(axis=1)
new_titanic_train = titanic_train.dropna(axis=0, subset=["Age", "Sex"])
print(new_titanic_train)

print(titanic_train.loc[83, "Age"])
print(titanic_train.loc[766, "Pclass"])

"""
排序与reindex
"""
new_titanic_train = titanic_train.sort_values("Age", ascending=False)
print(new_titanic_train[0:10])
titanic_train_reindex = new_titanic_train.reset_index(drop=True)
print(titanic_train_reindex[0:10])

print("====================")


def hundredth_row(column):
    """
    自定义函数
    """
    return column.loc[99]


hundredth_row = titanic_train.apply(hundredth_row)
print(hundredth_row)


def null_col_count(column):
    col_null = pd.isnull(column)
    # print(col_null) 每一列为null的列向量
    null = column[col_null]
    return len(null)


print(titanic_train.apply(null_col_count))


# 转换
# by passing in the axis = 1 argument,we can use the DataFrame.apply() method to iterate over rows instead of origin
def which_class(row):
    pclass = row["Pclass"]
    if pd.isnull(pclass):
        return "Unknown"
    elif pclass == 1:
        return "First Class"
    elif pclass == 2:
        return "Second Class"
    elif pclass == 3:
        return "Third Class"


print(titanic_train.apply(which_class, axis=1))


# 年龄离散化
def is_minor(row):
    if row["Age"] < 18:
        return True
    else:
        return False


print(titanic_train.apply(is_minor, axis=1))


def generate_age_label(row):
    age = row["Age"]
    if pd.isnull(age):
        return "Unknown"
    elif age < 18:
        return "minor"
    else:
        return "adult"


age_labels = titanic_train.apply(generate_age_label, axis=1)
# 获救人数
titanic_train["age_labels"] = age_labels
age_survival = titanic_train.pivot_table(index="age_labels", values="Survived")
print(age_survival)


