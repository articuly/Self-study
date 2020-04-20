# coding:utf-8
import pkuseg
from collections import Counter
import pprint

content = []
with open('2020.txt', encoding='utf-8') as f:
    content = f.read()

lexicon = ['老顾客', '沉寂顾客', '新购顾客']
seg = pkuseg.pkuseg(user_dict=lexicon)  # 加载模型，给定用户词典
text = seg.cut(content)

stopwords = []
with open('mystopword.txt', encoding='utf-8') as f:
    stopwords = f.read()

new_text = []
for w in text:
    if w not in stopwords:
        new_text.append(w)

# print(new_text)
counter = Counter(new_text)
pprint.pprint(counter.most_common(100))
