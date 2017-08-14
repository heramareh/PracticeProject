# encoding: UTF-8
import threading
import time
class MyThread(threading.Thread):
  def __init__(self, id):
    threading.Thread.__init__(self)

  def run(self):
    time.sleep(1)
    time.sleep(3)
    print "This is " + self.getName()

if __name__ == "__main__":
  t1 = MyThread(999)
  t1.setDaemon(True) # 将主线程设置为守护线程
  t1.start()
  time.sleep(2)
  print "I am the father thread."