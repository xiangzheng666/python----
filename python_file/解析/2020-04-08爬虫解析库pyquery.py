from pyquery import PyQuery as pq
import urllib.request as req

url='https://www.baidu.com/'
h={'User-agent':  'Baiduspider'}

u=req.Request(headers=h,url=url)
reaponse=req.urlopen(u,timeout=3)
html1=reaponse.read().decode('utf-8')
doc=pq(html1)
print('CSS选择器：')
print(doc('.mnav'))
print(doc('body  .mnav'))
print('在css选择器查找节点：')
print(doc('body').find('a'))
print(doc('body').children('*'))
print('生成器')
for i in doc('body').find('a').items():
    print(i,"\n")
print('获取信息：')
for i in doc('body').find('a').items():
    print(i.attr('href'),"\n")
    print(i.text(), "\n")
    print(i.html(), "\n")
print("节点操作增加class：")
doc('body').find('a').add_class('ll')
print('class:',doc('body').find('a').attr('class'))
print('伪类选择')
print(doc('body :first-child'))