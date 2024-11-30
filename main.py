import json
import requests
from datetime import datetime

HTTP_OK = list(range(200, 300))


def today_in_history(lang="zh-CN"):
    now = datetime.now()
    month = "%02d" % now.month
    day = "%02d" % now.day

    url = f"https://baike.baidu.com/cms/home/eventsOnHistory/{month}.json"
    agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/\
537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"
    headers = {
        "host": "baike.baidu.com",
        "referer": "https://www.baidu.com",
        "User-Agent": agent,
        "Accept-Language": lang,
        "Accept": "text/html",
        "Connection": "keep-alive",
        "sec-ch-ua-platform": "Windows"
    }

    response = requests.get(url=url, headers=headers)

    if response.status_code not in HTTP_OK:
        raise KeyError(f"{'远程服务器返回错误' if lang == 'zh-CN' else 'Remote server returned an error'}:{response.status_code}")

    meta = json.loads(response.content.decode("utf-8"))
    return meta[f"{month}"][f"{month}{day}"]
