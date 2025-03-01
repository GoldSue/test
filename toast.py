import requests
import base64
import json
import binascii

# 请求订阅链接
url = "https://sub.nccloud.co/api/v1/client/subscribe?token=a7474c86a1f1fe59f3671789a179b3ec"
response = requests.get(url)
# print(response.text)

if response.status_code == 200:
    print("请求成功，状态码:", response.status_code)
    response_text = response.text.strip()

a = base64.b64decode(response_text).decode('utf-8')
print(a)

#     # 分割并处理每一行
#     lines = response_text.split('\n')
# for line in a:
# if line.startswith("vmess://"):
#     try:
#         vmess_data = line[8:]  # 去掉 "vmess://"
#         decoded_data = base64.b64decode(vmess_data)
#         inner_decoded_data = base64.b64decode(decoded_data.decode('utf-8')[8:]).decode('utf-8')  # 解码嵌套的Base64
#         vmess_json = json.loads(inner_decoded_data)
#         print("VMess 解码结果:", json.dumps(vmess_json, indent=4, ensure_ascii=False))
#     except (binascii.Error, json.JSONDecodeError) as e:
#         print(f"VMess 解码失败: {e}")
# elif line.startswith("ss://"):
#     try:
#         ss_data = line[5:]  # 去掉 "ss://"
#         if '@' in ss_data:
#             method_pass, server_info = ss_data.split('@', 1)
#             method_pass = base64.b64decode(method_pass).decode('utf-8')
#             method, password = method_pass.split(':', 1)
#             server, port = server_info.split('#', 1)[0].split(':', 1)
#             print(f"SS 解码结果: method={method}, password={password}, server={server}, port={port}")
#         else:
#             print(f"SS 链接格式错误: {line}")
#     except binascii.Error as e:
#         print(f"SS 解码失败: {e}")
# else:
#     print(f"未知格式: {line}")
#
# else:
# print("请求失败，状态码:", response.status_code)
