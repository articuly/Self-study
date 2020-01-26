# 平面直角坐标系中，有1000万个点，x坐标和y坐标都是分布在[0,1)，哪一个点距离点(0.5,0.5)最近呢？
import numpy as np
import matplotlib.pyplot as plt

p = np.random.random((1000000, 2))
x, y = np.hsplit(p, 2)
d = np.hypot(x - 0.5, y - 0.5)
i = np.argmin(d)
print(f'距离(0.5, 0.5)最近的点坐标是({p[i][0]},{p[i][1]})，距离是{d[i][0]}')

# 分析两只股票的关联关系和收益率。pa 和 pb 是两只股票连续30个交易日的股价数组。每日股价收益率定义为当日股价与前一个交易日股价差除以最后一个交易日的股价。
pa = np.array(
    [79.66, 81.29, 80.37, 79.31, 79.84, 78.53, 78.29, 78.51, 77.99, 79.82, 80.41, 79.27, 80.26, 81.61, 81.39, 80.29,
     80.18, 78.38, 75.06, 76.15, 75.66, 73.90, 72.14, 74.27, 75.27, 76.15, 75.40, 76.51, 77.57, 77.06])
pb = np.array(
    [30.93, 31.61, 31.62, 31.77, 32.01, 31.52, 30.09, 30.54, 30.78, 30.84, 30.80, 30.38, 30.88, 31.38, 31.05, 29.90,
     29.96, 29.59, 28.71, 28.95, 29.19, 28.71, 27.93, 28.35, 28.92, 29.17, 29.02, 29.43, 29.12, 29.11])
corr = np.corrcoef(pa, pb)
print(corr)
pa_re = np.diff(pa) / pa[:-1]
pb_re = np.diff(pb) / pb[:-1]
plt.plot(pa_re)
plt.plot(pb_re)
plt.show()
