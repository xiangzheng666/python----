import requests

import re

url="http://spark.12192.top/"
url="https://www.12306.cn"
u1='https://github.com/favicon.ico'

try:
    r = requests.get(url, timeout=10)
    # print(r.text)
    # r.raise_for_status()
    r.encoding=r.apparent_encoding
    print(r.status_code)
    print(r.apparent_encoding)
    print(r.encoding)
    print(r.content)
    print(r.cookies)
    print(r.text)


    with open('github.ico','wb') as t:
        r=requests.request(method='get',url=u1)
        t.write(r.content)
        print(r.content)

except requests.ConnectionError as e:
    print("error")
    print(e.response)