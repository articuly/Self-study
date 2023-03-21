# coding:utf-8

import re

with open(r'./test.txt', 'r', encoding='utf8') as f:
    txt = f.read()

pattern = re.compile(r'\d{4}-\d{2}-\d{2}')

matched = re.findall(pattern, txt)

print(len(matched))
print(matched)
