#coding=utf-8
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
print u"表中所有数据："
for i in cursor.fetchall():
    print i
# 批量删除数据
delete = cursor.executemany("delete from user where name=%s", [('kzduxlc',), ('mvuqfwm',), ('sjxuxe')])
print u"删除语句影响的行数：", delete

print u"删除一条数据后，表中数据："
cursor.execute("select * from user")
for i in cursor.fetchall():
    print i

# 关闭游标
cursor.close()
# 提交事务
conn.commit()
# 关闭数据库连接
conn.close()
print u"sql语句执行成功！"
