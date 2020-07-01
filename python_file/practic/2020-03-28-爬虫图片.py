# from urllib import request
import pymysql

url='https://wx4.sinaimg.cn/thumb180/006pGX6ely1gd8jo4euurj30h80r7wfc.jpg'

# with open('E:/{0}.jpg'.format(1), 'wb') as file:
#     file.write(request.urlopen(url).read())
db=pymysql.connect(host='localhost',user='root',
                   password='1233211223',database="sprider",
                   charset="utf8")
cursor = db.cursor()
cursor. execute (" SELECT VERSION()")
data = cursor. fetchone()
print (" Database version:", data)

cursor.execute ("CREATE table spiders")
db.close()