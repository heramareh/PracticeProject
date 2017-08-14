#coding: utf-8
import multiprocessing
import os, time
def m1(x):
    time.sleep(0.5)
    print "pid:",os.getpid(),x*x
    return x * x
if __name__ == '__main__':
    pool = multiprocessing.Pool(multiprocessing.cpu_count())
    i_list = range(8)
    print pool.map(m1, i_list)