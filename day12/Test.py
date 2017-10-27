from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium import webdriver
d=webdriver.Chrome()
d.get('http://www.baidu.com')
d.find_element_by_id('kw').send_keys('selenium')
sleep(3)

d.find_element_by_id('kw').send_keys(Keys.CONTROL,'a')
sleep(2)
d.find_element_by_id('kw').send_keys(Keys.CONTROL,'c')
sleep(2)
d.find_element_by_id('kw').send_keys(Keys.BACK_SPACE)
sleep(3)
d.find_element_by_id('kw').send_keys(Keys.CONTROL,'v')
d.find_element_by_id('su').send_keys(Keys.ENTER)