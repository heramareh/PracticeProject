#encoding=utf-8
from multiprocessing import Process, Queue, Pool
import os
def offer(queue):
  # 入队列
  for i in range(3):
      queue.put(str(os.getpid()) + "_" + str(i))

if __name__ == '__main__':
  # 创建一个队列实例
  q = Queue()
  p = Process(target = offer, args = (q,))
  p.start()
  print os.getpid(),q.get() # 出队列