import pandas as pd
import numpy as np
from sklearn.decomposition import PCA
path = r'C:\Users\Administrator\Desktop\文件\Python DataAnalysis\chapter4\demo\data\principal_component.xls'

data = pd.read_excel(path, header=None)
# PCA并不是简单的剔除掉一些特征，而是将现有的特征进行一些变换，
# 选择最能表达该数据集的最好的几个特征来达到降维目的。
pca = PCA(n_components=2, copy=True)
pca.fit(data)
# 用X来训练PCA模型，同时返回降维后的数据。
dp = pca.fit_transform(data)
print(dp)
print(dp.shape)
# print(pca.components_)
# 返回所保留各个特征的方差百分比，与权重正比，如果n_components没有赋值，
# 则所有特征都会返回一个数值且解释方差之和等于1。
# print(pca.explained_variance_ratio_)
# 将降维后的数据转换成原始数据
p = pca.inverse_transform(dp)
print("**")
print(p)
# print(p.shape)
