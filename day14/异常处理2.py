

try:
    f = open("123.txt","r")
    print("打开文件成功")
    f.read('123')
except FileNotFoundError as e:
    print(e)
    print(type(e))
else:
    # 没有异常才会执行
    print("else 代码被执行")
finally:
    try:
        f.close()
    except Exception as e:
        print(e)
    else:
        print("文件关闭")