#encoding=utf-8
from multiprocessing import Process, Queue
import random
import os
def offer(queue,content):
  # 入队列
  print "pid:%s,write %s" %(os.getpid(),content)
  queue.put(content)

if __name__ == '__main__':
  process_list=[]
  q = Queue()
  for i in range(5):
      process_list.append(Process(target = offer, args = (q,str(random.randint(1,100)),))  )
      process_list[i].start()
      print "pid:%s,read %s" %(os.getpid(),q.get()) # 出队列
      process_list[i].join()