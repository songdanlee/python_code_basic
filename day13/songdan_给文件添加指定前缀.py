import os

def add_prefix(file_path,prefix):

    file_list = os.listdir(file_path)
    for f in file_list:
        f = file_path + "\\" + f
        if os.path.isfile(f):
            basename = os.path.basename(f)
            dirname = os.path.dirname(f)
            print(dirname+"\\"+prefix+basename)
            # os.rename(f,dirname+"\\"+prefix+basename)
        elif os.path.isdir(f):
            add_prefix(f,prefix)
add_prefix(r"E:\怪奇物语\a","songdan-")