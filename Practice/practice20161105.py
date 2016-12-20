#encoding=utf-8

'''1.使用尽可能多的方法实现list去重'''
# #方法一：
# la=[1,1,2,3,'a','a','a']
# lb=[]
# for i in la:
#     if i not in lb:
#         lb.append(i)
# print lb
# 
# #方法二：
# la=[1,1,2,3,'a','a','a']
# print list(set(la))
# 
# #方法三：
# la=[1,1,1,1,2,3,'a','a','a','a','a']
# for i in la[:-1]:
#     if i in la[la.index(i)+1:]:
#         la.remove(i)
# print la
# 
# #方法四：
# la=[1,1,2,3,'a','a','a']
# 
# for i in la:
#     if la.count(i) > 1:
#         la.remove(i)
# print la
# 
# #方法五：
# la=[1,1,2,3,'a','a','a']
# 
# dict1 = dict.fromkeys(la,0)
# la = dict1.keys()
# print la

'''2.成绩等级判断
利用条件运算符的嵌套来完成此题：学习成绩>=90分的同学用A表示，
60-89分之间的用B表示，60分以下的用C表示
'''
# import string
# 
# while True:
#     flag = False
#     score=raw_input('请输入分数[0-100]（输入“退出”则退出程序）：'.decode('utf-8').encode('gbk'))
#     if score == '':
#         continue
#     if score == '退出'.decode('utf-8').encode('gbk'):
#         print u'退出程序。'
#         break
#     for i in score:
#         if i not in string.digits:
#             print u'输入有误，请重新输入。'
#             flag = True
#             break
#         else:
#             continue
#     if(flag):
#         continue
#     if len(score) > 3:
#         print u'输入有误，请重新输入。'
#     elif len(score) == 3:
#         if int(score) != 100:
#             print u'输入有误，请重新输入。'
#         else:
#             print 'A'
#     elif len(score) == 2:
#         if int(score) >= 90:
#             print 'A'
#         elif int(score) >= 60:
#             print 'B'
#         elif int(score) >= 10:
#             print 'C'
#         else:
#             print u'输入有误，请重新输入。'
#             continue
#     elif int(score) >= 0 and len(score) == 1:
#         print 'C'
#     else:
#         print u'输入有误，请重新输入。'

'''3.实现数学中多项式求和公式的打印
比如：a6x^6 + a5x^5 + a4x^4 + a3x^3 + a2x^2 + a1x^1 + a0
'''
def multinomial(a, n, x) :
    mathStr = ''
    i = n
    while i >= 0 :
        if i == 0 :
            mathStr += a + "0"
        else :
            mathStr += a + str(i) + x + "^" + str(i) + " + " 
        i -= 1
    return mathStr

# print multinomial('a', 8, 'x') 

'''4.统计名字列表中，各名字的首字母在名字列表中出现的次数'''
# name_list = ["python","java","PHP","Android","ios","C","Groad","Javascript","Html","TCP","IP"]
# # method1
# firstName_str = ''
# for eachName in name_list:
#     firstName_str += eachName[0]
# firstName_str = firstName_str.upper()
# firstName_list = list(set(firstName_str))
# name_str = ''.join(name_list)
# name_str = name_str.upper()
# 
# print name_list
# 
# #method2
# for firstName in firstName_list:
#     count = 0
#     for name_str_char in name_str:
#         if firstName == name_str_char:
#             count += 1
#         else:
#             continue
# print firstName + ' appear '+ str(count) + ' times.'
# 
# #method3
# def char_Calc(listWord) :
#   dictChar = {}
#   #判断首字母是否在字典中存在，如存在value+1，不存在将value=1
#   for i in listWord :
#     if dictChar.has_key(i[0]) :
#       dictChar[i[0]] += 1
#     else :
#       dictChar[i[0]] = 1
#   return dictChar
# 
# name=['foster','foe','lily','mickel','live','moon','ruby','cindy','miya']
# dictStatistics = char_Calc(name)
# for i, j in dictStatistics.items() :
#   print u"姓名以字母 %s 开头的有 : %d人" %(i,j)

'''5.输入三个数，判断是否能构成三角形
能构成三角形三边关系：
三边都大于零
两边之和大于第三边，两边之差小于第三边
'''
# numbers_list = []
# flag = True
# try:
#     for i in xrange(3):
#         num = float(raw_input('请输入第 '.decode('utf-8').encode('gbk') + str(i+1) +' 个数：'.decode('utf-8').encode('gbk')))
#         if num <= 0:
#             print u'边长小于等于0，不能构成三角形'
#             flag = False
#             break
#         else:
#             numbers_list.append(num)
#     if flag:
#         numbers_list.sort()
#         if numbers_list[0] + numbers_list[1] > numbers_list[2]:
#             print u'能构成三角形'
#         else:
#             print u'不能构成三角形'
# except Exception, e:
# print u'输入有误'

'''6.实现字典的fromkeys方法
例如：
seq = ('name', 'age', 'sex')
dict = dict.fromkeys(seq, 10)
print "New Dictionary : %s" % str(dict)
结果：New Dictionary : {'age': 10, 'name': 10, 'sex': 10}
'''
def fromkeys(keys,value=None):
    dict1 = {}
    for i in keys:
        if dict1.has_key(i):
            continue
        else:
            dict1[i]=value
    return dict1

def haskey(dict1,key):
    la = dict1.keys()
    if key in la:
        return True
    else:
        return False

# la = [1,2,3,4,3,2,'a','a','bds','fd']
# print fromkeys(la)
# print fromkeys(la,0)
# print haskey(fromkeys(la),6)

