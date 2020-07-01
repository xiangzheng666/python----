from selenium import webdriver
from bs4 import BeautifulSoup
import re
import requests
from pyquery import PyQuery
import os
from lxml import etree

from urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


option = webdriver.ChromeOptions()
option.add_argument('headless')
browser=webdriver.Chrome()


base_url1=r'https://cise.jsu.edu.cn/'


base_url=r'https://cise.jsu.edu.cn/xygk/ggjs'
all_page=['.htm','/1.htm','/2.htm']

for i in all_page:
    url=base_url+i
    browser.get(url)
    page=browser.page_source


    h=PyQuery(page)
    all_pe=h('body > div.ntp > div > div > div.cla2 > div.cla22 > div.cla222 > div.gugan > div.gugan1 >a')
    for i in all_pe.items():
        s=str(i.attr('href'))
        url1=base_url1+'/'.join(re.findall(r'\w+',s)[:-1])+'.'+re.findall(r'\w+',s)[-1]
        r=browser.get(url1)
        k=PyQuery(browser.page_source)
        s=re.sub(r'<.+>','',k('#vsb_content > div').text())
        if s=='':
            s='暂无'
        print(s[0:4])
        print('====================')
        print(s)
        print('======================')
        with open('jsdx/jsdx.txt','a+',encoding='utf-8') as f:
            f.write(s+'\n')
        pic=etree.HTML(browser.page_source)
        p=pic.xpath('/html/body/div[3]/div/div/div[2]/div[2]/form/div[3]/div//p//img/@src')
        pic_u = base_url1 + p[0]
        if re.match(r'\w{2,4}', s):
                path = r'jsdx/%s.jpg' % re.match(r'\w{2,4}', s).group()
                with open(path,'ab+') as f:
                    f.write(requests.get(pic_u,verify=False).content)
                print('%s的图片下载完成'%re.match(r'\w{2,4}', s).group())
                print('======================')
    print('下一页开始')
    print('======================')
browser.close()