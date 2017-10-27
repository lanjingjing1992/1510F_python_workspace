#coding=utf-8
# list=[1,2,3,'abc']
# if 'bc' in list:
#     print 'hello'
# else:
#     print 'world'
#
#
# a=1
# b=2
# print a is b#==用来比较内容是否相同
#is 用来比较对象引用是否为同一个

# score=int(raw_input('请输入成绩'))
# if score>98:
#     print 'mp4'
# else:
#     print '罚写代码'
# age=int(raw_input('请输入年龄'))
# sex=raw_input('请输入性别')
# if age>=7 or (age>=5 and sex=='男'):
#     print '搬桌子'
# else:
#     print '搬不动'
# number=int(raw_input('请输入一个整数'))
# if number%3==0 or number%5==0:
#     print '是倍数'
# else:
#     print '不是倍数'
# money=int(raw_input('请输入压岁钱的数目'))
# if money>1000:
#     print '捐助'
# elif money>500:
#     print '航模'
# else:
#     print '百科全书'
list = [1, 2, 3, 4, 100]
# print max(list)
# print min(list)
# print sum(list)
# list.append('abc')
# print list.remove('abc')
# print list
list2 = [100, 200, 300, 400]
list.extend(list2)
print list