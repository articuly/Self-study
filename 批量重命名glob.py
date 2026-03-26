# coding:utf-8
import os
import glob
import re

path = r'E:\Downloads\techNASA天文图片'
os.chdir(path)
file_list = glob.glob(r'E:\Downloads\techNASA天文图片\*\*')


def parse_name(name: str) -> str:
    if name.endswith('_files'):
        name = name.replace('_files', '')
    if name.startswith('-'):
        name = name.replace('-', '')
    if re.search('\w-\s', name):
        name = name.replace('- ', ' - ')
    return name


# for f in file_list:
#     file_name = os.path.split(f)[-1]
#     if file_name != 'preview.jpg':
#         folder_name = os.path.split(f)[0]
#         folder_name = os.path.split(folder_name)[-1]
#
#         new_file_name = parse_name(folder_name) + '.jpg'
#         new_path = os.path.join(os.path.split(f)[0], new_file_name)
#         os.rename(f, new_path)
#         print(f, new_path)

for f in file_list:
    folder_name = os.path.split(f)[0]
    folder_name = os.path.split(folder_name)[-1]
    subfix = os.path.split(f)[-1].split('.')[-1]

    new_file_name = parse_name(folder_name) + '.' + subfix
    new_path = os.path.join(os.path.split(f)[0], new_file_name)
    os.rename(f, new_path)
    print(f, new_path)
