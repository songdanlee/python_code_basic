import os



def deltefile(file_name):
    os.remove(file_name)
    print("删除文件"+file_name)

def find_video(path):
    dirs = os.listdir(path)
    for dir in dirs:
        dir = path + "\\"+dir
        if os.path.isfile(dir) and "wmv" in dir:
            deltefile(dir)
        elif os.path.isdir(dir):
            find_video(dir)
if __name__ == '__main__':
    find_video(r"E:\视频")