#encoding=utf-8
import time

def get_datetime():
    return time.strftime("%Y-%m-%d %H:%M:%S")

def get_datetime2():
    return time.strftime("%Y%m%d%H%M%S")

def get_date():
    return time.strftime("%Y-%m-%d")

def get_time():
    return time.strftime("%H-%M-%S")

def get_time2():
    return time.time()

if __name__ == '__main__':
    print get_datetime()
    print get_date()
    print get_time()
