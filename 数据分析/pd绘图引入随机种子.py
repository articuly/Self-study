import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

ibm_stock = pd.read_csv(r'D:\Programing\python_projects\Self-study\data_set\ibmclose.txt')
x = ibm_stock['Time']
y = ibm_stock['Price']
# 显示IBM股价
plt.figure()
plt.plot(x, y)
plt.title('IBM Stock Prices')
plt.xlabel('Date')
plt.ylabel('Closing Price')
plt.show()

# 引入随机种子
np.random.seed(0)
plt.figure()
plt.plot(x, y + np.random.randn(len(x)) * 10)
plt.title('IBM Stock Prices + random seed')
plt.xlabel('Date')
plt.ylabel('Closing Price')
plt.show()

test = pd.read_csv(r'D:\Programing\python_projects\Self-study\data_set\ibmclose rank.txt')
print(test)
rank1 = test.sort_values(by='Time')
print(rank1)
rank2 = test.sort_values(by='Price')
print(rank2)
