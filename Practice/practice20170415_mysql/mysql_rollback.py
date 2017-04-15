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
datas = cursor.fetchall()
print u"修改前的数据：\n", datas
# 更新数据表中第一条数据
cursor.execute("update user set birthday='2100-08-12' where name='wle'")
cursor.execute("select * from user")
datas = cursor.fetchall()
print u"修改后的数据：\n", datas

# 回滚事务
conn.rollback()
cursor.execute("select * from user")
datas = cursor.fetchall()
print u"事务回滚后的数据：\n", datas

# 关闭游标
cursor.close()
# 提交事务
conn.commit()
# 关闭数据库连接
conn.close()
print u"sql语句执行成功！"
