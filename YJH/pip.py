from selenium import webdriver

from selenium.webdriver.common.keys import Keys

 

driver = webdriver.Chrome('C:/Users/W20143/Desktop/pyton/chromedriver.exe')

url='https://google.com'

driver.get(url)

 

driver.find_element_by_css_selector('.gLFyf.gsfi').send_keys('파이썬')

driver.find_element_by_css_selector('. gLFyf.gsfi').send_keys(Keys.ENTER)

driver.find_elements_by_css_selector('.LC20lb')[3].click()