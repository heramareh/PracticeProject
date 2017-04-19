#encoding=utf-8
import unittest
import time
import chardet
from selenium import webdriver
 
class VisitSogouByIE(unittest.TestCase):

    def setUp(self):
        #����IE�����
        self.driver = webdriver.Firefox(executable_path = "e:\\geckodriver")
        #self.driver = webdriver.Ie(executable_path = "e:\\IEDriverServer")
        
    def test_doubleClick(self):
        url = "http://127.0.0.1/test_doubleclick.html"
        # �����Զ����html��ҳ
        self.driver.get(url)
        # ��ȡҳ������Ԫ��
        inputBox = self.driver.find_element_by_id("inputBox")
        # ����֧��˫��������ģ��
        from selenium.webdriver import ActionChains
        # ��ʼģ�����˫������
        action_chains = ActionChains(self.driver)
        action_chains.double_click(inputBox).perform()

        time.sleep(3)

       



    def tearDown(self):
        # �˳�IE�����
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()