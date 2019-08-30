import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
db = sqlalchemy.create_engine("mysql+pymysql://root:1234@localhost/user")

base = declarative_base(db)
Session = sessionmaker(bind=db)
session = Session()


class User(base):
    __tablename__ = "user"
    id = sqlalchemy.Column(sqlalchemy.Integer,primary_key=True)
    name = sqlalchemy.Column(sqlalchemy.String(32))
    money = sqlalchemy.Column(sqlalchemy.Integer)
# users = session.query(User).filter(User.name=="张三").all()
# for x in users:
#     print(x.id,x.name,x.money)
# user = session.query(User).filter(User.name=="李四").first()
# print(user.id,user.name,user.money)

# session.add_all([
#     User(id=3,name="王五",money=890),
#     User(id=4,name="马六",money=190),
# ])
# session.commit()
# session.close()

# user = session.query(User).filter(User.name=="马六").first()
#
# user.money = 500
#
# session.merge(user)
user = session.query(User).get(1)
print(user.name,user.id,user.money)
#
# user = session.query(User).filter(User.name=="马六").first()
# session.delete(user)
#
# session.commit()
# session.close()
