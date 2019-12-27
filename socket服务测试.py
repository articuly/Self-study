# coding:utf-8
import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.bind(('127.0.0.1', 13579))
sock.listen(2)
sock.listen()
runing = True
while runing:
    c_sock, c_addr = sock.accept()  # 响应连接请求，取得远程连接的套接字对象和地址
    welcome = '欢迎你, 来自%s:%d的同学\r\n' % c_addr
    c_sock.sendall(welcome.encode('gbk'))  # 回复欢迎辞

    while True:  # 接收客户端发送的信息
        cmd = b''
        while not cmd.endswith(b'\r\n'):  # 反复读，直到收到了回车换行（telnet客户端敲回车键）
            cmd += c_sock.recv(1024)

        cmd = cmd.strip()
        if cmd in [b'bye', b'quit', b'exit']:  # telnet客户端输入bye/quit/exit，回复再见并关闭连接
            bye = '再见'.encode('gbk')
            c_sock.sendall(bye + b'\r\n')
            c_sock.close()
            runing = cmd == b'bye'  # 如果是byr，则继续响应下一个连接请求，否则，结束服务程序
            break
        else:  # 回复telnet客户端发来的信息
            reply = '你说的是：'.encode('gbk')  # 信息包含中文，使用GBK编码才能在telnet客户端上正确显示
            c_sock.sendall(reply + cmd + b'\r\n')