#coding=utf-8
#python标识符的命名规则
#字母  数字 下划线组成 不能以数字开头  大小写敏感 长度无限制
# if True:
#    print '你好'
#
#
# for i in  range(3):
#     print i
#
#
# print 'hello'
# print 'world'

# a='hello'
# b=1000000000
# # # print type(a)
# print type(b)

# c=1+2j
# print type(c)
#python2.2

# a=[1,2,3,'hello']

# print a
# print type(a)
# a[0]=100
# print a
#
#
# b=(1,2,3,'hello')
# b[0]=100
# print b

#key-map
# c={'a':1,
#    'b':2,'v':3}
# print c['b']
# a='hello' \
#   'world'
# a='helloworld'  #包左不包右0
# print a[2:4]
# print a[3:5]
# print a.count('l')
# print  'hello ' \
#        'i ' \
#        'am here'#三引号的作用是 所见即所得
# a='helloworld'
# print a.capitalize()#首字母大写
# print a.upper()#所有的字母都大写
list=[1,2,3,4,100]
list2 = [100, 200, 300, 400]
list.extend(list2)
print list