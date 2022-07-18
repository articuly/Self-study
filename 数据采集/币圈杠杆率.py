# coding:utf-8
import time
import re
import requests
import json
from selenium.webdriver.chrome.webdriver import Options, WebDriver
from selenium.webdriver.common.action_chains import ActionChains
import pymysql


def init_driver(driver_path, is_proxy=False):
    options = Options()
    # 无头模式
    options.add_argument('--headless')
    # 隐藏正在受到自动软件的控制
    options.add_experimental_option('excludeSwitches', ['enable-automation'])
    options.add_experimental_option('useAutomationExtension', False)
    # 去除webdriver特征
    options.add_argument('--disable-blink-features=AutomationControlled')

    if is_proxy:
        # 加socks5代理
        options.add_argument('proxy-server=socks5://127.0.0.1:63')
        # 关闭webrtc
        preferences = {
            'webrtc.ip_handling_policy': 'disable_non_proxied_udp',
            'webrtc.multiple_routes_enabled': False,
            'webrtc.nonproxied_udp_enabled': False
        }
        options.add_experimental_option('prefs', preferences)
        # 获取代理的地理与时区
        proxy_json = get_timezone_geolocation('149.28.24.220')
        print(proxy_json)
        geo = {'latitude': proxy_json['lat'], 'longitude': proxy_json['lon'], 'accuracy': 1}
        tz = {'timezoneId': proxy_json['timezone']}

    # 加header
    options.add_argument('lang=zh-CN,zh,zh-TW,en-US,en')
    options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                         'Chrome/84.0.4105.0 Safari/537.36')

    driver = WebDriver(driver_path, options=options)
    # 修改 webdriver 值
    with open(r"D:\OneDrive - business\python_projects\Self-study\数据采集\stealth.min.js", 'r') as f:
        js = f.read()
    driver.execute_cdp_cmd('Page.addScriptToEvaluateOnNewDocument', {'source': js})

    if is_proxy:
        # 设置代理的地理与时区
        driver.execute_cdp_cmd('Emulation.setGeolocationOverride', geo)
        driver.execute_cdp_cmd('Emulation.setTimezoneOverride', tz)
    driver.maximize_window()
    return driver


def read_config(config_path):
    f = open(config_path, 'r')
    txt = f.read()
    f.close()
    paras = json.loads(txt)
    return paras


def get_timezone_geolocation(ip):
    url = f'http://ip-api.com/json/{ip}'
    response = requests.get(url)
    return response.json()


def bot_test(driver):
    bot_test_url1 = 'https://bot.sannysoft.com/'
    bot_test_url2 = 'https://bot.incolumitas.com/'
    bot_test_url3 = 'https://browserleaks.com/ip'
    bot_test_url4 = 'https://whoer.net/'
    driver.set_page_load_timeout(90)
    driver.set_script_timeout(30)

    try:
        driver.get(bot_test_url1)
    except Exception as e:
        print(str(e))
        driver.execute_script("window.stop()")
    time.sleep(5)
    page1 = driver.page_source
    with open('test1.html', 'w', encoding='utf-8') as f:
        f.write(page1)

    try:
        driver.get(bot_test_url2)
    except Exception as e:
        print(str(e))
        driver.execute_script("window.stop()")
    time.sleep(5)
    page2 = driver.page_source
    with open('test2.html', 'w', encoding='utf-8') as f:
        f.write(page2)

    try:
        driver.get(bot_test_url3)
    except Exception as e:
        print(str(e))
        driver.execute_script("window.stop()")
    time.sleep(5)
    page3 = driver.page_source
    with open('test3.html', 'w', encoding='utf-8') as f:
        f.write(page3)

    try:
        driver.get(bot_test_url4)
    except Exception as e:
        print(str(e))
        driver.execute_script("window.stop()")
    time.sleep(5)
    page4 = driver.page_source
    with open('test4.html', 'w', encoding='utf-8') as f:
        f.write(page4)

    driver.close()


def vol_replace(string):
    return string.replace('$', '').replace(',', '')


