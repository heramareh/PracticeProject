#encoding=utf-8
from selenium import webdriver
import unittest, time
from PIL import Image


class ImageCompare(object):
    '''
    ����ʵ���˶�����ͼƬͨ�����رȶԵ��㷨����ȡ�ļ������ظ�����С
    Ȼ��ʹ��ѭ���ķ�ʽ������ͼƬ��������Ŀ����һһ�Աȣ�
    ������ȶԽ�������ƶȵİٷֱ�
    '''
    def make_regalur_image(self, img, size=(256, 256)):
        # ��ͼƬ�ߴ�ǿ������Ϊָ����size��С
        # Ȼ���ٽ���ת����RGBֵ
        return img.resize(size).convert('RGB')

    def split_image(self, img, part_size=(64, 64)):
        # ��ͼƬ��������С�з�
        w, h = img.size
        pw, ph = part_size
        assert w % pw == h % ph == 0
        return [img.crop((i, j, i + pw, j + ph)).copy() \
                for i in xrange(0, w, pw) for j in xrange(0, h, ph)]

    def hist_similar(self, lh, rh):
        # ͳ���зֺ�ÿ����ͼƬ�����ƶ�Ƶ������
        assert len(lh) == len(rh)
        return sum(1 - (0 if l == r else float(abs(l - r)) / max(l, r)) \
                   for l, r in zip(lh, rh)) / len(lh)

    def calc_similar(self, li, ri):
        # ��������ͼƬ�����ƶ�
        return sum(self.hist_similar(l.histogram(), r.histogram())\
            for l, r in zip(self.split_image(li), self.split_image(ri))) / 16.0

    def calc_similar_by_path(self, lf, rf):
        li, ri = self.make_regalur_image(Image.open(lf)), \
                 self.make_regalur_image(Image.open(rf))
        return self.calc_similar(li, ri)


class TestDemo(unittest.TestCase):

    def setUp(self):
        self.IC = ImageCompare()
        # ����Firefox�����
        self.driver = webdriver.Ie(executable_path = "d:\\IEDriverServer")

    def test_ImageComparison(self):
        url = "http://doc.outofmemory.cn/python/webpy-cookbook/"
        # �����ѹ���ҳ
        self.driver.get(url)
        time.sleep(3)
        # ��ȡ��һ�η����ѹ���ҳ��ͼƬ���������ڱ���
        self.driver.save_screenshot("d:\\sogou1.png")
        self.driver.get(url)
        time.sleep(3)
        # ��ȡ�ڶ��η����ѹ���ҳ��ͼƬ���������ڱ���
        self.driver.save_screenshot("d:\\sogou2.png")
        # ��ӡ���Ž�ͼ�ȶԺ����ƶȣ�100��ʾ��ȫƥ��
        print self.IC.calc_similar_by_path('d:\\sogou1.png','d:\\sogou2.png') * 100

    def tearDown(self):
        # �˳�IE�����
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()