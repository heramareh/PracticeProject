#encoding=utf-8
import string,time,datetime,os

'''二进制读取一个大文件，计算耗时'''
def count_read_time(filepath):
    try:
        start_time = time.time()
        print start_time
        with open(filepath,'rb') as fp:
            for eachLine in fp:
                pass
        end_time = time.time()
        print end_time
        print 'size:',os.path.getsize(filepath)/1024/1024,'M'
        return end_time - start_time
    except Exception,e:
        print e
        return -1

# print count_read_time("H:\\BaiduYunDownload\\EP10.mp4")

'''输出格式化时间：
2019||12||10
00%00%00
2019-10-10 00:00:00
'''
def get_date(structtime):
    return time.strftime("%Y||%m||%d",structtime)
def get_time(structtime):
    return time.strftime("%H%%%M%%%S",structtime)
def get_date_time(structtime):
    return time.strftime("%Y-%m-%d %H:%M:%S",structtime)

# structtime = time.localtime()
# print get_date(structtime)
# print get_time(structtime)
# print get_date_time(structtime)

'''输入一个时间字符串：2017||01||10 21%45%19，转化为时间戳'''
#time.strptime() 将一个时间字符串转为时间元组（struct_time）
#time.mktime() 将时间元组（struct_time）转为秒
# print time.mktime(time.strptime(get_date(structtime)+' '+get_time(structtime),"%Y||%m||%d %H%%%M%%%S"))

'''创建三级目录：去年年份作为第一级，上个月月份作为第二级，今天的日期作为第三级，
在第三级目录下建个文件，文件名为：当前时间的分时秒，
写入内容：今天是今年的第几天，今年的第几个星期'''
def make_dirs_file(path):
    now = time.localtime()
    lastYear = str(now.tm_year-1)
    lastMonth = str(now.tm_mon - 1)
    if lastMonth == '0':
        lastMonth = '12'
    today = str(now.tm_mday)
    try:
        filepath = os.path.join(path,lastYear,lastMonth,today)
        if not os.path.exists(filepath):
            os.makedirs(filepath)
        os.chdir(filepath)
        filename = time.strftime("%H%M%S",now)+'.txt'
        content = "今天是今年的第%s天，今年的第%s个星期" %(now.tm_yday,time.strftime("%U",now))
        with open(filename,'w') as fp:
            fp.write(content)
        return 1
    except Exception,e:
        print e
        return -1

# print make_dirs_file("d:\\test")