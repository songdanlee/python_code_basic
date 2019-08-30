import os

basepath = r"E:\怪奇物语\rename"
file = os.listdir(basepath)
for f in file:
    oldname = basepath+"\\"+f
    tu = f.rpartition(".")
    newname = basepath+"\\"+ tu[0]+".mp4.ts"
    os.rename(oldname,newname)