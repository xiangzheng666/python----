import requests
from lxml import etree
from urllib import error
from urllib import request,robotparser

url='http://spark.12192.top'
url1='https://www.baidu.com/'
kk={'User-agent': 'Baiduspider'}
url2='https://cn.bing.com/'

try:
    k=robotparser.RobotFileParser()
    print(k.can_fetch('*', url))
    r=requests.request(method='post',url=url1,timeout=5,headers=kk)
    r.encoding=r.apparent_encoding
    print(r.apparent_encoding)
    html=r.text
    print(html)
    h=etree.HTML(html)
    # print(etree.parse(html, etree.HTMLParser()))
    print(h.xpath('//html'))
    print(h.xpath('//html/head'))
    print(h.xpath('//html/head//text()'))
    print(h.xpath('//html//head//meta//@*'))
    print(h.xpath('//html/body//@class'))
    print(h.xpath('//html/body//a/@class'))
    print(h.xpath('//html/body//a/@href'))
    print(h.xpath('//html/body//a[@class="mnav"]/text()'))
    print(h.xpath('//html/body//a[@class="bri"]/text()'))
    print(h.xpath('//html/body//a[@href="http://tieba.baidu.com"]/../@*'))
    print(h.xpath('//html/body//a[@href="http://tieba.baidu.com"]/ancestor::*/@*'))

except error.HTTPError as e:
    print(e.reason)
