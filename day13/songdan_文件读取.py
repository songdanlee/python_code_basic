

def test_read():
    f = open("log.txt", mode="r", encoding="utf-8")
    content = f.read(10)
    print(content)

file_name = "log.txt"
def test_write():
    with open(file_name,mode="w",encoding="utf-8",newline="") as f:
        content = input("请输入任意字符")
        while content != 'bye':
            f.write(content+'\n')
            content = input("请输入任意字符")

# test_write()


def copy_file():
    f_tup = file_name.rpartition('.')
    new_file = f_tup[0]+"-副本"+f_tup[1]+f_tup[2]
    with open(file_name,mode="r",encoding="utf-8") as f:
        with open(new_file,mode="w",encoding="utf-8") as f1:
            #1024*1024 1M
            content = f.read(1024*1024)
            while content:
                f1.write(content)
                content = f.read(1024*1024)

# copy_file()
img_name = "abc.jpeg"

def copy_img(img_name):
    f_tup = img_name.rpartition('.')
    new_file = f_tup[0] + "-副本" + f_tup[1] + f_tup[2]
    with open(img_name, mode="rb") as f:
        with open(new_file, mode="wb") as f1:
            # 1024*1024 1M
            content = f.read(1024)
            while content:
                f1.write(content)
                content = f.read()
copy_img(img_name)