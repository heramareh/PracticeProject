# encoding=utf-8

# def my_bin(num):
#     u'''十进制转二进制'''
#     la = []
#     if num < 0:
#         return '-' + my_bin(abs(num))
#     while True:
#         num, remainder = divmod(num, 2)
#         la.append(str(remainder))
#         if num == 0:
#             return ''.join(la[::-1])
# 
# print my_bin(5)
# print my_bin(0)
# print my_bin(-5)

# all_list = [1,2]
# for index in xrange(2,21):
#     all_list.insert(index, all_list[index-1]+all_list[index-2])
# print sum(map(lambda x,y:float(x)/y,all_list[1:],all_list[:-1]))

# print '   *'
# print '  *'+' *'*1
# print ' *'+' *'*2
# print '*'+' *'*3

# def draw_solid_right_triangle(length):
#     """draw a solid right triangle"""
#     for i in xrange(1,length+1):
#         print '* '*i
# 
# def draw_hollow_right_triangle(length):
#     """draw a hollow right triangle"""
#     for i in xrange(1,length+1):
#         if i == 1:
#             print '*'
#         elif i == length:
#             print '* '*i
#         else:
#             print "*"+" "*(2*i-3)+"*"
# 
# draw_solid_right_triangle(6)
# 
# draw_hollow_right_triangle(6)


#    * * * *
#   * * *
#  *
#  *
#   * * *
#    * * * *

# def draw_letter_C(size):
#     """draw a letter C"""
#     for i in xrange(size,0,-1):
#         if i == size:
#             print ' '*i+'*'+' *'*i
#         else:
#             print ' '*i+'*'
#     for i in xrange(1,size+1):
#         if i == size:
#             print ' '*i+'*'+' *'*i
#         else:
#             print ' '*i+'*'
# draw_letter_C(3)
# draw_letter_C(2)
# draw_letter_C(5)

# *       *
# * *   * *
# * * * * *
# * *   * *
# *       *

# def draw_letter_N(size):
#     """draw a letter N"""
#     n = 2*size-3
#     for i in xrange(1,size+1):
#         m = 2*i-3
#         if i == 1 or i == size:
#             print '*'+' '*n+'*'
#         else:
#             print "*"+" "*m+"*"+" "*(n-m-1)+"*"
# 
# draw_letter_N(5)
# draw_letter_N(4)
# draw_letter_N(3)
# draw_letter_N(2)
# draw_letter_N(1)

# *   *
# * * *
# *   *
# 
# *     *
# *     *
# * * * *
# *     *
# *     *
# 
# *       *
# *       *
# *       *
# * * * * *
# *       *
# *       *
# *       *

# 3 1  5 2  7 3  9 4  
# def draw_letter_H(size):
#     if size % 2 == 0:
#         print u"请输入一个奇数"
#     else:
#         for i in xrange(1,size+1):
#             if i == (size+1)/2:
#                 print " ".join("*"*((size-1)/2+2))
#             else:
#                 print "*"+" "*size+"*"
# 
# draw_letter_H(3)
# draw_letter_H(4)
# draw_letter_H(5)
# draw_letter_H(9)

# import string
# 
# def my_factorial(num):
#     if num == 0:
#         return 1
#     else:
#         return reduce(lambda x,y:x*y,range(1,num+1),1)
# 
# def C(n, m):
#     return my_factorial(n) / (my_factorial(n - m) * my_factorial(m))
# 
# def draw_triangle(rows):
#     if rows == 1:
#         print "%d: " %1,
#         print 1
#     # last row
#     listb = []
#     for j in xrange(0,rows):
#         listb.append(str(C(rows-1,j)))
#     s = ' '.join(listb)
#     length = len(s)
#     for row in xrange(1,rows):
#         if row == 1:
#             print "%d: " %row,
#             print string.center("1",length)
#         if row == rows-1:
#             print "%d: " %(row+1),
#             print s
#         else:
#             lista = []
#             for j in xrange(0,row+1):
#                 lista.append(str(C(row,j)))
#             print "%d: " %(row+1),
#             print string.center(' '.join(lista),length)
# 
# draw_triangle(1)
# draw_triangle(2)
# draw_triangle(3)
# draw_triangle(5)
# draw_triangle(10)
# draw_triangle(15)
