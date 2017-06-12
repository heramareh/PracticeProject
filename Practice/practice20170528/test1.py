#encoding=utf-8
from selenium import webdriver
import time
import logging, traceback
from selenium.common.exceptions import NoSuchElementException

# 初始化日志对象
logging.basicConfig(
    # 日志级别
    level = logging.INFO,
    # 日志格式
    # 时间、代码所在文件名、代码行号、日志级别名字、日志信息
    format = '%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
    # 打印日志的时间
    datefmt = '%a, %Y-%m-%d %H:%M:%S',
    # 日志文件存放的目录（目录必须存在）及日志文件名
    filename = 'e:/dataDriveRreport.log',
    # 打开日志文件的方式
    filemode = 'w'
)

driver=""
def ie():
    global driver
    driver = webdriver.Ie(executable_path = "d:\\IEDriverServer")

def visit(url):
    global driver
    driver.get(url)

def input(word):
    global driver
    driver.find_element_by_id("kw").send_keys(u"光荣之路自动化测试")

def click():
    global driver
    driver.find_element_by_id("su").click()

def sleep(seconds):
    time.sleep(seconds)

def assert_word(word):
    global driver
    assert True==(word in driver.page_source)

def close():
    global driver
    driver.quit()


if __name__=="__main__":
    ie()
    visit("http://www.baidu.com")
    input("gloryroad test")
    click()
    sleep(3)
    assert_word("gloryroad")
    close()