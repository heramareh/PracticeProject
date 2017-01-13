#encoding=utf-8
import calendar

# #calendar.day_name：星期的全称
# print type(calendar.day_name)
# print calendar.day_name[:]
# print list(calendar.day_name)
# print list(calendar.day_name)
# for day_name in calendar.day_name:
#     print day_name,
# print
# #calendar.day_abbr：星期的简称
# for day_abbr in calendar.day_abbr:
#     print day_abbr,
# print
# #calendar.month_name：月的全称
# for month_name in calendar.month_name:
#     print month_name,
# print
# #calendar.month_abbr：月的简称
# for month_abbr in calendar.month_abbr:
#     print month_abbr,
# print
# #calendar.isleap(year)：判断是否是闰年
# print calendar.isleap(2015)
# print calendar.isleap(2000)
# #calendar.month(year,month,w=2,l=1))：返回指定年的某月的日历
# '''w：每日宽度间隔；7*w+6：每行的长度；l：相邻行数差'''
# print calendar.month(2017,1,4,3)
#calendar.calendar(year,w=2,l=1,c=6)：返回指定年的日历，3个月一行
'''w：每日宽度间隔；c：每月之间的间隔；21*w+18+2*c：每行长度；l：相邻行数差'''
print calendar.firstweekday() #获取当前设置的每周的开始星期，星期一是0星期日是6
calendar.setfirstweekday(calendar.SUNDAY) # 设置每周的开始星期
print calendar.firstweekday()
# print calendar.calendar(2017)
print calendar.month(2017,1)
# print calendar.calendar(2018,w=4,c=5,l=3)
#calendar.HTMLCalendar()：返回HTML格式的日历
myCal = calendar.HTMLCalendar(calendar.SUNDAY)
# print myCal.formatmonth(2017,1)
# print myCal.formatyear(2017,2)
with open("d:\\test\\myCal.html",'w') as fp:
    fp.write(myCal.formatmonth(2017,1))
#     fp.write(myCal.formatyear(2017,3))
