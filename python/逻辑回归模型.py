import random
import numpy as np
from sklearn.linear_model import LogisticRegression as LR
from stability_selection.randomized_lasso import RandomizedLogisticRegression as RLR
import pandas as pd
from stability_selection import StabilitySelection
path = r'C:\Users\Administrator\Desktop\文件\Python DataAnalysis\chapter5\demo\data\bankloan.xls'
data = pd.read_excel(path)
x = data.iloc[:, :8].as_matrix()
y = data.iloc[:, 8].as_matrix()
# print(x)
# 随机逻辑回归筛选特征，现在用不了
# selector = StabilitySelection(lambda_name='model__C').fit(x, y)
# print(selector.get_support(indices=True))
lr = LR()
# 逻辑回归模型训练
lr.fit(x, y)
# 模型准确率
print(lr.score(x, y))
v = random.randint(1, 60)
for i in range(v, v+10):
    print('true: ', y[i])
    print(lr.predict(x[i].reshape((1, -1))))

