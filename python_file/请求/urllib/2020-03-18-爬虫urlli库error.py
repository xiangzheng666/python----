from urllib import request,error

url="http://spark.12192.top"

try:
    re=request.urlopen("http://spark.12192.top",timeout=40)
    print(re.read().decode('UTF-8'))
except error.URLError as e:
    print(e.reason)
