#coding=utf-8
# encoding=utf-8
from selenium import webdriver
import time
import datetime
import os
import re


def create_dir_by_date_time():
    today = datetime.date.today()
    print "today:",str(today)
    if not os.path.exists("e:\\"+str(today)):
        os.mkdir("e:\\"+str(today))
    return "e:\\"+str(today)


def create_url_list_file():
    with  open("e:\\urllist.txt","w") as f:
        f.write("http://www.sogou.com\n")
        f.write("http://www.baidu.com\n")
        f.write("http://www.youdao.com\n")

def capture_url_image_by_browser(browser_name,url):
    if browser_name=="ie":
        driver= webdriver.Ie(executable_path = "e:\\IEDriverServer")
    elif browser_name=="chrome":
        driver = webdriver.Chrome(executable_path = "e:\\chromedriver")
    else:
        driver =webdriver.Firefox(executable_path = "e:\\geckodriver")
    
    driver.get(url)
    picpath= create_dir_by_date_time()+"\\"+browser_name+"_"+\
             re.search(r"http://www\.(\w+)\..*",url).group(1)+".png"
    driver.get_screenshot_as_file(picpath)
        
    driver.quit()
   

if __name__=="__main__":
    create_dir_by_date_time()
    create_url_list_file()
    #capture_url_image_by_browser("ie","http://www.sogou.com")
    browser_list=["ie","chrome","firefox"]
    for browser_name in browser_list:
        with open("e:\\urllist.txt") as f:
            for line in f:
                url=line.strip()
                capture_url_image_by_browser(browser_name,url)