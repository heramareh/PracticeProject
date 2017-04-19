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
        
    def test_operateRadio(self):
        url = "http://127.0.0.1/test_radio.html"
        # �����Զ����html��ҳ
        self.driver.get(url)
        # ʹ��xpath��λ��ȡvalue����ֵΪ'berry'��inputԪ�ض���Ҳ���ǡ���ݮ��ѡ��
        berryRadio = self.driver.find_element_by_xpath("//input[@value='berry']")
        # ���ѡ�񡰲�ݮ��ѡ��
        berryRadio.click()
        # ���ԡ���ݮ����ѡ�򱻳ɹ�ѡ��
        self.assertTrue(berryRadio.is_selected(), u"��ݮ��ѡ��δ��ѡ�У�")
        if berryRadio.is_selected():
            # �������ݮ����ѡ�򱻳ɹ�ѡ�У�����ѡ�����ϡ�ѡ��
            watermelonRadio = self.driver.find_element_by_xpath("//input[@value='watermelon']")
            watermelonRadio.click()
            # ѡ�����ϡ�ѡ���Ժ󣬶��ԡ���ݮ��ѡ���δ��ѡ��״̬
            self.assertFalse(berryRadio.is_selected())
        # ��������name����ֵΪ��fruit���ĵ�ѡ��Ԫ�ض��󣬲������radioList�б���
        radioList = self.driver.find_elements_by_xpath("//input[@name='fruit']")
        '''
        ѭ������radioList�е�ÿ����ѡ��ť������value����ֵΪ��orange���ĵ�ѡ��
        ����ҵ��˵�ѡ���Ժ󣬷���δ����ѡ��״̬�������click����ѡ�и�ѡ�
        '''
        for radio in radioList:
            if radio.get_attribute("value") == "orange":
                if not radio.is_selected():
                    radio.click()
                    self.assertEqual(radio.get_attribute("value"), "orange")


    def tearDown(self):
        # �˳�IE�����
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()