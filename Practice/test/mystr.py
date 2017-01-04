#encoding=utf-8
import string
from collections import Iterable

def isdigit(s):
    try:
        if not isinstance(s,basestring):
            raise Exception("expected a string")
        for i in s:
            if not i.isnum():
                return False
        return True
    except Exception,e:
        return "TypeError: "+str(e)

def strip(s, strip_str=None):
    try:
        if not isinstance(s,basestring):
            raise Exception("expected a string")
        length=len(s)
        if strip_str == None:
            for index in range(len(s)):
                if s[index] not in string.whitespace:
                    start = index
                    break
            for index in range(len(s)):
                if s[length-1-index] not in string.whitespace:
                    end = length-index
                    break
            if start > end:
                return ''
            else:
                return s[start:end]
        else:
            strip_length = len(strip_str)
            if strip_length == 0:
                return s
            while s[:strip_length] == strip_str:
                s = s[strip_length:]
            while s[-strip_length:] == strip_str:
                s = s[:-strip_length]
            return s
    except Exception,e:
        return "TypeError: "+str(e)

def join(s,sep=''):
    try:
        if not isinstance(s,Iterable):
            raise Exception("can only join an iterable")
        elif isinstance(s,(list,tuple)):
            for i in range(len(s)):
                if not isinstance(s[i],basestring):
                    raise Exception("sequence item "+str(i)+": expected string")
        result = ''
        for j in s:
            result += j
            result += sep
        if len(sep) > 0:
            return result[:-len(sep)]
        else:
            return result
    except Exception,e:
        return "TypeError: "+str(e) 

def split(s,split_str='',count=None):
    try:
        if not isinstance(s,basestring):
            raise Exception("expected a string")
        list_s = []
        each = ''
        num = 0
        if split_str == '':
            for i in s:
                if num == count:
                    break
                if i != ' ':
                    each+=i
                else:
                    if each != '':
                        list_s.append(each)
                        each = ''
                        num += 1
            list_s.append(each)
            return list_s
        else:
            length = len(split_str)
            while split_str in s:
                if num == count:
                    break
                index = s.find(split_str)
                list_s.append(s[:index])
                s = s[index+length:]
                num += 1
            list_s.append(s)
            return list_s
    except Exception,e:
        return "TypeError: "+str(e)
