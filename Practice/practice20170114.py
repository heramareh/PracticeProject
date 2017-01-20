#encoding=utf-8
import time

class Animal(object):
    count_animal = 0
    animal_name_list = []
    def __init__(self,name,sex,length):
        self.name = name
        self.sex = sex
        self.length = length
        Animal.count_animal += 1
        Animal.animal_name_list.append(name)

    def get_name(self):
        return self.name

    @property
    def get_length(self):
        return self.length

    @classmethod
    def get_count_animal(cls,n):
        print u"动物总数：",Animal.count_animal
        print "*"*n

    @staticmethod
    def static_fun(m):
        print u"所有动物：",' '.join(Animal.animal_name_list)
        print "*"*m

# cat = Animal("tom","male",60)
# print getattr(cat,"name")
# print hasattr(cat,"length")
# setattr(cat,"length",100)
# setattr(cat,"age",18)
# delattr(cat,"age")
# print hasattr(cat,"age")
# cat.name = "cat" #修改
# cat.age = 10 #增加
# del cat.length #删除
# print cat.name,cat.sex,cat.age
# print cat.get_name()
# print cat.get_length
# Animal.get_count_animal(20)
# Animal.static_fun(20)
# dog = Animal("jarry","female",80)
# print dog.get_length
# Animal.get_count_animal(20)
# Animal.static_fun(20)
# print dog.get_count_animal()
# print cat.get_name()
# print dog.get_name()

class Employee (object):
    '''所有员工基类'''
    empCount = 0

    def __init__(self, name, salary) :
        #类的构造函数
        self.name = name
        self.salary = salary
        Employee.empCount += 1

    def displayCount(self) :
        '''统计总数'''
        print "total employee ",Employee.empCount

    def displayEmployee(self) :
        print "name :",self.name , ", salary :", self.salary

# emp1 = Employee("zhangsan",1)
# emp1.displayEmployee()
# emp1.displayCount()
# emp1.name
# Employee.empCount
# 
# emp2 = Employee("lisi",2)
# emp2.displayEmployee()
# emp2.displayCount()
# emp2.name
# Employee.empCount
# print Employee.__doc__
# print Employee.displayCount.__doc__

def kanchai(name, age, gender):
    print u"%s,%s岁,%s,上山去砍柴" %(name, age, gender)

def qudongbei(name, age, gender):
    print u"%s,%s岁,%s,开车去东北" %(name, age, gender)

def dabaojian(name, age, gender):
    print u"%s,%s岁,%s,最爱大保健" %(name, age, gender)

# kanchai(u'小明', 10, u'男')
# qudongbei(u'小明', 10, u'男')
# dabaojian(u'小明', 10, u'男')
# 
# kanchai(u'老李', 90, u'男')
# qudongbei(u'老李', 90, u'男')
# dabaojian(u'老李', 90, u'男')

class Foo:
    
    def __init__(self, name, age ,gender):
        self.name = name
        self.age = age
        self.gender = gender

    def kanchai(self):
        print u"%s,%s岁,%s,上山去砍柴" %(self.name, self.age, self.gender)

    def qudongbei(self):
        print u"%s,%s岁,%s,开车去东北" %(self.name, self.age, self.gender)

    def dabaojian(self):
        print u"%s,%s岁,%s,最爱大保健" %(self.name, self.age, self.gender)
# xiaoming = Foo(u'小明', 10, u'男')
# xiaoming.kanchai()
# xiaoming.qudongbei()
# xiaoming.dabaojian()
# 
# laoli = Foo(u'老李', 90, u'男')
# laoli.kanchai()
# laoli.qudongbei()
# laoli.dabaojian()

# #####################  定义实现功能的类  #####################
class Person:

    def __init__(self, na, gen, age, fig):
        self.name = na
        self.gender = gen
        self.age = age
        self.fight =fig

    def grassland(self):
        """注释：草丛战斗，消耗200战斗力"""

        self.fight = self.fight - 200

    def practice(self):
        """注释：自我修炼，增长100战斗力"""
        
        self.fight = self.fight + 200

    def incest(self):
        """注释：多人游戏，消耗500战斗力"""
        
        self.fight = self.fight - 500

    def detail(self):
        """注释：当前对象的详细情况"""

        temp = u"姓名:%s ; 性别:%s ; 年龄:%s ; 战斗力:%s"  % (self.name, self.gender, self.age, self.fight)
        print temp

