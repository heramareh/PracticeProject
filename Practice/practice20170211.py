#encoding=utf-8

# class A():
#     "hahaha"
#     def __repr__(self):
#         print "jo"
#         return "1+2"
#     
#     def __str__(self):
#         return "GR"

# a = A()
# print eval(repr(a))
# print a
# print a.__doc__
# print A.__doc__

# from lib.aa import C
# 
# obj = C()
# print obj.__module__  # 输出 lib.aa，即：输出模块
# print obj.__class__      # 输出 lib.aa.C，即：输出类

# class Foo:
# 
#     def __del__(self):
#         print "i will be deleted!"
# 
# f=Foo()

# class Foo:
# 
#     def __init__(self):
#         pass
#     
#     def __call__(self, *args, **kwargs):
#         print args
#         print kwargs
#         sum = 0
#         for i in args:
#             sum += i
#         for j in kwargs.values():
#             sum += j
#         return sum
# obj = Foo() # 执行 __init__
# print obj(1,2,3,a=1,b=2,c=3)       # 执行 __call__

# class Province:
# 
#     country = 'China'
# 
#     def __init__(self, name, count):
#         self.name = name
#         self.count = count
# 
#     def func(self, *args, **kwargs):
#         print 'func'
# # 获取类的成员，即：静态字段、方法、
# print Province.__dict__
# 
# obj1 = Province('HeBei',10000)
# print obj1.__dict__
# # 获取 对象obj1 的成员
# # 输出：{'count': 10000, 'name': 'HeBei'}
# 
# obj2 = Province('HeNan', 3888)
# print obj2.__dict__
# # 获取 对象obj1 的成员
# # 输出：{'count': 3888, 'name': 'HeNan'}

# class Foo:
# 
#     def __str__(self):
#         print "123"
#         return 'gloryroad'
# 
# 
# obj = Foo()
# obj

# class Foo(object):
# 
#     def __init__(self, dict1={}):
#         self.dict1 = dict1
#     
#     def __getitem__(self, key):
# #         print '__getitem__',key
#         return self.dict1[key]
#  
#     def __setitem__(self, key, value):
# #         print '__setitem__',key,value
#         self.dict1[key] = value
#     def __delitem__(self, key):
# #         print '__delitem__',key
#         del self.dict1[key]
# 
#     def __str__(self):
#         return str(self.dict1)
# 
# obj = Foo()
# obj['k1'] = 'gloryroad'
# result = obj['k1']      # 自动触发执行 __getitem__
# print result
# obj['k2'] = 'wupeiqi'   # 自动触发执行 __setitem__
# print obj
# del obj['k1']           # 自动触发执行 __delitem__
# print obj

# class Foo(object):
# 
#     def __getslice__(self, i, j):
#         print '__getslice__',i,j
#  
#     def __setslice__(self, i, j, sequence):
#         print '__setslice__',i,j
#  
#     def __delslice__(self, i, j):
#         print '__delslice__',i,j
# 
# obj = Foo()
# 
# obj[-1:1]                   # 自动触发执行 __getslice__
# obj[0:1] = [11,22,33,44]    # 自动触发执行 __setslice__
# del obj[0:2]                # 自动触发执行 __delslice__

# class Foo(object):
#     string=list("0123456789")
#     def __getslice__(self, i, j):
#         print '__getslice__',i,j
#         return Foo.string[i:j]
#  
#     def __setslice__(self, i, j, sequence):
#         print '__setslice__',i,j
#         Foo.string[i:j]=sequence
#  
#     def __delslice__(self, i, j):
#         print '__delslice__',i,j
#         del Foo.string[i:j]
# 
# obj = Foo()
# 
# print obj[0:2]                   # 自动触发执行 __getslice__
# obj[0:2] = ["aa","bb"]    # 自动触发执行 __setslice__
# print Foo.string
# del obj[0:2]                # 自动触发执行 __delslice__
# print Foo.string

# class Foo(object):
# 
#     def __init__(self, sq):
#         self.sq = sq
# 
#     def __iter__(self):
#         return iter(self.sq.values())
# 
# obj = Foo({'a':1,'b':2,'c':3})
# 
# for i in obj:
#     print i
    
# class A(object): 
#     def __init__(self): 
#         print "init"
#     def __new__(cls,*args, **kwargs): 
#         print "new %s"%cls
#         return object.__new__(cls, *args, **kwargs) 
#   
# A()

# class Singleton(object):
#     def __new__(cls, *args, **kw):
#         if not hasattr(cls, '_instance'):
#             orig = super(Singleton, cls)
#             cls._instance = orig.__new__(cls, *args, **kw)
#         return cls._instance
# 
# class MyClass(Singleton):
#     a = 1
# 
# one = MyClass()
# two = MyClass()
# 
# two.a = 3
# print one.a
# #3
# #one和two完全相同,可以用id(), ==, is检测
# print id(one)
# #29097904
# print id(two)
# #29097904
# print one == two
# #True
# print one is two
# #True

# class Foo(object):
#     value={'key1':"gloryroad"}
#     def __init__(self,*args,**kw):
#         print args
#         print kw
# obj = Foo(1,2,3,a=4,b=5)

# class LeakTest:
#         def __init__(self):
#                 self.a = None
#                 self.b = None
#                 print "object = %d born here." % id(self)
# 
#                 
# A = LeakTest()
# B = LeakTest()
# A.a = B
# B.b = A
# 
# import sys
# print sys.getrefcount(A)
# print sys.getrefcount(B)
# 
# 
# del A
# try:
#     print sys.getrefcount(A)
# except Exception,e:
#     print e
# 
# del B
# try:
#     print sys.getrefcount(B)
# except Exception,e:
#     print e

