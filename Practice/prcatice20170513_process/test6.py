#encoding=utf-8
from multiprocessing import Process
def f(n, a):
    n = 3.1415927
    print n
    for i in range(len(a)):
        a[i] = -a[i]
        print a[i]
    print "id(a):",id(a)

if __name__ == '__main__':
    num = 0 #
    arr = range(10)
    p = Process(target = f, args = (num, arr))
    p.start()
    p.join()
    print num
    print "id(arr):", id(arr)
    print arr[:]
