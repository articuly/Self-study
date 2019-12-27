# coding-utf-8
import time
import threading


def hello(name, t):
    for i in range(10):
        print('Hello, I am {0}'.format(name))
        time.sleep(t)


def demo():
    A = threading.Thread(target=hello, args=("Artic", 1), name="Artic")
    B = threading.Thread(target=hello, args=("Bath", 2), name="Bat")
    C = threading.Thread(target=hello, args=("Cat", 3), name="Cat")
    # C.setDaemon(True)  # 设置子线程在主线程结束时是否无条件跟随主线程一起退出
    A.start()
    A.join(5)
    B.start()
    C.start()
    time.sleep(20)
    print('进程A%s' % ('还在工作中' if A.isAlive() else '已经结束工作',))
    print('进程B%s' % ('还在工作中' if B.isAlive() else '已经结束工作',))
    print('进程C%s' % ('还在工作中' if C.isAlive() else '已经结束工作',))
    print('have a break.')


if __name__ == '__main__':
    demo()
