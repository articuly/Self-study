# coding:utf-8
import logging
import json
import requests


def build_logger(log_path, file_level=logging.DEBUG, console_level=logging.DEBUG):
    # init_logger
    logger = logging.getLogger(__file__)
    logger.setLevel(logging.DEBUG)

    # set two handlers
    file_handler = logging.FileHandler(log_path, mode='w', encoding='utf-8')
    file_handler.setLevel(file_level)
    console_handler = logging.StreamHandler()
    console_handler.setLevel(console_level)
    # set formatter
    formatter = logging.Formatter('[%(asctime)s] {%(filename)s:%(lineno)d} %(levelname)s - %(message)s',
                                  datefmt='%Y-%m-%d %H:%M:%S')
    console_handler.setFormatter(formatter)
    file_handler.setFormatter(formatter)

    # add handler
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)
    return logger


def plogger(content, logger):
    # log info or print info
    if logger:
        logger.info(content)
    else:
        print(content)


def read_json(path):
    # read config from json file
    f = open(path, 'r', encoding='utf-8')
    txt = f.read()
    f.close()
    params = json.loads(txt)
    return params


def write_json(path, dictionary):
    # write dict to json file
    json_txt = json.dumps(dictionary)
    f = open(path, 'w', encoding='utf-8')
    f.write(json_txt)
    f.close()


def get_timezone_geolocation(ip):
    # get ip geo info
    try:
        geotz_url = f'http://ip-api.com/json/{ip}'
        response = requests.get(geotz_url)
        dct = response.json()
        response.close()
    except Exception as e:
        print(str(e))
        dct = {"status": "success", "country": "Japan", "countryCode": "JP", "region": "13", "regionName": "Tokyo",
               "city": "Heiwajima", "zip": "143-0001", "lat": 35.5819, "lon": 139.7663, "timezone": "Asia/Tokyo",
               "isp": "The Constant Company", "org": "Vultr Holdings, LLC", "as": "AS20473 The Constant Company, LLC",
               "query": "149.28.24.220"}
    return dct
