#encoding=utf-8

'''小练习：统计一下一个英文句子中，出现的字母个数'''
def count_alpha(s):
    result = dict.fromkeys(s,0)
    for i in result.keys():
        if not i.isalpha():
            del result[i]
        else:
            result[i]=s.count(i)
    return result
 
# print count_alpha("aa.bbC,CDD 's.")

'''
循环打印a-z 100次，格式如下：
1 a
2 b
...
将结果写入文件中

'''
import string
import os
def write_num_letter_in_file_method1(filename,lines):
    line = os.linesep
    fp = open(filename,'w')
    lower_letters = string.lowercase
    for i in xrange(1,lines+1):
        fp.write(str(i)+" "+lower_letters[0]+line)
        lower_letters = lower_letters[1:]
        if len(lower_letters) == 0:
            lower_letters = string.lowercase
    fp.close()
 
def write_num_letter_in_file_method2(filename,lines):
    line = os.linesep
    fp = open(filename,'w')
    for i in xrange(lines):
        fp.write(str(i+1)+" "+chr(i%26+97)+os.linesep)
    fp.close()
 
def write_num_letter_in_file_method3(filename,lines):
    fp=open(filename,"w")
    ascii_code=97
    for i in range(1,lines+1):
       if ascii_code<=122:
           fp.write(str(i)+" "+chr(ascii_code)+"\n") #1 a
           ascii_code+=1  #+1来实现写后续的字母
       else:
           ascii_code=97
           fp.write(str(i)+" "+chr(ascii_code)+"\n")
           ascii_code+=1
    fp.flush()  #将写入文件的内容从内存中强制写入到文件中
    fp.close()
 
# filename = "D:\\test.txt"
# lines = 120
# write_num_letter_in_file_method1(filename,lines)
# fp = open("d:\\ttttt.txt",'r+')
# fp.write("123hello world!\n")
# fp.close()
# fp = open("d:\\ttttt.txt",'r')
# print fp.read()
# fp.close()

'''练习r+ a+ w+三种操作'''
def read_add(filename):
    fp = open(filename, "r+")
    fp.write("hello world!\n")
    fp.write("test!!!\n")
    fp.seek(0,0)
    print fp.read()
    print fp.tell()
    fp.close()
     
def append_add(filename):
    fp = open(filename, "a+")
    fp.write("hello world!\n")
    fp.write("test!!!\n")
    print fp.tell()
    fp.seek(0,0)
    fp.write("test!!!\n")
    fp.seek(0,0)
    print fp.read(),
    fp.close()
 
def write_add(filename):
    fp = open(filename, "w+")
    fp.write("hello world!\nhello python!\n")
    fp.write("test!!!\n")
    fp.seek(0,0)
    fp.write("test!!!\n")
    fp.seek(0,0)
    print fp.read(),
    print fp.tell()
    fp.close()

# for i in ["d:\\ra.txt","d:\\aa.txt","d:\\wa.txt"]:
#     fp = open(i,'w')
#     fp.write("world!\npython!\ntest!!!\n")
#     fp.close()
# 
# read_add("d:\\ra.txt")
# print "*"*20
# append_add("d:\\aa.txt")
# print "*"*20
# write_add("d:\\wa.txt")

# fp = open("d:\\wa.txt",'r')
# print fp.readlines(),
# print fp.readline()
# fp.close()

'''读取文件指定行的内容'''
def read_line(filename,line):
    try:
        fp = open(filename,'r')
        row = 1
        for eachLine in fp:
            if line == row:
                fp.close()
                return eachLine
            else:
                row += 1
        fp.close()
        return "exceed the file line!"
    except Exception,e:
        return "file does not exist!"
 
# print read_line("d:\\wa.txt",4)
# 
# import chardet
# fp=open("d:\\wa.txt","r")
# file_content=fp.read()
# print chardet.detect(file_content)
# print file_content.decode("utf-8").encode("gbk","ignore")  # ignore：忽略掉那些无法编码和解码的字符,避免报错
# print file_content.decode("gbk").encode("utf-8", "ignore")
# fp.close()

'''自定义with方法'''
class Sample:
    def __enter__(self):
        print "In __enter__()"
        return "Foo"
 
    def __exit__(self, type,value, trace):
        print "In __exit__()"
 
