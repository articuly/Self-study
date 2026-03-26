# coding:utf-8
import json
import logging
import os
import time

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from seleniumwire import webdriver

from Util import read_json, build_logger


class WebChatGPT:
    current_dir: str = os.path.abspath(__file__).rsplit('\\', 1)[0]

    def __init__(self, config_name: str, log_name: str):
        self.paras = read_json(os.path.join(WebChatGPT.current_dir, config_name))
        self.q = ''
        self.result = ''
        self.driver_dir = ''
        self.driver = None
        self.options = None
        self.log_name = log_name
        self.log_path = os.path.join(WebChatGPT.current_dir, self.log_name)
        self.log = build_logger(self.log_path, logging.DEBUG, logging.DEBUG)

    def build_diver(self, driver_dir: str):
        self.driver_dir = driver_dir
        self.options = webdriver.ChromeOptions()
        # 无头模式
        # options.add_argument('--headless')
        # 隐藏正在受到自动软件的控制
        self.options.add_experimental_option('excludeSwitches', ['enable-automation'])
        self.options.add_experimental_option('useAutomationExtension', False)
        # 去除webdriver特征
        self.options.add_argument('--disable-blink-features=AutomationControlled')
        # 加header
        self.options.add_argument('lang=zh-CN,zh;q=0.9,zh-TW;q=0.8,en;q=0.7,en-US;q=0.6,en-GB;q=0.5')
        self.options.add_argument(
            'user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)'
            ' Chrome/111.0.0.0 Safari/537.36')
        # 启动时最大化窗口
        self.options.add_argument('--start-maximized')
        self.driver = webdriver.Chrome(service=Service(self.driver_dir), options=self.options)
        # 修改 webdriver 值
        with open(os.path.join(WebChatGPT.current_dir, 'stealth.min.js'), 'r') as f:
            js = f.read()
        self.driver.execute_cdp_cmd('Page.addScriptToEvaluateOnNewDocument', {'source': js})
        self.log.debug('完成Selenium浏览器的初始化')

    def get_pass(self):
        # 访问并输入密码
        self.driver.get("https://gpt.moyunav.com")
        self.driver.implicitly_wait(30)
        self.driver.find_element(By.CLASS_NAME, "n-input__input-el").clear()
        self.driver.find_element(By.CLASS_NAME, "n-input__input-el").send_keys(self.paras['web_gpt_pw'])
        buttons = self.driver.find_elements(By.XPATH, "//button/span[@class='n-button__content']")
        buttons[-1].click()
        # 保存cookie
        self.log.debug('已输入密码，现在为您保存cookie...')
        with open(os.path.join(WebChatGPT.current_dir, 'web_chatgpt_cookie.txt'), 'w', encoding='utf-8') as f:
            json.dump(self.driver.get_cookies(), f)

    def ask_question(self, question: str):
        # 提交问题
        self.q = question
        time.sleep(6)
        wait = WebDriverWait(self.driver, 30)
        edit = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "n-input__textarea-el")))
        edit.send_keys(self.q)
        submit = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='n-icon-slot']/span")))
        submit.click()
        self.log.debug(f"已提交问题：{self.q}")
        # 获取答案
        time.sleep(6)
        wait.until_not(EC.visibility_of_element_located(
            (By.XPATH, "//button/span[contains(text(), ' Stop Responding ')]")))
        self.result = self.driver.find_element(By.XPATH, "(//div[@class='markdown-body'])[last()]").text
        # 保存答案
        self.log.debug(f"已获取该问题的回答：{self.q}")
        self.log.info(f'{self.result}'.replace('复制代码\n', ''))
        with open(os.path.join(WebChatGPT.current_dir, 'web_chatgpt_temp.txt'), 'w', encoding='utf-8') as f:
            f.write(self.result)
        # 打开文件
        os.startfile(os.path.join(WebChatGPT.current_dir, 'web_chatgpt_temp.txt'))


if __name__ == '__main__':
    d = WebChatGPT(config_name='config.json', log_name='web_chatgpt.log')
    d.build_diver(driver_dir=r'D:\Browser\Chromium\chromedriver.exe')
    d.get_pass()
    d.ask_question(question='python spark')

    # d.driver.close()
    # d.driver.quit()
    # exit()
