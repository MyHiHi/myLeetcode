import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import pandas as pd
import sys
import os
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
baseDir = '\\'.join(sys.path[0].split('\\')[:-2])
path = os.path.join(
    baseDir, 'Python DataAnalysis\chapter5\demo\data\consumption_data.xls')
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
# print(r)


# def density_plot(data, id):

#     p = data.plot(kind='kde', linewidth=2, subplots=True,
#                   sharex=False)
#     [p[i].set_ylabel(u'密度') for i in range(k-1)]
#     plt.legend()
#     plt.title('分群%d的概率函数密度图' % id, y=-0.5)
#     return plt


# for i in range(k):
#     density_plot(data[r['聚类类别'] == i], i+1).savefig(
#         os.path.join(sys.path[0], 'temp\%s%s.png' % ('da_', i)))
# print('****', '\n', data[r['聚类类别'] == i])
'''
TSNE 数据降维 、展示聚类结果
    TSNE是Laurens van der Maaten和Geoffrey Hintton在2008年提出的，
    它的定位是高维 数据的可视化。我们总喜欢能够直观地展示研究结果，聚类也不例外。
    然而，通常来说输入 的特征数是高维的（大于3维），一般难以直接以原特征对聚类结果进行展示。
    而TSNE提供 了一种有效的数据降维方式，让我们可以在2维或者3维的空间中展示聚类结果。

'''


def tsne(data):
    from sklearn.manifold import TSNE
    tsne = TSNE()
    tsne.fit_transform(data)
    tsne = pd.DataFrame(tsne.embedding_, index=data.index)
    styles = ['r.', 'go', 'b*', 'y.']
    print(tsne)
    for i in range(k):
        d = tsne[r['聚类类别'] == i]
        # print(d)
        plt.plot(d[0], d[1], styles[i])
    plt.colorbar()
    plt.show()


tsne(data_zs)
print('ok')
