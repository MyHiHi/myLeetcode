from sklearn.cluster import KMeans
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
# data = pd.DataFrame(np.random.randn(4, 7))
# print(data)
# print(data.cumsum())
# print(data.kurt())
# print(data.cummax())


data = pd.DataFrame(np.random.randn(4))
data = pd.DataFrame([1, 2, 3, 4, 5])
# print(data)
data.columns = ['随机数']
print(data)
data = data.rolling(3).sum()[1:]
print(data)
# data.replace(np.nan, 0, inplace=True)
# fig, (ax1, ax2) = plt.subplots(2, 1)
# ax1.plot(data[data['随机数'] > 0], color='r')
# plt.legend('>0')
# ax1.plot(data[data['随机数'] <= 0],  color='g')
# plt.legend('<=0')
# plt.show()


# data = np.random.randn(1000)
# pd.DataFrame([data, data+1]).boxplot()
# plt.show()


# error = np.cos(np.arange(10))
# y = pd.Series(np.sin(np.arange(10)))
# y.plot(yerr=error, label='误差棒', legend=True)
# print(y, '**', error)
# plt.show()
data = np.random.randn(1200)
kmodel = KMeans(n_clusters=4, n_jobs=2)
kmodel.fit(data.reshape((-1, 1)))
print(kmodel.cluster_centers_)
