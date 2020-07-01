from pyquery import PyQuery as pq
import requests
import json

def json1():
    url='https://www.dytt8.net/'
    h={'User-agent':  'Baiduspider'}

    r=requests.get(url=url,headers=h)
    r.encoding=r.apparent_encoding
    doc=pq(r.text)

    a=doc('a')
    kk=[]
    for i in a.items():
        k=dict()
        k['name']=i.text()
        k['href']=i.attr('href')
        kk.append(k)
    str1=[{"name":"s","year":"44"},{"name":"ss","year":"445"}]
    with open('data.json','w+',encoding='utf-8') as t:
        for i in kk:
          t.write(json.dumps(i,ensure_ascii=False,indent=2))


    str1='''
    [{"name":"s","year":"44"},{"name":"ss","year":"445"}]
    '''
    print(str1)
    print(json.loads(str1))
def k():
    import json

    print(json.loads('[{"asdsadas":1},{"ad":4}]'))
def main():
    k()
if __name__ == '__main__':
    main()