# encoding=utf-8
from threading import Thread
import time


class MyThread(Thread):
    def __init__(self, a):
        # 调用父类的构造方法
        super(MyThread, self).__init__()
        self.a = a

    def run(self):
        time.sleep(self.a)
        print "sleep :", self.a


t1 = MyThread(2)
t2 = MyThread(4)
t1.start()
t2.start()
t1.join()
t2.join()