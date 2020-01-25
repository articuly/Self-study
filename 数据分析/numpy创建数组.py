import numpy as np
import matplotlib.pyplot as plt

talls = np.random.normal(170, 4, 3000)
bins = np.arange(156, 190, 2)
plt.hist(talls, bins)
plt.show()

a = np.arange(5)
# 重复元素3次
np.repeat(a, 3)
# 重复数组3次
np.tile(a, 4)
# 重复数组3行2列
np.tile(a, (3, 2))

b = np.arange(24).reshape((3, 4, 2))
b
np.repeat(b, 3)
np.repeat(b, 3, axis=0)
np.repeat(b, 3, axis=1)
np.repeat(b, 3, axis=2)
np.tile(b, 2)
np.tile(b, (2, 3))

lon = np.linspace(-180, 180, 37)
lat = np.linspace(-90, 90, 19)

lons, lats = np.meshgrid(lon, lat)
lons.shape
lons
lats.shape
lats

# 构造网格，除了 np.meshgrid() 之外，还有一个更牛的方法，可以直接生成纬度网格和经度网格（请注意，纬度在前，经度在后）
# 网格精度为5°，网格shape为(37,73)
lats, lons = np.mgrid[-90:91:5., -180:181:5.]
lons.shape, lats.shape
# 也可以用虚实指定分割点数，网格精度同样为5°
lats, lons = np.mgrid[-90:90:37j, -180:180:73j]
lons.shape, lats.shape

lons = np.radians(lons)
lats = np.radians(lats)
z = np.sin(lats)
x = np.cos(lats) * np.sin(lons)
y = np.cos(lats) * np.sin(lons)
import mpl_toolkits.mplot3d

ax = plt.subplot(111, projection='3d')
ax.plot_surface(x, y, z, cmap=plt.cm.coolwarm, alpha=0.8)
plt.show()
