import pymysql
conn = pymysql.connect(host="127.0.0.1",user="root",password="1234",port=3306,db="user")


cursor = conn.cursor()

cursor.execute("select * from user")

for f in cursor.fetchall():
    print(f)

cursor.close()

import sqlalchemy
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
conn = sqlalchemy.create_engine("mysql+pymysql://root:1234@localhost/user")

base = declarative_base(conn)


class User(base):
    id = sqlalchemy.Column(sqlalchemy.Integer,primary_key=True)
    name = sqlalchemy.Column(sqlalchemy.String(32))
    money = sqlalchemy.Column(sqlalchemy.Integer)



Session = sessionmaker(bind=conn);
session = Session()
resu = session.query(User).all()
print(resu)