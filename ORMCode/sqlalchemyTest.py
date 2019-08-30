import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
import logging

logging.captureWarnings(True)


# 连接数据库

# mysql+pymysql://用户名:密码@主句地址/库名
db = sqlalchemy.create_engine("mysql+pymysql://root:1234@localhost/user?charset=utf8")

# 创建一个继承基类
base = declarative_base(db)


# 映射
# 将表名映射为类名
# 将字段映射Wie属性
class Demo(base):
    __tablename__ = "user"

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    name = sqlalchemy.Column(sqlalchemy.String(32))
    phone = sqlalchemy.Column(sqlalchemy.String(32))
    idcard = sqlalchemy.Column(sqlalchemy.String(32))
    create_time = sqlalchemy.Column(sqlalchemy.Date)


from sqlalchemy.orm import sessionmaker

session = sessionmaker(bind=db)
session = session()

# user = Demo(
#     id=8,
#     name='bilibili',
#     phone="123456789",
#     idcard="123456789012345678",
#     create_time="2019-09-12"
# )
#
# session.add(user)
# session.commit()

# 增加多条
# session.add_all([
#     Demo(id=8,name="bili"),
#     Demo(id=9,name="acfun")
# ])
# session.commit()
# 查询
# all 返回列表，返回复合条件的多条数据
# datas = session.query(Demo).all()
# for data in datas:
#     print(data,data.id,data.name)
# first 返回值为一个对象
# firstData = session.query(Demo).first()
# print(firstData,firstData.id,firstData.name)
# get 返回值对象，通过id查询
# indentData = session.query(Demo).get(8)
# print(indentData,indentData.id,indentData.name)

# datas = session.query(Demo).filter(Demo.id<5).all()
# for data in datas:
#     print(data,data.id,data.name)
#
# datas = session.query(Demo).filter_by(id=5).all()
# for data in datas:
#     print(data,data.id,data.name)
#
# data = session.query(Demo).filter_by(id=5).first()
# print(data)
# 修改
# data = session.query(Demo).get(5)
# data.name = "lili"
# session.merge(data)
# session.commit()
# 修改多列
# datas = session.query(Demo).filter(Demo.id<5).all()
# for data in datas:
#     data.name = 'acfun'
#     session.merge(data)
# session.commit()

# update 修改
# session.query(Demo).filter(Demo.id == 2).update({Demo.id:2,Demo.name:"xxx"})
# session.commit()
# 删除
# data = session.query(Demo).get(5)
# session.delete(data)
# session.commit()
# data = session.query(Demo).filter(Demo.id == 7).first()
# session.delete(data)
# session.commit()

session.query(Demo).filter(Demo.id == 8).delete()
session.commit()


# if __name__ == '__main__':
# 根据写好的model模型  创建表
# base.metadata.create_all(db)


