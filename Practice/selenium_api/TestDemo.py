# encoding=utf-8
from selenium import webdriver
import unittest, time, os
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
import win32api
import win32con

VK_CODE ={'enter':0x0D, 'down_arrow':0x28}

#���̼�����
def keyDown(keyName):
    win32api.keybd_event(VK_CODE[keyName], 0, 0, 0)
#���̼�̧��
def keyUp(keyName):
    win32api.keybd_event(VK_CODE[keyName], 0, win32con.KEYEVENTF_KEYUP, 0)

class TestDemo(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Ie(executable_path = "d:\\IEDriverServer")
        #self.driver = webdriver.Chrome(executable_path="d:\\chromedriver")
    def test_dataPickerByRightKey(self):
        # ���彫Ҫ���ʵ���ַ
        url = "http://ftp.mozilla.org/pub/mozilla.org//firefox/releases/35.0b8/win32/zh-CN/"
        self.driver.get(url)
        # ���������
        self.driver.maximize_window()
        # ��ͣ5�룬Ŀ�ķ�ֹҳ����һЩ����ĵ���ռ�ݽ���
        time.sleep(5)
        # �ҵ��ı�����Ϊ��Firefox Setup 35.0b8.exe��������Ԫ��
        a = self.driver.find_element_by_link_text("Firefox Setup 35.0b8.exe")
        time.sleep(2)
        # ���ҵ�������Ԫ����ģ��������Ҽ���
        # �Ա����ѡ�����Ϊ��ѡ��Ĳ˵�
        ActionChains(self.driver).context_click(a).perform()
        # ��ͣ2�룬��ֹ����ִ��̫��
        time.sleep(2)
        for i in range(4):
            # ѭ����4���¼�ͷ���������л��������Ϊ��ѡ����
            # ��ͬ�������ѡ���λ�ÿ��ܲ�ͬ
            #a.send_keys(Keys.DOWN)
            keyDown("down_arrow")
            keyUp("down_arrow")
            print i
            time.sleep(2)
        time.sleep(2)
        # �������л��������Ϊ��ѡ���Ϻ�ģ�����س���
        # �������������ļ�·����Windows����
        keyDown("enter")
        keyUp("enter")
        time.sleep(3)
        # ͨ��ִ��AutoIt��д�Ĳ���������Windows�ļ����洰��
        # ����ļ�����·��������
        os.system("D:\\liwang\\autoit\\upload_file.exe")
        # �ȴ��ļ�������ɣ����ݸ��Ե������������趨�ȴ���Ӧ��ʱ��
        time.sleep(5)

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()