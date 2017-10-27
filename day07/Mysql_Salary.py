#coding=utf-8
import pymysql
import  re
class DbTest:
    def __init__(self):
        self.db=pymysql.connect('localhost','root')#地址  用户名  密码  需要连接的数据库
        self.cursor=self.db.cursor()#游标
        self.cursor.execute('use lanjingjing')
        self.cursor.execute('select name,salary from test1')#查询姓名 工资
        data = self.cursor.fetchall()  #取出来所有人的姓名 工资
        print data
        self.n = len(data)
        file=open('test.txt','w+')  #新建一个名字为test.txt的文件
    def Select(self,name='',month=1):


        self.cursor.execute('select name,salary from test1')
        for i in range(self.n):
                data=self.cursor.fetchone()  #取出来一条查询记录
                if name==data[0]:     #如果遍历到控制台输入的姓名  就打印出他的工资
                    calc=CalcSalary(data[0],data[1])
                    calc.Calc(month)
                    calc.writetofile()
                else:    #如果没有控制台输入  则全部打印出来
                    calc = CalcSalary(data[0], data[1])
                    calc.Calc(month)
                    calc.writetofile()







class CalcSalary:
    def __init__(self,name,salary):

        #初始化属性 姓名  工资  需要写入文件的字符串属性
        self.name=name
        self.salary=salary
        self.str=''


    def Calc(self,month):
        self.str=self.name+'的工资为：'+str(self.salary*month)  #将字符串赋值给str
    def writetofile(self):

        file=open('test.txt','a+')  #以追加的形式打开一个文件test.txt
        print self.str      #打印出来这个字符串
        file.write(self.str)  #将这个字符串写入到文件
        file.close()  #关闭文件






test=DbTest()  #创建对象
# name=raw_input('请输入姓名')
# month=int(raw_input('请输入月份'))
test.Select()   #调用查询方法
