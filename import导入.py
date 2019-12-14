import requests

test = requests.get("http://news.baidu.com")
print(test.content)

import random

for i in range(10):
    value = random.randint(1, 100)
    print(value, end=', ')

from math import pi, sqrt

print(pi)
print(sqrt(3))
