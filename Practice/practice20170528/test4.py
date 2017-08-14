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
            steps = each_line.strip().split('||')
            if len(steps) == 2:
                step = steps[1] + "()"
            elif len(steps) == 3:
                step = steps[1] + '(\"' + steps[2] + '\")'
            else:
                step = steps[1] + '(\"' + '\", \"'.join(steps[2:]) + '\")'
            print steps[0]
            print step
            try:
                exec(step)
            except NoSuchElementException, e:
                logging.error(u"查找的页面元素不存在，异常堆栈信息："\
                          + str(traceback.format_exc()))
            except AssertionError, e:
                logging.info(u"断言错误")
            except Exception, e:
                logging.error(u"未知错误，错误信息：" + str(traceback.format_exc()))
            else:
                logging.info(steps[0].decode() + u"：执行成功")
