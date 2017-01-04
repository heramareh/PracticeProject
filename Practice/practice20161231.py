# encoding=utf-8
import os
import sys
import shutil
import time
'''模块'''
# import practice20161029 as practice
# import gloryroad.glory
# from gloryroad.glory import *
# print gloryroad.glory.a
# print fun()

'''子包'''
# import gloryroad.gloryroad_1.glory_1
# print gloryroad.gloryroad_1.glory_1.b
# import gloryroad.gloryroad_1.glory_1 as ss
# print ss.b
# from gloryroad.gloryroad_1.glory_1 import *
# print func()

'''多级包__init__.py配置'''
# import gloryroad
# print gloryroad.glory_1.a
# from gloryroad import *
# print glory_1.a
# print glory.fun()

# def join(s):
#     return s
# from string import join
# 
# print join(['a','b','c'])

'''创建一个目录：年月日
进入这个目录，创建一个当前小时的目录
在进入小时的目录的，创建一个分钟的目录
再进入分钟的目录
创建一个文件，当前秒数为文件名，然后文件内容写上年月日时分秒
'''
def make_dir_by_localtime(path):
    localtime = time.localtime()
    abspath = os.path.join(path, time.strftime("%Y-%m-%d", localtime), str(localtime.tm_hour) + 'hour', str(localtime.tm_min) + 'min')
    if not os.path.exists(abspath):
        os.makedirs(abspath)
    os.chdir(abspath)
    with open(str(localtime.tm_sec) + "s.txt", 'w') as fp:
        fp.write(time.strftime("%Y-%m-%d %H:%M:%S", localtime))

# make_dir_by_localtime("d:\\test")

'''异常处理'''
# print 'hello python!'
# try:
#     print 1/0
# except:
#     print "error!"
# print "gloryroad!"

# while True:
#     try:
#         num = float(raw_input("input a number: "))
#         print num
#         break
#     except Exception,e:
#         print e
#         print "not a number!"

'''读一个文件，如果在，打印文件的全部内容
不在，新建这个文件，写入内容“gloryroad”
需要使用异常处理'''
def get_file_content(filepath):
    try:
        with open(filepath,'r') as fp:
            print fp.read()
    except Exception,e:
        print "filepath not exists"
        path = os.path.dirname(filepath)
        if not os.path.exists(os.path.dirname(filepath)):
            os.makedirs(path)
        with open(filepath,'w') as fp:
            fp.write("gloryroad!"+os.linesep)

# get_file_content("d:\\test123\\123.txt")

'''嵌套异常处理'''
# def valueError():
#     int('a')
# 
# try:
#     try:
#         try:
#             print 1/0
#         except IOError,e:
#             print "IOError"
#         else:
#             print 'done'
#     except ZeroDivisionError,e:
#         print "ZeroDivisionError"
#     valueError()
# except ValueError,e:
#     print "ValueError"

'''except后写多个异常'''
# try:
#     try:
#         int("a")
#     except (ValueError,IOError),e:
#         print type(e)
#         1/0
# except Exception,e:
#     print e

'''finally不管抛不抛异常都会执行'''
# try:
#     1/0
# except Exception,e:
#     print e
# else:
#     print "else"
# finally:
#     print "finally"

'''文件打开关闭异常处理'''
# try:
#     fh = open("d:\\test\\1.txt", "r")
#     try:
#         content = fh.read()
#         print content
#     finally:
#         print u"关闭文件"
#         fh.close()
# except IOError:
#     print u"Error: 没有找到文件或读取文件失败"

'''raise触发异常'''
# def exceptionTest(num):
#     if num < 0:
#         raise Exception("Invalid num")
#     else:
#         print num
#     if num == 0:
#         raise ZeroDivisionError("integer division or modulo by zero")
# #调用函数，触发异常
# exceptionTest(-12)

# class GloryRoadError(RuntimeError):
#     def __init__(self, value,message):
#         self.value = value
#         self.message = message
# 
# try:
#     raise GloryRoadError("0","gloryroaderror")
# except GloryRoadError,e:
#     print e.value
#     print e.message

# class ShortInputException(Exception):
#     '''A user-defined exception class.'''
#     def __init__(self, length, atleast):
#         Exception.__init__(self)
#         self.length = length
#         self.atleast = atleast
# try:
#     s = raw_input('Enter something --> ')
#     if len(s) < 3:
#     #如果输入的内容长度小于3，触发异常
#         raise ShortInputException(len(s), 3)
# except EOFError:
#     print '\nWhy did you do an EOF on me?'
# except ShortInputException, x:
#     print 'ShortInputException: The input was of length %d, \
#     was expecting at least %d' % (x.length, x.atleast)
# else:
#     print 'No exception was raised.'

'''自定义实现with'''
# class opened(object):
#     def __init__(self, filename):
#         self.handle = open(filename)
#         print 'Resource: %s' % filename
#     def __enter__(self):
#         print '[Enter %s]: Allocate resource.' % self.handle
#         return self.handle   # 可以返回不同的对象
#     def __exit__(self, exc_type, exc_value, exc_trackback):
#         print '[Exit %s]: Free resource.' % self.handle
#         if exc_trackback is None:
#             print '[Exit %s]: Exited without exception.' % self.handle
#         else:
#             print '[Exit %s]: Exited with exception raised.' % self.handle
#             return False   # 可以省略，缺省的None也是被看做是False
#             self.handle.close()
# 
# with opened(r'c:\withTest.txt') as fp:
#     for line in fp.readlines():
#         print(line)

# class my_open(object):
#     def __init__(self,filename,mode='r'):
#         self.filename = filename
#         self.mode = mode
#     def __enter__(self):
#         self.openedFile = open(self.filename,self.mode)
#         return self.openedFile
#     def __exit__(self, exc_type, exc_value, exc_trackback):
#         self.openedFile.close()
# 
# with my_open("d:\\test\\1.txt") as fp:
#     print fp.read()

'''1、实现自己的数学模块mymath，提供有4个函数，分别为加减乘除，
在B模块中调用mymath模块的函数。
'''
#mymath.py中的内容：
'''def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b
'''
# B.py中的内容：
'''
import mymath    # 引入mymath模块，调用方式：模块名.方法名()
print mymath.add(2, 3)

import mymath as A    # 引入mymath模块，起别名为A，调用方式：别名.方法名()
print A.subtract(3, 2)

from mymath import *    # 引入mymath模块中的所有方法，变量，调用方式：方法名()
print multiply(2, 3)

from mymath import divide    # 引入mymath模块中的指定方法，调用方式：指定的方法名()
print divide(3, 2)
'''

'''2、实现自己的字符串模块mystr，里面有方法：isdigit,strip, join,split'''
#见test.mystr

