import requests
import re

url='https://maoyan.com/board/4'
# url='http://spark.12192.top'

r=requests.request(method='get',url=url,timeout=4)
print(r.status_code)
r.encoding=r.apparent_encoding

a=re.compile(r'>\w.+\w</')
text=re.findall(a,r.text)
print(text)
text1=text

for i in range(len(text1)):
    text1[i]=re.sub(r'<a.+>|</|>','',text1[i])
print(text1)

print(re.findall(r'[a-z|:|\d|.]+@[a-z|.|\d]+',r.text))

r=requests.request(method='get',url=url,timeout=4,files={'files':open('test.txt')},verify=False,proxies={'http':'http:loaclhost:8080'})
print(r.status_code)