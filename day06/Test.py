#coding=utf-8
import pymysql


class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    def count(self,month):
        count=int(self.salary)*month
        return self.name+'  %s个月工资为：'%month+str(count)


class CalcSalary:
        def __init__(self):
            self.db=pymysql.connect('localhost','root')
            self.cursor=self.db.cursor()
            self.cursor.execute('use lanjingjing')
            self.cursor.execute('show tables')
            self.cursor.execute('select name from test1')
            print self.cursor.fetchall()

        def countSalary(self,month,name):
            self.cursor.execute('select NAME,salary from test1')

            for i in range(3):
                data=self.cursor.fetchone()
                if name == data[0]:
                    emlpoyee=Employee(data[0],data[1])
                    return emlpoyee.count(month)

            return '数据库中没有此人名'

calc=CalcSalary()
month=int(raw_input('请输入月数'))
name=raw_input('请输入名字')
result=calc.countSalary(month,name)
calc.db.close()
file=open('lanjingjing.txt','w+')
file.write(result)
file.seek(0)
print file.read()
file.close()




