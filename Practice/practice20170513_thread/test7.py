#encoding=utf-8
import threading
import time

data = 0
lock = threading.Lock()#创建一个锁对象

def func() :
  global data
  print "%s acquire lock...\n" %threading.currentThread().getName()
  if lock.acquire() :
    print "%s get lock...\n" %threading.currentThread().getName()
    data += 1 #must lock
    time.sleep(2)#其它操作
    print "%s release lock...\n" %threading.currentThread().getName()

    #调用release()将释放锁
    lock.release()

startTime = time.time()
t1 = threading.Thread(target = func)
t2 = threading.Thread(target = func)
t3 = threading.Thread(target = func)
t1.start()
t2.start()
t3.start()
t1.join()
t2.join()
t3.join()

endTime = time.time()
print "used time is", endTime - startTime
print data
