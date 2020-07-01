from urllib import request,error,robotparser

url='http://www.baidu.com'
u='https://www.jsu.edu.cn/'

try:
    r=request.urlopen(url,timeout=4)
    f=robotparser.RobotFileParser()
    f.set_url(url+'/robots.txt')
    f.read()
    print(f)
    print(f.parse('EasouSpider'))
    print(f.can_fetch('*', url))
    print(f.mtime())
except error.URLError as e:
    print(e.reason)