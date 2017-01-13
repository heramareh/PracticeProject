#encoding=utf-8
import string,time,datetime,os

'''一个单词的数据文件，有两行单词，
有重复的单词，也有不重复的单词，
需要你把所有出现过的单词排重后列出来，
并且统计一下唯一出现的单词有多少个。'''
def count_words(filepath):
    try:
        with open(filepath,'r') as fp:
            content = fp.read()
        for i in string.punctuation:
            content=content.replace(i,' ')
        words = content.split()
        print "words:",' '.join(sorted(list(set(words))))
        print "count:",len(set(words))
    except Exception,e:
        print e

# count_words("d:\\test\\test.txt")

'''遍历集合'''
# sTest = set(['e', 'two', 'o', 'n', '1', '3', '2'])
# #遍历集合
# for index, elem in enumerate(sTest) :
#     print u"元素的索引号为：", index, u"对应的元素为：", elem

#获取当前时间的struct_time对象
# formatTime = time.localtime()
# print formatTime

#格式化时间字符串
# strTime = time.strftime("%Y年%m月%d日 %H:%M:%S 星期%w，本年第%W个星期，本年第%j天,本月第%d天",  formatTime)
# print strTime

#创建一个时间字符串变量stime
# stime = "2015-08-24 13:01:30"
#通过strptime()函数将stime转化成strcut_time形式
# formattime = time.strptime(stime,"%Y-%m-%d %H:%M:%S")
# print formattime
#遍历返回的时间元组序列
# for i in formattime:
#     print i,

#获取date能表示的最大日期
# print datetime.date.max

#获取date能表示的最小日期
# print datetime.date.min

# #获取当前时间的时间戳
# now = time.time()
# print now
# #将时间戳转换为date类型的时间
# s = datetime.date.fromtimestamp(now)
# print s

# t = datetime.datetime.now()
# print t
# #替换年月日
# print t.replace(year = 1988)
# print t.replace(month = 12)
# print t.replace(day = 8)
# print t.replace(year = 1988,month = 12,day = 8)

# now = datetime.datetime.now()
# print now.timetuple()

# now = datetime.datetime.now()
# print now
# 
# s = datetime.date.isocalendar(now)
# print s

# #获取今天的日期
# today = datetime.date.today()
# print today
# 
# #在今天的日期上再加10天
# print today + datetime.timedelta(days = 1000)

# #获取今天的日期
# today = datetime.date.today()
# print today
# 
# #替换形成一个新的日期
# future = today.replace(day = 15)
# print future
# 
# #算一下两日期间的间隔
# delta= future - today
# print delta
# 
# #在原日期上添加一个日期间隔
# print future + delta

# #今天的日期
# now = datetime.date.today()
# print now
# 
# #未来的日期
# tomorrow = now.replace(day = 13)
# print tomorrow
# 
# #比较两日期大小
# print tomorrow > now

'''1、能够熟练进行字符串、列表、元组和set之间的转换。'''
# #字符串转列表、元组、集合
# s = '123123'
# print "str:",s
# print "str->list:",list(s)
# print "str->tuple:",tuple(s)
# print "str->set:",set(s)
# print '*'*30
# #列表转字符串、元组、集合
# lista = ['1', '2', '3', '1', '2', '3']
# print "list:",lista
# print "list->str:",''.join(lista)
# print "list->tuple:",tuple(lista)
# print "list->set:",set(lista)
# print '*'*30
# #元组转字符串、列表、集合
# t = ('1', '2', '3', '1', '2', '3')
# print "tuple:",t
# print "tuple->str:",''.join(t)
# print "tuple->list:",list(t)
# print "tuple->set:",set(t)
# print '*'*30
# #集合转字符串、列表、元组
# s = set(['1', '2', '3'])
# print "set:",s
# print "set->str:",''.join(s)
# print "set->list:",list(s)
# print "set->tuple:",tuple(s)

'''2、结合set对象，统计某个list出现的重复元素个数'''
def count_duplicate_element_number(lista):
    listb = lista[:]
    for i in set(listb):
        listb.remove(i)
    print set(listb)
    return len(set(listb))

# count_duplicate_element_number([1,2,3,1,2,3,4,5,6])

