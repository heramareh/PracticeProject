#encoding=utf-8
import string
import os
import sys
import shutil
import time

'''第一题：命令行输入4个参数，然后用程序求和，例如： python b.py 10 100 1000 10000'''
def my_sum():
    sum = 0
    for i in sys.argv[1:]:
        sum += int(i)
    return sum

# print my_sum()

'''第二题：自己构造一个目录A，下面有2个文件a.txt和b.txt ，
新建一个目录B，下面有文件c.txt。
请使用程序构造这个目录并且封装在一个函数中'''
def make_dir_and_file(path,dirA,dirB):
    try:
        os.chdir(path)
        os.makedirs(dirA)
        with open(os.path.join(dirA,"a.txt"),'w'):
            pass
        with open(os.path.join(dirA,"b.txt"),'w'):
            pass
        os.makedirs(dirB)
        with open(os.path.join(dirA,"c.txt"),'w'):
            pass
        return 1
    except Exception,e:
        return -1

'''第三题：把刚才的目录中的子目录和所有文件的路径，
写入到一个文件d.txt中，文件在同级创建的目录下。'''

'''练习：统计某个一级目录下有几个文件和子目录'''
def count_dirs_and_files(path):
    try:
        count_dir = 0
        count_file = 0
        for each in os.listdir(path):
            if os.path.isfile(os.path.join(path,each)):
                count_file += 1
                print "file:",each
            else:
                count_dir += 1
                print "dir:",each
        print "count_dir: %s\ncount_file: %s" %(count_dir,count_file)
        return {"count_dir":count_dir,"count_file":count_file}
    except Exception,e:
        return str(e)

# print count_dirs_and_files("d:\\test")

'''查找目录下是否存在后缀为.txt的文件，若存在返回True，否则返回False'''
def isexists_suffix_txt(path):
    try:
        if not os.path.exists(path):
            return "path is not exists"
        txt_files = []
        for each in os.listdir(path):
            if os.path.isfile(os.path.join(path,each)) and os.path.splitext(each)[1] == ".txt":
                txt_files.append(each)
        if txt_files:
            print "txt_files:",txt_files
            print "count_txt_files:",len(txt_files)
            return True
        else:
            return False
    except Exception,e:
        return str(e)

# print isexists_suffix_txt("d:\\test")

'''统计目录下一共有多少个txt文件'''
def count_allTxtFiles(path):
    try:
        count = 0
        for root,dirs,files in os.walk(path):
            for file in files:
                if os.path.splitext(file)[1] == ".txt":
                    count += 1
                    print "file: ",os.path.join(root,file)
        return count
    except Exception,e:
        return -1

# print count_allTxtFiles("d:\\test")