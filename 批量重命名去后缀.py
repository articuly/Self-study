# coding:utf-8
import os
import re

# path='C:\\Users\\artic\Music\\Song'
path = r'E:\Documents\09.金融\BTC report'

f = os.listdir(path)

for i in f:
    # 替换名字的空格
    new = i.replace(' ', '-')
    os.chdir(path)
    os.rename(i, new)

    # fname, ext = os.path.splitext(i)
    # oldname = path + '\\{}'.format(i)

    # 修改特定后缀的名称
    # if re.match('.*?\[mqms2\]',i) or re.match('.*?\[weiyun\]', i):
    #     newname=path+'\\{0}{1}'.format(fname[:-8], ext)
    #     print(oldname, newname)
    #     try:
    #         os.renames(oldname, newname)
    #     except Exception as e:
    #         print(e)

    # 删除名称后缀
    # if re.match('.*?\[mqms\]', i):
    #     newname = path + '\\{0}{1}'.format(fname[:-7], ext)
    #     try:
    #         os.renames(oldname, newname)
    #     except Exception as e:
    #         print(e)

    # 修改包括特殊字符名称
    # if re.match('.*?&.*?', i):
    #     fname=fname.replace('&', ',')
    #     newname=path+'\\{0}{1}'.format(fname, ext)
    #     print(oldname)
    #     os.remove(oldname)
    #     os.renames(oldname, newname)
