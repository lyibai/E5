import requests

# 发送 HTTP 请求
response = requests.get("https://data.js/api/data")

# 解析响应
data = response.json()

# 打印数据
print(data)
