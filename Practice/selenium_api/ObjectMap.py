#encoding=utf-8
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import ConfigParser
import os,time

class ObjectMap(object):
    def __init__(self):
        # ��ȡ���ҳ��Ԫ�ض�λ��﷽ʽ����λ���ʽ�������ļ����ھ���·��
        # os.path.abspath(__file__)��ʾ��ȡ��ǰ�ļ�����·��Ŀ¼
        self.uiObjMapPath = os.path.dirname(os.path.abspath(__file__))\
                            + "\\UiObjectMap.ini"
        print self.uiObjMapPath

    def getElementObject(self, driver, webSiteName, elementName):
        try:
            # ����һ����ȡ�����ļ���ʵ��
            cf = ConfigParser.ConfigParser()
            # �������ļ����ݼ��ص��ڴ�
            cf.read(self.uiObjMapPath)
            # ����section��option��ȡ�����ļ���ҳ��Ԫ�صĶ�λ��ʽ��
            # ��λ���ʽ��ɵ��ַ�������ʹ�á�>���ָ�
            locators = cf.get(webSiteName, elementName).split(">")
            # �õ���λ��ʽ
            locatorMethod = locators[0]
            # �õ���λ���ʽ
            locatorExpression = locators[1]
            print locatorMethod, locatorExpression
            # ͨ����ʾ�ȴ���ʽ��ȡҳ��Ԫ��
            element = WebDriverWait(driver, 10).until(lambda x: \
                    x.find_element(locatorMethod, locatorExpression))
        except Exception, e:
            raise e
        else:
            # ��ҳ��Ԫ�ر��ҵ��󣬽���ҳ��Ԫ�ض��󷵻ظ�������
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
