#coding=utf-8
from selenium import webdriver
from time import sleep
# from selenium.webdriver.support.wait import WebDriverWait
# driver.get('https://qzone.qq.com/')
# time.sleep(1)#强制休眠
# kw=driver.find_element_by_id('kw')#搜索框
# time.sleep(1)
# kw.send_keys(u'八维')
# su=driver.find_element_by_id('su')
# su.click()
# driver.switch_to_frame('login_frame')
# driver.find_element_by_id('switcher_plogin').click()
# driver.find_element_by_id('u').send_keys('2364365304')
# driver.find_element_by_id('p').send_keys('1234466776')
# driver.find_element_by_id('login_button').click()
# driver.get('http://www.baidu.com')
# sleep(3)#强制等待3秒
# driver.implicitly_wait(3)#隐形等待3秒
#
# # driver.find_element_by_name('wd').send_keys(u'八维')
# # driver.find_element_by_xpath('//*[@id="kw"]').send_keys('hello')
# # print driver.title
# # print driver.find_element_by_id('cp').text
# driver.set_window_size(480,800)
# sleep(3)
# driver.maximize_window()#最大化
# driver.get('http://news.baidu.com/')
# sleep(2)
# driver.back()
# kw=driver.find_element_by_id('kw')
# kw.send_keys(u'八维')
# sleep(2)
# kw.clear()
# kw.send_keys(u'贴吧')
# from selenium import webdriver
#
# d=webdriver.Chrome()
#
# d.get('http://www.baidu.com')
# d.find_element_by_xpath('//*[@id="u1"]/a[7]').click()#登陆
# #
# d.switch_to_alert()
#
# d.implicitly_wait(30)#隐式等待
# d.find_element_by_xpath('//*[@id="pass_phoenix_btn"]/ul/li[1]/a').click()
#
# #找不到元素的原因：  进入到iframe层   跳转窗口   页面未完全加载成功，需设置等待
# current=d.current_window_handle#驱动停留在的页面
# all_windows=d.window_handles#驱动中存储的所有的窗口页面
# for i in all_windows:
#     if i!=current:
#         d.switch_to_window(i)
# d.switch_to_frame('ptlogin_iframe')
#
# d.find_element_by_id('img_out_2364365304').click()

