from urllib.request import urlopen, Request
import urllib.parse

host = 'http://xinshubzxr.market.alicloudapi.com'
path = '/ws/repository/executedList'
method = 'POST'
appcode = 'ab937b81925c450e9558e7ad92609pr9'
btype = '2'  # 必选，被执行人类型，1-个人;2-企业/机构
entityId = ''  # 可选,主体代码,当被执行人类型为个人时，该字段必填
entityName = '东莞市合和市政工程有限公司'
name = urllib.parse.quote_plus(entityName)
sign = '386e2ced3321db2bfc87a643edbe3e59'  # 请填写 6tj4uYYYYMMDD的32位md5加密值，加密工具地址：http://www.cmd5.com/
headerfortest = {'btype': btype, 'entityName': entityName, 'sign': sign}
# 例子querys = 'btype=1&entityId=5102241972****149x&entityName=%E7%AE%80*%E6%96%8C&sign=sign'
querys = urllib.parse.urlencode(headerfortest)
encode_querys = urllib.parse.urlencode(headerfortest).encode('utf-8')
url = host + path + '?' + querys

bodys = {}
bodys[''] = ""
post_data = bodys['']

request = Request(url, post_data)
request.add_header('Authorization', 'APPCODE ' + appcode)
# 根据API的要求，定义相对应的Content-Type
request.add_header('Content-Type', 'application/json; charset=UTF-8')
response = urlopen(request, data=encode_querys)
content = response.read()
if (content):
    print(content)

import json
import pandas as pd

content_dict = json.loads(content)
result_dict = content_dict['data']['list']
len(result_dict)

df_result = pd.DataFrame(result_dict)
# df_result.drop(['entityName'],axis=1)
df_result.head()
