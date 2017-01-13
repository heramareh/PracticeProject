#encoding=utf-8
import time,datetime
# print datetime.MAXYEAR
# print datetime.MINYEAR

# from datetime import date
# print date.max
# print date.min
# #当前时期
# print date.today()
# #date.fromtimestamp(timestamp)：将时间戳转换为date类型的时间
# print date.fromtimestamp(time.time())
# print type(date.fromtimestamp(time.time()))
# print date.today() == date.fromtimestamp(time.time())
# #date.year,date.month,date.day：年，月，日
# now = date.today()
# print now.year
# print now.month
# print now.day
# #date.replace()：用参数给定的年，月，日代替原有对象中的属性，生成一个新的date对象，原对象保持不变
# print now.replace(year=1998)
# print now.replace(month=10,day=30)
# print now
# #date.timetuple()：返回date对应的struct_time对象
# print now.timetuple()
# #date.weekday()：返回本周的第几天，星期一返回0,星期日返回6
# print date.weekday(now)
# #date.isoweekday()：返回本周的第几天，星期一返回1，星期日返回7
# print date.isoweekday(now)
# print date(2008,8,10).isoweekday()
# #date.isocalendar()：以元组的形式返回date对象中的(year,week,weekday)
# '''year：从本年的第一个星期一开始到最后一周的星期日结束。如：2016是从2016年1月4日到2017年1月1日
# week：一年中的第几周[1-52/53]
# weekday：星期一是1，星期日是7[1,7]'''
# print date.isocalendar(now)
# print date(2016,1,3).isocalendar()
# print date(2016,1,4).isocalendar()
# print date(2016,12,31).isocalendar()
# print (date(2016,12,31)+datetime.timedelta(days=1)).isocalendar()
# print date(2017,1,2).isocalendar()
# #date.isoformat()：返回格式化时间字符串'YYYY-mm-dd'
# print date(2017,1,1).isoformat()
# #date.__str__()相当于date.isoformat()
# print date(2017,1,1).__str__()
# #date.strftime(format)：返回指定格式的时间字符串
# print date(2017,1,20).strftime("%m/%Y/%d")
# #date.__format__()：同date.strftime(format)
# print date(2017,1,20).__format__("%Y年%m月%d日 %H时%M分%S秒%f微秒")
# #datetime.timedelta=date1-date2
# print date(2017,1,20)-date(2017,1,10)
# print type(date(2017,1,20)-date(2017,1,10))
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        
# from datetime import time
# print time.min
# print time.max
# print time.resolution
# 
# now= time(23,34,45,001356)
# print now
# print now.hour
# print now.minute
# print now.second
# print now.microsecond
# print now.replace(hour=9,minute=30)
# print now.isoformat()
# print now.__str__()
# print now.strftime("%H %M %S %f")
# print now.__format__("%H-%M-%S")

# from datetime import datetime
# print datetime.min
# print datetime.max
# 
# tm = datetime.now()
# print tm
# print datetime.today()
# print tm.year
# print tm.month
# print tm.day
# print tm.hour
# print tm.minute
# print tm.second
# print tm.microsecond
# print datetime.fromtimestamp(time.time())
# datetimes = datetime.strptime("2015-08-27 17:23:05","%Y-%m-%d %H:%M:%S")
# print datetimes
# print type(datetimes)
# print str(datetimes)
# dates = datetime.date(datetime.today())
# print type(dates)
# print dates
# print dates.year
# times = datetime.time(datetime.today())
# print type(times)
# print times
# print times.hour
# print datetime.combine(datetime.today(),datetime.time(datetime.today()))

from datetime import timedelta
print timedelta(weeks=1).days
print timedelta(hours=1).seconds
print timedelta(milliseconds=1).microseconds
#求两个日期间的天数差
d1 = datetime.datetime(2017,1,1)
d2 = datetime.datetime(2018,3,5)
print (d2-d1).days
#当前时间
nowtime = datetime.datetime.now()
print nowtime
#明天的时间
delta = datetime.timedelta(days=1)
tomorrow = nowtime + delta
print tomorrow
print str(tomorrow)[:-7]
#100天前的日期
print datetime.date.today()+datetime.timedelta(days=-100)
#3小时前
print datetime.datetime.today()+datetime.timedelta(hours=-3)
#获取总共的秒数
print datetime.timedelta(hours=1,seconds=20).total_seconds()
