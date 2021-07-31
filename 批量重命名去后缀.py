# coding:utf-8
import os
import re

path = 'C:\\Users\\artic\Music\\Song'

f = os.listdir(path)

for i in f:
    fname, ext = os.path.splitext(i)
    oldname = path + '\\{}'.format(i)
    # if re.match('.*?\[mqms2\]',i) or re.match('.*?\[weiyun\]', i):
    #     newname=path+'\\{0}{1}'.format(fname[:-8], ext)
    #     print(oldname, newname)
    #     try:
    #         os.renames(oldname, newname)
    #     except Exception as e:
    #         print(e)
    # if re.match('.*?\[mqms\]', i):
    #     newname = path + '\\{0}{1}'.format(fname[:-7], ext)
    #     try:
    #         os.renames(oldname, newname)
    #     except Exception as e:
    #         print(e)
    if re.match('.*?&.*?', i):
        fname = fname.replace('&', ',')
        newname = path + '\\{0}{1}'.format(fname, ext)
        print(oldname)
        # os.remove(oldname)
        # os.renames(oldname, newname)
