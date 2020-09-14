from selenium.webdriver.chrome.webdriver import Options, WebDriver
from time import sleep

# 创建实例
options = Options()
options.add_experimental_option('excludeSwitches', ['enable-automation'])  # 关闭浏览器受到控制的提示
browser = WebDriver(r'D:\Browser\Chromium\chromedriver.exe', options=options)
browser.get("https://www.baidu.com")
sleep(2)

# 打印浏览器的宽和高
size_Dict = browser.get_window_size()
print("当前浏览器的宽：", size_Dict['width'])
print("当前浏览器的高：", size_Dict['height'])

# 设置浏览器的大小
browser.set_window_size(width=800, height=500, windowHandle="current")
# windowHandle = "current" 控制当前窗口的意思
sleep(2)

# 打印窗口坐标
position = browser.get_window_position()
print(position)
print("浏览器所在位置的横坐标：", position["x"])
print("浏览器所在位置的纵坐标：", position["y"])

# 设置窗口位置并打印位置坐标
browser.set_window_position(x=100, y=200)
print(browser.get_window_position())
sleep(2)

# 最大化浏览器并输出浏览器的大小和位置坐标
browser.maximize_window()
print(browser.get_window_size())
print(browser.get_window_position())
sleep(2)

# 退出浏览器
browser.quit()