# cang = Person(u'苍井井', u'女', 18, 1000)    # 创建苍井井角色
# dong = Person(u'东尼木木', u'男', 20, 1800)  # 创建东尼木木角色
# bo = Person(u'波多多', u'女', 19, 2500)      # 创建波多多角色
# 
# cang.incest() #苍井空参加一次多人游戏
# dong.practice()#东尼木木自我修炼了一次
# bo.grassland() #波多多参加一次草丛战斗
# 
# 
# #输出当前所有人的详细情况
# cang.detail()
# dong.detail()
# bo.detail()
# 
# 
# cang.incest() #苍井空又参加一次多人游戏
# dong.incest() #东尼木木也参加了一个多人游戏
# bo.practice() #波多多自我修炼了一次
# 
# #输出当前所有人的详细情况
# cang.detail()
# dong.detail()
# bo.detail()


class MyFile(object):
    def __init__(self,path,mode='r'):
        '''构造函数'''
        self.path = path
        self.mode = mode

    def get_file_handle(self):
        try:
            self.fp = open(self.path,self.mode)
            return self.fp
        except Exception,e:
            print e

    def get_content_by_line(self,line):
        try:
            if self.get_file_handle():
                number = 1
                for eachLine in self.fp:
                    if number ==line:
                        return eachLine
                    number += 1
                return -1
            return -1
        except Exception,e:
            print e
            return -1

    def close_file(self):
        self.fp.close()

    def __del__(self):
        '''析构函数'''
        print "deleted!"

# ff = MyFile("d:\\test\\d.txt")
# print ff.get_content_by_line(10),
# ff.close_file()

'''随机的10个数字，10个字母，10个数字和字母的组合，
初始化的时候传入参数指定数字出现的范围和字母范围'''
import string,random
class F(object):
    def __init__(self,num_start,num_end,letter_start,letter_end):
        self.num_start = num_start
        self.num_end = num_end
        self.letter_start = letter_start
        self.letter_end = letter_end

    def get_num_range(self):
        try:
            return string.digits[self.num_start:self.num_end+1]
        except Exception,e:
            print e

    def get_letter_range(self):
        try:
            return string.letters[string.letters.index(self.letter_start):string.letters.index(self.letter_end)+1]
        except Exception,e:
            print e

    def __get_random_str(self,length,str_range):
        try:
            s = ''
            for i in xrange(length):
                s += random.choice(str_range)
            return s
        except Exception,e:
            print e

    def get_nums(self,length):
        num_range = self.get_num_range()
        if num_range:
            return self.__get_random_str(length,num_range)

    def get_letters(self,length):
        letter_range = self.get_letter_range()
        if letter_range:
            return self.__get_random_str(length,letter_range)

    def get_alnums(self,length):
        num_range = self.get_num_range()
        letter_range = self.get_letter_range()
        if num_range and letter_range:
            return self.__get_random_str(length,num_range+letter_range)

# f = F(0,8,'a','H')
# print f.get_num_range()
# print f.get_letter_range()
# print f.get_nums(10)
# print f.get_letters(8)
# print f.get_alnums(10)

class Foo2:

    def __init__(self, name):
        self.name = name

    def ord_func(self):
        """ 定义普通方法，至少有一个self参数 """

        # print self.name
        print u'普通方法'

    @classmethod
    def class_func(cls):
        """ 定义类方法，至少有一个cls参数 """

        print u'类方法'

    @staticmethod
    def static_func():
        """ 定义静态方法 ，无默认参数"""

        print u'静态方法'

# f1=Foo2("f1")
# f1.ord_func()
# Foo2.class_func()
# Foo2.static_func()

class Goods(object):

    def __init__(self):
        self.number = 0
    @property
    def price(self):
        print '@property'
        return self.number

    @price.setter
    def price(self, value):
        print '@price.setter'
        if value < 100:
            self.number=0
        else:
            self.number=value

    @price.deleter
    def price(self):
        print '@price.deleter'


# obj = Goods()
# print obj.price          # 自动执行 @property 修饰的 price 方法，并获取方法的返回值
# obj.price = 123    # 自动执行 @price.setter 修饰的 price 方法，并将  123 赋值给方法的参数
# print obj.price
# del obj.price      # 自动执行 @price.deleter 修饰的 price 方法


