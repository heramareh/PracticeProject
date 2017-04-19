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
        
    def test_checkSelectText(self):
        url = "http://127.0.0.1/test_select.html"
        # �����Զ����html��ҳ
        self.driver.get(url)
        # ����Selectģ��
        from selenium.webdriver.support.ui import Select
        # ʹ��xpath��λ��ʽ��ȡselectҳ��Ԫ�ض���
        select_element = Select(self.driver.find_element_by_xpath("//select"))
        # ��ȡ����ѡ�����ҳ��Ԫ�ض���
        actual_options = select_element.options
        # ����һ��list���󣬴洢�����б������������ֵ���������
        expect_optionsList = [u"����",u"����",u"����",u"⨺���",u"ɽ�",u"��֦"]
        # ʹ��Python����map()������ȡҳ���������б�չʾ��ѡ��������ɵ��б����
        actual_optionsList = map(lambda option: option.text, actual_options)
        # ���������б�����ʵ���б�����Ƿ���ȫһ��
        self.assertListEqual(expect_optionsList, actual_optionsList)



    def tearDown(self):
        # �˳�IE�����
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()