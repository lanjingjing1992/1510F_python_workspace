#coding=utf-8
print 'MyShopping结算管理系统 >  结算\n' \
      '\n' \
      '********************************\n' \
      '            1 客户信息管理           \n' \
      '            2 购物结算              \n' \
      '            3 真情回馈                \n' \
      '            4 注销                    \n' \
      '***********************************'
#       '请选择购买的商品编号：\n' \
#       '1 体恤     2 网球鞋    3 网球拍\n' \
#       '********************************'
#
# map={1:['体恤',570],2:['网球鞋',245],3:['网球拍',300]}
# count=0
# def f():
#     id=int(raw_input('请输入商品编号：'))
#     num=int(raw_input('请输入数量'))
#
#     if id in map.keys():
#         print map[id][0]+'        ¥'+str(map[id][1])+'    '+str(num)
#         y_n=raw_input('是否继续输入,是的话输入y否则的话输入其他')
#         sum=num*map[id][1]
#         global count
#         count+=sum
#         if y_n=='y':
#             f()
#
#         else:
#             print '结束,总价为%s'%count
#             return
#     else:
#         print '编号输入错误'
#         f()
#
#
# f()
#
# def f():
#     num=int(raw_input('请选择输入数字：'))
#     map={1:'客户信息管理',2:'购物结算',3:'真情回馈',4:'注销'}
#     if num in map.keys():
#         print map[num]
#
#     else:
#         print '输入有错误'
#
#     f()
#
#
# f()
# 一：定义一个学生类。有下面的类属性：
# 1 姓名
# 2 年龄
# 3 成绩（语文，数学，英语)[每课成绩的类型为整数]
# 类方法：
# 1 获取学生的姓名：get_name() 返回类型:str
# 2 获取学生的年龄：get_age() 返回类型:int
# 3 返回3门科目中最高的分数。get_course() 返回类型:int
# 写好类以后，可以定义2个同学测试下:
# zm = Student('zhangming',20,[69,88,100])
# 返回结果：
# zhangming
# 20
# 100
class Student:
    def __init__(self,name,age,course):#构造方法
        #属性
        self.name=name
        self.age=age
        self.course=course

    def get_name(self):#self指代的是对象的引用  不可以给self赋值
        return self.name

    def get_age(self):
        return self.age
    def get_course(self):
        return self.course


zm=Student('zhangming',20,[69,88,100]) #定义对象
print zm.get_name()
print zm.get_age()
print zm.get_course()[2]





