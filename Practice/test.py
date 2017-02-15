#encoding=utf-8

# import gloryroad

# if __name__ == '__main__':
# #     print gloryroad.fun111()
# #     print gloryroad.add(1,2)
# #     print gloryroad.sub(2,1)
#     try:
#         fp = open("d:\\test\\test.log",'r')
#         content = fp.readlines()
#     except IOError:
#         print "IOError!"
#     finally:
#         # 检测某个变量是否有定义的三种方法：
#         if vars().has_key('fp'):
# #         if 'fp' in dir():
# #         if 'fp' in locals().keys():
#             print "finally!"
#             fp.close()

'''写一个逐页显示文本文件的程序。
每次显示文本文件的指定行数，
暂停并向用户提示'按任意键继续'，按键后继续执行'''
# import os
# def get_content_by_lines(path,lines):
#     try:
#         if not os.path.exists(path):
#             raise IOError("path not exists!")
#         if not os.path.isfile(path):
#             raise IOError("path not a file!")
#         lineno = 0
#         with open(path) as fp:
#             for eachline in fp:
#                 if lineno % lines == 0 and lineno != 0:
#                     os.system('pause')
#                 print eachline,
#                 lineno += 1
#     except Exception,e:
#         print str(e)

# get_content_by_lines("d:\\test\\d.txt",5)

# import win32api,time
# import win32con
# # os.system('pause')
# while False:
#     print 1
#     # 回车
#     win32api.keybd_event(38,0,0,0)
#     win32api.keybd_event(38,0,win32con.KEYEVENTF_KEYUP,0)
#     time.sleep(0.1)
#     # 上方向键
#     win32api.keybd_event(13,0,0,0)
#     win32api.keybd_event(13,0,win32con.KEYEVENTF_KEYUP,0)
#     time.sleep(0.1)
#     print 2

# def foo():
#     print "calling foo()..."
#     aString = 'bar'
#     anInt = 123
#     print "foo()'s globals:",globals().keys()
#     print "foo()'s locals:",locals().keys()
# a = 100
# print "__main__'s globals:",globals().keys()
# print "__main__'s locals:",locals().keys()
# foo()

# class P(object):
#     def __init__(self):
#         print "P's constructor"
#         
# class C(P):
# #     pass
#     def __init__(self):
#         print "C's constructor"

# c = C()

class SortedKeyDict(dict):
    def keys(self):
        return sorted(super(SortedKeyDict,self).keys())

# d = SortedKeyDict((('a',1),('b',2),('c',3)))
# print [key for key in d]
# print d.keys()

# class A(object): pass
# class B(A): pass
# class C(A): pass
# class D(B, C): pass
# print D.__mro__

# 修改文件夹下的所有文件及文件夹的修改时间
import os
def recname(path):
    print "path:",path
    os.system("pause")
    if os.path.exists(path):
        for root,dirs,files in os.walk(path):
            for dir in dirs:
#                 print os.path.join(root,dir)
                os.utime(os.path.join(root,dir),None)
            for file in files:
#                 print os.path.join(root,file)
                os.utime(os.path.join(root,file),None)
        print "done!"
    else:
        print "path not exists!"
    os.system("pause")

path = raw_input("please input path:")
recname(path)