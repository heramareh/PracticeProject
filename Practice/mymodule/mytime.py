#encoding=utf-8
import time
def get_now_time():
    now_time = time.localtime()
    return str(now_time.tm_year)+'-'+str(now_time.tm_mon)+'-'+str(now_time.tm_mday)+' '+str(now_time.tm_hour)+':'+str(now_time.tm_min)+':'+str(now_time.tm_sec)

print get_now_time()

