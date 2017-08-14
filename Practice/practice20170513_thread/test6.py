#encoding=utf-8
import time
from multiprocessing.dummy import Pool as ThreadPool
#ThreadPool表示给线程池取一个别名ThreadPool
import random

def run(fn):
  time.sleep(random.randint(1,5)*2)
  print fn

if __name__ == '__main__':
  testFL = [1,2,3,4,5]
  pool = ThreadPool(10)#创建10个容量的线程池并发执行
  pool.map(run, testFL)
  pool.close()
  pool.join()