def get_sample():
    return Sample()
 
with get_sample() as sample:
    print "sample:",sample

'''获取文件对象的各种信息：'''
# fp = open( "c:\\tuan.txt",'wb+')  
# fp.close()
# print u"文件是否关闭：", fp.closed
# print u"文件的访问模式：", fp.mode
# print u"文件名称：", fp.name
# print u"末尾是否强制加空格：", fp.softspace

# testList = ['abcede\n', '123\n', 'this is a test', '文件操作']
# #打开文件准备写文件
# fp = open( "c:\\test.txt",'w')  
# #将列表testList所有内容一次全部写入文件
# fp.writelines( testList )

# fp = open( "c:\\test.txt",'r')  
# print fp.fileno()
# #关闭文件
# fp.close()
# 
# fp = open( "c:\\test.txt",'r')  
# print fp.isatty()
# #关闭文件
# fp.close()

'''linecache.getlines方法'''
# import linecache
# file_content= a=linecache.getlines('d:\\wa.txt')
# print file_content
# file_content =linecache.getlines('d:\\wa.txt')[0:4]
# print file_content
# file_content =linecache.getline('d:\\wa.txt',2)
# print file_content
# file_content =linecache.updatecache('d:\\wa.txt')
# print file_content
# #更新缓存
# linecache.checkcache('d:\\wa.txt')
# #清理缓存
# linecache.clearcache()

'''删除空行'''
# fp = open('d:\\wa.txt')
# aList = []
# for item in fp:
#     if item.strip():
#         aList.append(item)
# fp.close()
# fp = open('d:\\wa2.txt','w')
# fp.writelines(aList)
# fp.close()

'''练习题1：同时读写文件'''
def read_and_write_file_by_w_add(filename,data):
    try:
        fp = open(filename,'w+') #以w+方式打开文件
        for i in data: #遍历列表，将每个元素写入文件
            fp.write(i)
        fp.seek(0.0) #把游标重置到文件开头
        result = fp.read() #读取文件所有内容为一个字符串
        fp.close() #关闭文件
        return result
    except Exception,e:
        return "file path not exist"
 
def read_and_write_file_by_r_add(filename,data):
    try:
        fp = open(filename,'r+')
        for line in fp:
            print line,
        print "*"*20
        fp.seek(0,2) #将游标指向文件结尾
        fp.writelines(data) #将列表内容一次性写入文件
        fp.seek(0,0)
        print "update after:"
        print "*"*20
        print fp.read()
        fp.close()
    except Exception,e:
        print "file not exist"
 
import linecache
def read_and_write_file_by_a_add(filename,data):
    try:
        with open(filename,'a+') as fp:
            old_data = fp.readlines() #将文件内容按行读取存入列表中
            print "-"*10,"old_data","-"*10,"\n",''.join(old_data),"-"*30,"\n"
            index = fp.tell() #查看游标位置
            fp.writelines(data) #在文件末尾追加内容
            fp.seek(index,0) #将游标指向追加内容前的位置
            new_data = fp.read()
            print "-"*10,"new_data","-"*10,"\n",new_data,"-"*30,"\n"
        all_data = linecache.getlines(filename) #按行读取文件内容
        linecache.clearcache() #清除缓存
        print "-"*10,"all_data","-"*10,"\n",''.join(all_data),"-"*30,"\n"
    except Exception,e:
        print "file path not exist"
 
# filename = "d:\\export.log"
# data = ["Hello World!\n","Hello Python!\n","Hello Gloryroad!\n","Hello everyone\n","大家好!\n","test123!\n"]
# print read_and_write_file_by_w_add(filename,data)
# read_and_write_file_by_r_add(filename,data)
# read_and_write_file_by_a_add(filename,data)

'''练习题2：创建一个空文件'''
import os
def new_empty_file(path, filename):
    try:
        if path.endswith(os.sep): #判断目录是否以反斜扛结尾，若不是在目录和文件名之间加上反斜扛
            filepath = path+filename
        else:
            filepath = path + os.sep + filename
        with open(filepath,'w') as fp: #创建一个文件，若文件存在则清空文件内容
            pass
        print "down"
    except Exception,e:
        print "file path not exist"
 
# new_empty_file("d:\\test\\", "test.log")

'''练习题3：读取文件的前两行'''



















