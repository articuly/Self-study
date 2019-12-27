# coding:utf-8
import time
import threading

S = threading.Semaphore(5)


def us_hammer(id):
    S.acquire()
    time.sleep(0.2)
    print('{0}刚刚用完电锤'.format(id))
    S.release()


def demo():
    threads = list()
    for i in range(30):
        threads.append(threading.Thread(target=us_hammer, args=(i,)))
        threads[-1].start()
    for t in threads:
        t.join()
    print('All threads work over')


if __name__ == '__main__':
    demo()
