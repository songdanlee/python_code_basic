import json

strs = """
[{
    "name":"Bob",
    "gender":"male",
    "birthday":"1992-09-21"
    },{
    "name":"Slina",
    "gender":"female",
    "birthday":"1995-10-18"
    }
]
"""
print(type(strs))
data = json.loads(strs)

print(data[0].get("name"))
print(type(data))

dict = {"name":"zs","age":12}

datas = json.dumps(dict)
print(type(datas))
print(datas)

json.loads()
json.dumps()