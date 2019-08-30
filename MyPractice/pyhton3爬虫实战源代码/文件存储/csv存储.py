import csv

# with open("dada.csv","w",encoding="utf-8") as csvfile:
#     # writer = csv.writer(csvfile,delimiter=" ")
#     writer = csv.writer(csvfile)
#     writer.writerow(["id","name","age"])
#     writer.writerow(["1001","Mkie","30"])
#     writer.writerow(["1002","Jordan","21"])
#     writer.writerow(["1003","Bob","22"])

# 写入字典对象
# with open("data.csv","w") as csvfile:
#     fildnames = ["id","name","age"]
#     writer = csv.DictWriter(csvfile,fieldnames=fildnames)
#     writer.writeheader()
#     writer.writerow({"id":1001,"name":"zs","age":12})
#     writer.writerow({"id":1002,"name":"ls","age":22})
#     writer.writerow({"id":1003,"name":"zl","age":32})

with open("data.csv","r") as csvfile:
    reader = csv.reader(csvfile)
    print("---")
    for line in reader:
        if len(line) != 0:
            print(line)

# 利用panda读取csv文件
import pandas as pd

f = pd.read_csv("data.csv")
print(f)