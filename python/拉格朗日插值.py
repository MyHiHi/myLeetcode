import pandas as pd
import matplotlib.pyplot as plt
path = r'c:\Users\Administrator\Desktop\文件\Python DataAnalysis\chapter4\demo\data\catering_sale.xls'


def getData(path):
    data = pd.read_excel(path)
    data['销量'][(data['销量'] > 5000) | (data['销量'] < 400)] = None
    return data


def lagrange_solve(s, n, k=5):
  # 拉格朗日插值
    from scipy.interpolate import lagrange
    y = s.reindex(list(range(n-k, n))+list(range(n+1, n+1+k)))
    y = y[y.notnull()]
    return lagrange(y.index, list(y))(n)


if __name__ == "__main__":
    data = getData(path)
    print("********", data['销量'][2])
    for i in data.columns:
        for j in range(len(data)):
            if (data[i].isnull())[j]:
                data[i][j] = lagrange_solve(data[i], j)
    # data.to_excel(r'd:\\r.xls')
    opath = r'd:\\r.csv'
    # data = data.iloc[:, -1]
    # writer = pd.ExcelWriter(opath, )
    # data.to_excel(writer)
    data.to_csv(opath, index=False, mode='a', columns=['销量'])

    # writer.save()
