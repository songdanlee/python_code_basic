import pymysql


def create_database():
    db = pymysql.connect(host="localhost", user="root", password="1234", port=3306)
    cursor = db.cursor()
    sql = " CREATE  DATABASE  spiders  DEFAULT  CHARACTER  SET utf8 "
    cursor.execute(sql)
    cursor.close()
    db.commit()
    db.close()


# create_database()

def create_table():
    db = pymysql.connect(host="localhost", user="root", password="1234", db="spiders", port=3306)
    cursor = db.cursor()
    sql = " CREATE TABLE IF NOT EXISTS students (id VARCHAR(255) NOT NULL,name VARCHAR(255) NOT NULL,age INT NOT NULL,PRIMARY KEY (id))"
    cursor.execute(sql)
    cursor.close()
    db.commit()
    db.close()

# create_table()

def insert_table():
    db = pymysql.connect(host="localhost",user="root",password="1234",port=3306,db="spiders")
    cursor = db.cursor()
    user = {
        "id": "2012003",
        "name": "j3ob",
        "age": 22,
    }
    table = "students"
    keys = ",".join(user.keys())
    values = ",".join(['%s']*len(user))
    sql = f"insert into {table} ({keys}) values ({values})"
    print(sql)
    try:
        if cursor.execute(sql,tuple(user.values())):
            print("successful")
            db.commit()
        else:
            print("error")
    except Exception as e:
        print("field")
        db.rollback()
        print(e)
    finally:
        cursor.close()
        db.close()
# insert_table()

# 插入重复主键key
def insert_duplicate_key():
    db = pymysql.connect(host="localhost", user="root", password="1234", port=3306, db="spiders")
    cursor = db.cursor()
    user = {
        "id": "2012003",
        "name": "mike",
        "age": 22,
    }
    table = "students"
    keys = ",".join(user.keys())
    values = ",".join(['%s'] * len(user))
    sql = f"insert into {table} ({keys}) values ({values}) ON DUPLICATE KEY UPDATE "

    update = ",".join(["{key} = %s".format(key=key) for key in user])
    print(update)
    sql += update
    print(sql)
    try:
        if cursor.execute(sql, tuple(user.values())*2):
            print("successful")
            db.commit()
        else:
            print("error")
    except Exception as e:
        print("field")
        db.rollback()
        print(e)
    finally:
        cursor.close()
        db.close()
# insert_duplicate_key()

def delete_from_table():
    db = pymysql.connect(host="localhost", user="root", password="1234", port=3306, db="spiders")
    cursor = db.cursor()
    table = "students"
    condition = "age > 20"
    sql = f"delete from {table} where {condition}"
    print(sql)
    try:
        cursor.execute(sql)
        print("successful")
        db.commit()
    except Exception as e:
        print(e)
        db.rollback()
    finally:
        db.close()
# delete_from_table()

def select_from_table():
    db = pymysql.connect(host="localhost", user="root", password="1234", port=3306, db="spiders")
    cursor = db.cursor()
    table = "students"
    condition = "age > 20"
    sql = f"select *  from {table} where {condition}"
    print(sql)

    try:
        cursor.execute(sql)
        print("count:", cursor.rowcount)

        result_one = cursor.fetchone()
        print("one", result_one)

        result_all = cursor.fetchall()

        print(type(result_all))
        print("all", result_all)
    except Exception as e:
        print("error")
        print(e)
    db.close()

select_from_table()