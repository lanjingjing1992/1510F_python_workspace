#coding=utf-8
from day05.Person import *


class Calc:
    def __init__(self):
        self.i=3
        self.p=Person()

    def f(self):
        name=raw_input('请输入姓名：')#控制台输入一行
        id=raw_input('请输入密码')#密码
        if name in self.p.map.keys():#字典中键的集合
            if self.p.map[name]==id:
                print '登陆成功'
                return
            else:
                print '密码错误'

        else:
            print '用户名错误'
        self.i-=1
        if self.i==0:
            print '锁定'
        else:
            print '你还有%s次机会'%self.i
            self.f()

calc=Calc()#创建对象自动调用构造方法
calc.f()#使用对象调用普通方法