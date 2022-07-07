# coding:utf-8
import json
from selenium.webdriver.chrome.webdriver import Options, WebDriver
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
import re


def read_config(config_path):
    f = open(config_path, 'r')
    txt = f.read()
    f.close()
    paras = json.loads(txt)
    username = paras['username']
    password = paras['password']
    old_passkey = paras['old_passkey']
    new_passkey = paras['new_passkey']
    return username, password, old_passkey, new_passkey


def init_driver(browser_path, web_url):
    options = Options()
    options.add_experimental_option('excludeSwitches', ['enable-automation'])  # 关闭浏览器受到控制的提示
    driver = WebDriver(browser_path, options=options)
    driver.get(web_url)
    driver.maximize_window()
    return driver


def login(driver, username, password):
    driver.find_element_by_id('username').send_keys(username)
    driver.find_element_by_id('password').send_keys(password)
    driver.find_element_by_id('login').click()


if __name__ == '__main__':
    USERNAME, PASSWORD, OLDPASSKEY, NEWPASSKEY = read_config('config.json')

    # init
    browser_path = r'D:\Tools\Chromium\chromedriver.exe'
    web_url = 'http://articuly.ddns.net:29093'
    d = init_driver(browser_path, web_url)
    sleep(2)

    # login
    login(d, USERNAME, PASSWORD)
    sleep(2)

    # click tracker tab
    d.find_element_by_id('PropTrackersLink').click()
    # find torrent list
    torrents = d.find_elements_by_class_name('torrentsTableContextMenuTarget')
    start_num = int(input('please enter the start row number'))
    for i, t in enumerate(torrents):
        if i >= start_num:
            # select the row
            t.click()
            sleep(1)
            tracker_url = d.find_element_by_xpath('//*[@id="trackers"]/table/tbody/tr[4]/td[2]').text
            if tracker_url.find(OLDPASSKEY) > 0:
                # right click to open edit frame
                torrent_name = d.find_element_by_xpath(
                    '//*[@id="torrentsTableDiv"]/table/tbody/tr[{num}]/td[3]'.format(num=i + 1)).text
                print('{} uses old passkey'.format(torrent_name))
                new_tracker_url = tracker_url.replace(OLDPASSKEY, NEWPASSKEY)
                tracker_row = d.find_element_by_xpath('//*[@id="trackersTable"]/tr[4]')
                ActionChains(d).move_to_element(tracker_row).context_click().perform()
                tracker_edit = d.find_element_by_xpath('//*[@id="torrentTrackersMenu"]/li[2]/a')
                ActionChains(d).move_to_element(tracker_edit).click().perform()
                # print(torrent_name, tracker_url)

                # try to replace old passkey
                try:
                    sleep(6)
                    d.switch_to.frame('trackersPage_iframe')  # 切换到悬浮框架才能生效
                    d.find_element_by_id('trackerUrl').clear()
                    d.find_element_by_id('trackerUrl').send_keys(new_tracker_url)
                    d.find_element_by_id('editTrackerButton').click()
                    d.switch_to.default_content()
                except Exception as e:
                    print(e)
                print('{} has modified to new passkey'.format(torrent_name))
                print('finished {} row'.format(i + 1))
            # skip torrent with new passkey
            else:
                continue

    print('selenium has replace all torrents passkey')
    print('browser will be close in 10 seconds')
    sleep(10)
    d.quit()
