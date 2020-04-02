import numpy as np
import pydotplus
from sklearn.externals.six import StringIO
from sklearn.tree import export_graphviz
from sklearn.tree import DecisionTreeClassifier as DTC
import pandas as pd
import os
import sys
path = os.path.join(
    sys.path[0], 'Python DataAnalysis\chapter5\demo\data\sales_data.xls')
data = pd.read_excel(path, index_col='序号')
data[data == '好'] = 1
data[data == '是'] = 1
data[data == '高'] = 1
data[data != 1] = -1
x = data.iloc[:, :3].astype(int)
y = data.iloc[:, 3].astype(int)
# print("**", x.columns)
dtc = DTC(criterion='entropy')
dtc.fit(x, y)

with open('D:\\tree.dot', 'w', encoding="utf-8") as f:
    f = export_graphviz(dtc, feature_names=x.columns, out_file=f)
print('ok')
# cmd:dot -Tpng tree.dot -o tree.png
