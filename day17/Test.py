#coding=utf-8
import unittest
from time import sleep
from selenium import webdriver
from HTMLTestRunner import HTMLTestRunner

class Baidu(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Chrome()
        self.url='http://www.baidu.com'
    def testLogin(self): # 登陆
        d=self.driver
        d.get(self.url)  # 打开网址
        d.implicitly_wait(30)
        d.find_element_by_xpath('//*[@id="u1"]/a[7]').click() #点击登陆
        sleep(3)
        d.switch_to_alert()
        d.find_element_by_xpath('//*[@id="pass_phoenix_btn"]/ul/li[1]/a').click() #点击第三方QQ登陆
        # 第三方框架
        current = d.current_window_handle
        all_window = d.window_handles
        for i in all_window:
            if i != current:
                d.switch_to_window(i)
        sleep(3)
        d.switch_to_frame('ptlogin_iframe')
        d.find_element_by_id('img_out_2364365304').click()
        sleep(5)
        d.close() #关闭该页面
        # sleep(3)

    def testSet(self):
        d=self.driver
        d.get(self.url)
        d.find_element_by_xpath('//*[@id="u1"]/a[8]').click()
        sleep(3)
        d.find_element_by_xpath('//*[@id="wrapper"]/div[6]/a[1]').click()
        sleep(3)
        d.find_element_by_xpath('//*[@id="gxszButton"]/a[2]').click() #点击恢复默认
        sleep(3)
        alter = d.switch_to_alter()  # 处理弹出框
        alter.accept()
        sleep(5)
        d.close()

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    suite=unittest.TestSuite()
    # suite.addTest(Baidu('testLogin'))
    suite.addTest(Baidu('testSet'))
    runner=HTMLTestRunner.HTMLTestRunner(stream=open('r.html','w+'),title='result',description='this is a result')
    runner.run(suite)