'''3、定义一个不可变集合，向不可变集合中添加元素或者修改已有元素，
并捕获异常'''
# try:
#     try:
#         fs = frozenset([1,2,3])
#         fs.add(0)
#     except AttributeError,e:
#         print "AttributeError:",e
#         fs.remove(1)
# except Exception,e:
#     print e

'''4、列出你所有知道的排重方法'''
# lista=[1,2,3,1,2,3,5,5,5,5,6,6,6]
# #method1
# print list(set(lista))
# #method2
# listb=[]
# for i in lista:
#     if i not in listb:
#         listb.append(i)
# print listb
# #method3
# print dict.fromkeys(lista).keys()
# #method4
# listc=lista[:]
# for i in lista:
#     if listc.count(i) > 1:
#         listc.remove(i)
# print listc

'''1、计算程序执行耗时'''
# start_time = time.time()
# try:
#     with open("E:\\eclipse.rar",'rb') as fp:
#         for i in fp:
#             pass
# except Exception,e:
#     print e
# end_time = time.time()
# print end_time - start_time

'''2、将字符串转换为时间戳'''
def timestr_to_timestamp(timestr,f):
    try:
        structtime = time.strptime(timestr,f)
        return time.mktime(structtime)
    except Exception,e:
        print e
        return -1

# print timestr_to_timestamp("2017-01-12 17:48:00","%Y-%m-%d %H:%M:%S")

'''3、将格式时间字符串转换成时间元组，然后再转换成自定义的时间格式字符串'''
def timestr_to_newtimestr(timestr,f,new_f):
    try:
        structtime = time.strptime(timestr,f)
        return time.strftime(new_f,structtime)
    except Exception,e:
        print e
        return -1

# print timestr_to_newtimestr("2017-01-12 17:48:00","%Y-%m-%d %H:%M:%S","%Y/%m/%d %H%%%M%%%S")

'''4、将当前时间戳转换为指定格式日期
创建名称为当前时间(年月日)的目录，在这个目录下创建名称为当前时间(年月日)
的txt文件，并且输入内容为“你好”'''
def mk_dir_file(path):
    try:
        name = time.strftime("%Y%m%d",time.localtime(time.time()))
        filepath = os.path.join(path,name)
        if not os.path.exists(filepath):
            os.makedirs(filepath)
        os.chdir(filepath)
        filename = name + '.txt'
        with open(filename,'w') as fp:
            fp.write('你好')
        return 1
    except Exception,e:
        print e
        return -1

# print mk_dir_file("d:\\test")

'''1、将当前时间戳转换为指定格式日期'''
# print datetime.date.fromtimestamp(time.time()).strftime("%Y/%m/%d")

'''2、获得三天（三小时和三分钟）前的时间方法'''
# now = datetime.datetime.today()
# print now + datetime.timedelta(days=-3)
# print now + datetime.timedelta(hours=-3)
# print now + datetime.timedelta(minutes=-3)

'''3、计算昨天和明天的日期'''
# print datetime.date.today() + datetime.timedelta(days=-1)
# print datetime.date.today() + datetime.timedelta(days=1)

'''4、使用datetime模块来获取当前的日期和时间'''
# print datetime.date.today()
# print datetime.datetime.today().strftime("%H:%M:%S:%f")

'''9、创建名称为log的目录，目录下创建三个文件夹，名分别为去年今天的日期、
当前日期(年月日)、明年今天的日期，然后分别在这三个目录中创建三个.log文
件，名分别为当年的今天在当年中第多少天，文件中分别写入当年的今天是这
一年的第几个星期以及当前是星期几。'''
def make_dirs_files(path):
    try:
        parent_dir_name = "log"
        path = os.path.join(path,parent_dir_name)
        if not os.path.exists(path):
            os.mkdir(path)
        today = datetime.date.today()
        tomrrow = today + datetime.timedelta(days=1)
        lastday = today + datetime.timedelta(days=-1)
        for i in today,tomrrow,lastday:
            dir_name = str(i)
            os.chdir(path)
            if not os.path.exists(dir_name):
                os.mkdir(dir_name)
            os.chdir(dir_name)
            file_name = i.strftime("%j")+'.log'
            content = "今天是这一年的第%s个星期，当前是星期%s" %(i.strftime("%U"),i.strftime("%w"))
            with open(file_name,'w') as fp:
                fp.write(content)
        return 1
    except Exception,e:
        print e
        return -1

# print make_dirs_files("d:\\test")