import os
import sys

import pandas as pd

baseDir = '\\'.join(sys.path[0].split('\\')[:-2])
path = os.path.join(
    baseDir, 'Python DataAnalysis\chapter5\demo\data\menu_orders.xls')

data=pd.read_excel(path)
ct=lambda x:pd.Series(1,index=x[pd.notnull(x)])
print()
