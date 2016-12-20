#encoding=utf-8

'''1. 输入1-127的ascii码并输出对应字符'''
# try:
#     num = int(raw_input("Please input a number(1-127):"))
#     if num >= 1 and num <=127:
#         print num,':',chr(num)
#     else:
#         print 'error!'
# except Exception, e:
#     print 'error!'

'''2. 输入a，b，c，d4个整数，计算a+b-c*d的结果'''
# try:
#     a = float(raw_input("Please input number a: "))
#     b = float(raw_input("Please input number b: "))
#     c = float(raw_input("Please input number c: "))
#     d = float(raw_input("Please input number d: "))
#     print "a+b-c*d = %.2f" %(a+b-c*d)
# except Exception, e:
#     print 'error!'

'''3. 计算一周有多少分钟、多少秒钟'''
# print u'一周有 %d 分钟' %(7*24*60)
# print u'一周有 %d 秒' %(7*24*60*60)

'''4. 3个人在餐厅吃饭，想分摊饭费。总共花费35.27美元，他们还想给15%的小费。每个人该怎么付钱，'''
# print '%.2f' %((35.27+35.27*0.15)/3)

'''5. 计算一个12.5m X 16.7m的矩形房间的面积和周长'''
# print u'面积：%.2f' %(12.5*16.7)
# print u'周长：%.2f' %(2*(12.5+16.7))

'''6. 怎么得到9 / 2的小数结果'''
# 9.0/2
# float(9)/2

'''7. python计算中7 * 7 *7 * 7，可以有多少种写法'''
# 7*7*7*7
# 7**4
# import math
# math.pow(7,4)

'''8. 写程序将温度从华氏温度转换为摄氏温度。转换公式为C = 5 / 9*(F - 32)'''
# try:
#     F = float(raw_input('输入一个华氏温度：'.decode('utf-8').encode('gbk')))
#     print u'华氏温度 %.2f 转换为摄氏温度为：%.2f' %(F,(5/9.0*(F-32)))
# except Exception, e:
#     print u'输入有误！'

'''9. 一家商场在降价促销。如果购买金额50-100元（包含50元和100元）之间，会给10%的折扣，如果
购买金额大于100元会给20%折扣。编写一程序，询问购买价格，再显示出折扣（10%或20%）和
最终价格。
'''
# try:
#     price = int(raw_input('购买价格为：'.decode('utf-8').encode('gbk')))
#     if price <=0:
#         print u'输入有误！'
#     elif price>=50 and price<=100:
#         print u'折扣10%，',
#         print u'最终价格：%.1f' %(price-price*0.1)
#     elif price>100:
#         print u'折扣20%，',
#         print u'最终价格：%.1f' %(price-price*0.2)
#     else:
#         print u'没有折扣，',
#         print u'最终价格：%d' %(price)
# except Exception, e:
#     print u'输入有误！'

'''10. 判断一个数n能否同时被3和5整除'''
# try:
#     n = int(raw_input('n = '))
#     if n % 15 == 0:
#         print u'%d ：能同时被3和5整除。' % n
#     else:
#         print u'%d ：不能同时被3和5整除。' % n                                                 
# except Exception, e:
#     print u'输入有误！'

'''11. 求1 + 2 + 3 +….+100'''
# sum = 0
# for i in xrange(1,101):
#     sum += i
# print sum

'''12交换两个变量的值'''
# 方法一：
# a,b = b,a
# 方法二：
# temp = a
# a = b
# b = temp

'''13一个足球队在寻找年龄在10到12岁的小女孩（包括10岁和12岁）加入。编写一个程序，询问用户的性别（m表示男性，
f表示女性）和年龄，然后显示一条消息指出这个人是否可以加入球队，询问10次后，输出满足条件的总人数。
'''
# sum = 0
# for i in xrange(10):
#     sex = raw_input('sex: ')
#     age = int(raw_input('age: '))
#     if sex == 'f' and age >=10 and age <=12:
#         sum += 1
#         print 'OK'
#     else:
#         print 'NG'
# print 'sum =',sum

'''14 长途旅行中，刚到一个加油站，距下一个加油站还有200km，而且以后每个加油站之间距离都是200km。编写一个程
序确定是不是需要在这里加油，还是可以等到接下来的第几个加油站再加油。
程序询问以下几个问题：
1）你车的油箱多大，单位升
2）目前油箱还剩多少油，按百分比算，比如一半就是0.5
3）你车每升油可以走多远（km）
提示：
油箱中包含5升的缓冲油，以防油表不准。
'''
# try:
#     cont = float(raw_input('你车的邮箱多大，单位升：'.decode('utf-8').encode('gbk')))
#     remain = float(raw_input('目前邮箱还剩多少油（按百分比算，比如一半就是0.5）：'.decode('utf-8').encode('gbk')))
#     distance = int(raw_input('你车每升油可以走多远（km）'.decode('utf-8').encode('gbk')))
#     if cont <= 0 or remain < 0 or remain > 1 or distance <= 0:
#         print u'输入有误！'
#     else:
#         if ((cont*remain+5)*distance) < 200:
#             print u'需要在这里加油！'
#         else:
#             print u'可以到第 %d 个加油站再加油。' % (((cont*remain+5)*distance)//200)
# except Exception, e:
#     print u'输入有误！'

'''15 现有面包、热狗、番茄酱、芥末酱以及洋葱，数字显示有多少种订购组合，其中面包必订，0不订，1订，比如10000，
表示只订购面包
'''
# for i in range(2**4):
#     la = ['1','0','0','0','0']
#     n = 4
#     while 1:
#         la[n] = str(i % 2)
#         i=i / 2
#         n -= 1
#         if i == 0:
#             break
#     print ''.join(la)

