#coding=utf-8
import pymysql
from selenium import webdriver

db=pymysql.connect('localhost','root')#连接数据库 地址  用户名  密码  数据库名字
cursor=db.cursor()#游标
# cursor.execute('show databases')#查询语句  用来查询所有的数据库
# data=cursor.fetchall()#获取游标所有的数据
# print data
# cursor.execute('show tables')
cursor.execute('create database lanjingjing')
cursor.execute('use lanjingjing')
cursor.execute('create table test(name VARCHAR(50),password VARCHAR(50))')
cursor.execute('insert into test(name,password) values '
               '(\'admin\',\'123\'),(\'tom\',\'456\'),(\'jerry\',\'789\')')
db.commit()
print cursor.fetchall()

