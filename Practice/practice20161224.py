#encoding=utf-8
import string
import os
import sys
import shutil

'''一个文件有很多英文单词，
找到出现次数最多的字母，
将字母和出现次数加在第一行，
其他文件内容加后面，原文保持不变。'''
def find_most_letter(filename):
    with open(filename,'r') as fp:
        file_content = fp.read()
    letter_dict = {}
    for each in file_content:
# method1: 用count函数统计次数
#         if (each in string.letters) and (not letter_dict.has_key(each)):
#             letter_dict[each] = file_content.count(each)
# method2: 若字母在字典里则次数加1，若不在则赋值为1
        if each.isalpha():
            if letter_dict.has_key(each):
                letter_dict[each] += 1
            else:
                letter_dict[each] = 1
    max_count = max(letter_dict.values())
    result_list = []
    for alpha in letter_dict.keys():
        if letter_dict[alpha] == max_count:
            result_list.append(alpha+' ')
    result_list.append(", max_count:"+str(max_count)+os.linesep)
    with open(filename,'w') as fp:
        fp.write("letters: ")
        fp.writelines(result_list)
        fp.write(file_content)

# find_most_letter("d:\\wa.txt")

'''在文件中指定的位置写入字符串'''
# def write_str_in_specified_location(filename,location,s):
#     try:
#         with open(filename,'r+') as fp:
#             length = len(fp.read())
#             if location > length:
#                 fp.seek(0,2)
#                 fp.write(s)
#             else:
#                 fp.seek(location-1,0)
#                 last_str = fp.read()
#                 fp.seek(location-1,0)
#                 fp.write(s+last_str)
#                 fp.seek(0,0)
# #                 print fp.read()
#             return 1
#     except Exception,e:
#         return str(e)
# 
# write_str_in_specified_location("d:\\wa.txt",5,"abcdefg")
# 
# def write_words_in_specific_position(file_path,position,word):
#     with open("e:\\a.txt","r+") as fp:
#         max_position=len(fp.read())
#         if position>max_position:
#             fp.seek(0,2)
#             fp.write(str(word))
#         else:
#             fp.seek(position-1,0)
#             fp.write(str(word))
# 
# if __name__=="__main__":
#     write_words_in_specific_position("e:\\a.txt",100,"gloryroad")

'''统计文件中有效代码行数'''
def count_lines(filename):
    try:
        fp = open(filename,'r')
        count = 0
        for eachline in fp:
            if eachline.strip() == '':
                continue
            elif eachline.strip()[0].isalpha():
                print eachline,
                count += 1
        fp.close()
        return os.linesep+"lines:"+str(count)
    except Exception,e:
        return str(e)

# print count_lines(ur"d:\笔记.txt")

'''创建文件目录，指定级次'''
def mk_dir(filePath, dirName, level):
    try:
        for i in range(level):
            os.chdir(filePath)
            os.mkdir(dirName)
            filePath = filePath + os.sep + dirName
            with open(filePath+os.sep+dirName+".txt",'w') as fp:
                fp.write(filePath)
        return 1
    except Exception,e:
        return str(e)

# print mk_dir("d:\\test","gloryroad",5)
'''输出文件权限模式'''
# print os.access(r'd:\test\test.txt', os.W_OK)
# print os.access(r'd:\test\test.txt', os.R_OK)
# print os.access(r'd:\test\test.txt', os.X_OK)

# dirList = os.popen('dir d:\\test*.*')
# for i in dirList.readlines() :
#     print i

'''拼接路径下的所有文件夹和文件的绝对路径'''
# for root,dirs,files in os.walk("d:\\test"):
#     print n
#     for file in files:
#         print os.path.join(root,file)
#     for dir in dirs:
#         print os.path.join(root,dir)+os.sep

# for root, dirs, files in os.walk("d:\\test",topdown=False) :
#     print u"上级目录:",root #打印目录绝对路径
#     for name in files :
#         print u'文件名：',os.path.join(root,name) #打印文件绝对路径
# 
#     for name in dirs :
#         print u'目录名：',name #打印目录绝对路径

'''如果文件路径存在，就把文件中添加“gloryroad”的字符串，不存在就创建这个文件'''
def add_str(filepath,s='gloryroad'):
    if not os.path.exists(filepath):
        with open(filepath,'a') as fp:
            pass
    else:
        with open(filepath,'a') as fp:
            fp.write(s)
# add_str("d:\\test\\aa.txt")

# for arg in sys.argv:
#     print arg
# print sys.argv

'''1.基础题：
检验给出的路径是否是一个文件：
检验给出的路径是否是一个目录：
判断是否是绝对路径：
检验给出的路径是否真地存在:
'''
# print os.path.isfile("d:\\test\\test.txt")
# print os.path.isdir("d:\\test")
# print os.path.isabs("test\\wa")
# print os.path.exists("d:\\test")

'''2.返回一个路径的目录名和文件名'''
# print os.path.split("d:\\test\\test.txt")
# print os.path.split("d:\\test\\test")

'''3.分离文件名与扩展名'''
# print os.path.splitext(os.path.split("d:\\test\\test.txt")[1])

'''4.找出某个目录下所有的文件，并在每个文件中写入“gloryroad”'''
def write_content_in_all_files(path,content):
    try:
        if not os.path.isdir(path):
            return "path is not exist or dir"
        for root,dirs,files in os.walk(path):
            for file in files:
                print os.path.join(root,file)
                with open(os.path.join(root,file), 'a') as fp:
                    fp.write(content)
        return 1
    except Exception,e:
        return -1

print write_content_in_all_files("d:\\test", "gloryroad")

'''5.如果某个目录下文件名包含txt后缀名，则把文件后面追加写一行“被我找到了！”'''
def find_file_by_suffix(path,suffix):
    try:
        if not os.path.isdir(path):
            return "path is not exist or dir"
        for root,dirs,files in os.walk(path):
            for file in files:
                if os.path.splitext(file)[1] == '.' + suffix:
                    with open(os.path.join(root,file),'a') as fp:
                        fp.write("被我找到了！")
        return 1
    except Exception,e:
        return -1

# print find_file_by_suffix("d:\\test","txt")

sys.stdout.write("abc123\n")
sys.stderr.write("abc123\n")

