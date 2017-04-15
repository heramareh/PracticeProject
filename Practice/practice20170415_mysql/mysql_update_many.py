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

#查询一条数据
query = cursor.execute("select * from user")
print u"表中所有数据："
for i in cursor.fetchall():
    print i 
# 批量更新数据
cursor.executemany("update user set password = %s where name=%s", [('pzs@qq.com', 'pzs'), ('snav123', 'snav')])
# 查看更新后的结果
query = cursor.execute("select * from user")
print u"表中所有数据："
for i in cursor.fetchall():
    print i 
# 关闭游标
cursor.close()
# 提交事务
conn.commit()
# 关闭数据库连接
conn.close()
print u"sql语句执行成功！"