'''7.键盘读入一字符串，逆序输出'''
# #method1
# s = raw_input('input a string: ')
# print s[::-1]

# #method2
# s = raw_input('input a string: ')
# la = list(s)
# la.reverse()
# print ''.join(la)

#method3
def reverse_recursion(s):
  if len(s) == 1:
    return s
  else:
    return reverse_recursion(s[1:]) + reverse_recursion(s[0])

# s = "abcdesd"
# print reverse_recursion(s)

'''8.读入一个整数n，输出n的阶乘'''
def factorial(number):
    if number == 1 or number == 0:
        return 1
    if number > 0:
        return number * factorial(number - 1)


# while True:
#     num = int(raw_input('input a number: '))
#     if num < 0:
#         print 'input error'
#         continue
#     else:
#         print '%d! = ' %num,factorial(num)
#         break

'''9.打印1/2, 1/3, 1/4,….1/10'''
# num = int(raw_input('输入一个非负整数：'.decode('utf-8').encode('gbk')))
# if num <= 0:
#     print u'输入有误！'
# else:
#     for i in xrange(2,num+1):
#         if i == num:
#             print '1/'+str(i)
#         else:
#             print '1/'+str(i)+',',

'''10.写一个函数实现一个数学公式'''
def sqrt(x,y):
    z = 1
    for i in xrange(y):
        z *= x
    return z

# print sqrt(2,3)

'''11.输入数字a，n，如a，4，则打印a+aa+aaa+aaaa之和'''
# a=3
# n=4
# sum = 0
# for i in range(1,n+1):
#     print int(str(a)*i)
#     sum += int(str(a)*i)
# print sum

'''12.求100个随机数之和，随机数要求为0—9的整数'''
# import random
# sum = 0
# for i in xrange(100):
#     num = random.randint(0,9)
#     sum += num
# 
# print sum

'''13.要求在屏幕上分别显求1到100之间奇数之和与偶数之和'''
# import random
# sum_jishu = 0
# sum_oushu = 0
# for i in xrange(1,101):
#     if i%2 == 0:
#         sum_oushu += i
#     else:
#         sum_jishu += i
# 
# print u'奇数和：',sum_jishu
# print u'偶数和：',sum_oushu
# 
# print sum(range(1,100,2))
# print sum(range(2,101,2))

'''14.输入10个数，并显示最大的数与最小的数'''
# str = raw_input('输入10个数以逗号隔开：'.decode('utf-8').encode('gbk'))
# la = str.split(',')
# print la
# for i in range(len(la)-1):
#     for j in range(len(la)-1-i):
#         if la[j]>la[j+1]:
#             la[j],la[j+1] = la[j+1],la[j]
# print u'最大值：',la[len(la)-1]
# print u'最小值：',la[0]

'''15.给一个不多于5位的正整数，要求：一、求它是几位数，二、逆序打印出
各位数字。
'''
# num = int(raw_input('输入一个不多于5位的正整数：'.decode('utf-8').encode('gbk')))
# print u'数字%d是%d位数' %(num,len(str(num)))
# print u'逆序输出结果：',str(num)[::-1]

'''16.求所有的水仙花数'''

'''17.编程求s=1!+2!+3!+…..+n!'''
# num = int(raw_input('输入一个非负整数：'.decode('utf-8').encode('gbk')))
# if num < 0:
#     print u'输入有误！'
# elif num == 0 or num == 1:
#     print u'%d的阶乘：%d' %(num, 1)
# else:
# print u'%d的阶乘：%d' %(num, reduce(lambda x,y:x*y,xrange(1,num+1)))

'''18.钞票换硬币
把一元钞票换成一分、二分、五分硬币（每种至少一枚），有多种换法，分
别有哪些？
'''
# # 1分
# penny = 1
# # 2分
# twoPenny = 2
# # 5分
# fivePenny = 5
# # 一元等于100分
# smacker = 100
# total = 0
# print "1分\t2分\t5分"
# '''
#   1、2、5分币至少都要有一个，100 - 1 - 2 -5 = 92
#   剩下的换法只能在92分中进行分配，
#   如果全是1分最多有92个
#   如果全为2分的话，最多有42个
#   但不可能全为5分，因为92不能被5整除，所以5分最多的只能是18个，
#   由此出现了下列循环区间数
# '''
# for p in range(93):
#   for t in range(47):
#     for f in range(19):
#       if p + t * twoPenny + f * fivePenny + penny + twoPenny + fivePenny == smacker:
#         print str(p+1) + '\t' + str(t+1) + "\t" + str(f+1)
#         total += 1
# print u"总共有%d种换法。" %total

'''19.自己实现在一句话中查找某个单词的算法，存在返回索引号，否则返回False'''
# import re
# str = raw_input('输入一段英文：'.decode('utf-8').encode('gbk'))
# word = raw_input('输入要查找的单词：'.decode('utf-8').encode('gbk'))
# word_list = re.findall('[a-zA-z]',str)
# print word_list
# if word in word_list:
#     print word_list.index(word)
# else:
#     print 'False'

'''20.读入一个十进制整数，实现十进制转二进制算法将其转成二进制数
要求：不能使用现成进制转换函数，自己写代码实现
'''
def my_bin(num):
    u'''十进制转二进制'''
    la = []
    if num < 0:
        return '-'+my_bin(abs(num))
    while True:
        if num == 0:
            return ''.join(la[::-1])
        num, remainder = divmod(num,2)
        la.append(str(remainder))

# print my_bin(13)
# print my_bin(0)
# print my_bin(-13)
