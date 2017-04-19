#encoding=utf-8
from selenium import webdriver
import unittest
import time, os
import traceback
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException

class TestDemo(unittest.TestCase):

    def setUp(self):
        # ����Chrome�����
        self.driver = webdriver.Ie(executable_path = "d:\\IEDriverServer")

    def test_uploadFileByAutoIt(self):
        url = "http://127.0.0.1/test_upload_file.html"
        # �����Զ�����ҳ
        self.driver.get(url)
        try:
            # ����һ����ʾ�ȴ�����
            wait = WebDriverWait(self.driver, 10, 0.2)
            # ��ʾ�ȴ��жϱ�����ҳ���ϵ��ϴ��ļ���ť�Ƿ��ڿɱ����״̬
            wait.until(EC.element_to_be_clickable((By.ID, 'file')))
        except TimeoutException, e:
            # ����TimeoutException�쳣
            print traceback.print_exc()
        except NoSuchElementException, e:
            # ����NoSuchElementException�쳣
            print traceback.print_exc()
        except Exception, e:
            # ���������쳣
            print traceback.print_exc()
        else:
            # ����ҳ����ID����ֵΪ��file�����ļ��ϴ���,
            # ���������ѡ���ļ��ϴ���
            self.driver.find_element_by_id("file").click()
            # ͨ��Python�ṩ��osģ���system����ִ�����ɵ�test.exe�ļ�
            os.system("d:\\test.exe")
            # ����AutoIt�ű�ת����Ŀ�ִ���ļ�test.exe����ִ���ٶȱȽ�����
            # ����ȴ�5�룬��ȷ��test.exe�ű�ִ�гɹ�
            time.sleep(5)
            # �ҵ�ҳ����ID����ֵΪ��filesubmit�����ļ��ύ��ť����
            fileSubmitButton = self.driver.find_element_by_id("filesubmit")
            # �����ύ��ť������ļ��ϴ�����
            fileSubmitButton.click()
            # ��Ϊ�ļ��ϴ���Ҫʱ�䣬����������������ʾ�ȴ�������
            # �ж��ļ��ϴ��ɹ���ҳ���Ƿ���ת���ļ��ϴ��ɹ���ҳ�档
            # ͨ��EC.title_is()�����ж���ת���ҳ���Title
            # ֵ�Ƿ�������������ƥ�佫����ִ�к�������
            #wait.until(EC.title_is(u"�ļ��ϴ��ɹ�"))
            time.sleep(2)
    def tearDown(self):
        # �˳�IE�����
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()