def connect_db(conf, max_retry=10, retry_time=60):
    count = 0
    conn_status = False
    while count <= max_retry and not conn_status:
        try:
            conn = pymysql.connect(host=conf['mydb_url'], port=conf['mydb_port'], user=conf['mydb_user'],
                                   passwd=conf['mydb_pw'], db='blockchain', charset='utf8')
            conn_status = True
            print('connect db success')
            return conn
        except Exception:
            count += 1
            print(f'connect db timeout, retry {count} time')
            time.sleep(retry_time)
        continue
    print('out of retry times')
    exit()


if __name__ == '__main__':
    # init driver
    driver_path = r'D:\Browser\Chromium\chromedriver.exe'
    web_url = 'https://coinmarketcap.com/view/stablecoin/'
    d = init_driver(driver_path, is_proxy=True)
    # bot_test(d)
    try:
        d.implicitly_wait(90)
        d.get(web_url)
        d.execute_script('window.scrollBy(0,1200)')
        time.sleep(10)
    except Exception as e:
        print(str(e))
    # find sample stable caps
    caps = d.find_elements_by_xpath("//tbody//td//p//span[@class='sc-1ow4cwt-1 ieFnWP']")
    caps_list = [i.text for i in caps]
    caps_list_val = [int(vol_replace(i)) for i in caps_list]
    # find stable caps
    stable_market = d.find_elements_by_xpath("//section//div//div//div//div//span[@class='sc-1eb5slv-0 iworPT']")
    stable_coin_cap = int(vol_replace(stable_market[0].text))
    stable_trade_vol = int(vol_replace(stable_market[1].text))
    # find total cap
    top_info = d.find_elements_by_xpath("//*[@class='cmc-link']")
    total_market_cap = int(float(vol_replace(top_info[2].text)))
    print(total_market_cap, stable_coin_cap)
    # find other top info
    cryptos = int(vol_replace(top_info[0].text))
    exchanges = int(vol_replace(top_info[1].text))
    day_vol = int(float(vol_replace(top_info[3].text)))
    print(day_vol, stable_trade_vol)
    print(cryptos, exchanges)
    btc_domi = round(float(re.search('BTC:\s?(\d+\.\d)+%', top_info[4].text).group(1)), 2)
    eth_domi = round(float(re.search('ETH:\s?(\d+\.\d)+%', top_info[4].text).group(1)), 2)
    print(btc_domi, eth_domi)
    # calc lever
    stable_coin_sample_cap = sum(caps_list_val)
    stable_sample = len(caps_list_val)
    sample_lever = total_market_cap / stable_coin_sample_cap
    lever = total_market_cap / stable_coin_cap
    print(sample_lever, lever)
    # calc trading ratio
    coin_ratio = round(stable_trade_vol / day_vol * 100, 2)
    fiat_ratio = round((day_vol - stable_trade_vol) / day_vol * 100, 2)
    print(coin_ratio, fiat_ratio)
    # get local time
    date_id = time.strftime("%Y%m%d", time.localtime())
    collect_dtm = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    id = time.strftime("%Y%m%d%H%M%S", time.localtime())

    # connect db
    conf = read_config(r"D:\OneDrive - business\python_projects\Self-study\数据采集\config.json")
    conn = connect_db(conf)
    cur = conn.cursor()
    sql_txt = f"insert into top_info values ('{id}', '{date_id}', str_to_date('{collect_dtm}', '%Y-%m-%d %H:%i:%S'), " \
              f"{total_market_cap}, {stable_coin_cap}, {stable_coin_sample_cap}, {stable_sample}, " \
              f"{lever}, {sample_lever}, {cryptos}, {exchanges}, {day_vol}, " \
              f"{stable_trade_vol}, {btc_domi}, {eth_domi}, {coin_ratio}, {fiat_ratio})"
    # insert data
    try:
        cur.execute(sql_txt)
        conn.commit()
        print('insert data into db successfully')
    except Exception as e:
        print(str(e))
        conn.rollback()
        print('failed to insert data into db')
    finally:
        cur.close()
        conn.close()
        d.close()
        exit()
