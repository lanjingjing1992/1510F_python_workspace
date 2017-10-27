#coding=utf-8      #防止中文乱码
from selenium import webdriver
from selenium.webdriver.common.by import By
#加载键盘使用的模块
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException

#加载unittest模块
import unittest
import time
import os
from autoTest.sendEmail import Sendmail
#加载HTMLTestRunner，用于生成HTMLreuslt
from HTMLTestRunner import HTMLTestRunner

class BaiduYun(unittest.TestCase):
    def setUp(self):
        self.browser=webdriver.Chrome()
        self.browser.implicitly_wait(30)
        self.base_url="http://yun.baidu.com"
    def testLogin(self):
        browser=self.browser
        browser.get(self.base_url+'/')
        u"""百度云登录"""
        browser.find_element_by_name("userName").clear()
        username=browser.find_element_by_name("userName")
        username.send_keys("15901337131")
        username.send_keys(Keys.TAB)
        time.sleep(2)
        password=browser.find_element_by_name("password")
        password.send_keys("442131zkk")
        password.send_keys(Keys.ENTER)
        time.sleep(3)
        browser.close()

    def tearDown(self):
        self.browser.quit()
if __name__=="__main__":

    testunit=unittest.TestSuite()
    #将测试用例加入到测试容器中
    testunit.addTest(BaiduYun("testLogin"))
    # #获取当前时间，这样便于下面的使用。
    # now = time.strftime("%Y-%m-%d-%H_%M_%S",time.localtime(time.time()))
    # #打开一个文件，将result写入此file中
    # path='/Users/lanjingjing/Desktop/1510F_python_workspace/autoTest/result/'
    # os.chdir(path)
    # fp=open(now+".html",'wb')
    # runner=HTMLTestRunner.HTMLTestRunner(stream=fp,title='test result',description=u'result:')
    # runner.run(testunit)
    # fp.close()
    # send=Sendmail()
    # print fp
    # print path
    # send.sendmail(path,fp.name)
