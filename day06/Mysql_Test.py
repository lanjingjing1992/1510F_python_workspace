#coding=utf-8
import pymysql
class Test:
    def __init__(self):
        db=pymysql.connect('localhost','root')#连接数据库 地址  用户名  密码  数据库名字
        cursor=db.cursor()#游标
        cursor.execute('use lanjingjing')
        cursor.execute('select * from test')
        self.map={}
        for i in range(3):
            data= cursor.fetchall()
            self.map.update({data[0]:data[1]})

        # print self.map#打印字典


