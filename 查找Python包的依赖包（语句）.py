'''
获取一个Python包的依赖包（语句列表）
2018-06-24 1625：第一版，并不完善，短时间内也不准备完善了
'''
import os
import logging
import re

zllog = logging.getLogger("zl.yilai")


class ModuleYilai:
    '''
    找到模块依赖的模块：

    '''
    __module_path = ''
    __module_name = ''
    __yilai_modules = set()

    def __init__(self, module_path):
        '''
        输入模块的安装路径：绝对路径，不能为根目路“/”
        '''
        zllog.debug('ModuleYilai.__init__')

        # 检查module_path是否符合要求
        if not isinstance(module_path, str):
            print('moule_path (%s) is not str' % type(module_path))
            return

        if len(module_path) == 1:
            print('the length of module_path (%s) is 1' % module_path)
            return

        if not os.path.isabs(module_path):
            print('module_path (%s) is not an absolute path' % module_path)
            return

        if not os.path.isdir(module_path):
            print('module_path (%s) is not a directory' % module_path)
            return

        if not os.path.exists(module_path):
            print('module path (%s) does not exist' % module_path)
            return

        if module_path.endswith('//') or module_path.endswith('\\\\'):
            print('too many forward slashes or back slashes in the end of the module_path (%s)' % module_path)
            return

        # 目录下是否有__init__.py文件
        # 存在此文件，那么，这是一个package
        dl = os.listdir(module_path)
        try:
            dl.index('__init__.py')
        except:
            print('module_path (%s) is not a package: there is no __init__.py' % module_path)
            return

        # 检查完毕后，设置内部_module_path
        self.__module_path = module_path

        # 找出模块名称
        temp_path = module_path
        if temp_path.endswith('/') or temp_path.endswith('\\'):
            print('module_path processing...')
            temp_path = temp_path[:len(temp_path) - 1]

        last_slash_index = temp_path.rfind('/')
        if last_slash_index < 0:
            last_slash_index = temp_path.rfind('\\')

        self.__module_name = temp_path[last_slash_index + 1:]

        # 寻找模块依赖，并将找打的依赖模块存放到_yilai_modules中
        self._search_yilais()

    # 寻找模块依赖
    def _search_yilais(self):
        if self.__module_path == '':
            return

        # 1.找到模块下每一个目录（包括目录本身）
        dirlist = get_all_dirs(self.__module_path)
        zllog.debug('length of dirlist: ', len(dirlist))

        # 2.找到模块下每一个模块文件（*.py），将其绝对路径存入列表中
        pyfiles = []
        for item in dirlist:
            pyfiles.extend(get_all_pyfiles(item))
        zllog.debug('length of pyfiles: ', len(pyfiles))

        # 3.找到每一个模块文件的依赖模块
        fileyilais = []
        for item in pyfiles:
            fileyilais.extend(get_pyfile_yilais(item))
        zllog.debug('length of fileyilais: ', len(fileyilais))

        # 4.将fileyilais转换为set并将其存入实例的_yilai_modules中
        self.__yilai_modules = set(fileyilais)
        zllog.debug('length of self.__yilai_modules: ', len(self.__yilai_modules))

    # 获取模块名称
    def mod_name(self):
        return self.__module_name

    # 获取依赖的包的列表
    def yilais(self):
        return list(self.__yilai_modules)


# 判断一个文件夹是否是Python包
def ispackage(dirpath):
    try:
        dl = os.listdir(dirpath)
        dl.index('__init__.py')
        return True
    except:
        return False


# 找到dirpath下所有目录（包括目录本身），以列表形式返回
# 递归算法
# level为True时，添加目录本身，否则，不添加（查找子目录下的目录时不添加）
def get_all_dirs(dirpath, level=True):
    # 统一使用UNIX样式路径分隔符（/）
    # 替换后，Windows下也可以运行
    dirpath = dirpath.replace('\\', '/')

    dirlist = []

    # 添加目录自身
    if level:
        dirlist.append(dirpath)

    dl = os.listdir(dirpath)

    # 排除其中的__pycache__和test文件夹
    try:
        dl.remove('__pycache__')
        dl.remove('test')
    except:
        pass

    for item in dl:
        itempath = dirpath + '/' + item
        if os.path.isdir(itempath):
            # 将目录添加到返回列表中
            dirlist.append(itempath)

            # 执行get_all_dirs获取其下的目录并添加到dirlist中！
            dirlist.extend(get_all_dirs(itempath, level=False))

    return dirlist


