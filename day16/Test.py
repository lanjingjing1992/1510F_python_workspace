#coding=utf-8
import unittest
from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains
from HTMLTestRunner import HTMLTestRunner
class Youdao(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Chrome()
        self.url='http://dict.youdao.com/'

    def testMore(self):
        d=self.driver
        d.get(self.url)#进入到有道首页
        #鼠标事件
        more=d.find_element_by_xpath('//*[@id="more"]/div[1]')
        ActionChains(d).click_and_hold(more).perform()
        #点击有道精品课
        d.find_element_by_class_name('icon_jingpink').click()
        d.close()
    def testcloud(self):
        d=self.driver
        d.get(self.url)
        d.implicitly_wait(30)
        d.find_element_by_link_text(u'云笔记').click()#点击云笔记
        d.find_element_by_xpath('//*[@id="dropdown-button"]').click()
        time.sleep(3)
        d.find_element_by_xpath('/html/body/div[2]/div[2]/div[2]/div[1]/div[1]/span').click()
        all_windows=d.window_handles#所有的windows
        current_window=d.current_window_handle#当前的window
        for window in all_windows:#遍历
            if window!=current_window:#找出新的window
                d.switch_to_window(window)


        time.sleep(5)
        d.switch_to_frame('ptlogin_iframe')
        d.find_element_by_id('img_out_2364365304').click()
        time.sleep(3)
        d.close()
    def tearDown(self):
        self.driver.quit()



if __name__ == '__main__':
    suite=unittest.TestSuite()
    suite.addTest(Youdao('testMore'))
    suite.addTest(Youdao('testcloud'))
    t=time.strftime('%Y_%m_%d',time.localtime())
    name='测试报告-%s-lanjingjing.html'%t
    runner=HTMLTestRunner.HTMLTestRunner(stream=open(name,'w+'),title='result',description='this is shuiashuai result')
    runner.run(suite)










