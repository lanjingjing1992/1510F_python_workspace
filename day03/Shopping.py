#coding=utf-8
#普通顾客购物满100元打9折；会员购物打8折；会员购物满200元打7.5折
money=int(raw_input('请输入消费金额'))
if money<100:
    print '消费0-100之间无优惠,消费金额为%s'%money
else:
    vip = raw_input('是否为会员，如果是的话请输入y，否则的话输入其他')
    if vip=='y':
        if money>200:
            print '欢迎VIP，大于200的时候将打7.5折，消费金额为%s'%(money*0.75)
        else:
            print '欢迎vip，100-200之间将打8折，消费金额为%s'%(money*0.8)

    else:
        print '非会员消费大于100的时候将打9折，消费金额为%s'%(money*0.9)
