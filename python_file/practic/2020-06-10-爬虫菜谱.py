from selenium import webdriver
import pandas as pd
from pyquery import PyQuery
from bs4 import BeautifulSoup
import re

op=webdriver.ChromeOptions()
op.add_argument('headless')

ch=webdriver.Chrome(options=op)



#获取url中一系列菜的网址,获取每一个菜的网址后返回菜名，菜的用料
def get_foods(url,out):
    base="http://www.xiachufang.com"
    ch.get(url)
    page=ch.page_source


    doc=PyQuery(page)
    h=doc("body > div.page-outer > div > div > div.pure-u-2-3.main-panel > div.white-bg.block > div > div.pure-u-3-4.category-recipe-list > div.normal-recipe-list > ul").items()
    for k,j in enumerate(h):
        soup=BeautifulSoup(str(j),'html.parser')
        for i in soup.find_all('div',attrs={"class":"info pure-u"}):
            tem=[]
            name=i.select('p a')[0].get_text().strip()

            all=i.select('p')[1].get_text().strip()

            score=re.findall(r'[\d,\.]+', i.select('p')[2].get_text())[0]

            ht=str(i.select('p')[3])
            http=base+re.findall(r'/cook/\d+',ht)[0]

            tem.append(name)
            tem.append(all)
            tem.append(score)
            tem.append(http)
            print(len(out))
            out.append(tem)
    return out


def test():
    base_url="http://www.xiachufang.com/category/"
    s=40076
    out=[]
    for i in range(3):

        url=base_url+str(s+i)+'/'
        get_foods(url,out)

    c=pd.DataFrame(out,columns=['name','all','score','http'])
    c.iloc[1:,:].to_csv('food.csv',index=False)

if __name__ == '__main__':
    pass