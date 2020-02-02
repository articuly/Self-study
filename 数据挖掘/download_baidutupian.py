# coding:utf-8

# https://image.baidu.com/search/acjson
# ?tn=resultjson_com&ipn=rj&ct=201326592&is=&fp=result&queryWord=python&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=-1&z=&ic=0&hd=&latest=&copyright=&word=python&s=&se=&tab=&width=&height=&face=0&istype=2&qc=&nc=1&fr=&expermode=&force=&pn=30&rn=30&gsm=&1577088696945=
# https://image.baidu.com/search/acjson?tn=resultjson_com&ipn=rj&ct=201326592&is=&fp=result&queryWord=python&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=-1&z=&ic=0&hd=&latest=&copyright=&word=python&s=&se=&tab=&width=&height=&face=0&istype=2&qc=&nc=1&fr=&expermode=&force=&pn=60&rn=30&gsm=&1577088697695=

from urllib.parse import quote, unquote
import json
import requests
from uuid import uuid4

import sys
import os
import time

KEYWORD = quote(input("请输入您需要下载的图片名称: "))

# try:
#     curr_path = os.getcwd()
#     file_path = curr_path + "/images"
#     os.mkdir(file_path)
# except:
#     pass


headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36",
    # "Cookie": "BDqhfp=python%26%260-10-1undefined%26%260%26%261; BIDUPSID=04E5191177AE6FE842E3879F27C2F876; PSTM=1576811339; BAIDUID=04E5191177AE6FE8B70E34EBD448B186:FG=1; H_PS_PSSID=; BDORZ=FFFB88E999055A3F8A630C64834BD6D0; BDRCVFR[dG2JNJb_ajR]=mk3SLVN4HKm; userFrom=null; indexPageSugList=%5B%22python%22%2C%22%E7%9A%AE%E5%8D%A1%E4%B8%98%22%2C%22%E5%9B%BE%E7%89%87%22%5D; cleanHistoryStatus=0; BDRCVFR[X_XKQks0S63]=mk3SLVN4HKm; BDRCVFR[-pGxjrCMryR]=mk3SLVN4HKm; firstShowTip=1",
    # "Referer": "https://image.baidu.com/search/index?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&fm=result&fr=&sf=1&fmq=1577088610411_R&pv=&ic=0&nc=1&z=&hd=&latest=&copyright=&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&ie=utf-8&sid=&word=python"
}

session = requests.Session()


def get_url():
    headers[
        "Cookie"] = "BDqhfp={}%26%260-10-1undefined%26%260%26%261; BIDUPSID=04E5191177AE6FE842E3879F27C2F876; PSTM=1576811339; BAIDUID=04E5191177AE6FE8B70E34EBD448B186:FG=1; H_PS_PSSID=; BDORZ=FFFB88E999055A3F8A630C64834BD6D0; BDRCVFR[dG2JNJb_ajR]=mk3SLVN4HKm; userFrom=null; indexPageSugList=%5B%22python%22%2C%22%E7%9A%AE%E5%8D%A1%E4%B8%98%22%2C%22%E5%9B%BE%E7%89%87%22%5D; cleanHistoryStatus=0; BDRCVFR[X_XKQks0S63]=mk3SLVN4HKm; BDRCVFR[-pGxjrCMryR]=mk3SLVN4HKm; firstShowTip=1".format(
        KEYWORD)
    headers[
        "Referer"] = "https://image.baidu.com/search/index?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&fm=result&fr=&sf=1&fmq=1577088610411_R&pv=&ic=0&nc=1&z=&hd=&latest=&copyright=&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&ie=utf-8&sid=&word={}".format(
        KEYWORD)

    session.headers = headers

    start = time.time()

    for i in range(1, 6):
        pnn = i * 30
        url = 'https://image.baidu.com/search/acjson?tn=resultjson_com&ipn=rj&ct=201326592&is=&fp=result&queryWord={kw}&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=-1&z=&ic=0&hd=&latest=&copyright=&word={kw2}&s=&se=&tab=&width=&height=&face=0&istype=2&qc=&nc=1&fr=&expermode=&force=&pn={pn}&rn=30&gsm=&1577088697695='.format(
            kw=KEYWORD, kw2=KEYWORD, pn=pnn)

        html = session.get(url)

        if html.status_code == 200:
            try:
                json_data = (html.json()['data'])

                for i in range(len(json_data) - 1):
                    download_img(json_data[i]['middleURL'])
            except:
                pass

    end = time.time()

    print("耗时", end - start)


def download_img(url):
    filename = '../images'
    if not os.path.exists(filename):
        os.mkdir(filename)

    html = session.get(url)

    if html.status_code == 200:
        with open('./images/{}.jpg'.format(uuid4()), 'wb') as f:

            for chunk in html.iter_content(225):
                f.write(chunk)


if __name__ == "__main__":
    get_url()
