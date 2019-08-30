

# with open("a.txt",'a+',encoding='utf-8') as f:
#     line = """hello python
# hello world
# hello java """
#
#     f.writelines(line)
#     f.write("hello")

with open("a.txt",'r',encoding='utf-8') as f:
    lines = f.readlines()
    for i in lines:
        print(i.strip())
