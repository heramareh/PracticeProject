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
        
    def test_operateDropList(self):
        url = "http://127.0.0.1/test_select.html"
        # �����Զ����html��ҳ
        self.driver.get(url)
        # ����Selectģ��
        from selenium.webdriver.support.ui import Select
        # ʹ��xpath��λ��ʽ��ȡselectҳ��Ԫ�ض���
        select_element = Select(self.driver.find_element_by_xpath("//select"))
        # ��ӡĬ��ѡ������ı�
        print select_element.first_selected_option.text
        # ��ȡ����ѡ�����ҳ��Ԫ�ض���
        all_options = select_element.options
        # ��ӡѡ���ܸ���
        print len(all_options)
        '''
        is_enabled()���ж�Ԫ���Ƿ�ɲ���
        is_selected()���ж�Ԫ���Ƿ�ѡ��
        '''
        if all_options[1].is_enabled() and not all_options[1].is_selected():
            # ����һ��ͨ�����ѡ��ڶ���Ԫ�أ���Ŵ�0��ʼ
            select_element.select_by_index(1)
            # ��ӡ��ѡ������ı�
            print select_element.all_selected_options[0].text
            # assertEqual()�������Ե�ǰѡ�е�ѡ���ı��Ƿ��ǡ����ϡ�
            self.assertEqual(select_element.all_selected_options[0].text, u"����")
        time.sleep(2)
        # ��������ͨ��ѡ�����ʾ�ı�ѡ���ı�Ϊ��⨺��ҡ�ѡ��
        select_element.select_by_visible_text("⨺���")
        # ������ѡ������ı��Ƿ��ǡ�⨺��ҡ�
        self.assertEqual(select_element.all_selected_options[0].text, u"⨺���")
        time.sleep(2)
        # ��������ͨ��ѡ���value����ֵѡ��value=��shanzha��ѡ��
        select_element.select_by_value("shanzha")
        print select_element.all_selected_options[0].text
        self.assertEqual(select_element.all_selected_options[0].text, u"ɽ�")


    def tearDown(self):
        # �˳�IE�����
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()