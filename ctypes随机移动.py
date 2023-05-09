import time
import random
import ctypes

# 获取屏幕的宽度和高度
user32 = ctypes.windll.user32
width, height = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)

while True:
    # 将光标移动到一个随机的位置
    x, y = random.randint(0, width), random.randint(0, height)
    user32.SetCursorPos(x, y)

    # 稍微暂停一下，让移动看起来更自然
    time.sleep(random.uniform(5, 10))