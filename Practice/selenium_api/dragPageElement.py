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
        
    def test_dragPageElement(self):
        url = "http://jqueryui.com/resources/demos/draggable/scroll.html"
        # ���ʱ�������ҳ
        self.driver.get(url)
        # ��ȡҳ���ϵ�һ������ק��ҳ��Ԫ��
        initialPosition = self.driver.find_element_by_id("draggable")
        # ��ȡҳ���ϵڶ�������ק��ҳ��Ԫ��
        targetPosition = self.driver.find_element_by_id("draggable2")
        # ��ȡҳ���ϵ���������ק��ҳ��Ԫ��
        dragElement = self.driver.find_element_by_id("draggable3")
        # �����ṩ��קԪ�ط�����ģ��ActionChains
        from selenium.webdriver import ActionChains
        import time
        '''
        ����һ���µ�ActionChains����webdriverʵ������driver��Ϊ����ֵ����
        Ȼ��ͨ��WebDriverʵ��ִ���û�������
        '''
        action_chains = ActionChains(self.driver)
        # ��ҳ���ϵ�һ���ܱ���ק��Ԫ����ק���ڶ���Ԫ��λ��
        action_chains.drag_and_drop(initialPosition, targetPosition).perform()
        # ��ҳ���ϵ���������ק��Ԫ�أ��������϶�10�����أ����϶�5��
        for i in xrange(5):
            action_chains.drag_and_drop_by_offset(dragElement, 10, 10).perform()
            time.sleep(2)



    def tearDown(self):
        # �˳�IE�����
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()