# outerVar = "this is a global variable"
# def test() :
#     innerVar = "this is a Local variable"
#     print "local variables :"
#     print locals()
# 
# test()
# print "global variables :"
# print globals()

# def outer() :
#     name = "python"
#     def inner() :
#         print name
#     return inner()
# 
# print outer()

# def add(x, y):
#     return x + y
# def sub(x, y):
#     return x - y
# def apply(func, x, y): 
#     return func(x, y) 
# 
# print apply(add, 2, 1) 
# print apply(sub, 2, 1)

#闭包
# def outer() :
#     name = "python"
#     m = 1
#     def inner() :
#         print name
#         n = 1+m
#     return inner
# 
# res = outer()
# res()
# print res.func_closure

# def outer(name) :
#     def inner() :
#         print name
#     return inner
# 
# res1 = outer("python")
# res2 = outer("java")
# res1()
# res2()

import time

#定义装饰器
# def log(func):
#     def wrapper(*args, **kw):
#         print 'call func is %s' %func.__name__
#         return func(*args, **kw)
#     return wrapper
# 
# @log
# def now():
#     now = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
#     print "current time is %s" %now
# 
# now()
# log(now)()

# def log(func):
#     def wrapper(*args, **kw):
#         start_time = time.time()
#         print "start_time",start_time
#         func(*args, **kw)
#         end_time = time.time()
#         print "end_time",end_time
#         return end_time-start_time
#     return wrapper
# 
# @log
# def now():
#     now = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
#     print "current time is %s" %now
#     time.sleep(3)
# 
# print now()

# def deco(func):
#     print "before myfunc() called."
#     func()
#     print "  after myfunc() called."
#     return func
#  
# def myfunc():
#     print " myfunc() called."
#  
# myfunc = deco(myfunc)
# myfunc()
# myfunc()

# def deco(func):
#     print "before myfunc() called." 
#     func()
#     print "  after myfunc() called."
#     return func
# 
# @deco
# def myfunc():
#     print " myfunc() called."
# 
# myfunc()
# myfunc()

# def deco(func):
#     def _deco():
#         print "before myfunc() called."
#         func()
#         print "  after myfunc() called."
#         # 不需要返回func，实际上应返回原函数的返回值
#     return _deco
#  
# @deco
# def myfunc():
#     print " myfunc() called."
#     return 'ok'
#  
# myfunc()
# myfunc()

# def deco(func):
#     def _deco(a, b):
#         print "before myfunc() called."
#         ret = func(a, b)
#         print "  after myfunc() called. result: %s" % ret
#         return ret
#     return _deco
#  
# @deco
# def myfunc(a, b):
#     print " myfunc(%s,%s) called." % (a, b)
#     return a + b
#  
# myfunc(1, 2)  #deco(myfunc)(1,2)
# myfunc(3, 4)  #deco(myfunc)(3,4)

# def deco(func):
#     def _deco(*args):
#         print "before myfunc() called."
#         ret = func(*args)
#         print "  after myfunc() called. result: %s" % ret
#         return ret
#     return _deco
#  
# @deco
# def myfunc(*args):
#     print " myfunc%s called." %(str(args))
#     return sum(args)
#  
# myfunc(1,2,3,4)
# deco(myfunc)(3,4)

# def deco(func):
#     def _deco(*args, **kwargs):
#         print "before %s called." % func.__name__
#         ret = func(*args, **kwargs)
#         print "  after %s called. result: %s" % (func.__name__, ret)
#         return ret
#     return _deco
# 
# @deco
# def myfunc(a, b):
#     print " myfunc(%s,%s) called." % (a, b)
#     return a+b
# 
# @deco
# def myfunc2(a, b, c):
#     print " myfunc2(%s,%s,%s) called." % (a, b, c)
#     return a+b+c
# 
# myfunc(1, 2)
# myfunc(3, 4)
# myfunc2(1, 2, 3)
# myfunc2(3, 4, 5)

def deco(arg):
    def _deco(func):
        def __deco():
            print "before %s called [%s]." % (func.__name__, arg)
            func()
            print "  after %s called [%s]." % (func.__name__, arg)
        return __deco
    return _deco

@deco("mymodule")
def myfunc():
    print " myfunc() called."

@deco("module2")
def myfunc2():
    print " myfunc2() called."

# myfunc()
# myfunc2()

class Foo(object):
    def __init__(self,la=[]):
        self.la = la

    def __len__(self):
        return len(self.la)

    def __getitem__(self, ind):
        return self.la[ind]

    def __setitem__(self, ind, val):
        self.la[ind] = val

    def __delitem__(self,ind):
        del self.la[ind]

    def __getslice__(self,ind1,ind2):
        return self.la[ind1:ind2]

    def __setslice__(self,ind1,ind2,val):
        self.la = self.la[:ind1]+val+self.la[ind2:]

    def __delslice__(self,ind1,ind2):
        self.la = self.la[:ind1]+self.la[ind2:]
 
    def __contains__(self,val):
        if val in self.la:
            return True
        return False

    def __add__(self, obj):
        return self.la+obj.la

    def __mul__(self, n):
        return self.la*n

    def __iter__(self):
        return iter(self.la)

lista = Foo([1,2,3])
print lista.la
print lista.__len__()
print lista.__getslice__(0,3)
lista.__setitem__(1, 0)
for i in lista.__iter__():
    print i
        
