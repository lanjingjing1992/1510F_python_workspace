#coding=utf-8
class Dog:
    def __init__(self,*args):#默认参数
        # self.color=color
        # self.name = name
        print args
    # def sleeping(self):
    #     print self.name+'在睡觉'
    #     print self.name+'的颜色：'+self.color




# d=Dog(name='大黑',color='白色',)
d=Dog('hello','world','python')

# d.sleeping()