#encoding=utf-8

from selenium import webdriver
from selenium.webdriver import ActionChains
import time

driver = webdriver.Chrome(executable_path='d:\\chromedriver')
driver.maximize_window()
driver.get("http://clive.cuctv.com/zywh")
time.sleep(2)
bar = driver.find_element_by_id('box')
time.sleep(1)
location =  bar.location
size = bar.size
action = ActionChains(driver)
action.move_by_offset(location['x']+size['width']/2, location['y']+size['height']/2)
time.sleep(1)
action.click_and_hold()
time.sleep(1)
action.move_by_offset(location['x']+size['width']/2, location['y']+size['height'])
time.sleep(2)
action.move_by_offset(location['x']+size['width']/2, location['y']+size['height']*2)
time.sleep(2)
action.release()
time.sleep(2)