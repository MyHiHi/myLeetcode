import matplotlib.pyplot as plt
from keras.layers.core import Dense, Activation
from keras import Sequential
import pandas as pd
import os
import sys
path = os.path.join(
    sys.path[0], 'Python DataAnalysis\chapter5\demo\data\sales_data.xls')
data = pd.read_excel(path, index_col='序号')
data[data == '好'] = 1
data[data == '是'] = 1
data[data == '高'] = 1
data[data != 1] = 0
x = data.iloc[:, :3].astype(int)
y = data.iloc[:, 3].astype(int)
model = Sequential()
model.add(Dense(input_dim=3, units=10))
model.add(Activation('relu'))
model.add(Dense(input_dim=10, units=1))
model.add(Activation('sigmoid'))
model.compile(loss='binary_crossentropy',
              optimizer='adam',)
model.fit(x, y, epochs=1000, batch_size=10)
yp = model.predict_classes(x).reshape(len(y))

# -*- coding: utf-8 -*-


def cm_plot(y, yp):

    from sklearn.metrics import confusion_matrix  # �������������

    cm = confusion_matrix(y, yp)  # ��������
    print('cm', cm)
    import matplotlib.pyplot as plt  # ������ͼ��
    # ����������ͼ����ɫ���ʹ��cm.Greens����������ο�������
    plt.matshow(cm, cmap=plt.cm.Greens)
    plt.colorbar()  # ��ɫ��ǩ

    for x in range(len(cm)):  # ���ݱ�ǩ
        for y in range(len(cm)):
            plt.annotate(cm[x, y], xy=(
                x, y), horizontalalignment='center', verticalalignment='center')

    plt.ylabel('True label')  # �������ǩ
    plt.xlabel('Predicted label')  # �������ǩ
    return plt


cm_plot(y, yp).show()
