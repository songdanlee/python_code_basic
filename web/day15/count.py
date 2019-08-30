import os

result = {}
with os.popen("ps aux") as f:
    for i in f.readlines():
        user = i.split(" ",1)
        if len(user) >= 2:
            if user[0] in result:
                result[user[0]] += 1
            else:
                result[user[0]] = 1

print(result)
