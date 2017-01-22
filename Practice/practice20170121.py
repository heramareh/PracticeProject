#encoding=utf-8

import time
class Animal(object):  #类定义
    "created  by gloryroad!"
    count=0
    def __init__(self,name):
        self.name=name
        print self.name +" is created!"
        Animal.count+=1
        self.__feather=True

    def get_name(self):
        return self.name

    def set_name(self,name):
        self.name=name
    
    def get_count(self):
        return Animal.count
 

    @classmethod
    def print_doc(cls):
        return cls.__doc__

    def get_feather(self):
        #print self.__get_feather()
        return self.__feather

    def set_feather(self,value):

        if value not in [True,False]:
            print "value is not valid!"
            return
        self.__feather=value

    def __get_feather(self):
        return "feahter"

    @staticmethod
    def print_module():
        return Animal.__module__

class Cat(Animal):
    def __init__(self,age):
        Animal.__init__(self, "cat")
        self.age = age

    def get_length(self):
        return 100

# c = Cat('cat')
# print isinstance(c,Cat)
# print isinstance(c,Animal)

class Person(object):
    def __init__(self,name,sex,age):
        self.name = name
        self.sex = sex
        self.age = age

    def get_name(self):
        return self.name

    def set_name(self,name):
        self.name = name
class Student(Person):
    def __init__(self,name,sex,age,grade,number):
        super(Student,self).__init__(name, sex, age)
#         Person.__init__(self, name, sex, age)
        self.grade = grade
        self.number = number

#     def __init__(self,name,sex,age,grade,number):
#         Person.__init__(self, name, sex, age)
#         self.grade = grade
#         self.number = number

    def get_number(self):
        return self.number

    def set_number(self,number):
        self.number = number

# s1 = Student('zhangsan','m',18,2,20170001)
# print s1.get_name()
# print s1.get_number()

class Parent(object): # define parent class 
    parentAttr = 100 
    def __init__(self): 
        "父类构造方法，用于初始化工作"
        print "Calling parent constructor" 

    def parentMethod(self): 
        print 'Calling parent method' 

    def setAttr(self, attr): 
        Parent.parentAttr = attr 

    def getAttr(self): 
        print "Parent attribute :", Parent.parentAttr

class Child1(Parent): # define child1 class 
    def __init__(self): 
        "子类构造方法，用于初始化子类本身数据的工作"
        print "Calling child1 constructor" 

    def childMethod(self): 
        print 'Calling child1 method' 
        Parent.parentMethod(self) #调用基类的方法，所以要加上参数self
class Child2(Parent): # define child2 class 
    #没有实现__init__方法，则会调用基类的__init__方法
    def childMethod(self): 
        print 'Calling child2 method' 
        self.parentMethod()  #子类调用自己从父类那继承过来的父类的方法

# c1 = Child1() # 实例化子类 1
# c2 = Child2() # 实例化子类 2
# c1.childMethod() # 调用子类1的方法
# c2.childMethod() # 调用子类2的方法
# c1.parentMethod() # 子类实例对象调用父类方法
# c1.setAttr(200) # 再次调用父类的方法
# c1.getAttr() # 再次调用父类的方法

class UniversityMember(object):

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def getName(self):
        return self.name

    def getAge(self):
        return self.age

class Student1(UniversityMember):
    def __init__(self, name, age, sno, Department):
        #注意要显示调用父类构造方法，并传递参数self
        UniversityMember.__init__(self, name, age) 
        self.sno = sno
        self.Department = Department

    def getSno(self):
        return self.sno

    def getDepartment(self):
        return self.Department

# s = Student1("fosterwu", "18", "CS", 18)
# print s.name, s.age
# s.name = 'superman'
# print s.name
# print s.getName()
# print s.getAge()
# print issubclass(Student1,UniversityMember)
# print issubclass(Student,UniversityMember)

class A(object):
    def __init__(self):
        print "A constructor"
    def a_method(self):
        print "call a_method"

    def method(self):
        print "A method"

class B(A):
    def __init__(self):
        print "B constructor"
        A.__init__(self)
    def b_method(self):
        print "call b_method"

    def method(self):
        print "B method"

class C(A):
    def __init__(self):
        print "C constructor"
        A.__init__(self)
    def c_method(self):
        print "call c_method"
    
    def x(self):
        print "C method"

class D(C,B):
    def __init__(self):
        B.__init__(self)
        C.__init__(self)
    def x(self):
        print "D method"
    def d_method(self):
        print "call d_method"

# d=D()
# d.method()

class Animal1(object):

    def __init__(self, name): 
        #构造方法一个对象创建后会立即调用此方法
        self.Name = name
        print self.Name

    def accessibleMethod(self):
        #绑定方法对外公开
        print "I have a self! current name is:"
        print self.Name
        print "the secret message is:"
        self.__inaccessible()

    def __inaccessible(self):
        #私有方法对外不公开以双下划线开头
        print "U cannot see me..."

    @staticmethod
    def staticMethod():
