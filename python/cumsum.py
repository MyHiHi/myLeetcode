import matplotlib.pyplot as plt
import pandas as pd
path = r'C:\Users\Administrator\Desktop\文件\Python DataAnalysis\chapter3\demo\data\catering_dish_profit.xls'
data = pd.read_excel(path, index_col='菜品名')
data = data['盈利'].copy()
# data.sort_index(ascending=False)
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
plt.figure()
data.plot(kind='bar')
plt.ylabel('盈利(元)')
p = 1.0*data.cumsum()/data.sum()
p.plot(color='r', secondary_y=True, style='-o',
       linewidth=2)
for x, y in enumerate(p):
    plt.annotate("(%d,%.4f)" % (x+1, y), xy=(x, y),  xytext=(-20, 10),
                 textcoords='offset points', color='y')

plt.annotate(format(p[6], '.4%'), xy=(6, p[6]),
             xytext=(6*0.9, p[6]*0.9),
             arrowprops=dict(arrowstyle='->', connectionstyle='arc3,rad=.2'))

plt.ylabel('盈利(比例)')
plt.show()
