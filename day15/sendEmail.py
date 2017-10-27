#coding=utf-8
import os
'''发送带附件的邮件'''
import smtplib
from email.mime.text import  MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
def sendemail(path):
        msg=MIMEMultipart()
        msg['From'] = '15901337131@163.com'#发件人邮箱地址
        msg['To']=','.join(['2364365304@qq.com'])#收件人
        msg['Subject']='Report'#主题
        txt=MIMEText('作业敬请查看附件','plain','utf-8')#正文
        msg[ 'Accept - Language'] = 'zh - CN'
        msg[ 'Accept - Charset'] = 'ISO - 8859 - 1，utf - 8'
        msg.attach(txt)
        os.chdir(path)
        fileName='result.html'#附件

        att1 = MIMEImage((lambda f: (f.read(), f.close()))(open(fileName, 'rb'))[0], _subtype ='')
        att1.add_header('Content-Disposition', 'attachment', filename = fileName)
        msg.attach(att1)
        smtp = smtplib.SMTP()
        smtp.connect('smtp.163.com:25')#服务器地址
        smtp.login('15901337131@163.com', '442131zkk')#账号  授权码
        smtp.sendmail(msg['From'], msg['To'], msg.as_string())
        smtp.quit()
