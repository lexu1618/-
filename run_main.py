from selenium import webdriver
import time

base_url = 'https://www.baidu.com'

browser = webdriver.Chrome()
browser.get(base_url)

# 2.提交
search_text = browser.find_element_by_id('kw')
search_text.send_keys('selenium')
search_text.submit()
time.sleep(3)