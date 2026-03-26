# coding: utf-8
import glob
import os
import zipfile


def file2zip(zip_file_name: str, file_names: list):
    """ 将多个文件夹中文件压缩存储为zip

    :param zip_file_name:   /root/Document/test.zip
    :param file_names:      ['/root/user/doc/test.txt', ...]
    :return:
    """
    # 读取写入方式 ZipFile requires mode 'r', 'w', 'x', or 'a'
    # 压缩方式  ZIP_STORED： 存储； ZIP_DEFLATED： 压缩存储
    with zipfile.ZipFile(zip_file_name, mode='w', compression=zipfile.ZIP_DEFLATED) as zf:
        for fn in file_names:
            parent_path, name = os.path.split(fn)

            # zipfile 内置提供的将文件压缩存储在.zip文件中， arcname即zip文件中存入文件的名称
            # 给予的归档名为 arcname (默认情况下将与 filename 一致，但是不带驱动器盘符并会移除开头的路径分隔符)
            zf.write(fn, arcname=name)


def zip2file(zip_file_name: str, extract_path: str, members=None, pwd=None):
    """ 压缩文件内容提取值指定的文件夹

    :param zip_file_name: 待解压的文件  .zip          r'D:\Desktop\tst.zip'
    :param extract_path:  提取文件保存的目录           r'D:\Desktop\tst\test\test'
    :param members:       指定提取的文件，默认全部
    :param pwd:           解压文件的密码
    :return:
    """
    with zipfile.ZipFile(zip_file_name) as zf:
        zf.extractall(extract_path, members=members, pwd=pwd)


if __name__ == "__main__":
    path = r'E:\Downloads\@note扫描版'
    os.chdir(path)
    file_list = glob.glob(os.path.join(path, '*.html'))
    for f in file_list:
        # print(f)
        fn = os.path.split(f)[-1].split('.')[0]
        dn = fn + '.pdf_files'
        dn_path = os.path.join(path, dn)
        if os.path.exists(dn_path):
            if os.path.isdir(dn_path):
                # print(f, dn_path)
                file2zip(zip_file_name=fn + '.zip', file_names=[f, os.path.join(dn_path, '*')])
                print(f'compress zip file: {fn}.zip')
        else:
            file2zip(zip_file_name=fn + '.zip', file_names=[f])
            print(f'create zip file: {fn}.zip')
