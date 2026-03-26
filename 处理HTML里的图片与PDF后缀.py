# coding:utf-8
import glob
import os
import re

path = r'D:\Downloads\note'
html_list = glob.glob(os.path.join(path, '*.html'))
old_list = glob.glob(os.path.join(path, '*.pdf.html'))
folder_list = glob.glob(os.path.join(path, '*.pdf_files'))

for h in html_list:
    fn = os.path.split(h)[-1].split('.')[0]
    new_path = os.path.join(path, fn + '.html')
    print(new_path)
    f = open(h, 'r', encoding='utf-8')
    t = open(new_path, 'w', encoding='utf-8')
    html_lines = f.readlines()
    html_lines = [line for line in html_lines if not re.search('pdf2htmlEX', line)]
    t.writelines(html_lines)
    f.close()
    t.close()

for o in old_list:
    print(o)
    os.remove(o)

for f in folder_list:
    fn = os.path.split(f)[-1]
    new_path = os.path.join(path, fn.replace('.pdf', ''))
    print(new_path)
    os.rename(f, new_path)
    

    