import pymysql
import os
db=pymysql.connect('localhost','root','123456')# 地址  用户名  密码
cursor=db.cursor()#游标
cursor.execute('show databases')
print cursor.fetchall()


cursor.execute('use 1510F')
cursor.execute('select month,days from lanjingjing')
str=cursor.fetchall()


os.chdir('d:/')
file=open('test.txt','w+')
file.write(str(str))
file.close()
db.close()