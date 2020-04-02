from sklearn import datasets
import numpy as np
# import matplotlib.pyplot as plt
# x = np.linspace(-10, 10, 1000)
# y = np.sin(x)+1
# z = np.cos(x**2)+1
# plt.figure(figsize=(8, 4))
# plt.plot(x, y, label='$sin(x)+1$', color='red')
# plt.plot(x, z, 'b--', label='$cos(x^2)+1$')
# plt.xlabel = 'Times(s)'
# plt.ylabel('Value')
# plt.title('Example')
# plt.legend(loc='upper right')
# plt.show()

# import pandas as pd
# np.random.seed(12)
# c = np.random.rand(1, 4, 5)
# print(c.max())

# data = pd.DataFrame(np.arange(16).reshape(
#     4, 4), index=list('abcd'), columns=list('ABCD'))
# print(data)
# print(data.loc['a':'c', 'A':'B'].T.mean())
# print(data.iloc[1:3, 1:2].mean()-12)
# e = pd.read_excel('D:\\3.16.xls', encoding='utf-8', skiprows=3)
# # print(e)
# r = e['午检体温']
# print(r.iloc[:, 0])
# c = pd.Series([1, 2, 3], index=['a', 'b', 'c'])
# print(c)
# a = pd.DataFrame([[1, 2, 3], [3, 4, 5]])
# print(a)
# d=pd.DataFrame(c);
# print(d)

from sklearn.linear_model import LinearRegression
model = LinearRegression()
# X = np.random.randint(1, 100, size=(100)).reshape((20, 5))
# Y = np.random.rand(20)
# # model.fit([[0, 0], [1, 1], [2, 2]], [0, 1, 2])
# # print(X, Y)
# model.fit(X, Y)
# v = model.predict([[1, 3, 2, 3, 4], [1, 45, 2, 3, 4]])
# print(v)
# print(model.coef_)


iris = datasets.load_iris()
model.fit(iris.data, iris.target)
print(model.coef_)
v = model.predict([[1.2, 3, 3.2, 1.4]])
print(v)
