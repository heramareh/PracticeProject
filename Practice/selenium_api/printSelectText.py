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
        
    def test_printSelectText(self):
        url = "http://127.0.0.1/test_select.html"
        # �����Զ����html��ҳ
        self.driver.get(url)
        # ʹ��name�����ҵ�ҳ����name����Ϊ��fruit���������б�Ԫ��
        select = self.driver.find_element_by_name("fruit")
        all_options = select.find_elements_by_tag_name("option")
        for option in all_options:
            print u"ѡ����ʾ���ı���", option.text
            print u"ѡ��ֵΪ��", option.get_attribute("value")
            option.click()
            time.sleep(1)

       



    def tearDown(self):
        # �˳�IE�����
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()