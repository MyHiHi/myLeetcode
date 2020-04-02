from sklearn.cluster import KMeans
import pandas as pd
import matplotlib.pyplot as plt
path = r'C:\Users\Administrator\Desktop\文件\Python DataAnalysis\chapter4\demo\data\discretization_data.xls'
data = pd.read_excel(path).iloc[:, 0].copy()
k = 4
# 等宽离散化
d1 = pd.qcut(data, k, labels=range(k))
# 等频率离散化
w = [1.0*i/k for i in range(k+1)]
w = data.describe(percentiles=w)[4:4+k+1]
w[0] = w[0]*(1-1e-10)
d2 = pd.cut(data, w, labels=range(k))

# 聚类离散化
kmodel = KMeans(n_clusters=k, n_jobs=2)
kmodel.fit(data.values.reshape((-1, 1)))
c = pd.DataFrame(kmodel.cluster_centers_).sort_values(0)
print(c)
print(c.rolling(2).mean())
w = c.rolling(2).mean().iloc[1:]
w = [0]+list(w[0])+[data.max()]
d3 = pd.qcut(data, w, labels=range(k))


def cluster_plot(d1, d2, d3, k):
    fig = plt.figure(figsize=(6, 8))
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.rcParams['axes.unicode_minus'] = False

    for i in range(k):
        ax = fig.add_subplot(221)
        ax.set_title("等宽离散化")
        ax.plot(data[d1 == i], [i for _ in d1[d1 == i]], 'o')
        ax = fig.add_subplot(222)
        ax.set_title('等频率离散化')
        ax.plot(data[d2 == i], [i for _ in d2[d2 == i]], 'o')
        ax = fig.add_subplot(223)
        ax.set_title('聚类离散化')
        ax.plot(data[d3 == i], [i for _ in d3[d3 == i]],
                'o')
    plt.legend()
    plt.ylim(-0.5, k-0.5)
    return plt


cluster_plot(d1, d2, d3, k).show()
