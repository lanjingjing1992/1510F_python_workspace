#coding=utf-8
import unittest
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from HTMLTestRunner import HTMLTestRunner
class Baidu(unittest.TestCase):
    def setUp(self):

        self.driver=webdriver.Chrome()
        self.url='http://www.baidu.com'
    def testLogin(self):
        d=self.driver
        d.get(self.url)
        d.implicitly_wait(30)
        d.find_element_by_link_text(u'登录').click()
        d.switch_to_alert()
        d.find_element_by_xpath('//*[@id="pass_phoenix_btn"]/ul/li[1]/a').click()#qq登陆
        #新的窗口
        all_windows=d.window_handles
        current_window=d.current_window_handle
        for window in all_windows:
            if window!=current_window:
                d.switch_to_window(window)
        d.switch_to_frame('ptlogin_iframe')
        d.find_element_by_id('img_out_2364365304').click()
        d.close()
    def testSetting(self):
        d = self.driver
        d.get(self.url)
        d.implicitly_wait(30)
        set=d.find_element_by_link_text(u'设置')

        ActionChains(d).click_and_hold(set).perform()
        d.find_element_by_xpath('//*[@id="wrapper"]/div[6]/a[1]').click()
        sleep(2)
        d.find_element_by_xpath('//*[@id="gxszButton"]/a[2]').click()
        d.switch_to_alert().accept()
        d.close()
    def testSearch(self):
        d = self.driver
        d.get(self.url)
        d.implicitly_wait(30)
        d.find_element_by_id('kw').send_keys('selenium')
        d.find_element_by_id('su').click()
        d.close()
    def tearDown(self):
        self.driver.quit()




# if __name__ == '__main__':
#     suite=unittest.TestSuite()
#     suite.addTest(Baidu('testSearch'))
#     suite.addTest(Baidu('testSetting'))
#     suite.addTest(Baidu('testLogin'))
#     runner=HTMLTestRunner.HTMLTestRunner(stream=open('result.html','w+'),title='lanjignjing',description='this is mahuazhan result')
#     runner.run(suite)


