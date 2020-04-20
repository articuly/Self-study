import base64
import requests
import time
import json


def encode_audio(audio_file):
    with open(audio_file, 'rb') as au:
        audio_content = au.read()
    uri = base64.b64encode(audio_content)
    return uri


# def encode_audio(audio):
#   audio_content = audio.read()
#   return base64.b64encode(audio_content)

def longrunning_recognize(appid, token, url):
    data = {
        'config': {
            'encoding': 'LINEAR16',
            'sample_rate_hertz': 16000,
            'language_code': 'zh-cmn-Hans-CN'
        },
        'audio': {
            'uri': url
        }
    }
    headers = {
        'Content-Type': 'application/json',
        'Appid': appid,
        'Authorization': 'Bearer ' + token
    }

    r = requests.post('https://api.zhiyin.sogou.com/apis/asr/v1/longrunning_recognize', data=json.dumps(data),
                      headers=headers)
    resp = json.loads(r.text)
    print(resp['name'])

    time.sleep(30)
    r = requests.get('https://api.zhiyin.sogou.com/apis/longrunning/get_operation/' + resp['name'], headers=headers)
    print(r.text)


APP_ID = '1amnWXhelnPxbCHgHDevySoqUIg'
TOKEN = "eyJhbGciOiJkaXIiLCJjdHkiOiJKV1QiLCJlbmMiOiJBMTI4R0NNIiwidHlwIjoiSldUIiwiemlwIjoiREVGIn0..MhOS8C4ySNMRAGK3.q533_HxiZaUdiljKMMZN5eGdOwOQObaHCxMRLQ5NUWDQ4C-HOxH_boURGkGYU-5UD80ywmP-NDP0NCcT_gcXkHcEHSuPqFnf6ulvjbocoFaxuzebnq-X5Lx10SqAhnyLyflwbwAeiKXpRX7jd-T4ZcKSs0RiJU7Q0IngrWOiY925samX7dsc3gZReGkwFYPaWmYaz6gdhdFCzDu2xJnHRxS64orzD_huvDQrkAUGnja33xyhGUXnqLrpiDHL7KomLvFBX52b7yPFtQKFi00AVcB1pX2a3DdWDtsUZJDK2hXizoh4_LIY8lxhEF2dbM1KH5zVxtH_pK_b1NS5PnU7xglA1EkwXlMPV0yJUS0n.QJW8_9-C2U-tsescUJs2bg"

base64_uri = encode_audio('output1.wav')
url = r'https://articuly.com/wp-content/uploads/2020/04/未命名混音项目-1_缩混.wav'

longrunning_recognize(APP_ID, TOKEN, url)
