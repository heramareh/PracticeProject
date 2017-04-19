#encoding=utf-8
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import ConfigParser
import os,time

class ObjectMap(object):
    def __init__(self):
        # 获取存放页面元素定位表达方式及定位表达式的配置文件所在绝对路径
        # os.path.abspath(__file__)表示获取当前文件所在路径目录
        self.uiObjMapPath = os.path.dirname(os.path.abspath(__file__))\
                            + "\\UiObjectMap.ini"
        print self.uiObjMapPath

    def getElementObject(self, driver, webSiteName, elementName):
        try:
            # 创建一个读取配置文件的实例
            cf = ConfigParser.ConfigParser()
            # 将配置文件内容加载到内存
            cf.read(self.uiObjMapPath)
            # 根据section和option获取配置文件中页面元素的定位方式及
            # 定位表达式组成的字符串，并使用“>”分割
            locators = cf.get(webSiteName, elementName).split(">")
            # 得到定位方式
            locatorMethod = locators[0]
            # 得到定位表达式
            locatorExpression = locators[1]
            print locatorMethod, locatorExpression
            # 通过显示等待方式获取页面元素
            element = WebDriverWait(driver, 10).until(lambda x: \
                    x.find_element(locatorMethod, locatorExpression))
        except Exception, e:
            raise e
        else:
            # 当页面元素被找到后，将该页面元素对象返回给调用者
            return element

if __name__ == '__main__':
    driver = webdriver.Ie(executable_path = "d:\\IEDriverServer")
    driver.get("https://www.baidu.com")
    obj=ObjectMap()
    search_input_text = obj.getElementObject(driver, "baidu", "search_input_text")
    search_input_text.send_keys("hahaha")
    search_btn = obj.getElementObject(driver, "baidu", "search_btn")
    search_btn.click()
    time.sleep(3)
    driver.quit()
