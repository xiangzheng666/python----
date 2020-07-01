import requests
from bs4 import BeautifulSoup,NavigableString,Tag
import re

url='https://www.baidu.com/'
h={'User-agent':  'Baiduspider'}

try:
    r=requests.request(method='get',url=url,headers=h)
    r.encoding=r.apparent_encoding
    html=r.text
    bs=BeautifulSoup(html,'html.parser')
    print(bs.prettify())
    print('bs.title.string:'+bs.title.string)
    print('bs.title.get_text():',bs.title.get_text())
    print('=节点选择器:')
    print(bs.html.body.a.name,bs.html.body.a.string)
    print('=====直接子节点:')
    print(bs.body.contents)
    for i, j in enumerate(bs.body.children):
        print(i, j)
    print('=====全部子节点：节点+ string')
    for i, j in enumerate(bs.descendants):
        print(i, j)
    print('=====全部父亲节点a：节点+ string')
    for i, j in enumerate(bs.a.parents):
        print(i, j)
    print('=====父亲节点a：节点+ string')
    for i, j in enumerate(bs.a.parent):
        print(i, j)
    print('=====直接旁边节点：节点+ string')
    for i, j in enumerate(bs.a.next_siblings):
        print(i, j)
    print('=====直接旁边节点：节点+ string')
    for i, j in enumerate(bs.a.previous_siblings):
        print(i, j)
    for body_child in bs.body.children:
        if isinstance(body_child, NavigableString):
            continue
        if isinstance(body_child, Tag):
            print(body_child.name)
    print('==========方法选择器：')
    print("find返回第一个")
    print(bs.find('a'))
    print("find_all返回所有")
    print(bs.find_all('a'))
    print("find_all返回所有特定attr")
    print(bs.find_all('a',attrs={'class':'mnav'}))
    print("find_all返回所有特定text")
    print(bs.find_all('a', text=re.compile(r'\w{4}')))
    print("find_all_next返回所有")
    print(bs.a.find_all_next())
    print("find_next返回一个")
    print(bs.a.find_next())
    print('parent:', bs.find('a').find_parents())
    print('==========css选择')
    print('id选择器\n', bs.select('.mnav'))
    print('id选择器的信息')
    for i in bs.body.select('.mnav'):
        print(i.get_text())
    print('tag选择器的信息')
    for i in bs.body.select('div'):
        print(i.select('a'))
except requests.ConnectionError as e:
    print(e.response)