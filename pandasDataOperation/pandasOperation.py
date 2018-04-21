# coding=utf-8

import pandas

food_info = pandas.read_csv("D://python-study//food_info.csv")
print(type(food_info))
# pandas中的字符值为object
print(food_info.dtypes)
print(food_info.head())

print(food_info.head(3))
print(food_info.tail(3))
print(food_info.columns)
print(food_info.shape)

"""
索引与计算
"""

# pandas use zero-indexing
# Series object representing the row at index 0.
print(food_info.loc[0])

"""
类型对应
object： string
int：integer
float：float
datetime：time
bool：Boolean
"""

# return a Dataframe containing the rows at indexes 3,4,5 and 6
print(food_info.loc[3:6])

print(food_info["NDB_No"])

cols = ['NDB_No', 'Shrt_Desc']
print(food_info[cols])

"""
获取以g结尾的列名
"""
col_name = food_info.columns.tolist()
gram_col = []

for c in col_name:
    if c.endswith("(g)"):
        gram_col.append(c)

gram_df = food_info[gram_col]
print(gram_df.head(3))

# mg 转换成 g
div = food_info["Iron_(mg)"] / 1000
print(div)

"""
计算两列乘积
插入一列
"""
water_energy = food_info["Water_(g)"] * food_info["Energ_Kcal"]
print(water_energy)

iron_grams = food_info["Iron_(mg)"] / 1000
print(food_info.shape)
food_info["Iron_(g)"] = iron_grams
print(food_info.shape)

max_kcal = food_info["Energ_Kcal"].max()
print(max_kcal)

# 每列都除以最大值
normalized_fat = food_info["Lipid_Tot_(g)"] / food_info["Lipid_Tot_(g)"].max()
normalized_protein = food_info["Protein_(g)"] / food_info["Protein_(g)"].max()
food_info["Normalized_Fat"] = normalized_fat
food_info["Normalized_Protein"] = normalized_protein
print(food_info.shape)

"""
数据预处理
"""
# Sorts the DataFrame in-place, rather than=True returning a new dataframe
food_info.sort_values("Sodium_(mg)", inplace=True)
print(food_info["Sodium_(mg)"])
food_info.sort_values("Sodium_(mg)", inplace=True, ascending=False)
print(food_info["Sodium_(mg)"])


