# coding:utf-8
import os
import datetime

path = r'E:\发票'
now = datetime.datetime.now()
print(f'当前时间：{now.strftime("%Y-%m-%d %H:%M:%S")}')
for root, dirs, files in os.walk(path):
    for file in files:
        absFilePath = os.path.join(root, file)
        modifiedTime = datetime.datetime.fromtimestamp(os.path.getmtime(absFilePath))
        diffTime = now - modifiedTime
        print(
            f'{absFilePath:<36s}修改时间[{modifiedTime.strftime("%Y-%m-%d %H:%M:%S")}]距今[{diffTime.days:3d}天'
            f'{diffTime.seconds // 3600:2d}时{(diffTime.seconds % 3600) // 60:2d}分]')
