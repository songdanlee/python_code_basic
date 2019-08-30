import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# 创建连接
db = sqlalchemy.create_engine("mysql+pymysql://root:1234@localhost/user")
# 基类
base = declarative_base(db)


# 映射
class User(base):
    __tablename__ = "person"
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    name = sqlalchemy.Column(sqlalchemy.String(32))


# 创建session
Session = sessionmaker(bind=db)
session = Session()

if __name__ == '__main__':
    # 添加多条数据
    # session.add_all([
    #     User("张三"),
    #     User("李四"),
    # ])
    # 添加单条数据
    # session.add(User("张三"))

    # 查询数据
    user = session.query(User).filter(User.name == "张三").first()
    print(user.name)

    users = session.query(User).filter(User.id < 5).all()
    for user in users:
        print(user.name)


    # 修改数据
    user = session.query(User).filter(User.name == "李四").first()
    user.name = "王五"
    session.merge(user)

    # 删除数据
    user = session.query(User).filter(User.name == "张三").first()
    session.delete(user)



    session.commit()
    session.close()
