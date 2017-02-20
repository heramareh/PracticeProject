#encoding=utf-8

import re

# def re_str(r, str):
#     result = re.search(r,str)
#     if result:
#         print u"找到了：",result.group()
#     else:
#         print u"没找到"
# 
# re_str('[0-9]{5}','1fe4253443wfe')

def re_str(s):
    result=re.search(r'\D\d{5}\D|^\d{5}\D|\D\d{5}$|^\d{5}$',s)
    if result:
        word_list=[]
        for s in result.group():
            if s in "0123456789": 
                word_list.append(s)
        return "".join(word_list)

    else:
        return None

def test_re_str(s,expect_result):
    for i in range(len(s)):
        print 's:',s[i]
        print 'expect_result:',expect_result[i]
        export_result = re_str(s[i])
        print 'export_result:',export_result
        if export_result == expect_result[i]:
            print "right!"
        else:
            print "wrong!"
    print "done!"
# if __name__ == '__main__':
# #     s = ['12345','1234','123456','a12345','a123456','a1234','12345a','1234a','123456a','a12345a','a1234a','a123456a']
# #     expect_result = ['12345',None,None,'12345',None,None,'12345',None,None,'12345',None,None]
# #     test_re_str(s,expect_result)
# #     s = ['1234','123456','a123456','123456a','a123b456a']
#     fp = open('d:\\test\\test.txt')
#     for eachLine in fp:
#         assert re_str(eachLine) == None
#     fp.close()
#     print "completed!"

# # 将正则表达式编译成Pattern对象
# p = re.compile(r'(\w+) (\w+)(?P<sign>.*)', re.DOTALL)
# 
# #获取编译时用的匹配模式
# print "p.flags: ", p.flags
# 
# #获取表达式中分组的数量
# print "p.groups: ", p.groups
# 
# #获取表达式中所有分组的别名和分组序号组成的字典
# print "p.groupindex: ", p.groupindex

# #匹配字符串中所有连续字母组成的子串
# for i in re.finditer(r'[A-Za-z]+','one12two34three56four') :
#     print i.group(),
    
p = re.compile(r'(\w+) (\w+)')
s = 'i say, hello world!'
#\2, \1表示分组引用，分别代表第二个分组，第一个分组
print p.sub(r'\2 \1', s)

#当repl为方法时，将匹配的结果m传入方法
def func(m):
    print m.group()
    return m.group(1).title() + ' ' + m.group(2).title()

print p.sub(func, s)