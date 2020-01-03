# coding:utf-8
import pandas as pd
import numpy as np

# 导包，根据列表，利用Series函数创建Series数据
# 这里是根据列表进行Series的创建，也可以传入array数据格式
st = pd.Series([3.5, 7.2, 12.6, 4.7, 8.2],
               index=['300773', '600751', '300405', '002937', '601615'],
               name='Stock')
st
type(st)
st.name
st.index
# 查阅数据值，注意，该方法返回array格式
st.values
# Series的索引更为方便，你可以直接传入单个索引值进行检索
st['300773']
# 传入列表进行索引，返回格式仍是pandas.core.series.Series
st[['300773', '002937']]
# 利用布尔进行索引
st[[True, False, True, False, True]]
# 切片索引。要特别注意的是，对于index切片进行索引，pandas是左闭右闭的区间，这里和Python有明显不同
st['300773':'300405']
# 筛选出开盘价在8以上的个股
st[st > 8]
# 计算个股的双倍价格
st * 2
# 计算股票池的均价
np.average(st)
# 查看空值与非空值
st.isnull()
st.notnull()
# 修改index
st.index = ["拉卡拉", "海航科技", "科隆股份", "兴瑞科技", "明阳智能"]
st
# 如果数据被存放在字典中，也可以通过字典来创建Series

# 传入array类型，生成一个DataFrame数据结构
dff = pd.DataFrame(np.arange(12).reshape(3, 4),
                   index=[200, 201, 202], columns=['A', 'B', 'C', 'D'])
dff
# 利用字典生成DataFrame
data = {'a': [0, 3], 'b': [1, 4], 'c': [2, 5]}
dfg = pd.DataFrame(data, index=[11, 12])
dfg
# 用中括号传入对应的列名，可以进行列索引。索引的结果为Series格式
dff['A']
dff[['B', 'C']]
# 筛选A值为0的行
dff[dff['A'] == 0]
# 选择索引为2000的行
dff.loc[201]
# 选择“A”列
dff.loc[:, 'A']
dff.loc[202, 'B':'C']
# 通过位置，选择索引为2000的行
dff.iloc[0]
# 通过位置，选择“A”列
dff.iloc[:, 0]
# 这里要区分开来，涉及到位置切片，仍然为左闭右开的规则
dff.iloc[1, 1:]
