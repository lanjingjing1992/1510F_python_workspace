#coding=utf-8
# file=open('test1.txt','a')#可写入可读取
# file.write('world')#写入字符串
# file.seek(0,0)#光标定位
# file=open('test1.txt','r')
# data=file.read()#不写参数的话是全部读取
# print file.name
import os

# file.write('helloworld')
# file.seek(0,0)
# print file.tell()#光标的位置
# print file.read(2)
# os.rename('test1.txt','1510F.txt')
# os.remove('1510F.txt')
os.chdir('/Users/lanjingjing/Desktop/1510F/')#切换路径
file=open('test1.txt','w+')
os.mkdir('文件夹')#新建文件夹
os.chdir('d:/')
file.close()
