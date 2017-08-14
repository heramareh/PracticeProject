#encoding=utf-8
from threading import Thread
import time

def run(a = None, b = None) :
  print a, b
  time.sleep(1)

for i in range(5):
    t = Thread(target = run, args = ("this is a", "thread"+str(i)),name="gloryroad"+str(i))
    #此时线程是新建状态

    print t.getName() #获得线程对象名称
    print t.isAlive() #判断线程是否还活着，在start后，在执行完毕前调用isAlive()才会返回True
    t.start() #启动线程
# t.join()  #主线程等待子线程t执行结束
