import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import pandas as pd
import sys
import os
path = os.path.join(
    sys.path[0], 'Python DataAnalysis\chapter5\demo\data\consumption_data.xls')
data = pd.read_excel(path, index_col='Id')
data_zs = 1.0*(data-data.mean())/data.std()
# print(data_zs)
k = 4
iteration = 500
model = KMeans(n_clusters=k, n_jobs=4, max_iter=iteration)
model.fit(data_zs)
centers = model.cluster_centers_
labels = model.labels_
r1 = pd.Series(labels).value_counts()
r2 = pd.DataFrame(centers)
r = pd.concat([r2, r1], axis=1)
r.columns = list(data.columns)+[u"类别数目"]
r = pd.concat([data, pd.Series(labels, index=data.index)], axis=1)
r.columns = list(data.columns)+[u'聚类类别']


def density_plot(data, id):
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.rcParams['axes.unicode_minus'] = False
    p = data.plot(kind='kde', linewidth=2, subplots=True,
                  sharex=False)
    [p[i].set_ylabel(u'密度') for i in range(k-1)]
    plt.legend()
    plt.title('分群%d的概率函数密度图' % id, y=-0.5)
    return plt


for i in range(k):
    density_plot(data[r['聚类类别'] == i], i+1).savefig(
        os.path.join(sys.path[0], 'temp\%s%s.png' % ('da_', i)))
    print('****', '\n', data[r['聚类类别'] == i])
print('ok')
