# coding:utf-8
import json
import re


# 定义一个函数，用于提取 json 对象
def extract_json(text):
    # 使用 json.loads() 函数解析 json 字符串
    json_obj = json.loads(text)

    # 返回 json 对象
    return json_obj


# 定义一个变量，用于保存混合文本
text = '''
Here is some text that contains a json object: {"key1": "value1", "key2": "value2"}
And here is some more text that contains another json object: {"key3": "value3", "key4": "value4"}
'''

# 使用正则表达式，在混合文本中提取所有 json 字符串
json_str_list = re.findall(r'\{.*\}', text)

# 对每个 json 字符串，使用 extract_json() 函数提取 json 对象
json_obj_list = [extract_json(json_str) for json_str in json_str_list]

# 输出提取到的 json 对象
print(json_obj_list)
