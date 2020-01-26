import time

print('Loading', end='')
for i in range(20):
    print('.', end='', flush=True)
    time.sleep(0.2)

print('\n')


def printer(text, delay=0.2):
    # 打字机效果
    for ch in text:
        print(ch, end='', flush=True)
        time.sleep(delay)


printer('玄铁重剑，是金庸小说笔下第一神剑，持之则无敌于天下。')
print('\n')


def waiting(cycle=20, delay=0.1):
    # 旋转式进度指示
    for i in range(cycle):
        for ch in ['-', '\\', '|', '/']:
            print('\b%s' % ch, end='', flush=True)
            time.sleep(delay)


waiting()
print('\n')


# ‘\b’ 的作用是回退一个字符，’\r’ 则可以退回到行首
def cover(cycle=100, delay=0.2):
    # 覆盖式打印效果
    for i in range(cycle):
        s = '\r%d' % i
        print(s.ljust(3), end='', flush=True)
        time.sleep(delay)


cover()
print('\n')
