from pyquery import PyQuery as pq
import urllib.request as req
import csv
def url1():
    url='https://www.baidu.com/'
    h={'User-agent':  'Baiduspider'}

    u=req.Request(headers=h,url=url)
    reaponse=req.urlopen(u,timeout=3)
    html1=reaponse.read().decode('utf-8')
    doc=pq(html1)

    k=doc('body').text()
    k=list(k)
    print(len(k))
    q=[]
    kk=1
    for i in range(1,306):
       if i%5==0:
           q.append(k[kk-1:i-1])
           kk=kk+5
    print(q)

    with open('t.csv','w',encoding='utf-8') as t:
        w=csv.writer(t,delimiter=',')
        for i in q:
            w.writerow(i)
def list1():
    l1=['id','year','num']
    l2=[[100,2019,3],[400,2015,60]]
    with open('list.csv','w+',encoding='utf-8') as t:
        w=csv.writer(t,delimiter=' ')
        w.writerow(l1)
        w.writerows(l2)

def dict1():
    l1=['id','year','num']
    l2=[[100,2019,3],[400,2015,60]]
    with open('dict.csv','w+',encoding='utf-8') as t:
        w=csv.DictWriter(t,delimiter=' ',fieldnames=l1)
        w.writeheader()
        w.writerow({'id':4,'year':5,'num':7})
        w.writerow({'id': 40, 'year': 50, 'num': 70})

def new():
    import requests
    import csv

    url = 'https://www.dytt8.net/'
    h = {'User-agent': 'Baiduspider'}

    r= requests.get(url=url, headers=h)
    r.encoding = r.apparent_encoding
    doc = pq(r.text)

    a = doc('a')
    l1 = ['name of a', 'href of a']
    with open('dict.csv','w+',encoding='utf-8') as t:
        w=csv.DictWriter(t,delimiter=' ',fieldnames=l1)
        w.writeheader()
        for i in a.items():
            tem={'name of a':i.text(),'href of a':i.attr('href')}
            w.writerow(tem)


if __name__ == '__main__':
    new()