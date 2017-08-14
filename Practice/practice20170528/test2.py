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
def browser(brower_name):
    global driver
    if brower_name.lower()=="ie":
        driver = webdriver.Ie(executable_path = "d:\\IEDriverServer")
    elif brower_name.lower()=="chrome":
        driver = webdriver.Chrome(executable_path = "d:\\chromedriver")
    else:
        driver = webdriver.Firefox(executable_path = "d:\\geckodriver")
def visit(url):
    global driver
    driver.maximize_window()
    driver.get(url)

def input(xpath,word):
    global driver
    driver.find_element_by_xpath(xpath).send_keys(word)

def click(xpath):
    global driver
    driver.find_element_by_xpath(xpath).click()

def sleep(seconds):
    time.sleep(float(seconds))

def assert_word(word):
    global driver
    assert True==(word in driver.page_source)

def close():
    global driver
    driver.quit()


if __name__=="__main__":
    with open("e:\\data\\testdata.txt") as fp:
        for each_line in fp:
            step = each_line.strip().split('||')
            if len(step) == 1:
                step = step[0] + "()"
            elif len(step) == 2:
                step = step[0] + '(\"' + step[1] + '\")'
            else:
                step = step[0] + '(\"' + '\", \"'.join(step[1:]) + '\")'
            print step
            exec(step)
