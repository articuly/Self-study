# coding:utf-8
import time
import os
import json
import gzip
import zlib
import brotli
from datetime import datetime
from seleniumwire import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import matplotlib.pyplot as plt
import smtplib
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


class DownloadBaiDuIndex:
    current_dir = os.path.abspath(__file__).rsplit('\\', 1)[0]

    def __init__(self, driver_dir):
        self.driver_dir = driver_dir
        self.keyword = ''
        self.ptbk = None
        self.data = None
        self.paras = {}
        self.start_date = ''
        self.end_date = ''
        self.results = ''
        self.num_list = []
        self.date_list = None
        self.df = None

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
        with open(os.path.join(DownloadBaiDuIndex.current_dir, 'stealth.min.js'), 'r') as f:
            js = f.read()
        self.driver.execute_cdp_cmd('Page.addScriptToEvaluateOnNewDocument', {'source': js})

    def get_cookie(self):
        browser = WebDriver(service=Service(self.driver_dir), options=self.options)
        browser.get("https://index.baidu.com/v2/index.html")
        browser.find_element(By.CSS_SELECTOR, "span.username-text").click()

        print('等待登录...')
        while True:
            if browser.find_element(By.CSS_SELECTOR, "span.username-text").text != "登录":
                break
            else:
                time.sleep(3)

        print('已登录，现在为您保存cookie...')
        with open(os.path.join(DownloadBaiDuIndex.current_dir, 'baidu_cookie.txt'), 'w', encoding='utf-8') as f:
            json.dump(browser.get_cookies(), f)

        print('cookie保存完成，游览器已自动退出...')
        browser.close()

    def load_cookies(self):
        with open(os.path.join(DownloadBaiDuIndex.current_dir, 'baidu_cookie.txt'), 'r', encoding='utf-8') as f:
            cookies = json.load(f)
        self.driver.get('https://index.baidu.com/v2/index.html')
        for cookie in cookies:
            self.driver.add_cookie(cookie)
        self.driver.get('https://index.baidu.com/v2/index.html')
        print('已读取cookie，自动完成登陆')

    @staticmethod
    def read_config(config_name):
        f = open(os.path.join(DownloadBaiDuIndex.current_dir, config_name), 'r')
        txt = f.read()
        f.close()
        paras = json.loads(txt)
        return paras

    def enter_keyword(self, keyword):
        self.keyword = keyword
        wait = WebDriverWait(self.driver, 30)
        edit = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#search-input-form > input.search-input')))
        print("清空前历史记录数：", len(self.driver.requests))
        del self.driver.requests  # 清空历史数据
        edit.send_keys(Keys.CONTROL + 'a')
        edit.send_keys(Keys.DELETE)
        edit.send_keys(self.keyword)
        submit = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'span.search-input-cancle')))
        submit.click()
        print("清空后再执行搜索后的历史记录数：", len(self.driver.requests))

    @staticmethod
    def decompress(res):
        content_encoding = res.headers["content-encoding"]
        if content_encoding == 'gzip':
            res.body = gzip.decompress(res.body)
        elif content_encoding == 'deflate':
            res.body = zlib.decompress(res.body)
        elif content_encoding == 'br':
            res.body = brotli.decompress(res.body)

    @staticmethod
    def decrypt(ptbk, index_data):
        n = len(ptbk) // 2
        a = dict(zip(ptbk[:n], ptbk[n:]))
        return ''.join([a[s] for s in index_data])

    def fetch_data(self, rule, encoding="utf-8", is_json=True):
        for request in reversed(self.driver.requests):
            if rule in request.url:
                res = request.response
                self.decompress(res)
                result = res.body.decode(encoding)
                if is_json:
                    result = json.loads(result)
                return result

    def get_index(self):
        self.ptbk = self.fetch_data("Interface/ptbk")['data']
        self.data = self.fetch_data("api/SearchApi/index")['data']

        for idx in self.data['userIndexes']:
            word = idx['word'][0]['name']
            index_data = idx['all']['data']
            self.start_date = idx['all']['startDate']
            self.end_date = idx['all']['endDate']
            self.results = self.decrypt(self.ptbk, index_data)
            print(word, self.results)
            self.num_list = self.results.split(',')

        self.date_list = pd.date_range(self.start_date, self.end_date)
        if len(self.date_list) == len(self.num_list):
            self.df = pd.DataFrame({'date': self.date_list,
                                    'num': [int(i) for i in self.num_list]})
            plt.figure(figsize=(9, 6))
            plt.plot(self.df['date'], self.df['num'])
            plt.xlabel('date')
            plt.ylabel('indexes')
            plt.savefig(os.path.join(DownloadBaiDuIndex.current_dir, 'baidu_index.png'))
            plt.close()
        else:
            print('日期长度与数据长度不一致，请检查')

    def send_mail(self, config_name):
        self.paras = self.read_config(config_name)
        sender = self.paras['mail_sender']
        passwd = self.paras['mail_password']
        receiver = self.paras['mail_receiver']
        smtp_server = self.paras['smtp_server']
        smtp_port = self.paras['smtp_port']
        mail_server = smtplib.SMTP(host=smtp_server, port=smtp_port)
        mail_server.starttls()
        is_login = False
        try:
            mail_server.login(sender, passwd)
            is_login = True
        except Exception as e:
            print(str(e))
        if is_login:
            msg = MIMEMultipart()
            body = '''<h3>你好</h3>
            <p>这是最近一个月百度{word}的搜索指数</p>
            <p>邮件通过Python脚本生成，仅供参考</p>
            <table border="1">
            <tbody>
                <tr>
                    <td>最大值：{max}</td><td>最小值：{min}</td><td>极差：{s_range}</td>
                </tr>
                <tr>
                    <td>平均值：{mean}</td><td>标准差：{std}</td><td>天数：{count}</td>
                </tr>
                <tr>
                    <td>25%分位数：{p25}</td><td>50%分位数：{p50}</td><td>75%分位数：{p75}</td>
                </tr>
            </tbody>
            </table>
            <p><br><img src="cid:image1"></br></p>
            '''
            mail_body = MIMEText(body.format(word=self.keyword, max=self.df['num'].max(), min=self.df['num'].min(),
                                             s_range=(self.df['num'].max() - self.df['num'].min()),
                                             mean=round(self.df['num'].mean(), 2), std=round(self.df['num'].std(), 2),
                                             count=self.df['num'].count(), p25=round(self.df['num'].quantile(0.25), 2),
                                             p50=round(self.df['num'].quantile(0.5), 2),
                                             p75=round(self.df['num'].quantile(0.75), 2)),
                                 _subtype='html', _charset='utf-8')
            msg.attach(mail_body)

            fp = open("baidu_index.png", 'rb')
            images = MIMEImage(fp.read())
            fp.close()
            images.add_header('Content-ID', '<image1>')
            msg.attach(images)

            msg['From'] = sender
            msg['To'] = receiver
            today_str = datetime.today().strftime('%Y%m%d')
            msg['Subject'] = f'百度指数-{self.keyword}-{today_str}'
            mail_server = smtplib.SMTP(smtp_server, smtp_port)
            mail_server.ehlo()  # Hostname to send for this command defaults to the fully qualified domain name of the local host.
            mail_server.starttls()  # Puts connection to SMTP server in TLS mode
            # mail_server.ehlo()
            mail_server.login(sender, passwd)
            mail_server.sendmail(sender, receiver.split(','), msg.as_string())
            mail_server.quit()
            print('发送成功！')


if __name__ == '__main__':
    d = DownloadBaiDuIndex(driver_dir=r'D:\Browser\Chromium\chromedriver.exe')
    # d.get_cookie()
    d.load_cookies()
    d.enter_keyword(keyword='疫情')
    d.get_index()
    d.send_mail(config_name='config.json')

    d.driver.close()
    d.driver.quit()
    exit()
