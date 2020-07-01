import urllib.request as req
from urllib import parse
from urllib.request import HTTPPasswordMgrWithDefaultRealm, HTTPBasicAuthHandler, build_opener,ProxyHandler

####url.request.urlopn()######
#urllib的request模块的请求urlopen(url)
# urllib . request . urlopen(url, data=None, [timeout,]*, cafile=None, capath=None, cadefault=False, context=None)
# response=req.urlopen("http://spark.12192.top")
#请求的类型为HTTPresponse
# print(type(response))
# 它是一个 HTTPResposne 类型的对象，
# 主要包含 read （）
# readinto （）
# getheader(name）
# getheaders（）
# fileno（）等方法
# 以及 msg
# version
# status
# reason
# debuglevel
# losed 等属性
#获取response的信息
# print(response.getheaders())
# print(response.getheader('server'))
# #请求的html
# print(response.read().decode('utf-8'))
# #请求的文本类型为bytes
# print(type(response.read()))
# #请求的状态码
# print(response.status)
####url.request.urlopen()######

####Request######
# headers = {
# 'User-Agent':'Mozilla/4.0(compatible;MSIE S.S;Windows NT)',
# 'Host':'www.captainbed.net'}
# dict={'name':'world'}
# data=bytes(parse.urlencode(dict), encoding='utf8')

# urllib.request.Request(ur1,data=None,headers={},origin_req_host=None,unverifiable=False, method=None)
# Re=req.Request(url="https://www.captainbed.net/", headers=headers, method='post',origin_req_host='localhost',unverifiable=False)
# response=req.urlopen(Re)
# print(response.read().decode('utf-8'))
####Request######


# ####验证####
# usename='usenaem'
# password='password'
# url="http://localhost:5000"
#
# p=HTTPPasswordMgrWithDefaultRealm()
# p.add_password(None,url,usename,password)
# a=HTTPBasicAuthHandler(p)
# opener=build_opener(a)
#
# r=opener.open(url)
# print(r.read().decode('utf-8'))
# ####验证####

# ####代理####
proxy_handler = ProxyHandler({
'http':'111.222.141.127 '
})

opener = build_opener(proxy_handler)
response = opener.open('http://spark.12192.top/')
print(response.status)
# ####代理####

# ####cookie####
# # import http.cookiejar,urllib.request
# # cookie = http.cookiejar.CookieJar()
# # handler = urllib.request.HTTPCookieProcessor (cookie)
# # # opener = urllib.request.build_opener(handler )
# # response = opener.open('http://www.baidu.com')
# # for item in cookie:
# #     print(item.name+'='+item.value)
# # ####COOKIE####
