#encoding=utf-8
from multiprocessing import Process, Value, Array

def f(n, a):
    n.value = 3.1415927
    for i in range(len(a)):
        a[i] = -a[i]

def add(n):
    n.value += 1

if __name__ == '__main__':
    num = Value('d', 0.0) # 创建一个进程间共享的数字类型，默认值为0
    arr = Array('i', range(10)) # 创建一个进程间共享的数组类型，初始值为range[10]
    p = Process(target = f, args = (num, arr))
    p.start()
    p.join()

    print num.value # 获取共享变量num的值
    print arr[:]

    # n = 1 # 非共享
    n = Value('d', 0) # 共享
    for i in range(5):
        p = Process(target = add, args = (n,))
        p.start()
        p.join()
    # print n
    print n.value