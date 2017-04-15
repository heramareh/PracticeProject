#coding=utf-8
#使用fetchmany select 读取数据：
import MySQLdb

conn = MySQLdb.connect(
host = "127.0.0.1", 
port = 3306,
user = "root", 
passwd = "gloryroad" ,
db = "pythondb", 
charset = "utf8"
)
# 使用cursor()方法获取数据库的操作游标
cursor = conn.cursor()
cursor.execute("select * from user")

# 获取游标处两条数据
resTuple = cursor.fetchmany(2)
print u"结果集类型：", type(resTuple)
for i in resTuple:
    print i
# 关闭游标
cursor.close()
# 提交事务
conn.commit()
# 关闭数据库连接
conn.close()