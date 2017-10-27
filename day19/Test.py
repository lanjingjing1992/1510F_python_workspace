#coding=utf-8
# import time
# import random
# r=random.randint(1,100)
# t=time.strftime('%Y%m%d',time.localtime())
# print '测试报告%s%s'%(t,r)
class Menu:
    def __init__(self):
        self.map={1:['鱼香肉丝',15],2:['狮子头',20],3:['宫保鸡丁',12],4:['土豆丝',15],5:['麻婆豆腐',15]}

def login():

        #管理员
        name=raw_input('请输入管理员姓名')
        if name=='admin':
            passwd=raw_input('请输入密码')
            if passwd=='123':
                print 'welcome'
            else:
                print '密码输入错误'
                login()
        else:
            print '名字输入错误'
            login()


class Person:
    def __init__(self):
        self.m=Menu()
        self.sum=0
        self.str='您的点餐信息如下：\n' \
                      '--------------------------------\n' \
                      '编号          菜品名称       价格      小计\n'
    def order(self):

            print '菜品展示\n' \
                  '------------------------\n' \
                  '编号         菜品名称        价格：'
            # print m.map[1][0]
            # print m.map[1][1]
            for i in range(1,len(self.m.map)+1,1):
                print '%s         %s         %s'%(i,self.m.map[i][0],self.m.map[i][1])
            id=int(raw_input('请根据菜单输入您所需菜品的编号'))
            num=int(raw_input('请输入菜品数量'))
            count=self.m.map[id][1]*num
            self.sum+=count
            self.str+='%s       %s      %s      %s\n'%(id,self.m.map[id][0],self.m.map[id][1],count)
            y_n=raw_input('是否继续点餐，输入n则结束，输入其他继续')
            if y_n=='n':
                self.str+='-----------------------------\n' \
                          '总计：%s\n' \
                          '********************************'%self.sum
                print self.str
            else:
                self.order()




number = raw_input('请输入1为管理员，输入其他则为顾客')
if number == '1':

    login()
else:
    p=Person()
    p.order()