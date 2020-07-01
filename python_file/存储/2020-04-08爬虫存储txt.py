import urllib.request as req

from pyquery import PyQuery as pq

url='https://www.baidu.com/'
h={'User-agent':  'Baiduspider'}

u=req.Request(headers=h,url=url)
reaponse=req.urlopen(u,timeout=3)
html1=reaponse.read().decode('utf-8')
doc=pq(html1)

with open('t.txt','a',encoding='utf-8') as t:
    t.write(doc('body').text())