#coding=utf-8
from Queue import Queue #队列类
import random
import threading
import time

#生成者线程
class Producer(threading.Thread):
    def __init__(self, t_name, queue):
        #调用父线程的构造方法。
        threading.Thread.__init__(self, name = t_name)
        self.data = queue

    def run(self):
        for i in range(5):
            print "%s: %s is producing %d to the queue!\n" %(time.ctime(), self.getName(), i)
            self.data.put(i)#向队列中添加数据
            #产生一个0-2之间的随机数进行睡眠
            time.sleep(random.randrange(10) / 5)
        print "%s: %s finished!" %(time.ctime(), self.getName())
#消费者线程
class Consumer(threading.Thread):
    def __init__(self, t_name, queue):
        threading.Thread.__init__(self, name = t_name)
        self.data = queue

    def run(self):
        for i in range(5):
            val = self.data.get()#从队列中取出数据
            print "%s: %s is consuming. %d in the queue is consumed!\n" %(time.ctime(), self.getName(), val)
            time.sleep(random.randrange(10))
        print "%s: %s finished!" %(time.ctime(), self.getName())
#Main thread
def main():
    queue = Queue()#创建一个队列对象（特点先进先出）
    producer = Producer('Pro.', queue)#生产者对象
    consumer = Consumer('Con.', queue)#消费者对象
    producer.start()
    consumer.start()
    producer.join()
    consumer.join()
    print 'All threads terminate!'

if __name__ == '__main__':
    main()