# 找到diapath下所有Python模块（*.py文件），以列表形式返回
# dirpath为绝对路径
def get_all_pyfiles(dirpath):
    # 统一使用UNIX样式路径分隔符（/）
    # 替换后，Windows下也可以运行
    dirpath = dirpath.replace('\\', '/')

    rs = []

    if not os.path.isdir(dirpath):
        return

    dl = os.listdir(dirpath)
    for item in dl:
        itempath = dirpath + '/' + item
        # 检查是否是文件，是否要是py文件
        if os.path.isfile(itempath) and item.endswith('.py'):
            rs.append(itempath)

    return rs


# 获取一个Python模块（.py文件）导入的包
# 结果以列表形式返回
# 
# 可能的形式：
# 1.import sys
# 2.from __future__ import absolute_import
# 3.from socket import error as SocketError, timeout as SocketTimeout
# 4.
# from .connection import (
#     port_by_scheme,
#     DummyConnection,
#     HTTPConnection, HTTPSConnection, VerifiedHTTPSConnection,
#     HTTPException, BaseSSLError,
# )
# 5.
# if six.PY2:
#     # Queue is imported for side effects on MS Windows
#     import Queue as _unused_module_Queue  # noqa: F401
# 6.import mod1, mod2, mod3
# 7....
def get_pyfile_yilais(pyfile):
    '''
    格式很多，尚未完善！！
    '''
    rs = []

    if not os.path.isfile(pyfile):
        print('[get_pyfile_yilais] pyfile (%s) is not a file.' % pyfile)
        return rs

    with open(pyfile, 'r', encoding='utf-8') as f:
        content = f.read()

        # rs1 = re.findall('\n(from\s+.+)\s', content)
        # from可以在文件的开头，或者一行的开头，或者注释中，需要前面两种
        rs1 = re.findall('^(from\s+[\_\.0-9a-zA-Z]+)\s', content)
        rs2 = re.findall('\n(from\s+[\_\.0-9a-zA-Z]+)\s', content)
        # print('rs1 = ', rs1)
        # print('rs2 = ', rs2)

        rs3 = re.findall('^(import\s+.+)', content)
        rs4 = re.findall('\n(import\s+.+)', content)
        # print('rs3 = ', rs3)
        # print('rs4 = ', rs4)
        rs = rs1 + rs2 + rs3 + rs4

    return rs


if __name__ == '__main__':
    # 一些测试
    # m1 = ModuleYilai('C:\\Python36\\Lib\\sqlite3')
    # m2 = ModuleYilai('C:\\Python36\\Lib\\sqlite3\\')
    # m3 = ModuleYilai('C:\\Python36\\Lib')
    # m4 = ModuleYilai('C:\\Python36\\Lib\\')
    # m5 = ModuleYilai('C:/Python36/Lib/sqlite3')
    # m6 = ModuleYilai('C:/Python36/Lib/sqlite3/')
    # m7 = ModuleYilai('C:/Python36/Lib/sqlite3//')
    # m8 = ModuleYilai('C')
    # m9 = ModuleYilai('/')
    # m10 = ModuleYilai('\\')

    # 测试get_pyfile_yilais
    # get_pyfile_yilais('C:\\Python36\\Lib\\sqlite3\\dbapi2.py')
    # print()
    # get_pyfile_yilais('C:\\Python36\\Lib\\site-packages\\urllib3\\connectionpool.py')

    # 测试get_all_dirs
    # retlist = get_all_dirs('C:\\Python36\\Lib\\site-packages\\urllib3')
    # for item in retlist:
    #    print(item)

    # Test urllib3 module
    m1 = ModuleYilai(r'D:\Programing\Anaconda3\envs\ml_env\Lib\site-packages\sklearn')
    print('module name: ', m1.mod_name())
    print('length: ', len(m1.yilais()))
    print(m1.yilais())
    print()

    # Test of requests module
    m2 = ModuleYilai(r'D:\Programing\Anaconda3\envs\ml_env\Lib\site-packages\matplotlib')
    print('module name: ', m2.mod_name())
    print('length: ', len(m2.yilais()))
    print(m2.yilais())
    print()

    # Test of D:\\Users\\log
    m3 = ModuleYilai('D:\\Users\\log')
    print('module name: ', m3.mod_name())
    print('length: ', len(m3.yilais()))
    print(m3.yilais())
