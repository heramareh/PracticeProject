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

#批量插入条数据
sql = "insert into user values(%s, %s, %s, %s)"
insert = cursor.executemany(sql, [
    (5,'tom','tom','1989-03-17'), 
    (6,'amy','test','1898-12-01'),
    (7,'lily','linux','1994-06-23')])
print u"批量插入返回受影响的行数：", insert

# 关闭游标
cursor.close()
# 提交事务
conn.commit()
# 关闭数据库连接
conn.close()
print u"sql语句执行成功！"