class Goods2(object):
    number = 0

    @property
    @classmethod
    def price(cls):
        print '@property'
        return Goods2.number

    @price.setter
    @classmethod
    def price(cls, value):
        print '@price.setter'
        if value < 100:
            Goods2.number=0
        else:
            Goods2.number=value

    @price.deleter
    @classmethod
    def price(cls):
        print '@price.deleter'
        Goods2.number=0


# obj = Goods2()
# print Goods2.price          # 自动执行 @property 修饰的 price 方法，并获取方法的返回值
# Goods2.price = 123    # 自动执行 @price.setter 修饰的 price 方法，并将  123 赋值给方法的参数
# print Goods2.price
# del Goods2.price      # 自动执行 @price.deleter 修饰的 price 方法

class Employee2 (object):
  #所有员工基类
  empCount = 0

  def __init__(self, name, salary) :
    #类的构造函数
    self.name = name
    self.salary = salary
    Employee.empCount += 1

  def displayCount(self) :
    #类方法
    print "total employee ",Employee.empCount

  def displayEmployee(self) :
    print "name :",self.name , ", salary :", self.salary

#创建Employee类的实例对象
# emp1 = Employee2("SR", 10000)
# emp1.displayCount()
# emp1.displayEmployee()
# emp1.salary = 20000  #修改属性 salary
# print emp1.salary
# emp1.age = 25   #添加属性 age
# print emp1.age
# del emp1.age #删除 age属性

class Employee22 (object):
    #所有员工基类
    empCount = 0

    def __init__(self, name, salary) :
        #类的构造函数
        self.name = name
        self.salary = salary
        Employee.empCount += 1

    def displayCount(self) :
        #类方法
        print "total employee ",Employee.empCount

    def displayEmployee(self) :
        print "name :",self.name , ", salary :", self.salary

# #创建Employee类的实例对象
# emp1 = Employee22("SR", 10000)
# 
# #判断实例对象是否存在某个属性
# if hasattr(emp1, 'name'):#如果存在tel属性，返回True，否则返回False
#     print u"属性name存在"
# else :
#     print u"属性name不存在"
# #访问对象的属性
# try :  
#     a = getattr(emp1, 'name') #返回name属性的值
#     print u"name属性的值：", a
# except Exception, e:
#     print e
# 
# #给实例添加一个属性
# setattr(emp1, 'tel', '13111111111') #添加tel属性
# try :  
#     a = getattr(emp1, 'tel') #返回tel属性的值
#     print u"新添加的tel属性的值：", a
# except Exception, e:
#     print e
# 
# #删除某个属性
# try :
#     delattr(emp1, 'tel')#删除tel属性
# except Exception, e:
#     print e
# else :
#     #未发生异常时执行这里
#     if hasattr(emp1, 'tel'):#如果存在tel属性，返回True，否则返回False
#         print u"属性tel存在"
#     else :
#         print u"属性tel不存在"

class Person2(object):
    "a person class"
    def __init__(self,name,sex,age):
        self.name = name
        self.sex = sex
        self.age = age
    
    def get_name(self):
        return self.name
    
    def get_sex(self):
        return self.sex
    
    def get_age(self):
        return self.age
    
    def set_name(self,value):
        self.name = value

# p = Person2("zhangsan","m",18)
# print Person2.__dict__
# print Person2.__doc__
# print Person2.__name__
# print object.__module__
# print Person2.__bases__

class f(object) :
    count = 12#类变量

# t = f()
# print u"t.count内存地址 =", id(t.count), "t.count =", t.count
# print u"f.count内存地址 =", id(f.count), "f.count =", f.count
# print t.__dict__
# t.count = 10
# print u"通过实例对象修改count的值后"
# print u"t.count内存地址 =", id(t.count), "t.count =", t.count
# print t.__dict__
# print u"f.count内存地址 =", id(f.count), "f.count =", f.count
# del t.count
# print t.count

class f2(object) :
    count = 12

# t = f2()#创建类的实例对象
# print t.count
# print f2.count
# 
# #通过实例对象修改属性
# t.count = 10
# print u"****添加一个同名的实例count属性后****"
# print t.count
# print f2.count
# print u"****添加一个类变量后****"
# f2.age = 34
# print f2.age
# print t.age
# print u"****给实例对象添加一个新的属性后****"
# t.address = u'北京'
# print t.address
# print u"*****使用类名直接访问实例属性时："
# print f2.address


