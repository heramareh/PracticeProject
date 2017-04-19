#encoding=utf-8
import unittest
import time
import chardet
from selenium import webdriver
 
class VisitSogouByIE(unittest.TestCase):

    def setUp(self):
        #����IE�����
        #self.driver = webdriver.Firefox(executable_path = "e:\\geckodriver")
        self.driver = webdriver.Ie(executable_path = "e:\\IEDriverServer")
        
    def test_operateMultipleOptionDropList(self):
        url = "http://127.0.0.1/test_input_select.html"
        # �����Զ����html��ҳ
        self.driver.get(url)
        from selenium.webdriver.common.keys import Keys
        # element.send_keys("some text")
        self.driver.find_element_by_id("select").clear()

        # �����ͬʱ���¼�ͷ��
        self.driver.find_element_by_id("select").send_keys("c", Keys.ARROW_DOWN)
        self.driver.find_element_by_id("select").send_keys( Keys.ARROW_DOWN)
        self.driver.find_element_by_id("select").send_keys( Keys.ENTER)
        time.sleep(3)

    def tearDown(self):
        # �˳�IE�����
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()