'''16 基于上题：给出每种食物的卡路里（自定义），再计算出每种组合总共的卡路里'''
# lb = [20,30,40,50,60]
# for i in range(2**4):
#     la = ['1','0','0','0','0']
#     n = 4
#     while 1:
#         la[n] = str(i % 2)
#         i=i / 2
#         n -= 1
#         if i == 0:
#             break
#     sum = 0
#     for j in range(5):
#         sum += int(la[j])*lb[j]
#     print ''.join(la),
#     print u'卡路里共计：',sum

'''17输入5个名字，排序后输出'''
# la = []
# for i in range(5):
#     print u'请输入第',i+1,
#     name = raw_input('个名字：'.decode('utf-8').encode('gbk'))
#     la.append(name)
# la.sort()
# print u'排序后：',la

'''18实现一个简单的单词本
功能：
可以添加单词和词义，当所添加的单词已存在，让用户知道；
可以查找单词，当查找的单词不存在时，让用户知道；
可以删除单词，当删除的单词不存在时，让用户知道；
以上功能可以无限制操作，直到用户输入bye退出程序。
'''
# wordBooks = {}
# while True:
#     try:
#         content = raw_input('请选择要做的操作：'.decode('utf-8').encode('gbk')).strip()
#         if content == 'bye':
#             print u'退出程序！'
#             break
#         elif content == 'find':
#             if len(wordBooks.keys()) == 0:
#                 print u'当前单词本中没有单词。'
#                 continue
#             word = raw_input('请输入要查找的单词：'.decode('utf-8').encode('gbk')).strip()
#             if word == '':
#                 print u'输入有误'
#                 continue
#             elif word not in wordBooks.keys():
#                 print u'当前查找的单词不存在。'
#             else:
#                 print word,':',wordBooks[word]
#         elif content == 'del':
#             if len(wordBooks.keys()) == 0:
#                 print u'当前单词本中没有单词。'
#                 continue
#             word = raw_input('请输入要删除的单词：'.decode('utf-8').encode('gbk')).strip()
#             if word == '':
#                 print u'输入有误'
#                 continue
#             elif word not in wordBooks.keys():
#                 print u'当前删除的单词不存在。'
#             else:
#                 del wordBooks[word]
#                 print u'删除成功！'
#         elif content == 'add':
#             word = raw_input('请输入要添加的单词：'.decode('utf-8').encode('gbk')).strip()
#             if word == '':
#                 print u'输入有误'
#                 continue
#             elif word not in wordBooks.keys():
#                 meaning = raw_input('请输入要添加的词义：'.decode('utf-8').encode('gbk')).strip()
#                 if word == '':
#                     print u'输入有误'
#                     continue
#                 else:
#                     wordBooks[word] = meaning
#                     print u'添加成功！'
#             else:
#                 print u'当前所添加的单词已存在。'
#         elif content == 'count':
#             if len(wordBooks.keys()) == 0:
#                 print u'当前单词本中没有单词。'
#                 continue
#             else:
#                 la = wordBooks.keys()
#                 la.sort()
#                 for k in la:
#                     print k,':',wordBooks[k]
#         else:
#             print u'输入有误'
#     except Exception, e:
#         print u'输入有误'

'''19输入一个正整数，输出其阶乘结果'''
# try:
#     num = int(raw_input('请出入一个正整数：'.decode('utf-8').encode('gbk')))
#     if num <= 0:
#         print u'输入有误！'
#     elif num == 1:
#         print u'1 的阶乘是：1'
#     else:
#         result = 1
#         for i in range(1,num+1):
#             result = i*result
#         print num,u'的阶乘是:',result
# except Exception, e:
#     print u'输入有误！'

'''20  计算存款利息
4种方法可选：
活期，年利率为r1；
一年期定息，年利率为r2；
存两次半年期定期，年利率为r3
两年期定息，年利率为r4
现有本金1000元，请分别计算出一年后按4种方法所得到的本息和。
提示：本息= 本金+ 本金* 年利率* 存款期
'''
# print '活期：本息 =', 1000 + 1000 * r1*1
# print '一年期定息：本息 =', 1000 + 1000 * r2*1
# print '两年半期定息：本息 =', 1000 + 1000 * r3*1
# print '两年期定息：本息 =', 1000 + 1000 * r4*2

'''21输入3个数字，以逗号隔开，输出其中最大的数'''
# lt = []
# str = raw_input('输入三个数字，以逗号隔开'.decode('utf-8').encode('gbk'))
# for i in str:
#     try:
#         lt.append(int(i))
#     except Exception, e:
#         continue
# lt.sort()
# lt.reverse()
# print u'最大数为：',lt[0]

'''22输入一个年份，输出是否为闰年
是闰年的条件：
能被4整数但不能被100整除，或者能被400整除的年份都是闰年。
'''
# while True:
#     try:
#         year = raw_input("请出入一个年份(输入“退出”则退出程序)：".decode("utf-8").encode("gbk"))
#         if year == "退出".decode("utf-8").encode("gbk"):
#             print u"退出程序！"
#             break
#         y = int(year)
#         if (((y % 4 == 0) and (y % 100 != 0)) or (y % 400 == 0)) and (y > 0):
#             print year + u"年是闰年。"
#         elif y > 0:
#             print year + u"年不是闰年。"
#         else:
#             print u"输入有误。"
#     except Exception,e:
#             print u"输入有误。"

'''23求两个正整数m和n的最大公约数'''
def gcd(num1, num2):
    if num1 % num2 == 0:
        return num2
    else:
        return gcd(num2, num1%num2)

# print gcd(8, 12)
