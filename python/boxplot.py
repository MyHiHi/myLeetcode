import pandas as pd
import matplotlib.pyplot as plt
path = r'C:\Users\Administrator\Desktop\文件\Python DataAnalysis\chapter3\demo\data\catering_sale.xls'


def analyse(path):
    data = pd.read_excel(path, index_col='日期')
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.rcParams['axes.unicode_minus'] = False
    plt.figure('test')
    p = data.boxplot(return_type='dict')
    x, y = p['fliers'][0].get_xdata(), p['fliers'][0].get_ydata()
    y.sort()
    for i, v in enumerate(zip(x, y)):
        a, b = v
        if i > 0:
            prev = y[i-1]
            plt.annotate(b, xy=(a, b), xytext=(a+0.05-0.8/(b-prev), b))
        else:
            plt.annotate(b, xy=(a, b), xytext=(a+0.08, b))

    x1, y1 = p['fliers'][1].get_xdata(), p['fliers'][1].get_ydata()
    y1.sort()
    for i, v in enumerate(zip(x1, y1)):
        a, b = v
        if i > 0:
            prev = y[i-1]
            plt.annotate(b, xy=(a, b), xytext=(a+0.05-0.8/(b-prev), b))
        else:
            plt.annotate(b, xy=(a, b), xytext=(a+0.08, b))
    plt.show()


analyse(path)
