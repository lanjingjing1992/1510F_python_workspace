#coding=utf-8
import pymysql

class AnimalSell:
    def __init__(self):
         self.db = pymysql.connect(host='60.205.189.12',
                                   user='visitor', port=3306,
                                   passwd='123456',database='1510f',charset='utf8')
         self.cursor = self.db.cursor()
         self.str='种类    单价    数量    小计  '
         self.all=0
    def getKind(self,kind):

        self.cursor.execute('select kind from animal_sell')
        data = self.cursor.fetchall()
        for i in range(len(data)):
            if data[i][0]==kind:
                return 'success'
        return 'not find error'
    def getPrice(self,kind):
        self.cursor.execute('select price from animal_sell  where kind=\'%s\''%kind)
        price= self.cursor.fetchall()[0][0]
        return price
    def showAll(self):
        self.cursor.execute('select kind from animal_sell')
        data = self.cursor.fetchall()
        print '宠物列表如下\n' \
              '*********************************'
        for i in range(len(data)):

            print data[i][0],

    def calc(self):
        k = raw_input('\n请输入宠物种类')
        result = self.getKind(k)
        if result == 'success':
            n = int(raw_input('请输入数量'))
            price = self.getPrice(k)
            sum = price * n
            self.str+= '\n%s    %s    %s    %s' % (k,price,n,sum)
            self.all+=sum
            y_n=raw_input('是否继续购买可爱的小宠物啊,输入n结束，输入其他继续')
            if y_n=='n':
                print self.str
                print '\n总计:   %s'%self.all
            else:
                self.calc()
        else:
            print '没有这个种类，请重新输入'
            self.calc()



a=AnimalSell()
a.showAll()
a.calc()