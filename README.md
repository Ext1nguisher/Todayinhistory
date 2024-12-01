# Todayinhistory
基于百度百科 API 的历史上的今天


## 使用方法

On Windows

```powershell
python -m pip install requests
```

On Linux/OSX(macOS)

```bash
python3 -m pip install requests
```

使用代码

```python
import main


content = main.today_in_history()

# 可指定 lang 参数，例如英语
content = main.today_in_history(lang="en-US")
```
参考 [MDN - Accept-Language](https://developer.mozilla.org/zh-CN/docs/Web/HTTP/Headers/Accept-Language)

将会返回一个包含多个字典的列表

json 字典格式：
```json
{
        "year": "1602",
        "title": "日本战国女城主\u003Ca target=\"_blank\" href=\"https://baike.baidu.com/item/%E7%AB%8B%E8%8A%B1%E8%A8%9A%E5%8D%83%E4%BB%A3\"\u003E立花訚千代\u003C/a\u003E逝世",
        "festival": "",
        "link": "https://baike.baidu.com/item/%E7%AB%8B%E8%8A%B1%E8%A8%9A%E5%8D%83%E4%BB%A3",
        "type": "death",
        "desc": "立花訚千代（たちばな ぎんちよ、永禄12年8月13日（1569年9月23日）—\u003Ca target=\"_blank\" href=\"https://baike.baidu.com/item/%E5%BA%86%E9%95%BF\"\u003E庆长\u003C/a\u003E7年10月17日（1602年11月30日））是\u003Ca target=\"_blank\" href=\"https://baike.baidu.com/item/%E6%97%A5%E6%9C%AC%E6%88%98%E5%9B%BD%E6%97%B6%E4%BB%A3\"\u003E日本战国时代\u003C/a\u003E的女",
        "cover": false,
        "recommend": false
      }
```
