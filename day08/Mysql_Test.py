#coding=utf-8
import pymysql
import os
# db=pymysql.connect('192.168.163.1','root','123456')
db=pymysql.connect(host='60.205.189.12',user='visitor',port=3306,passwd='123456')

t=db.cursor()
t.execute('show databases')
print t.fetchall()
t.execute('use 1510F')
t.execute('select * from lanjingjing')
print t.fetchall()
t.execute('select * from lanjingjing')
d=t.fetchall()
os.chdir('/etc/')
file=open('test.txt','w+')
file.write(str(d))

