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
