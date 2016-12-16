#encoding=utf-8
import os

def rename(path,newname):
    # 获取path目录下的所有文件名和目录名
    filenames = os.listdir(path)
    for filename in filenames:
        # 判断是文件还是目录
        if os.path.isdir(os.path.join(path,filename)):
            continue
        # 获取文件后缀名（如：mkv）
        filetype = filename.rsplit('.', 1)[1]
        print filetype
        for i in xrange(1,len(filenames)+1):
            # 关键字查找（如：查找文件名中带有E01/E02/E03这种字样的文件）
            if filename.find('E'+str(i).zfill(2)) > -1:
                # 修改文件名
                os.rename(os.path.join(path,filename),os.path.join(path,newname+u'第'+str(i)+u'集'+'.'+filetype))
                break
            else:
                continue
    print u'完成。'

# 文件夹路径
path = u'E:\\迅雷\\'
# 文件目录
newname = u'越狱第一季'
# 文件路径
path = path + newname
# 批量修改指定目录下的文件名
rename(path, newname)