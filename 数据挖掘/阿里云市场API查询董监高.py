from urllib.request import urlopen, Request
import urllib.parse
import json
import pandas as pd


def search_high_level(name, key, type=0):
    # type参数 0：担任法定代表人；1：对外投资；2：在外任职
    # key参数 关键字（公司名、社会统一信用代码、注册号）
    # name参数 人员姓名
    host = 'http://ecisenior.market.alicloudapi.com'
    path = '/ECISeniorPerson/GetList'
    method = 'GET'
    appcode = 'ab937b81925c450e9558e7ad92609pr9'  # 改为自己的AppCode
    # 自定义参数
    dtype = 'json'  # json或xml，默认json
    pageIndex = 1  # 页码，默认第一页
    pageSize = 50  # 每页条目数，默认10条，最大不超过50条
    name_bytes = name.encode('utf-8').strip()
    key_bytes = key.encode('utf-8').strip()
    # 合并查询串
    fortest = {'personName': name_bytes, 'searchKey': key_bytes, 'dtype': dtype, 'pageIndex': pageIndex,
               'pageSize': pageSize, 'type': type}
    querys = urllib.parse.urlencode(fortest)
    url = host + path + '?' + querys
    print(url)
    # 查询
    request = Request(url)
    request.add_header('Authorization', 'APPCODE ' + appcode)
    response = urlopen(request)
    content = response.read()
    if (content):
        print(content)
    # 读取为字典
    content_dict = json.loads(content)
    result_dict = content_dict['Result']
    # 生成框架
    result_df = pd.DataFrame.from_dict(result_dict)
    return result_df


# 写入文件
def write_high_level(name, key, outputfile, type=0):
    df = search_high_level(name, key, type=type)
    writer = pd.ExcelWriter(outputfile)
    df.to_excel(writer, name)
    writer.save()


name, key = 'abc', 'abc有限公司'
outputfile = r'E:\我的坚果云\高管信息.xlsx'
write_high_level(name, key, outputfile)
