import pandas as pd
path = r'C:\Users\Administrator\Desktop\文件\Python DataAnalysis\chapter3\demo\data\catering_sale.xls'
data = pd.read_excel(path, index_col='日期')
data = data[(400 < data['销量']) & (data['销量'] < 5000)]
statistics = data.describe()

statistics.loc['max-min'] = statistics.loc['max']-statistics.loc['min']
statistics.loc['变异系数'] = statistics.loc['std']/statistics.loc['mean']
statistics.loc['四分位距'] = statistics.loc['75%']-statistics.loc['25%']
