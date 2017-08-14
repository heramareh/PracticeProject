#encoding=utf-8
from multiprocessing import Pool
import time
import random
import os

def f(x):
    time.sleep(1)
    y=x * x*random.random()
    print "pid:",os.getpid(),y
    time.sleep(random.random()*1)
    return y

if __name__ == '__main__':
    pool = Pool(processes = 4)      # start 4 worker processes
    result1 = pool.apply_async(f, [10])  # evaluate "f(10)" asynchronously
    result2 = pool.apply_async(f, [10])
    result3 = pool.apply_async(f, [10])
    result4 = pool.apply_async(f, [10])
    result5 = pool.apply_async(f, [10])
    print result5.get(timeout = 10)