#coding=utf-8
import MySQLdb
import random,string

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
# 插入一条数据
# insert = cursor.execute("insert into user values(1,'Tom','123','1990-01-01')")
# print u"添加语句受影响的行数：", insert
for i in range(10):
    id = random.randint(1,99)
    y = []
    for i in range(random.randint(3,7)):
        y.append(random.choice(string.lowercase))
    name = ''.join(y)
    x = []
    for i in range(random.randint(8,17)):
        x.append(random.choice(string.printable))
    password = ''.join(x)
    birthday = str(random.randint(1900,2017)) + '-' + str(random.randint(1,12)) + '-' + str(random.randint(1,31))
    # 另一种插入数据方法，通过格式字符串传入值，此方式可以防止sql注入
    sql = "insert into user values(%s, %s, %s, %s)"
    cursor.execute(sql, (id,name,password,birthday))
    # cursor.execute(sql, (3,'lucy','efg','1993-02-01'))
# 关闭游标
cursor.close()
# 提交事务
conn.commit()
# 关闭数据库连接
conn.close()
print u"sql语句执行成功！"
