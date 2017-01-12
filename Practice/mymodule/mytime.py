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

def timestamp():
    '''返回一个时间戳'''
    return time.time()

# 返回struct_time的函数主要有：localtime()、gtime()、strptime()
def localtime(secs = time.time()):
    '''将一个时间戳转换为struct_time返回,默认为当前时间'''
    return time.localtime(secs)

def gmtime(secs = time.time()):
    '''将一个时间戳转换为UTC时区的struct_time返回，默认为当前时间'''
    return time.gmtime(secs)

def strptime(stime,f):
    '''将格式字符串转化成struct_time返回'''
    return time.strptime(stime,f)

def mktime(t = time.localtime()):
    '''将一个struct_time转化为时间戳,默认为当前时间'''
    return time.mktime(t)

def sleep(second):
    '''睡眠指定秒'''
    time.sleep(second)

def clock():
    '''以浮点数计算的秒数返回当前的CPU时间'''
    return time.clock()

def strftime(f,t=time.localtime()):
    '''把struct_time转化为格式化的时间字符串'''
    return time.strftime(f,t)

if __name__ == '__main__':
#     print get_now_datetime()
#     print get_now_date()
#     print get_now_time()
#     print get_year(10)
#     print get_month(15)
#     print get_day(10)
#     print get_hour(15)
#     print get_minute(12)
#     print get_second(-30)
#     print localtime()
#     print localtime(1284120110.838)
#     print gmtime(1284120110.838)
#     print gmtime()
#     print mktime.__doc__
#     print mktime()
#     print mktime(localtime(1284120110.838))
#     print mktime(gmtime(1284120110.838))
#     print mktime((2017,1,11,16,5,24,2,11,0))
#     print clock()
#     sleep(2)
#     print clock()
    print "%a：星期，英文简写：",strftime("%a")
    print "%A：星期，英文全拼：",strftime("%A")
    print "%b：月份，英文简写：",strftime("%b")
    print "%B：月份，英文全拼：",strftime("%B")
    print "%c：日期和时间的字符串表示（mm/dd/YY HH:MM:SS）：",strftime("%c")
    print "%x：日期字符串（mm/dd/YY）：",strftime("%x")
    print "%X：时间字符串（HH:MM:SS）：",strftime("%X")
    print "%y：年（YY）：",strftime("%y")
    print "%Y：年（YYYY）：",strftime("%Y")
    print "%m：月（01-12）：",strftime("%m")
    print "%d：日（1-31）：",strftime("%d")
    print "%H：时（24小时制，00-23）：",strftime("%H")
    print "%I：时（12小时制，00-11）：",strftime("%I")
    print "%p：AM或PM：",strftime("%p")
    print "%M：分（00-59）：",strftime("%M")
    print "%S：秒（00-61（60和61为闰秒））：",strftime("%S")
    print "%f：微秒（000000-999999）(只适用于datetime中的datetime和time对象)：",datetime.datetime.now().strftime("%f")
    print "%U：一年中的第几周（00-53，星期天是一周的开始，第一个星期天之前的所有天数都放在第00周）：",strftime("%U")
    print "%W：一年中的第几周（00-53，星期一是一周的开始，第一个星期一之前的所有天数都放在第00周）：",strftime("%W")
    print "%j：一年中的第几天（001-366）：",strftime("%j")
    print "%w：一周中的第几天（0-6,0是星期天）：",strftime("%w")
    print "%z：时区名称，如果不能得到时区名称则返回空字符：",strftime("%z").decode("gbk").encode("utf-8")
    print "%Z：时区名称，如果不能得到时区名称则返回空字符：",strftime("%Z").decode("gbk").encode("utf-8")
    print "%%：",strftime("%%")