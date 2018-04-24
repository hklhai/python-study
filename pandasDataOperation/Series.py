# coding=utf-8

import pandas as pd
import numpy as np

from pandas import Series

"""
Series结构
"""
# Series (collection of  values)
# DataFrame (collection of Series objects)
# Pandas(DataFrame(Series(numpy-ndarray)))
fandango_score_comparison = pd.read_csv("D://python-study//fandango_score_comparison.csv")
film = fandango_score_comparison["FILM"]
series_rt = fandango_score_comparison["RottenTomatoes"]
print(type(film))
print(film[0:5])

film_names = film.values
print(type(film_names))
rt_scores = series_rt.values

series_custom = Series(rt_scores, index=film_names)
print(series_custom)
a2 = series_custom[["Inside Out (2015)", "Mr. Holmes (2015)"]]
print("============")
print(a2)

original_index = series_custom.index.tolist()
sorted_index = sorted(original_index)
sorted_by_index = series_custom.reindex(sorted_index)
print(sorted_by_index)

print(series_custom.sort_index)
sc3 = series_custom.sort_values()
print(sc3[0:9])

# Series相加
print(np.add(series_custom, series_custom))
# apply sine function to each value
np.sin(series_custom)
# return the highest value (will return  a single value not a Series)
np.max(series_custom)

# 过滤大于50的值
series_custom_than_50 = series_custom[series_custom > 50]
print(series_custom_than_50)

# data alignment same index
rt_critics = Series(fandango_score_comparison["RottenTomatoes"].values, index=fandango_score_comparison["FILM"])
rt_users = Series(fandango_score_comparison["RottenTomatoes_User"].values, index=fandango_score_comparison["FILM"])
rt_mean = (rt_critics + rt_users) / 2
print(rt_mean)

print("========================")
# reindex 后仍然可以使用原有的数值index标引
film = fandango_score_comparison.set_index("FILM", drop=False)
print(film.index)
print("========================")
print(film["Hot Tub Time Machine 2 (2015)":"Shaun the Sheep Movie (2015)"])
# print(film.loc["Hot Tub Time Machine 2 (2015)":"Shaun the Sheep Movie (2015)"])
print(film.loc["Hot Tub Time Machine 2 (2015)":"Shaun the Sheep Movie (2015)"])

"""
类型转换
"""
types = fandango_score_comparison.dtypes
print(types)
float_col = types[types.values == "float64"].index
float_df = fandango_score_comparison[float_col]
print(float_df)

deviations = float_df.apply(lambda x: np.std(x))
# print(deviations)
""""
lambda 对每个指标计算标准差
"""
rt_mt_user = float_df[["RT_user_norm", "Metacritic_user_nom"]]
rt_mt_user.apply(lambda x: np.std(x), axis=1) # axis=1 表示行
print(rt_mt_user)
