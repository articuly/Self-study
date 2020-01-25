# coding:utf-8
import numpy as np

arr = np.array([[1, 2, 3],
                [4, 5, 6]])
arr + 5
arr * 2
1 / arr
arr ** 2
arr ** 0.5
# 在进行数组的四则运算的时候，我们需要保证二者的维数一样
arr - arr
# 这里的乘法是表示数组对应位置的元素相乘，并不是高等数学上的矩阵的乘法。当然了数组的加法和除法规则都类似
arr * arr
np.multiply(arr, arr)
arr_rnd = np.random.normal(5, 10, (3, 4))
arr_rnd
np.rint(arr_rnd)
x = np.random.normal(5, 10, (3, 1))
y = np.random.normal(5, 10, (3, 1))
x
y
np.maximum(x, y)
np.minimum(x, y)
np.greater(x, y)
np.less_equal(x, y)
# 矩阵的乘法，输入的2个数组的维度需要满足矩阵乘法的要求，否则会报错；
# arr.T表示对arr数组进行转置
# np.dot表示对输入的两个数组进行矩阵乘法运算
np.dot(arr, arr.T)
# 利用inv函数，求解矩阵的逆矩阵（注意：矩阵可变，首先必须是方阵）
from numpy.linalg import inv, solve

arr_lg = np.array([[0, 1, 2], [1, 0, 3], [4, -3, 8]])
arr_inv = inv(arr_lg)
arr_inv
np.dot(arr_lg, arr_inv)
# numpy.linalg中的函数solve可以求解形如 Ax = b 的线性方程组，其中 A 为矩阵，b 为一维数组，x 是未知变量
A = np.array([[1, -2, 1], [0, 2, -8], [-4, 5, 9]])
b = np.array([0, 8, -9])
X = solve(A, b)
X
s = np.dot(A, X)
np.equal(s, b)
np.max(arr_rnd)
np.max(arr_rnd, axis=0)
np.min(arr_rnd, axis=1)
# 利用自带的随机数生成函数生成5位选手的评委打分结果，一共有7位评委。打分结果用5×7大小的数组表示
votes = np.random.randint(1, 10, (5, 10))
votes
# 总分-最高分-最低分，再求平均，即可求得最终结果
(np.sum(votes, axis=1) - np.max(votes, axis=1) - np.min(votes, axis=1)) / 8
# where 函数中输入3个参数，分别是判断条件、为真时的值，为假时的值
# 在Numpy中，空值是一种新的数据格式，我们用np.nan产生空值
np.where(arr_rnd < 5, np.nan, arr_rnd)


# 定义函数，购买x件订单，返回订单金额
def order(x):
    if x >= 100:
        return 20 * 0.6 * x
    if x >= 50:
        return 20 * 0.8 * x
    if x >= 10:
        return 20 * 0.9 * x
    return 20 * x
# frompyfunc函数有三个输入参数，分别是待转化的函数、函数的输入参数的个数、函数的返回值的个数
income = np.frompyfunc(order, 1, 1)
# order_lst 为5位顾客的下单量
order_lst = [600, 300, 5, 2, 85]
# 计算当天的营业额
np.sum(income(order_lst))
