import numpy as np

a = np.arange(9)
print(a[2:3])

b = np.arange(24).reshape(2, 3, 4)
print(b)
print(b[1][2][3])
# 这才是规范的用法
print(b[1, 2, 1])
print(b[0, :, :])
print(b[1, :, -1])

c = np.arange(12)
c.resize([3, 4])
c.ravel()
c.T
np.rollaxis(c, 0, 1)

np.append([[1, 2, 3]], [[4, 5, 6]])
np.append([[1, 2, 3]], [[4, 5, 6]], axis=0)
np.append([[1, 2, 3]], [[4, 5, 6]], axis=1)

d = np.arange(6).reshape(2, 3)
e = np.arange(6, 12).reshape(2, 3)
np.hstack((d, e))
np.vstack((d, e))
np.dstack((d, e))

f = np.arange(60).reshape(3, 4, 5)
g = np.arange(60).reshape(3, 4, 5)
np.stack((f, g), axis=0).shape
np.stack((f, g), axis=0)
np.stack((f, g), axis=1).shape
np.stack((f, g), axis=2).shape
np.stack((f, g), axis=3).shape

h = np.arange(12).reshape(3, 4)
np.vsplit(h, 3)
np.hsplit(h, 2)

dt = np.dtype([('name', 'S10'), ('age', int)])
i = np.array([("zhang", 21), ("wang", 25), ("li", 17), ("zhao", 27)], dtype=dt)
np.sort(i, order='name')
np.sort(i, order='age')

j = np.arange(10)
np.where(j < 5)
np.where(j > 5, j, j ** 2)

k = np.random.random((3, 4))
k
k[np.where(k > 0.5)]
k[(k > 0.3) & (k < 0.7)]
k[np.array([2, 1])]
k.ravel()
