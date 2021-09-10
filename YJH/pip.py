# -*- coding: utf-8 -*- 
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pyautogui as you
import re
from time import sleep
 
 
print("학교명을 입력하시오")
a=input()
driver = webdriver.Chrome('/Users/yujeonghyeop/Desktop/chromedriver')
url='http://apply.jinhakapply.com/SmartRatio'
driver.get(url)
typing = '//input[@id ="txtNowSearch"]'
click_1 = '//a [@class="btn_search"]'
view = '//a [@class="rate"]'
driver.find_element_by_xpath(typing).send_keys("{}".format(a))
driver.find_element_by_xpath(click_1).click()
driver.find_element_by_xpath(view).click()
p=re.compile("^기계공학")
print({0}.format(p))
# driver.find_element_by_css_selector('. gLFyf.gsfi').send_keys(Keys.ENTER)

# driver.find_elements_by_css_selector('.LC20lb')[3].click()http://addon.jinhakapply.com/RatioV1/RatioH/Ratio11400231.html
# http://addon.jinhakapply.com/RatioV1/RatioH/Ratio11040241.html