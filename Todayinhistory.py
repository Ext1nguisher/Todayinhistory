import json
import requests
from datetime import datetime

http_ok = range(200,300)

def Todayinhistory():


    timenow = datetime.now()

    if timenow.month < 10:
        month = f"0{timenow.month}"
    else:
        month = timenow.month

    if timenow.day < 10:
        day = f"0{timenow.day}"
    else:
        day = timenow.day

    url = f"https://baike.baidu.com/cms/home/eventsOnHistory/{month}.json"

    headers = {
        "host": "baike.baidu.com",
        "referer": "https://www.baidu.com",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
        "Accept-Language": "zh-CN",
        "Accept": "text/html",
        "Connection": "keep-alive",
        "sec-ch-ua-platform":"Windows"
    }

    response = requests.get(url=url,headers=headers)

    if not response.status_code in http_ok:
        raise KeyError(f"远程服务器返回错误:{response.status_code}")

    meta = json.loads(response.content.decode("utf-8"))

    return meta[f"{month}"][f"{month}{day}"]

