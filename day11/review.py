#coding=utf-8
import os
def replace():

    lines = open('test.txt').readlines()  # 打开文件，读入每一行
    fp = open('test_new.txt','w')  #打开你要写得文件test2.txt
    for s in lines:
    # replace是替换，write是写入
        fp.write(s.replace('2012','2013'))
    fp.close()  # 关闭文件

def stripFile(oldFName,newFName):
  '''''remove the space or Tab or enter in a file,and output to a new file in the same folder'''
  fp = open(oldFName,"r+")
  newFp = open(newFName,"w")
  for eachline in fp.readlines():
    newStr = eachline.replace(" ","").replace("\t","").strip()
    #print "Write:",newStr
    newFp.write(newStr)
  fp.close()
  newFp.close()

import os
# file=open('test.txt','rw')
# file.seek(0)
#请输出其内容。
# s= file.read()
# print s
# #请计算该文本的原始长度。
# print os.path.getsize('test.txt')  #12  14*3=42 换行占一个字符
# #请去除该文本的换行
# oldName = 'test.txt'
# nameList = oldName.split(".")
# newName = "%s%s%s" % (nameList[0], "_new.", nameList[1])
# stripFile(oldName, newName)
# print "finish output to new file:", newName

#请替换其中的字符"2012"为"2013"。
# replace()


file=open('test_new.txt','r')
len=os.path.getsize('test_new.txt')
offset=len//2-2

file.seek(offset,0)
print file.read(5)






