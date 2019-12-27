# coding:utf-8
import socket, time
from poetries import POUETRIES  # 此处导入诗词库（poetries.py）


def poetries_server():
    """古诗词服务器"""

    delay = 0.1  # 诗词显示速度（字间隔时间）
    subjects = [item.split()[0] for item in POUETRIES]  # 诗词目录
    welcome = '欢迎来到风花雪月古诗词库, 请输入序号后回车以选择你喜欢的诗词\r\n'
    welcome += '输入fast加速，输入slow减速，输入bye退出\r\n\r\n'  # 输入quit或exit，退出并同时关闭诗词服务
    for index, subject in enumerate(subjects):
        welcome += '%d %s\r\n' % (index + 1, subject)
    welcome += '\r\n'
    welcome = welcome.encode('gbk')

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind(('127.0.0.1', 56789))
    sock.listen(2)

    runing = True
    while runing:
        c_sock, c_addr = sock.accept()
        c_sock.sendall(welcome)

        while True:
            cmd = b''
            while not cmd.endswith(b'\r\n'):
                cmd += c_sock.recv(1024)

            cmd = cmd.strip()
            if cmd in [b'bye', b'quit', b'exit']:
                c_sock.sendall('再见\r\n'.encode('gbk'))
                c_sock.close()
                runing = cmd == b'bye'
                break
            elif cmd == b'help':
                c_sock.sendall(welcome)
            elif cmd == b'fast':
                delay /= 2
                c_sock.sendall('加速设置已完成\r\n'.encode('gbk'))
                c_sock.sendall('请选择诗词序号，输入help显示诗词目录：\r\n\r\n'.encode('gbk'))
            elif cmd == b'slow':
                delay *= 2
                c_sock.sendall('减速设置已完成\r\n'.encode('gbk'))
                c_sock.sendall('请选择诗词序号，输入help显示诗词目录：\r\n\r\n'.encode('gbk'))
            else:
                try:
                    index = int(cmd) - 1
                    assert -1 < index < len(POUETRIES)
                except:
                    c_sock.sendall('请输入有效的诗词序号，输入help显示诗词目录：\r\n\r\n'.encode('gbk'))
                    continue

                c_sock.sendall(b'--------------------------\r\n')
                for line in POUETRIES[index].split('\n'):
                    for word in line:
                        c_sock.sendall(word.encode('gbk'))
                        time.sleep(delay)
                    c_sock.sendall(b'\r\n')
                c_sock.sendall(b'--------------------------\r\n')
                c_sock.sendall('请选择诗词序号，输入help显示诗词目录：\r\n\r\n'.encode('gbk'))


if __name__ == '__main__':
    poetries_server()
