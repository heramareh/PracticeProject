#encoding=utf-8
import time,datetime
def get_now_datetime():
    '''XXXX-XX-XX XX:XX:XX'''
    return time.strftime("%Y-%m-%d %H:%M:%S")

def get_now_date():
    '''XXXX-XX-XX'''
    return time.strftime("%Y-%m-%d")

def get_now_time():
    '''XX:XX:XX'''
    return time.strftime("%H:%M:%S")

def get_year(offset = 0):
    return time.localtime().tm_year + offset

def get_month(offset = 0):
    offset = offset % 12
    month = time.localtime().tm_mon + offset
    if month <= 0:
        month += 12
        return month
    elif month >= 13:
        month -= 12
        return month
    else:
        return month

def get_day(offset = 0):
    today = datetime.date.today()
    new_date = today + datetime.timedelta(days = offset)
    return new_date.day

def get_hour(offset = 0):
    offset = offset % 24
    hour = time.localtime().tm_hour + offset
    if hour >=24:
        hour -= 24
        return hour
    elif hour < 0:
        hour += 24
        return hour
    else:
        return hour

def get_minute(offset = 0):
    offset = offset % 60
    minute = time.localtime().tm_min + offset
    if minute >= 60:
        minute -= 60
        return minute
    elif minute < 0:
        minute += 60
        return minute
    else:
        return minute

def get_second(offset = 0):
    offset = offset % 60
    second = time.localtime().tm_sec + offset
    if second >= 60:
        second -= 60
        return second
    elif second < 0:
        second += 60
        return second
    else:
        return second

if __name__ == '__main__':
    print get_now_datetime()
    print get_now_date()
    print get_now_time()
    print get_year(10)
    print get_month(15)
    print get_day(10)
    print get_hour(15)
    print get_minute(12)
    print get_second(-30)