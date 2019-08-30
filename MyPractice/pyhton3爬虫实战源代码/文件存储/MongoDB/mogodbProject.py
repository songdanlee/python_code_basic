import pymongo


client = pymongo.MongoClient(host="localhost",port=27107)
# client = pymongo.MongoClient("mongodb://127.0.0.1:27107")


db = client.test
# db = client["test"]

collection = db.students
# collection = db['students']

student = {
    'id':'20170101',
    'name':'Jordan',
    'age':20,
    'gender':'male'
}

result = collection.insert(student)
print(result)


