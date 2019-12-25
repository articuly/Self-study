# coding:utf-8
import numpy as np

data0 = [2, 4, 6.5, 8]
arr0 = np.array(data0)
# 创建多维数组
data1 = [[1, 2, 3, 4], [5, 6, 7, 8]]
arr1 = np.array(data1)
# 利用dtype关键字，传入合适的数据类型，显式地定义
arr2 = np.array(data1, dtype=np.float32)
arr2
# 查看arr2的各维度的大小，其结果用tuple表示。tuple的长度，表示数组的维数；具体值表示数组的大小
arr2.shape
# 通过整形1和0，定义布尔类型的数组
data3 = [[1, 0], [0, 1]]
arr3 = np.array(data3, dtype=np.bool)
arr3
# 更改ndarray的数据类型
data6 = [[1.230, 2.670], [1.450, 6.000]]
arr6 = np.array(data6, dtype=np.float32)
arr6.astype(np.float16)
arr6
arr6.astype(np.int8)
arr6
print(arr6)
# 对浮点数数组，保留3位有效数字，并禁用科学计数法；小数位数不够，后面不会补0
arr7 = np.array([[3.141592653], [9.8]], dtype=np.float16)  # 定义一个2维数组
np.set_printoptions(precision=3, suppress=True)
arr7
# 创建一个大小为10的全0数组
np.zeros(10, dtype=np.int8)
# 创建一个大小为2×3的全0数组
np.zeros((2, 3), dtype=np.float16)
# 创建一个大小为2×3的全1数组
np.ones((2, 5), dtype=np.int16)
# empty 函数返回值为未经过初始化的垃圾值
np.empty((3, 3), dtype=np.int8)
# 创建一个大小为3×3的单位矩阵
np.identity(4)
# 创建3×4的矩形矩阵,eye函数，identity的升级版本
np.eye(N=3, M=4, dtype=np.int8)
# 创建4×5的矩形矩阵，并且为1的对角线向右偏移1个单位。
np.eye(N=4, M=5, k=1, dtype=np.int8)
# 指定 start、stop、以及step。arange和range一样，是左闭右开的区间。
np.arange(0,33,3)
np.arange(25)
np.arange(1,12,0.25)
# np.linspace(start, stop[, num=50[, endpoint=True[, retstep=False[, dtype=None]]]]])
arr8=np.linspace(1,100,num=30)
# 这里定义了一个长度为20的等差数组，然后通过reshape方法，调整数组的大小为6×5
arr8.reshape(6,5)
# geomspace()方法，创建指数等比数列
arr9=np.geomspace(2,1024,10,dtype=np.int16)
arr9
arr9.reshape(5,2)
# logspace()方法，创建对数等比数列
arr10=np.logspace(1,20,num=20,base=2)
arr10
arr10.reshape(5,4)
# 产生一个大小为3×2，符合0-1之间的均匀分布的数组,创建[0, 1)之间的均匀分布的随机数组
np.random.rand(1,100)
# uniform方法可以指定产生随机数的范围[low, high)，size为数组的形状，输入格式为整形（一维）或者整形元祖
# 如果不指定size的话，则返回一个服从该分布的随机数
np.random.uniform(1,100,size=(3,3,3))
# 该方法和rand类似，函数的输入为若干个整数，表示输出随机数的大小为d0×d1× ...×dn
# 如果没有参数输入，则返回一个服从标准正态分布的float型随机数
np.random.randn(10)
# loc:指定均值 μ; scale:指定标准差 σ
# size:输入格式为整形（一维）或者整形元祖，指定了数组的形状
np.random.normal(100,10,10)
np.random.normal()
# 函数返回区间[low, high)内的离散均匀抽样，dtype指定返回抽样数组的数据类型,默认为整形
# size:输入格式为整形（一维）或者整形元祖，指定了数组的形状
np.random.randint(1,9,(9,9))
# 从样本a中进行抽样，a可以为数组、列表或者整数，若为整数，表示[0,a)的离散抽样；
# replace为False，表示无放回抽样；replace为True，表示有放回抽样，可重复
# size为生成样本的大小
# p为给定数组中元素出现的概率
# numpy.random.choice(a, size=None, replace=True, p=None)
# 因为理想情况下，每次投篮都不影响下一次的结果，所以把这个问题归结为有放回的抽样，一共进行10次
# shoot_lst用来存储投篮的结果
shoot_lst=[]
for i in range(10):
    shoot=np.random.choice(['命中','未命中'],size=1,replace=True,p=[0.8,0.2])
    shoot_lst.append(shoot[0])
shoot_lst
