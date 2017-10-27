#coding=utf-8
import unittest
from selenium import webdriver
from HTMLTestRunner import HTMLTestRunner

class Baidu(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Chrome()
        self.url='http://www.baidu.com'

    def testLogin(self):
        d=self.driver
        d.get(self.url)

    def tearDown(self):
        self.driver.quit()#退出浏览器


if __name__ == '__main__':
    suite=unittest.TestSuite()
    suite.addTest(Baidu('testLogin'))
    runner=HTMLTestRunner.HTMLTestRunner(stream=open('r.html','w+'),title='result',description='this is lanjingjing result')
    runner.run(suite)