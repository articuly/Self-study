from urllib.request import urlopen, Request
import urllib.parse
import json
import pandas as pd


def search_shixin(keyword, dtype='json', searchtype=None):
    # dtype参数：json或xml，默认json
    host = 'http://courtv4.market.alicloudapi.com'
    path = '/CourtV4/SearchShiXin'
    method = 'GET'
    appcode = 'ab937b81925c450e9558e7ad92609pr9'  # 改为自己的AppCode
    # 自定义参数
    pageSize = 50  # 每页条数，默认为10，最大不超过50
    pageIndex = 1  # 页码，默认第一页
    isExactlySame = True  # 是否要与关键字完全一样
    keyword_bytes = keyword.encode('utf-8').strip()
    # 合并查询串
    if searchtype == 1:
        fortest = {'searchKey': keyword_bytes, 'dtype': dtype, 'isExactlySame': isExactlySame, 'pageIndex': pageIndex,
                   'pageSize': pageSize, 'searchType': searchtype}
    else:
        fortest = {'searchKey': keyword_bytes, 'dtype': dtype, 'isExactlySame': isExactlySame, 'pageIndex': pageIndex,
                   'pageSize': pageSize}
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
    result_df = pd.DataFrame.from_dict(result_dict[0], orient='index').T
    result_df = result_df.drop([0])
    for result in result_dict:
        current_result = pd.DataFrame.from_dict(result, orient='index').T
        result_df = result_df.append(current_result)
    return result_df


# 批量查询
def search_shixin_list(keywordlist, dtype='json', searchtype=None):
    frame = []
    for keyword in keywordlist:
        result = search_shixin(keyword, dtype=dtype, searchtype=searchtype)
        frame.append(result)
    res = pd.concat(frame, keys=keywordlist)
    return res


# 写入文件
def write_list(keywordlist, outputfile):
    res = search_shixin_list(keywordlist)
    writer = pd.ExcelWriter(outputfile)
    res.to_excel(writer, "info_list")
    writer.save()


lst = ['abc', 'efg']
outputfile = r'E:\我的坚果云\失信信息.xlsx'
write_list(lst, outputfile)
