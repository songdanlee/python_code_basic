import pymysql

# 创建连接
# 主机 端口  用户  密码  库
db = pymysql.connect(host="127.0.0.1",port=3306,
                     user="root",password="1234",
                     db="user")

# 游标
cursor = db.cursor()

sql = "insert into user (id,name,phone) values(7,'hahah','123422222');"
# 执行sql
cursor.execute(sql)
# 提交事务
db.commit()

cursor.execute("select * from user;")

for s in cursor:
    print(s)

# 关闭连接
db.close()

import sqlalchemy

engn = sqlalchemy.create_engine()