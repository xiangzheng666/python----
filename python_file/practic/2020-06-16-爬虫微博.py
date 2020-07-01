from bs4 import BeautifulSoup
import time
from selenium import webdriver

op=webdriver.ChromeOptions()
op.add_argument('headless')
ch=webdriver.Chrome()

headers={
 'User_Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.163 Safari/535.1'
}

url="https://kyfw.12306.cn/otn/leftTicket/init?linktypeid=dc&fs=%E4%B8%8A%E6%B5%B7,SHH&ts=%E5%B9%BF%E5%B7%9E,GZQ&date=2020-06-"
mo="&flag=N,N,Y"

def get_page(url):
    ch.get(url)
    return ch.page_source

def main():
    for i in range(17,31):
        url1=url+str(i)+mo
        print(url1)
        page=get_page(url1)

        soup=BeautifulSoup(page,'html.parser')
        item=soup.find('tbody',attrs={'id':'queryLeftTable'}).contents
        for i in item:
            print(i)
            print("==============")
        print("*****************************")
        time.sleep(10)
if __name__ == '__main__':
    main()
#t-list > table