#coding=utf-8
import pymysql
import os
class dbTest:
    def __init__(self):
        self.db=pymysql.connect('localhost','root')#连接数据库 数据库地址 用户名
        self.cursor=self.db.cursor()#游标
        self.cursor.execute('show databases')#显示当前用户下的所有数据库
        print self.cursor.fetchall()#打印数据
        self.cursor.execute('use lanjingjing')#切换到lanjingjing数据库下
        self.str=''
        self.map = {}
    def selectMenu(self):
        self.cursor.execute('select name,price from test2')#查询菜单中所有的菜名  价格
        n = len(self.cursor.fetchall())#菜名的数量
        self.cursor.execute('select name,price from test2')

        for i in range(n):
            data=self.cursor.fetchone()
            self.map.update({data[0]:data[1]})#将查询出来的菜名 价格以键值对的形式添加到map中

        print self.map#打印字典

    def inputandCalc(self):
        n=raw_input('请输入菜名')#输入菜名
        if n in self.map.keys():#如果菜名存在的话
            num=int(raw_input('请输入数量'))#输入点菜的数量
            self.str='总价为：%d'%(num*self.map[n])#将总价赋值给str属性
        else:
            str=raw_input('是否添加菜名，输入y则添加，输入其他拒绝')#如果不存在的话  则判断是否添加到数据库
            if str=='y':#如果添加的话
                p=int(raw_input('请输入价格：'))#输入菜品的价格
                self.cursor.execute\
                    ('insert into test2(name,price) values (\'%s\',%d)'%(n,p))#插入到数据库
                self.db.commit()#注意 ：提交数据库
                print '更新成功'
                self.selectMenu()#再次查询
                self.inputandCalc()#再次点菜
            else:
                self.str=' 没有这个菜名'#选择不添加新的菜品名称到数据库
    def writetofile(self):#像文件写入
        os.chdir('d:/')#切换到D盘下
        f=open('test.txt','w+')#以可读可写的模式打开数据库
        f.write(self.str)#写入字符串
        f.seek(0)#将游标方法起始位置
        print f.read()#读取
        f.close()#关闭文件
        self.db.close()#关闭数据库








test=dbTest()
test.selectMenu()
test.inputandCalc()
test.writetofile()

