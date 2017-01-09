# encoding=utf-8
import os
import sys
import shutil
import time
import copy
import random
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

'''3、构建一个模块的层级包'''
#见gloryroad

'''4、实现一个除法函数，并处理异常'''
def divide(a, b):
    try:
        return a / b
    except Exception,e:
        return e

# print divide(1,0)

'''5、引发一个异常，并将它抛除到上层函数，上层函数捕获该异常并处理'''
# try:
#     try:
#         1/0
#     except IOError,e:
#         print "IOError!"
# except Exception,e:
#     print e

'''6、实现字符串、列表、元组和set之间互相转换'''
# s='abcabc'
# print '',list(s)
# print tuple(s)
# print set(s)
# lista = ['a','b','c','a','b','c']
# print str(lista)
# print tuple(lista)
# print set(lista)
# t = ('a','b','c','a','b','c')
# print str(t)
# print list(t)
# print set(t)
# se = set(t)
# print str(se)
# print list(se)
# print tuple(se)

'''7、结合set对象，统计某个list出现的重复元素个数'''
def count_duplicate_element_num(lista):
    try:
        if not isinstance(lista, list):
            raise TypeError("TypeError: need a list")
        listb = copy.deepcopy(lista)
        for element in set(listb):
            listb.remove(element)
        count = len(set(listb))
        result_dict = dict.fromkeys(listb,1)
        for element in listb:
            result_dict[element] += 1
        return {"count":count,"result_dict":result_dict}
    except Exception,e:
        print e

# print count_duplicate_element_num(['a','b','c','a','b','c','d'])

'''8、定义一个元组，向元组中添加元素或者修改已有元素，并捕获异常'''
# try:
#     t = (1,2,3)
#     t[0]=11
# except TypeError,e:
#     print "TypeError:",e

'''9、删除无重复元组中给定的元素'''
def delete_element(t, a):
    try:
        if not isinstance(t, tuple):
            raise TypeError("TypeError: need a tuple")
        list_t = list(t)
        try:
            list_t.remove(a)
            return tuple(list_t)
        except ValueError,e:
            return "ValueError: list.remove(x): x not in list"
    except Exception,e:
        return e

# print delete_element([1,2,3],'a')
# print delete_element((1,2,3),'a')
# print delete_element((1,2,3),3)

'''10、有一个ip.txt，里面每行是一个ip，实现一个函数，ping 每个ip的结
果，把结果记录存到ping.txt中，格式为ip:0或ip:1 ，0代表ping成功，1
代表ping失败'''
def ping_test(ip_file_path,result_file_path):
    try:
        try:
            with open(ip_file_path) as ip_fp:
                with open(result_file_path,'w') as result_fp:
                    for ip in ip_fp:
                        result = os.system("ping " + ip)
                        result_fp.write(ip.strip()+" : "+str(result)+os.linesep)
        except IOError,e:
            print "IOError:",e
    except Exception,e:
        print e

# ping_test("d:\\test\\ip.txt","d:\\test\\ping.txt")

'''11、实现DOS命令执行功能，接受输入命令并执行，然后把执行结果和
返回码打印到屏幕'''
def dos(s):
    try:
        os.system(s)
    except Exception,e:
        print e

# dos("python \n")

'''12、求一个n*n矩阵对角线元素之和'''
def sum_diagonal_element(matrix):
    try:
        if not isinstance(matrix, list):
            raise Exception("TypeError: need a list")
        if len(matrix) != len(matrix[0]):
            raise Exception("TypeError: it's not a n*n matrix")
        n = len(matrix)
        sum = 0
        for i in xrange(n):
            sum += matrix[i][i]
        return sum
    except Exception,e:
        return e

# print sum_diagonal_element([[1,2,3],[4,5,6],[7,8,9]])

'''13、输入一个数组，最大的与第一个元素交换，最小的与最后一个元素交换，输出数组'''
def exchange_element(arr):
    try:
        if not isinstance(arr, list):
            raise Exception("need a list")
        # 排序，找到最大值和最小值
        arr_sort = sorted(arr)
        max_element = arr_sort[-1]
        min_element = arr_sort[0]
        # 遍历，若元素等于最大值与第一个元素交换，若元素等于最小值，与最后一个元素交换
        for i in xrange(1,len(arr)-1):
            if arr[i] == max_element:
                arr[0], arr[i] = arr[i], arr[0]
            if arr[i] == min_element:
                arr[-1], arr[i] = arr[i], arr[-1]
        return arr
    except Exception,e:
        return e

# print exchange_element([4,2,5,65,3,2,21,34,2,12,3,43,65])

