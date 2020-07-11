# coding:utf-8
# author: Articuly
# datetime: 2020/7/3 9:53
# software: PyCharm

import numpy as np
from multiprocessing import Process


# 用while循环的方法
def fibona(n):
    a, b = 0, 1
    i = 1
    result = []
    while i <= n:
        print(a)
        result.append(a)
        a, b = b, a + b
        i += 1
    return result


p1 = Process(target=fibona, args=(1000000,))
p2 = Process(target=fibona, args=(1000000,))
p3 = Process(target=fibona, args=(1000000,))
p4 = Process(target=fibona, args=(1000000,))
p5 = Process(target=fibona, args=(1000000,))
p6 = Process(target=fibona, args=(1000000,))
p7 = Process(target=fibona, args=(1000000,))
p8 = Process(target=fibona, args=(1000000,))

if __name__ == '__main__':
    p1.start()
    p2.start()
    p3.start()
    p4.start()
    p5.start()
    p6.start()
    p7.start()
    p8.start()
