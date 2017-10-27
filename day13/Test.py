#coding=utf-8
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
d=webdriver.Chrome()
d.get('https://www.baidu.com/')#进入网址
d.implicitly_wait(30)
d.maximize_window()
setting=d.find_element_by_xpath('//*[@id="u1"]/a[8]')
ActionChains(d).click_and_hold(setting).perform()
d.find_element_by_xpath('//*[@id="wrapper"]/div[6]/a[1]').click()#搜索设置
sleep(3)
d.find_element_by_xpath('//*[@id="s1_1"]').click()#单选框
d.find_element_by_xpath('//*[@id="gxszButton"]/a[1]').click()
check=d.switch_to_alert()
check.accept()#点击确定
sleep(2)
d.quit()

