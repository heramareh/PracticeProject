#encoding=utf-8
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
cursor.execute("select * from user where name='wle';")
print cursor.fetchone()
# 更新一条数据
update = cursor.execute("update user set password = 'Tom_test' where name='wle'")
print u"修改语句受影响行数：", update
#查询一条数据
cursor.execute("select * from user where name='wle';")
print cursor.fetchone()

# 关闭游标
cursor.close()
# 提交事务
conn.commit()
# 关闭数据库连接
conn.close()
print u"sql语句执行成功！"
