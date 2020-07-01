import requests
from lxml import etree
from requests.auth import HTTPBasicAuth
from bs4 import BeautifulSoup,NavigableString,Tag
from pyquery import PyQuery
import re

def donban_a():
    url='https://movie.douban.com/'
    auths=HTTPBasicAuth('16533907258','liu123321')
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36'
    }
    r=requests.get(url, auth=auths,headers=headers)
    r.encoding=r.apparent_encoding


    html=etree.HTML(r.text)
    print("===============\n===lxml===")
    print(len(list(html.xpath('//a/text()'))))
    print(len(list(html.xpath('//a/@href'))))
    for i,j in zip(list(html.xpath('//a/text()')),list(html.xpath('//a/@href'))):
        print(i,j)
        s=i+j
        with open('lxml-a.txt', 'a', encoding='utf-8') as t:
            t.write(s)
            t.write('\n')

    print("===============\n===soup===")
    soup=BeautifulSoup(r.text,'html.parser')
    for i in soup.find_all('a'):
        if 'href' in dict(i.attrs).keys() and i.string!=None:
            print(i.string,i.attrs['href'])
            s=i.string+i.attrs['href']
            with open('soup-a.txt','a',encoding='utf-8') as t:
                t.write(s)
                t.write('\n')


    print("===============\n===pyquery===")
    doc=PyQuery(r.text)
    for i in doc('html').find('a').items():
        with open('pyquery-a.txt','a',encoding='utf-8') as t:
            if  i.attr.href!=None:
                print(i.text(),i.attr.href)
                t.write(i.text())
                t.write(i.attr.href)
                t.write('\n')


def tiant():
    url = 'https://www.dytt8.net/'
    auths = HTTPBasicAuth('16533907258', 'liu123321')
    headers = {
        'User-Agent': 'Mozilla/5.0 '

    }
    r = requests.get(url, auth=auths, headers=headers)
    r.encoding = r.apparent_encoding

    soup=BeautifulSoup(r.text,'html.parser')

    a=soup.find('div',attrs={'class':'bd2'})
    for i in soup.find('div',attrs={'class':'bd2'}):
        if isinstance(i, NavigableString):
            continue
        if isinstance(i, Tag):
            for co_area2 in i.find_all('div', attrs={'class': 'co_area2'}):
                k=co_area2.find('div',attrs={'class':'title_all'})
                k=str(k.find('strong'))

                print('===========================')
                print(re.sub(r'[a-z|A-Z]|[^\w]|\d',r'',k))

                k1 = co_area2.find('ul')
                k=co_area2.find('table')
                if k!=None:
                    for iii in k.find_all('td',{'class':'inddline'}):
                        k=iii.find_all('a')
                        k=" ".join('%s' %id for id in k)
                        print(re.sub(r'[a-z|A-Z]|[^\w]|\d',r'',k))
                else:
                    for iii in k1.find_all('a'):
                        print(iii.string,iii)



    # html = etree.HTML(r.text)
    # k=html.xpath('body//div[@class="bd2"]//*//text()')
    # print(k)
def main():
    tiant()

if __name__ == '__main__':
    main()