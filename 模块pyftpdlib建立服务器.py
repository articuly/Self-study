# coding:utf-8

from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler, ThrottledDTPHandler
from pyftpdlib.servers import FTPServer
from pyftpdlib.log import LogFormatter
import logging

# 记录日志
logger = logging.getLogger()
logger.setLevel(logging.INFO)
ch = logging.StreamHandler()
fh = logging.FileHandler(filename='myftpserver.log', encoding='utf-8')  # 默认方式是追加到文件
ch.setFormatter(LogFormatter())  # 使用模块提供的日志格式
fh.setFormatter(LogFormatter())
logger.addHandler(ch)  # 将日志输出到屏幕
logger.addHandler(fh)  # 将日志输出到文件

# 实例化虚拟用户，这是FTP验证首要条件
authorizer = DummyAuthorizer()
authorizer.add_user('articuly', '123456', 'E:/', perm='elradfmw')
authorizer.add_anonymous('E:/')  # 匿名用户只需要路经

# 初始化FTP句柄
handler = FTPHandler
handler.authorizer = authorizer

# 添加被动端口范围
handler.passive_ports = range(2000, 2400)

# 上传下载速度设置
dtp_handler = ThrottledDTPHandler
dtp_handler.read_limit = 2 * 1024 * 1024
dtp_handler.write_limit = 2 * 1024 * 1024
handler.dtp_handler = dtp_handler

# 监听IP端口，Linux要root用户才能使用21端口
server = FTPServer(('127.0.0.1', 21), handler)

# 最大连接数
server.max_cons = 100
server.max_cons_per_ip = 16

# 开始服务
server.serve_forever()
