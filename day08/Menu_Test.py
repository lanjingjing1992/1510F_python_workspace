#coding=utf-8
from day08.Menu import *
import json

class Menu_Test:
    def __init__(self):
        #初始化菜单
        self.menu=Menu()
        self.str=''
        self.count=0
    def login(self):
        str=raw_input('如果是管理员的话请输入1，顾客的话输入其他')
        if str=='1':
            name=raw_input('请输入姓名')
            passwd=raw_input('请输入密码')
            if name=='admin'  and passwd=='123':#验证是否是管理员权限
                new_name=raw_input('请输入新的菜品的名称')
                new_price=raw_input('请输入新的菜品单价')
                count_menu=len(self.menu.map)
                print '当前的菜品数量为%s'%count_menu
                self.menu.map.update({count_menu+1:[new_name,int(new_price)]})
                print json.dumps(self.menu.map, ensure_ascii=False, encoding='UTF-8')
                print '更新成功'
        self.order()#点餐
    def order(self):
        print '菜品展示\n' \
              '------------------------\n' \
              '编号      菜品名称      价格'
        # print '1     '+self.menu.map[1][0]+'      %s'%(self.menu.map[1][1])
        # print '2     '+self.menu.map[2][0]+'      %s'%(self.menu.map[2][1])
        # print '3     '+self.menu.map[3][0]+'      %s'%(self.menu.map[3][1])
        data = len(self.menu.map)
        for i in range(data):
            print '%s     ' % (i + 1) + \
                  self.menu.map[i + 1][0] + '      %s' % (self.menu.map[i + 1][1])
        print '---------------------------\n'
        id = raw_input('请根据菜单输入您所需菜品的编号')
        num = raw_input('请输入数量')
        sum=self.menu.map[int(id)][1]*int(num)#每一条点菜的小计
        self.count+=sum
        #拼接每一条点菜的信息
        self.str+=id+'   '+self.menu.map[int(id)][0]+'   '+\
                  '%s'%self.menu.map[int(id)][1]+'     '+num+'    %s'%sum

        self.str+='\n'#每拼接完一条换行
        print self.str
        y_n = raw_input('是否继续点餐，继续的话输入y，输入其他结束')
        if y_n == 'y':
            self.order()
        else:
            #结账
            print '您的结账信息如下\n' \
                  '*************************\n' \
                  '编号   菜品名称   价钱   数量  小计'
            print self.str
            print '-----------------------------\n' \
                  '合计                   %s元\n' \
                  '******************************'%self.count





test=Menu_Test()
test.login()






