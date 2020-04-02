# -*- encoding: utf-8 -*-
'''
@File    :   pandas操作1.py
@Time    :   2020/03/26 21:37:47
@Author  :   Zhang tao 
@Version :   1.0
@Desc    :   pandas操作1.py
'''


import pandas as pd
import numpy as np
import random

# 转html
n = 10
data = pd.DataFrame({
    'col1': np.random.random_sample(10),
    'col2': np.random.random_sample(10),
    'col3': [[random.randint(0, n) for _ in range(3, 6)] for _ in range(n)]
})
# to_html
'''
with open('data_html.html', 'w') as f:
    f.write(data.to_html())
'''
# read_html
'''
data = pd.read_html('data_html.html')
print(type(data), data)
'''
# to_latex
'''
la = data.to_latex()
print(la)
'''
# date_range
'''
data_from = '2019/02/04'
data_to = '2019/07/09'
print(pd.date_range(data_from, data_to, freq='M').tolist())

'''
# add_chart
'''
df = pd.DataFrame(
    np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), columns=["a", "b", "c"])

report_name = 'd:\\example_report.xlsx'
sheet_name = 'Sheet1'
writer = pd.ExcelWriter(report_name, engine='xlsxwriter')
df.to_excel(writer, sheet_name=sheet_name, index=False)
workbook = writer.book
worksheet = writer.sheets[sheet_name]
# create a chart line object
chart = workbook.add_chart({'type': 'line'})
# configure the series of the chart from the spreadsheet
# using a list of values instead of category/value formulas:
#     [sheetname, first_row, first_col, last_row, last_col]
chart.add_series({
    'categories': [sheet_name, 1, 0, 3, 0],
    'values':     [sheet_name, 1, 1, 3, 1],
})
chart.set_x_axis({'name': 'Index', 'position_axis': 'on_tick'})
chart.set_y_axis({'name': 'Value', 'major_gridlines': {'visible': False}})
worksheet.insert_chart('E2', chart)
writer.save()
'''
# to_csv('d://data.gz', compression='gzip', index=False)
'''
df = pd.DataFrame(np.random.randn(4000, 400))
# df.to_csv('d://data.csv', index=False)
# print(pd.read_csv('d://data.csv'))

# df.to_csv('d://data.gz', compression='gzip', index=False)
# print(pd.read_csv('d://data.gz'))

'''
