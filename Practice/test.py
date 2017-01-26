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

def foo():
    print "calling foo()..."
    aString = 'bar'
    anInt = 123
    print "foo()'s globals:",globals().keys()
    print "foo()'s locals:",locals().keys()
a = 100
print "__main__'s globals:",globals().keys()
print "__main__'s locals:",locals().keys()
foo()