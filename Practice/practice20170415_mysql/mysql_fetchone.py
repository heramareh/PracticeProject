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
cursor.execute("select * from user")
while 1:
    res = cursor.fetchone()
    if res is None:
        # 表示已经取完结果集
        break
    print res
    #将读取到的时间格式化
    print res[-1].strftime("%Y-%m-%d")

cursor.execute("select birthday from user where name = 'wle'")
res = cursor.fetchone()
print res
print res[0].strftime("%Y-%m-%d")
# 关闭游标
cursor.close()
# 提交事务
conn.commit()
# 关闭数据库连接
conn.close()
print u"sql语句执行成功！"
