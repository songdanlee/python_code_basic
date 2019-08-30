"""
重命名文件
    os.rename(src,dst)
    os.rename('123.txt','124.txt')
删除文件
    os.remove(path)
    os.remove('123.txt')
创建目录
    os.mkdir()
创建多级目录
    os.makedirs()
删除目录
    os.rmdir()
删除多级目录
    os.removedirs()
获取当前目录
    os.getcwd()
修改所在目录
    os.chdir()
判断文件是否存在
    os.path.exists()
判断是否为文件
    os.path.isfile()
判断是否为目录
    os.path.isdir()

获取绝对路径
    os.path.abspath()
判断是否为绝对路径
    os.path.isabs()
获取路径的最后部分
    os.path.basename()
获取父级路径
    os.path.dirname()

获取文件夹内的子文件(重要)
    os.listdir()

"""
import os
# os.rename("log.txt","log.properties")
# os.remove("log.properties")
# open("log.txt","w")
# os.mkdir("abc")
# os.rmdir("abc")
# os.makedirs("a/b/c/d")
# os.removedirs("a/b/c/d")
# os.chdir("../")
# print(os.getcwd())
# file_name = "abc.jpeg"
# if os.path.exists(file_name):
#     if os.path.isdir(file_name):
#         print("删除文件夹成功")
#         os.rmdir(file_name)
#     elif os.path.isfile(file_name):
#         print("删除文件成功")
#         os.remove(file_name)
# else:
#     print("文件不存在")

path = os.getcwd()

for f in os.listdir(path):
    if f.endswith(".py"):
        print(f)