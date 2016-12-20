#encoding=utf-8

# '''从界面输入一些单词，然后写入一个文件，保存后，从文件中找出长度最长的单词，然后写入到文件的最后。'''
# import os
# import string
# s = raw_input("input a string: ")
# filename = "d:\\words.txt"
# with open(filename,'w') as fp:
#     fp.write(s)
# fp = open(filename,'r')
# word_str = fp.read()
# fp.close()
# for c in word_str:
#     if c not in string.letters:
#         word_str = word_str.replace(c,' ')
# word_list = word_str.split()
# word_dict = {}
# for word in word_list:
#     word_dict[word] = len(word)
# longest = max(word_dict.values())
# longest_word_list = [os.linesep]
# for word in word_dict.keys():
#     if word_dict[word] == longest:
#         longest_word_list.append(word+" ")
# with open(filename,'a') as fp:
#     fp.writelines(longest_word_list)

'''输入5个单词，单词前加上时间，然后写入文件'''
import time,os
def get_current_time():
    return time.strftime("%Y-%m-%d %H:%M:%S")
# filename = "d:\\words.txt"
# with open(filename,'w') as fp:
#     for i in range(5):
#         word = raw_input("input a word:")
#         fp.write(get_current_time()+": "+word+os.linesep)

'''复制文件（支持复制二进制文件）'''
import os
def copy_file(source_file,new_file):
    if os.path.exists(source_file):
        source_fp = open(source_file,'rb')
        new_fp = open(new_file,'wb')
        for line in source_fp:
            new_fp.write(line)
        source_fp.close()
        new_fp.close()
        return 0
    else:
        return -1

# print copy_file("d:\\1.jpg", "d:\\7.jpg")