'''14、平衡点，一个数组，
有一个数字左边所有的数字加起来的总和等于这个数右边所有数字的总和，
请输出这个数以及坐标'''
def find_balance_point(arr):
    try:
        if not isinstance(arr, list):
            raise Exception("need a list")
        result = {}
        for i in xrange(0,len(arr)):
            if i == 0 and sum(arr[1:])==0: # 判断第一个元素是否是平衡点
                result[arr[i]] = i+1
            elif i == len(arr)-1 and sum(arr[:-1])==0: # 判断最后一个元素是否是平衡点
                result[arr[i]] = i+1
            elif sum(arr[:i]) == sum(arr[i+1:]): # 一般情况
                result[arr[i]] = i+1
        return result
    except Exception,e:
        return e

# print find_balance_point([-7,1,5,2,-4,3,0])

'''15、将单词表中由相同字母组成的单词归成一类，每类单词按照单词的
首字母排序，并按每类中第一个单词字典序由大到小排列输出各个类别。
输入格式：按字典序由小到大输入若干个单词，每个单词占一行，以end
结束输入。
cinema
iceman
maps
spam
aboard
abroad
end
输出格式：一类单词一行，类别间单词以空格隔开。
aboard abroad
cinema iceman
maps spam
'''
def sort_words():
    try:
        print u"按字典序由小到大输入若干个单词，每个单词占一行，以end结束输入"
        words = []
        # 循环输入单词，以end结束
        while True:
            word = raw_input("")
            if word == 'end':
                break
            words.append(word)
        # 把所有单词排序
        words.sort()
        print u"排序后："
        while words:
            # 获取单词列表中第一个单词
            result = [words[0]]
            # 从第二个单词开始循环遍历，查找跟第一个单词由相同字母组成的单词
            for word in words[1:]:
                if sorted(result[0]) == sorted(word):   # 比较排序后的两个单词是否相等
                    result.append(word)
            print ' '.join(result)  # 输出
            # 从单词列表中删除已输出的单词
            for result_word in result:
                words.remove(result_word)
    except Exception,e:
        print e

# sort_words()

'''16、输入一个数组，实现一个函数，让所有奇数都在偶数前面'''
def my_sort(arr):
    try:
        odd_list = []
        even_list = []
        for each in arr:
            if each % 2 ==0:
                even_list.append(each)
            else:
                odd_list.append(each)
        return odd_list + even_list
    except Exception,e:
        return e

# print my_sort([1,4,2,5,6,3,6,78,4,3,2,9])

'''17、lista=['a','abc','d','abc','fgi','abf']，
寻找列表中第一次出现次数最多的第一个字母，出现了几次'''
def find_most_first_alpha(lista):
    try:
        max_count = 0
        letters = ''.join(lista)
        for i in lista:
            if letters.count(i[0]) > max_count:
                max_count = letters.count(i[0])
                max_letter = i[0]
        return {"max_letter":max_letter,"max_count":max_count}
    except Exception,e:
        return e

# print find_most_first_alpha(['a','abc','d','abc','fgi','abf'])

'''18、请输入星期几的第一个字母来判断一下是星期几，
如果第一个字母一样，则继续判断第二个字母'''
def judge_week():
    try:
        first_alpha = raw_input("请输入星期几的第一个字母：").lower()
        weeks=["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
        first_letters = [x[0].lower() for x in weeks]
        for x in weeks:
            if first_alpha == x[0].lower():
                if first_letters.count(first_alpha) == 1:
                    return x
                else:
                    second_alpha = raw_input("请输入星期几的第二个字母：").lower()
                    for y in weeks:
                        if first_alpha+second_alpha == y[:2].lower():
                            return y
                    return None
        return None
    except Exception,e:
        return e

# print judge_week()

'''19、有一堆100块的石头，2个人轮流随机从中取1-5块，谁取最后一块就谁win，编程实现此过程'''
def who_is_winner():
    winner = 'n1'
    all = 100
    while True:
        # 随机一个1-5的数
        number = random.randint(1,5)
        # 如果随机数大于剩余总数，结束循环
        if number >= all:
            break
        # 剩余总数
        all -= number
        # 实现两人轮流取
        if winner == 'n1':
            winner = 'n2'
        else:
            winner = 'n1'
    print 'winner is',winner

# who_is_winner()

'''20、实现一个方法，判断一个正整数是否是2的乘方，
比如16是2的4次方，返回True；18不是2的乘方，返回False。
要求性能尽可能高'''
def is_power_of_two(n):
    try:
        if (not isinstance(n,(int,long))) or (n <= 0):
            raise TypeError("need a positive integer")
        
        while True:
            if n == 2 or n == 1:
                return True
            if n % 2 == 1:
                return False
            n = n / 2
    except Exception,e:
        return e

# print is_power_of_two(16)
