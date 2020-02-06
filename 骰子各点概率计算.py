import collections
import numpy as np

# 两个骰子
matrix2 = []
for i in range(1, 7):
    for j in range(1, 7):
        matrix2.append(i + j)

# print(np.resize(matrix2, (6, 6)))
print(collections.Counter(matrix2))
for k, v in collections.Counter(matrix2).items():
    print('N{0} : {1:.4f}%'.format(k, v * 100 / len(matrix2)), end=', ')
print('\n')

# 三个骰子
matrix3 = []
for i in range(1, 7):
    for j in range(1, 7):
        for k in range(1, 7):
            matrix3.append(i + j + k)

# print(np.resize(matrix3, (6, 6, 6)))
print(collections.Counter(matrix3))
for k, v in collections.Counter(matrix3).items():
    print('N{0} : {1:.4f}%'.format(k, v * 100 / len(matrix3)), end=', ')
print('\n')

# 四个骰子
matrix4 = []
for i in range(1, 7):
    for j in range(1, 7):
        for k in range(1, 7):
            for l in range(1, 7):
                matrix4.append(i + j + k + l)

# print(np.resize(matrix4, (6, 6, 6, 6)))
print(collections.Counter(matrix4))
for k, v in collections.Counter(matrix4).items():
    print('N{0} : {1:.4f}%'.format(k, v * 100 / len(matrix4)), end=', ')
print('\n')

# 五个骰子
matrix5 = []
for i in range(1, 7):
    for j in range(1, 7):
        for k in range(1, 7):
            for l in range(1, 7):
                for m in range(1, 7):
                    matrix5.append(i + j + k + l + m)

# print(np.resize(matrix5, (6, 6, 6, 6, 6)))
print(collections.Counter(matrix5))
for k, v in collections.Counter(matrix5).items():
    print('N{0} : {1:.4f}%'.format(k, v * 100 / len(matrix5)), end=', ')
print('\n')

# 六个骰子
matrix6 = []
for i in range(1, 7):
    for j in range(1, 7):
        for k in range(1, 7):
            for l in range(1, 7):
                for m in range(1, 7):
                    for n in range(1, 7):
                        matrix6.append(i + j + k + l + m + n)

# print(np.resize(matrix6, (6, 6, 6, 6, 6, 6)))
print(collections.Counter(matrix6))
for k, v in collections.Counter(matrix6).items():
    print('N{0} : {1:.4f}%'.format(k, v * 100 / len(matrix6)), end=', ')
print('\n')
