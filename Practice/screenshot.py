#encoding=utf-8

from selenium import webdriver
from selenium.common.exceptions import TimeoutException
import time,os,re

'''1 ie chrome firefox 三种浏览器下
2 分别截图 baidu sogou youdao 
3 保存在当前日期的目录下
4 网址要保存在某个数据文件中'''
class Screenshot(object):
    def __init__(self,urlfile,exportdir):
        self.urlfile = urlfile
        self.exportdir = exportdir
    
    def screen_shot(self,browser):
        self.browser = browser
        #判断要使用的浏览器驱动
        if self.browser == "chrome":
            self.driver = webdriver.Chrome(executable_path = "d:\\chromedriver")
        if self.browser == "firefox":
            self.driver = webdriver.Firefox(executable_path = "d:\\geckodriver")
        if self.browser == "ie":
            self.driver = webdriver.Ie(executable_path = "d:\\IEDriverServer")
        #读取url文件，获取所有url
        with open(self.urlfile) as fp:
            content = fp.readlines()
        #设置浏览器加载最长等待时长
        self.driver.set_page_load_timeout(10)
        #循环访问url，截屏
        for url in content:
            try:
                #访问url
                self.driver.get(url.strip())
                #最大化浏览器窗口
                self.driver.maximize_window()
            except TimeoutException, e:
                print u"页面没有完全加载完"
            time.sleep(2)
            #获取当前年月日，格式：YYYY-mm-dd
            date = time.strftime("%Y-%m-%d")
            #设置保存文件名
            filename = self.browser+'_'+ re.search(r'www\.(.+)\.com',self.driver.current_url).group(1)+'_'+date+'.png'
            #设置路径名
            dirname = os.path.join(self.exportdir,date)
            #判断路径是否存在，若不存在则新建
            if not os.path.exists(dirname):
                os.mkdir(dirname)
            #执行截屏
            self.driver.get_screenshot_as_file(os.path.join(dirname,filename))
        #退出浏览器
        self.driver.quit()

if __name__ == '__main__':
    screenshot=Screenshot("d:\\test\\config.txt","d:\\test\\exportfile")
    for i in ["ie","firefox","chrome"]:
        screenshot.screen_shot(i)
    print "done!"
