# coding:utf-8
import json
from selenium.webdriver.chrome.webdriver import Options, WebDriver
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
import re


def init_driver(browser_path):
    options = Options()
    # 无头模式
    # options.add_argument('--headless')
    # 隐藏正在受到自动软件的控制
    options.add_experimental_option('excludeSwitches', ['enable-automation'])
    options.add_experimental_option('useAutomationExtension', False)
    # 去除webdriver特征
    options.add_argument('--disable-blink-features')
    options.add_argument('--disable-blink-features=AutomationControlled')
    # 加socks5代理
    options.add_argument("proxy-server=socks5://127.0.0.1:63")
    # 加header
    options.add_argument('lang=zh-CN,zh,zh-TW,en-US,en')
    options.add_argument(
        'user-agent=Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4105.0 Safari/537.36')
    driver = WebDriver(browser_path, options=options)
    # 修改 webdriver 值
    with open('stealth.min.js', 'r') as f:
        js = f.read()
    driver.execute_cdp_cmd('Page.addScriptToEvaluateOnNewDocument', {'source': js})
    driver.maximize_window()
    return driver


def bot_test(driver):
    bot_test_url1 = 'https://bot.sannysoft.com/'
    bot_test_url2 = 'https://bot.incolumitas.com/'
    bot_test_url3 = 'https://browserleaks.com/ip'

    # driver.get(bot_test_url1)
    # sleep(5)
    # page1 = driver.page_source
    # with open('test1.html', 'w', encoding='utf-8') as f:
    #     f.write(page1)
    #
    # driver.get(bot_test_url2)
    # sleep(5)
    # page2 = driver.page_source
    # with open('test2.html', 'w', encoding='utf-8') as f:
    #     f.write(page2)
    # driver.close()

    driver.get(bot_test_url3)
    sleep(5)
    page3 = driver.page_source
    with open('test3.html', 'w', encoding='utf-8') as f:
        f.write(page3)
    driver.close()


if __name__ == '__main__':
    # init
    browser_path = r'D:\Browser\Chromium\chromedriver.exe'
    web_url = 'https://bot.incolumitas.com/'
    # web_url = 'https://bot.sannysoft.com/'
    d = init_driver(browser_path)
    bot_test(d)
