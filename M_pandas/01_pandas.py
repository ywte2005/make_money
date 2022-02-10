"""
@Author  : 亚博
@Time    : 2021/9/2 10:36 上午
@introduction ：
    1. pandas 入门
"""
import time

import pandas as pd
import numpy as np

# 生成对象
# s = pd.Series([1, 2, 3, np.nan, 4, 5, np.nan])
# print(s)

# 生成带有时间范围的
dates = pd.date_range("2021-8-17", periods=6)
print(dates)

df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list("ABCD"))
print(df)
print('---')
# 查看头部数据
# print(df.head(1))
# 查看尾部数据
# print(df.tail(1))
# 显示索引
# print(df.index)
# 显示行
# print(df.columns)
# 将数据转换成numpy
# print(df.to_numpy())
# 统计概要
# print(df.describe())
# 选择单列
# print(df["B"])
# 切片
# print(df[0:3])
# print(df["20210818":"20210820"]) 包含18号和20号
# print(df.loc["20210818":"20210820", ["A", "B"]])
# 快速访问标量值
# print(df.at[dates[0], "A"])

# --------------------------------按位置选择-------------------------
# 整数位置：
# print(df.iloc[3])
# 整数切片
# print(df.iloc[3:5, 0:2])
# 整数列表按位置切片
# print(df.iloc[[1, 2, 4], [0, 2]])
# 整行切片
# print(df[0:3, :])
# 整列切片
# print(df.iloc[:, 1:3])
# 显示提取值
# print(df.[1, 1])
# 快速显示提取
# print(df.iat[1, 1])


# ----------------------------------按bool选择-------------------------
# print(df[df.A > 0])

# 用isin 筛选
df2 = df.copy()
df2["E"] = ['one', 'one', 'two', 'three', 'four', 'three']
# print(df2)
# print(df2[df2["E"].isin(["one", 'two'])])
s1 = pd.Series([1, 2, 3, 4, 5, 6], index=pd.date_range("2021-8-17", periods=6))
df2["F"] = s1
# print(df2)

# -------------------------赋值=-===============
# 按标签赋值
# df2.at[dates[0], "A"] = 0
# 按位置赋值
# df2.iat[0, 1] = 0
# 按numpy数组赋值
# df2.loc[:, "D"] = np.array([4] * len(df))
# print(df2)
# where 条件赋值
# df3 = df
# df[df > 0] = -df3
# print(df)
# 删除所有缺失值的行
df2.iat[1, 1] = np.nan
# 返回新矩阵不改变原有矩阵
# df2 = df2.dropna(how='any')
# 填充空失值
# df2 = df2.fillna(value=5)
# 提取nan的布尔掩码
# print(pd.isna(df2))

print(df.mean(1))