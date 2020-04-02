import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
path = r'C:\Users\Administrator\Desktop\文件\Python DataAnalysis\chapter3\demo\data\catering_sale_all.xls'
data = pd.read_excel(path, index_col='日期')
datay = data.corr(method='pearson')['百合酱蒸凤爪'].sort_values(ascending=False)
# datay.plot(color='r', style='-o',
#            linewidth=2)
print(datay.iloc[:, [1]])

datay.to_excel('d:\\ff.xls')


plt.show()
data = data['百合酱蒸凤爪'].corr(data['翡翠蒸香茜饺'])
print(data)
