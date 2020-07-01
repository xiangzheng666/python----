'''
    this is a introduction of this file
'''






import requests
import urllib.request as r
from bs4 import BeautifulSoup

url='http://mp.weixin.qq.com/mp/jsreport?key=10&content=https%3A%2F%2Fmmbiz.qlogo.cn%2Fmmbiz_jpg%2FI0eRibQ2pVchES3IhGnQLzb0I48mv6JUxiaU2x5kh79uLIpiafmKMYvhNdjRFULv9ia9OCN8GkibMnveGYsYSGe1iblQ%2F640%3Fwx_fmt%3Djpeg%26tp%3Dwxpic%26wxfrom%3D5%26wx_lazy%3D1%26wx_co%3D1%26retryload%3D2[]&r=0.4202305850821919'
text=r.urlopen(url)
html=text.read().decode('utf-8')

print(html)