hhh="hahaha" #全局变量
class Person3(object):
    id = 12   #类静态成员在这儿定义，注意缩进
    def  __init__(self,name):
        self.name = name #类的实例变量
        self.inName = 'ads' #类的实例变量
    def getName(self) :
        name = "lucy" #局部变量
        return self.name, name, hhh
# p = Person3('linda')
# print p.name #访问对象的实例变量
# #通过函数访问实例变量和局部变量
# res = p.getName()
# print res

class Person4(object):
    id = 12   #类静态成员在这儿定义，注意缩进
    def  __init__( self,name ):
        self.name = name
        self.__inName = 'ads' 

    @classmethod   #类方法定义，用注解方式说明
    def up(cls,a ):   #这儿是cls，不是self
        print cls,cls.__name__
        return a+1

# #创建类的实例
# p = Person4( "alpha" )
# #调用类方法
# print Person4.up(20) #类名直接调用
# print p.up(12) #通过实例对象调用

class employee(object) : 
    city = 'BJ' #类属性

    def __init__(self, name) :
        self.name = name #实例变量

    #定义类方法
    @classmethod
    def getCity(cls) :
        return cls.city

    #定义类方法
    @classmethod
    def setCity(cls, city) :
        cls.city = city

    #实例方法
    def set_City(self, city) :
        employee.city = city

# emp = employee('joy') #创建类的实例
# print emp.getCity() #通过实例对象引用类方法
# print employee.getCity()#通过类对象引用类方法
# 
# emp.setCity('TJ')#实例对象调用类方法改变类属性的值
# print emp.getCity()
# print employee.getCity()
# 
# employee.setCity('CD')#类对象调用类方法改变类属性的值
# print emp.getCity()
# print employee.getCity()
# 
# emp.set_City('SH')#调用实例方法改变类属性的值
# print emp.getCity()
# print employee.getCity()
# 
# employee.city = 20 #直接修改类属性的值
# print emp.getCity()
# print employee.getCity()

class Person5(object):
    id = 12   #类静态成员在这儿定义，注意缩进
    def  __init__( self,name ):
        self.name = name
        self.__inName = 'ads'

    @staticmethod    #类静态方法定义，用注解方式说明
    def down( b ):   #静态方法不需要self，cls变量
        id = 13
        print u"类变量id =", id
        return b-1

# #创建类的实例
# p = Person5( "alpha" )
# 
# #调用静态方法
# print Person5.down(15) #类名直接调用
# print p.down(19) #通过实例对象调用

class Person6(object):
    count = 0
    def __init__(self):
        Person6.count += 1
    def __del__(self):
        Person6.count -= 1
        print "del!!!"

# p1 = Person6()
# print Person6.count
# p2 = Person6()
# print Person6.count
# p3 = Person6()
# print Person6.count
# p4 = Person6()
# print Person6.count
# del p1
# print Person6.count
# del p2
# print Person6.count
# del p3
# print Person6.count
# del p4
# print Person6.count

class Person7(object):
    __secretCount = 0 #私有属性
    def  __init__(self, name):
        self.name = name #实例属性
        self.__inName = 'ads' #私有属性

    def visit_private_attribute( self ):
        self.__secretCount += 1
        print "__secretCount: ", self.__secretCount
        print u"__inName：", self.__inName
# p = Person7("prel")
# p.visit_private_attribute()
# print u"在类外直接通过实例访问私有属性"
# print '*'*20
# print p._Person7__inName
# print '*'*20
# print p.__inName

class Person8(object):
    __secretCount = 0 #私有属性
    def  __init__(self, name):
        self.name = name #实例属性
        self.__inName = 'ads' #私有属性

    def visit_private_attribute( self ):
        self.__secretCount += 1
        print "__secretCount: ", self.__secretCount
        print u"__inName：", self.__inName
# p = Person8("prel")
# p.visit_private_attribute()
# print u"在类外直接通过实例访问私有属性"
# print p._Person8__inName
# print p._Person8__secretCount

class Person9(object):
    id = 12   #类静态成员在这儿定义，注意缩进
    def  __init__(self,name):
        self.name = name
        self.__inName = 'ads'

    def __setId(self,id): #隐藏方法
        Person.id = id * 2

    def getId(self):
        self.__setId(18) #类内部调用隐藏方法
        return Person.id

