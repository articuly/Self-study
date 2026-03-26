import requests
import json

def test_chat_api():
    # API端点
    url = "http://localhost:6969/v1/chat/completions"  # 根据实际本地服务器地址修改端口号

    # 请求头
    headers = {
        "Content-Type": "application/json"
    }

    # 请求数据
    payload = {
        "model": "gemini-2.5-flash-preview-05-20",
        "messages": [{"role": "user", "content": "Hello!"}]
    }

    try:
        # 发送POST请求
        response = requests.post(url, headers=headers, json=payload)

        # 检查响应状态码
        if response.status_code == 200:
            # 解析JSON响应
            result = response.json()
            print("请求成功！响应数据：")
            print(json.dumps(result, indent=2, ensure_ascii=False))
        else:
            print(f"请求失败，状态码：{response.status_code}")
            print("错误信息：", response.text)

    except requests.exceptions.ConnectionError:
        print("连接错误：无法连接到服务器，请确保服务器正在运行且地址正确")
    except Exception as e:
        print(f"发生错误：{str(e)}")

if __name__ == "__main__":
    test_chat_api()