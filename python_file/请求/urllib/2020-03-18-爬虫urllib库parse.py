from urllib import request,error,parse
import re

url="https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&tn=baidu&wd=%E7%88%AC%E8%99%AB.read().decode(%27utf-8%27)%E5%87%BA%E6%9D%A5%E7%9A%84%E4%B9%B1%E7%A0%81&oq=(re.read().decode(%2526%252339%253Butf-8%2526%252339%253B)%25E5%2587%25BA%25E6%259D%25A5%25E7%259A%2584%25E4%25B9%25B1%25E7%25A0%2581&rsv_pq=b6dc856900008b41&rsv_t=d3e4h4XBCPAF0jsbR9tiO8uzN%2BcY6Qj0rvwoHPJwy6om4qQBm9Whd4IoHII&rqlang=cn&rsv_dl=tb&rsv_enter=1&rsv_sug2=0&inputT=1084&rsv_sug4=1084"
data=["http","spark.12192.top",'','','','']
data1=["http","spark.12192.top",'','','']
url1=parse.urlunsplit(data1)

try:
    # re=request.urlopen("http://spark.12192.top",timeout=40)
    # print(re.read().decode('UTF-8','ignore'))
    reault=parse.urlparse(url)
    print(parse.urlparse(url))
    print(parse.urlunparse(data))
    print(parse.urlsplit(url))
    print(parse.urlunsplit(data1))
    print(parse.parse_qsl(reault.query))
    print(parse.parse_qs(reault.query))
    k = parse.parse_qs(reault.query)
    print(url1+parse.urlencode(k))
    print('=====')
    t=url1+parse.urlencode(k)
    request.urlopen(url)
    print('====')
    print(url1+parse.quote("急刹车皮的"))
    u=url1 + parse.quote("急刹车皮的")
    print('=====')
    print(parse.unquote(u))
except error.URLError as e:
    print(e.reason)
