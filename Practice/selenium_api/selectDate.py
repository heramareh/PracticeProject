#encoding=utf-8
from selenium import webdriver
import unittest, time, traceback
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException

class TestDemo(unittest.TestCase):

    def setUp(self):
        # ����Chrome�����
        self.driver = webdriver.Ie(executable_path = "d:\\IEDriverServer")

    def test_datePicker(self):
        url = "http://jqueryui.com/resources/demos/datepicker/other-months.html"
        # ����ָ������ַ
        self.driver.get(url)
        try:
            # ����һ����ʾ�ȴ�����
            wait = WebDriverWait(self.driver, 10, 0.2)
            # ��ʾ�ȴ��жϱ�����ҳ���ϵ�����������Ƿ�ɼ������ܱ����
            wait.until(EC.element_to_be_clickable((By.ID, 'datepicker')))
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
            # ���ұ�����ҳ���ϵ����������ҳ��Ԫ��
            dateInputBox = self.driver.find_element_by_id("datepicker")
            # ���ҵ����������ֱ������ָ����ʽ�������ַ���
            # �Ϳ��Ա���ģ�������ڿؼ��Ͻ���ѡ����
            dateInputBox.send_keys("11/24/2016")
            time.sleep(3)

    def tearDown(self):
        # �˳�IE�����
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()