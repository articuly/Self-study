# coding:utf-8
sex = ''
age = ''
legal_input = ('F', 'M', 'f', 'm', '男', '女', 'Q', 'q')
while sex not in legal_input:
    sex = input('请输入您的性别（F/M）：')
    if sex not in legal_input:
        print('请进入与性别有关的词汇（F/M，男/女)')
    if sex in ('q', 'Q'):
        break

while (not age.isdigit()) & (sex not in ('q', 'Q')):
    age = input('请输入您的年龄：')
    if not age.isdigit():
        print('请输入一个正整数。')
    if age in ('q', 'Q'):
        break

print('***你今年的运势***')
if int(age) <= 18:
    if sex in ('M', 'm', '男'):
        print('你会考上清华并找到一个女盆友')
    else:
        print('你会考上清华并找到一个男盆友')
elif 18 < int(age) < 60:
    if sex in ('M', 'm', '男'):
        print('你会有好工作并找到一个女盆友')
    else:
        print('你会有好工作并找到一个男盆友')
elif 60 <= int(age) <= 120:
    if sex in ('M', 'm', '男'):
        print('你会与你老婆安享晚年')
    else:
        print('你会与你老公安享晚年')
else:
    print('你是在开玩笑吧。')
