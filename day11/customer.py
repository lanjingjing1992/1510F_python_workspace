#coding=utf-8
l=[]


def f():
    y_n = raw_input('是否继续输入 y/n')
    if y_n == 'n':
        for i in l:
            print i,
        return
    elif y_n == 'y':
        f1()
    else:
        print '输入字符有误'
        f()

def f1():
    name=raw_input('请输入姓名')
    l.append(name)
    f()


f1()