# p = Person9("prel")
# print p.getId()
# print u"类外部调用私有方法"
# print p.__setId(10)

'''获取指定路径下所有一级目录中最新创建的目录名和绝对路径'''
import os
def get_newest_dir(path):
    try:
        # 判断路径是否存在
        if not os.path.exists(path):
            raise WindowsError("path not exist!")
        # 进入此路径下
        os.chdir(path)
        # 获取路径下所有一级目录及目录的创建时间存到一个字典里
        dirs_ctime = {}
        for i in os.listdir(path):
            if os.path.isdir(i):
                dirs_ctime[i] = os.path.getctime(i)
        # 获取最新创建时间
        newesttime = sorted(dirs_ctime.values())[-1]
        # 得到最新创建的目录名以及目录的绝对路径
        for dir in dirs_ctime.keys():
            if dirs_ctime[dir] == newesttime:
                return {"dir_name":dir,"dir_abspath":os.path.join(path,dir)}
        return None
    except Exception,e:
        print e
        return None

# print get_newest_dir("d:\\test")

'''9 、编写程序片段，定义表示课程的类Course 。
课程的属性包括课程名、编号、选修课号；
方法包括设置课程名、设置编号、设置选修课号
以及获取课程名、获取编号、获取选修课程号，
然后打印输出该对象的课程名、编号以及选修课号。'''
class Course(object):
    def __init__(self, course_name, number, elective_course_number):
        self.course_name = course_name
        self.number = number
        self.elective_course_number = elective_course_number

    def get_course_name(self):
        return self.course_name

    def get_number(self):
        return self.number

    def get_elective_course_number(self):
        return self.elective_course_number

    def set_course_name(self, new_course_name):
        self.course_name = new_course_name

    def set_number(self, new_number):
        self.number = new_number

    def set_elective_course_number(self, new_elective_course_number):
        self.elective_course_number = new_elective_course_number

# course1 = Course("python",2017001,1010110)
# print course1.get_course_name()
# print course1.get_course_name()
# print course1.get_elective_course_number()
# course1.set_course_name("java")
# course1.set_number(201702)
# course1.set_elective_course_number(1010111)
# print course1.get_course_name(),course1.get_number(),course1.get_elective_course_number()

'''写程序，实现出题：100内的加减乘除（减法要求大减小），10道题，满分100分，通过键盘输入答案，如果正确+10分，错误不加分，给出总分。'''
from operator import add, sub, mul, div
import random,time

class Student(object):
    def __init__(self, name):
        self.name = name
    def set_score(self, score):
        self.score = score
    def set_start_time(self):
        self.start_time = time.time()
    def set_end_time(self):
        self.end_time = time.time()
    def get_time(self):
        self.time = self.end_time - self.start_time
        return self.time
    def get_name(self):
        return self.name
    def get_score(self):
        return self.score
def arithmetic_figure(questions_count):
    operators = {'+':add, '-':sub, '*': mul, '/': div}
    score = 0
    everyone_score = 100 / questions_count
    while questions_count:
        op = random.choice('+-*/')
        nums = [random.randint(1, 100) for i in range(2)]
        if op in '-/':
            nums.sort(reverse=True)
        while True:
            if op == '/' and nums[0]%nums[1] != 0:
                nums = [random.randint(1, 100) for i in range(2)]
                nums.sort(reverse=True)
                continue
            else:
                break
        pr = "%d.  %d %s %d = " %(11-questions_count,nums[0],op,nums[1])
        result = operators[op](*nums)
        if result == int(raw_input(pr)):
            score += everyone_score
            print "right!"
        else:
            print "wrong!"
        questions_count -= 1
    return score

# student1 = Student("zhangsan")
# student1.set_start_time()
# student1.set_score(arithmetic_figure(10))
# student1.set_end_time()
# print '*'*20
# print "name:",student1.get_name()
# print "score:",student1.get_score()
# print "time: %ds" % int(student1.get_time())
# print '*'*20

