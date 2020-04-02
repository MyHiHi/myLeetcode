import pywt
import pandas as pd
from scipy.io import loadmat
path = r'C:\Users\Administrator\Desktop\文件\Python DataAnalysis\chapter4\demo\data\leleccum.mat'
mat = loadmat(path)
signal = mat['leleccum'][0]
# wavedec()函数完成1D多阶次离散小波分解，\
# 返回系数数组list，[cAn, cDn, cDn-1, …, cD2, cD1]，n为分解阶次，
# cAn是逼近系数数组，后面的依次是细节系数数组。
coeffs = pywt.wavedec(signal, 'bior3.7', level=5)
for i in range(5+1):
    print(len(coeffs[i]))
# print(coeffs)
# print(pywt.families())
# # 印出每个小波族的每个小波函数
# for f in pywt.families():
#     print(f+": "+','.join(pywt.wavelist(f)))
