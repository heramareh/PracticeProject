#encoding=utf-8
from multiprocessing import Pool
import time

def f(x):
    time.sleep(2)
    return x * x

if __name__ == '__main__':
    # 启动4个进程
    pool = Pool(processes = 4)      # start 4 worker processes
    # 异步
    result = pool.apply_async(f, [10])  # evaluate "f(10)" asynchronously
    # # 同步
    # result = pool.apple(f, [10])
    # prints "100" unless your computer is *very* slow
    print "try to get result:"
    print result.get(timeout = 3)
    print pool.map(f, range(10))   # prints "[0, 1, 4,..., 81]"