# coding:utf-8
import requests
import base64


def get_key_from_url(url: str, userid: str) -> str:
    """
    通过请求m3u8文件中的key的url,获取解密视频key的base64字符串密钥
    :param url: m3u8文件中获取key的url
    :param userid: 用户id，放视频时飘动的那一串
    :return: key的base64字符串
    """
    # url拼接uid参数
    url += f'&uid={userid}'
    # print(url)
    # 发送get请求
    rsp = requests.get(url=url)
    rsp_data = rsp.content
    if len(rsp_data) == 16:
        userid_bytes = bytes(userid.encode(encoding='utf-8'))
        result_list = []
        for index in range(0, len(rsp_data)):
            result_list.append(
                rsp_data[index] ^ userid_bytes[index])
        print(result_list)
        return base64.b64encode(bytes(result_list)).decode()
    else:
        print(f"获取异常，请求返回值：{rsp.text}")
        return ''


if __name__ == '__main__':
    url1 = 'https://app.xiaoe-tech.com/xe.basic-platform.material-center.distribute.vod.pri.get/1.0.0?app_id=appmy5R3FCm5076&mid=b968e172-5912-4e31-bc96-ecbbe6a3128d&urld=23fcc8473a95bd6913156de4c56ac165'
    url2 = 'https://app.xiaoe-tech.com/xe.basic-platform.material-center.distribute.vod.pri.get/1.0.0?app_id=appmy5R3FCm5076&mid=27e3c189-bd67-4716-a477-cf366ca3b696&urld=5868bf13d55fe7757743d99c183654a8'
    _uid = 'u_613611bce8ff5_XU5HtMX3Lg'
    base64_key = get_key_from_url(url=url2, userid=_uid)
    print(base64_key)
    # CZ96GcxuJWpJCVGz6a3NDQ==
    # +z+PJBfTe4/iNAlOZXZUeQ==
