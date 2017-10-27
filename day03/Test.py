#coding=utf-8
# for letter in 'Python':     # 第一个实例
#    if letter == 'h':
#       continue
#    print '当期字母 :', letter


# list=[1,2,3,4,5]

# for i in range(len(list)):
#     print list[i]


# for i in list:
#     print i

# var = 10                    # 第二个实例
# while var > 0:
#    print '当期变量值 :', var
#    var = var -1
#    if var == 5:   # 当变量 var 等于 5 时退出循环
#       break
# for letter in 'Python':     # 第一个实例
#    if letter == 'h':
#       continue
#    print '当前字母 :', letter
# for letter in 'Python':
#    if letter == 'h':
#       pass
#       print '这是 pass 块'
#    print '当前字母 :', letter
#
# print "Good bye!"
#!/usr/bin/python
# -*- coding: UTF-8 -*-

# var1 = 'Hello World!'
#
# print "更新字符串 :- ", var1[:6] + 'Runoob!'
# a = "Hello"
# b = "Python"
# print "a + b 输出结果：", a + b
# print "a * 2 输出结果：", a * 2
# print "a[1] 输出结果：", a[1]
# print "a[1:4] 输出结果：", a[1:4]
# a = "Hello"
# if( "M" not in a) :
#     print "M 不在变量 a 中"
# else :
#  print "M 在变量 a 中"
import random
import math
# print random.choice(range(10))+random.random()#随机数  整数
# print range(10)
# print random.random()#随机数 0到1之间
# print  math.sqrt(64)#开平方取正数
# print  math.floor(4.3)#向下取整
# print math.ceil(9.1)#向上取整
# #四舍五入  取绝对值
# print  math.fabs(-9)
# a=raw_input('请输入')
# print type(a)
# b=int(a)
# print type(b)
# import math
# a=2
# print type(a)
# b=float(a)
# print type(b)
# print math.pi
# l=[1,2,3]
# print l*2
# if 1 in l:
#     print 'hello'
# map={'a':1,'b':2}
# list1 = ['physics', 'chemistry', 1997, 2000];
# print list1;
# del list1[2];
# print "After deleting value at index 2 : "
# print list1;

#
# L = ['Google', 'Runoob', 'Taobao']#倒数的时候就是从-1开始 正着从0开始
# print L[2]
# print  L[-2]
# print L[1:]
# print len(L)
# L.reverse()
# print L


# tup3 = "a", "b", "c", "d"#在不加阔话的情况下 默认为元组
# print type(tup3)

# tup1 = (50,)
# print type(tup1)
# tup1 = (12, 34.56)
# tup2 = ('abc', 'xyz')
#
# tup3 = tup1 + tup2
# print tup3
# tup = ('physics', 'chemistry', 1997, 2000)
# print tup
# del tup
# print "After deleting tup : "
# print tup
# a=(4,5,1)
# b=(4,5,6)
# print cmp(a,b)
# dict2 = { 'abc': 123, 98.6: 37 }
# print type(dict2)

# print ['HI!']*4
#
# for x in [1, 2, 3]: print x结果为1，3
# dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
# dict['Age'] = 8 # update existing entry
# dict['School'] = "DPS School" # Add new entry
# print "dict['Age']: ", dict['Age']
# print "dict['School']: ", dict['School']
# dict = {'Name': 'Zara', 'Age': 7, 'Name': 'Manni'}#如果有重复的键 则后者覆盖前者
# print "dict['Name']: ", dict['Name']
import time
print time.strftime('%Y／ %m ／%d',time.localtime())#格式化当前时间  自己把时分秒加上