# self.accessibleMethod() #在静态方法中无法
#直接调用实例方法直接抛出NameError异常
        print "this is a static method"
    def setName(self,name): #访问器函数
        print "setName:"
        self.Name=name

    def getName(self): #访问器函数
        print "getName:"
        return self.Name

# a = Animal1("learns")
# print a.getName()
# a.setName("sr")
# print "new name:",a.getName()
# a.staticMethod()

import os
class Person1(object):
    def __init__(self,name):
        self.Name = name
    def getName1(self):
        print 'fetch...'
        return self.Name
    def setName2(self, name):
        print 'change...'
        self.Name = name
    def delName(self):
        print 'remove...'
        del self.Name
    name = property(getName1,setName2,delName,'name property docs')
    # name=property(getName,setName)

# bob = Person1('Bob Smith')
# print bob.name #自动调用getName
# bob.name = 'Robert Smith' #自动调用setName
# print bob.name
# del bob.name #自动调用delName

class Student2(object):
    def __init__(self,score):
        self.__score = self.__set_score(score)

    @staticmethod
    def __set_score(score):
        if not isinstance(score, (int,float)):
            raise TypeError("not int or float")
        if score > 100 or score < 0:
            raise ValueError("> 100 or < 0")
        return score

    def set_score(self, score):
        self.__score = self.__set_score(score)

    def get_score(self):
        return self.__score

# s1 = Student2(100)
# print s1.get_score()
# s1.set_score(50)
# print s1.get_score()

class Animal2:
    def tell(self):
        print "animal tells!"


class Cat2(Animal2):
    def tell(self):
        print "cat tells!"

class ChinaCat(Cat2):
    def tell(self):
        print "ChinaCat tells!"

def voice(x):
    print "animal voice:",
    x.tell()

# a=Animal2()
# c=Cat2()
# cc=ChinaCat()
# for obj in [a,c,cc]:
#     voice(obj)

class Vector(object) :
    def __init__(self, a, b) :
        self.a = a
        self.b = b
    def __str__(self): 
        return 'Vector (%d, %d)' % (self.a, self.b)
    def __add__(self,other) :
        return Vector(self.a + other.a, self.b + other.b)

# x =  Vector(3,7)
# y =  Vector(1, -10)
# print x + y #相当于 x.__add__(y)
# print x.__add__(y)
# print str(x)
# print x

'''运算符重写'''
class Student3(object):
    def __init__(self,name,score):
        self.name = name
        self.score = score

    def __add__(self,other):
        print "__add__:",
        return (self.score + other.score)/2

    def __sub__(self,other):
        print "__sub__:",
        return self.score - other.score

    def __mul__(self,other):
        print "__mul__:",
        return self.score * other.score

    def __div__(self,other):
        print "__div__:",
        return self.score / other.score

    def __ne__(self,other):
        print "__ne__:",
        return self.score != other.score

    def __eq__(self,other):
        print "__eq__:",
        return self.score == other.score

    def __gt__(self,other):
        print "__gt__:",
        return self.score > other.score

    def __lt__(self,other):
        print "__lt__:",
        return self.score < other.score

    def __ge__(self,other):
        print "__ge__:",
        return self.score >= other.score

    def __le__(self,other):
        print "__le__:",
        return self.score <= other.score

# s1 = Student3('zhangsan',80)
# s2 = Student3('lisi',70)
# print s1+s2
# print s1-s2
# print s1*s2
# print s1/s2
# print s1 != s2
# print s1 == s2
# print s1 > s2
# print s1 < s2
# print s1 >= s2
# print s1 <= s2

'''14 、 按如下规律打印列表
1 [1*, 2, 3, 4, 5]
2 [1, 2*, 3, 4, 5]
3 [1, 2, 3*, 4, 5]
4 [2, 3, 4*, 5, 6]
5 [3, 4, 5*, 6, 7]
6 [4, 5, 6*, 7, 8]
...
20 [16, 17, 18, 19, 20*]'''
def print_list(lines):
    for i in range(2):
        number_list = range(1,6)
        number_list[i] = str(number_list[i])+'*'
        print i+1,number_list
    for i in range(3,lines-1):
        number_list = range(i-2,i+3)
        number_list[2] = str(number_list[2])+'*'
        print i,number_list
    for i in range(2):
        number_list = range(lines-4,lines+1)
        number_list[-2+i] = str(number_list[-2+i])+'*'
        print lines-1+i,number_list

print_list(20)

'''15、写一个函数, 将驼峰命名法字符串转成下划线命名字符串，如GetItem -
> get_item，getItem -> get_item。'''
import string
def rename(name):
    new_name = [name[0].lower()]
    for i in name[1:]:
        if  i in string.uppercase:
            new_name.append('_'+i.lower())
            continue
        new_name.append(i)
    return ''.join(new_name)

# print rename("GetItem")
# print rename("getItem")

