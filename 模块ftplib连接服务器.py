from ftplib import FTP

# 登陆FTP
ftp = FTP(host='127.0.0.1', user='articuly', passwd='123456')
# 设置编码，Windows中文系统可能要设置成gpk
ftp.encoding = 'utf-8'
# 列出目录内容
ftp.retrlines('LIST')
# 切换目录
ftp.cwd('Downloads')
# 列出目录内容
ftp.dir()
# 下载
ftp.retrbinary('RETR abc.txt', open('abc.txt', 'wb').write)
# 上传
ftp.storbinary('STOR ftpserver.py', open('模块pyftpdlib建立服务器.py', 'rb'))
# 打印目录下文件详情
for f in ftp.mlsd(path='torrents'):
    print(f)
