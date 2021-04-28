# 测试 Serving 服务
import pandas as pd
import requests
import json

data = pd.read_csv("Advertising.csv")
# print(data.head())
test = data.iloc[:1, 1:-1]

# 类型为 DataFrame
# print(type(test))
# DataFrame 转 JSON 格式
# pay_load = test.to_json(orient='records')
# print(pay_load)
# DataFrame 转 List 格式
pay_load = test.values.tolist()

# 查看状态 http://127.0.0.1:8501/v1/models/sales
# 输入输出格式 http://127.0.0.1:8501/v1/models/sales/metadata

pay_load = {"signature_name": "serving_default", "inputs": {"dense_input": pay_load}}
# print(pay_load)
SERVER_URL = 'http://127.0.0.1:8501/v1/models/sales:predict'
response = requests.post(SERVER_URL, json=pay_load)
print(response.json()['outputs'][0])


