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
        url = "http://127.0.0.1/test_multiple_select.html"
        # �����Զ����html��ҳ
        self.driver.get(url)
        # ����Selectģ��
        from selenium.webdriver.support.ui import Select
        # ʹ��xpath��λ��ʽ��ȡselectҳ��Ԫ�ض���
        select_element = Select(self.driver.find_element_by_xpath("//select"))
        # ͨ�����ѡ���һ��Ԫ��
        select_element.select_by_index(0)
        # ͨ��ѡ����ı�ѡ��ɽ髡�ѡ��
        select_element.select_by_visible_text("ɽ�")
        # ͨ��ѡ���value����ֵѡ��value=��mihoutao����ѡ��
        select_element.select_by_value("mihoutao")
        # ��ӡ���е�ѡ�����ı�
        for option in select_element.all_selected_options:
            print option.text
        # ȡ��������ѡ����
        select_element.deselect_all()
        time.sleep(2)
        print u"-----------�ٴ�ѡ��3��ѡ��--------------"
        select_element.select_by_index(1)
        select_element.select_by_visible_text("��֦")
        select_element.select_by_value("juzi")
        # ͨ��ѡ���ı�ȡ����ѡ�е��ı�Ϊ����֦��ѡ��
        select_element.deselect_by_visible_text("��֦")
        # ͨ�����ȡ����ѡ�е����Ϊ1��ѡ��
        select_element.deselect_by_index(1)
        # ͨ��ѡ���value����ֵȡ����ѡ�е�value=��juzi����ѡ��
        select_element.deselect_by_value("juzi")

    def tearDown(self):
        # �˳�IE�����
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()