# class App:
#     def _init__(self, master,count):
#         self.count = count
#         frame = Tkinter.Frame(master)
#         frame.pack()
#         self.frame1 = Tkinter.Frame(master)
#         self.frame1.pack()
#         Tkinter.Button(frame, text = u'下一题',command = App.set_label()).grid(row=0,column=0)
#         Tkinter.Button(frame, text = u'退出',command = sys.exit()).grid(row=0,column=1)
#         label = Tkinter.Label(self.frame1, text = arithmetic_figure2(self.count))
#         label.pack()
#         
#     def set_label(self):
#         self.count -= 1
#         label = Tkinter.Label(self.frame1, text = arithmetic_figure2(self.count))
#         label.pack()
# 
# import Tkinter,sys,tkMessageBox
# def arithmetic_figure2():
#     global score,count,everyone_score,result
#     operators = {'+':add, '-':sub, '*': mul, '/': div}
#     op = random.choice('+-*/')
#     nums = [random.randint(1, 100) for i in range(2)]
#     if op in '-/':
#         nums.sort(reverse=True)
#     while True:
#         if op == '/' and nums[0]%nums[1] != 0:
#             nums = [random.randint(1, 100) for i in range(2)]
#             nums.sort(reverse=True)
#             continue
#         else:
#             break
#     pr = "%d、  %d %s %d = " %(11-count,nums[0],op,nums[1])
#     result = operators[op](*nums)
#     if result == w.get():
#         score += everyone_score
#         print "right!"
#     else:
#         print "wrong!"
#     count -= 1
#     return pr

# def set_label(label):
#     global score,result,everyone_score,count
#     if result == int(w.get()):
#         score += everyone_score
#         print "right!"
#     else:
#         print "wrong!"
#     count -= 1
#     if count == 0:
#         tkMessageBox.showinfo(u'成绩',str(score)+u'分！')
#         count =10
#         score = 0
#         v.set(arithmetic_figure2())
#         w.set('')
#     else:
#         v.set(arithmetic_figure2())
#         w.set('')
# 
# def quit():
#     root.quit()
# 
# def printCoords(event):
# #     print "event.char",repr(event.char)
# #     print "event.keycode",repr(event.keycode)
#     if repr(event.keycode) == '13': #回车
#         set_label(label)
#         entry.focus_set()
# 
# root = Tkinter.Tk()
# root.title(u'算术题')
# root.withdraw()
# screen_width = root.winfo_screenwidth()
# screen_height = root.winfo_screenheight() - 100
# # root.resizable(False, False)
# # root.update_idletasks()
# # root.deiconify()
# root.geometry('%sx%s+%s+%s' % (root.winfo_width() + 200, root.winfo_height() + 80, (screen_width - root.winfo_width())/2, (screen_height - root.winfo_height())/2))
# root.deiconify()
# frame = Tkinter.Frame(root)
# frame.pack()
# v = Tkinter.StringVar()
# score = 0
# count = 10
# result = 0
# everyone_score = 100 / count
# v.set(arithmetic_figure2())
# label = Tkinter.Label(frame,textvariable = v).grid(row=0,column=0)
# w = Tkinter.StringVar()
# entry = Tkinter.Entry(frame,textvariable = w,insertbackground = 'red')
# entry.focus_set()
# entry.bind('<Key>',printCoords)
# entry.grid(row=0,column=1)
# next = Tkinter.Button(frame, text = u'下一题',command=lambda : set_label(label))
# next.bind('<Key>',printCoords)
# next.grid(row=1,column=0)
# Tkinter.Button(frame, text = u'退出',command=quit).grid(row=1,column=1)
# 
# root.mainloop()


# a = App(root,10)
# root.mainloop()
# import Tkinter
# root = Tkinter.Tk()
# root.title(u'算术题')
# root.minsize(600, 300)
# label = Tkinter.Label(root, text = arithmetic_figure2(10))
# next = Tkinter.Button(root, text = u'下一题')
# quit = Tkinter.Button(root, text = u'退出')
# result = Tkinter.Entry()
# command = root.quit()
# label.pack()
# result.pack()
# next.pack()
# quit.pack()
# Tkinter.mainloop()
# print command

'''一个使用函数装饰器的打印时间戳的例子'''
import time
def tsfunc(func):
    def wrappedFunc():
        print "[%s] %s() called" % (time.ctime(), func.__name__)
    return wrappedFunc

@tsfunc
def foo(): pass
#等价于foo = tsfunc(foo)

foo()
time.sleep(4)
for i in range(2):
    time.sleep(2)
    foo()
