"""
查资料理解并行与并发的区别
并行是指两个或者多个事件在同一时刻发生；
而并发是指两个或多个事件在同一时间间隔发生，宏观上是同时执行，微观上是交替执行。
并发是指一个处理器同时处理多个任务。
并行是指多个处理器或者是多核的处理器同时处理多个不同的任务。

"""

"""
查资料理解同步与异步的区别
同步，是所有的操作都做完，才返回给用户结果。即写完数据库之后，在相应用户，用户体验不好。
异步，不用等所有操作等做完，就相应用户请求。即先相应用户请求，然后慢慢去写数据库，用户体验较好
"""
"""
查资料理解进程与线程的区别
1、进程是资源分配的最小单位，线程是程序执行的最小单位（资源调度的最小单位）
2、进程有自己的独立地址空间，每启动一个进程，系统就会为它分配地址空间，建立数据表来维护代码段、堆栈段和数据段，这种操作非常昂贵。
而线程是共享进程中的数据的，使用相同的地址空间，因此CPU切换一个线程的花费远比进程要小很多，同时创建一个线程的开销也比进程要小很多。
3、线程之间的通信更方便，同一进程下的线程共享全局变量、静态变量等数据，而进程之间的通信需要以通信的方式（IPC)进行。不过如何处理好同步与互斥是编写多线程程序的难点。
4、但是多进程程序更健壮，多线程程序只要有一个线程死掉，整个进程也死掉了，而一个进程死掉并不会对另外一个进程造成影响，因为进程有自己独立的地址空间。
"""
# 4.使用进程池完成一部电视剧的下载(模拟下载任务，下载完成时，在回调函数中给出对应的结果)
from multiprocessing import Pool
import time


def download(video_name):
    for i in range(1, 6):
        print(f"下载{video_name}:已完成{i * 20}%")
        time.sleep(0.1)
    return video_name


def alert(video_name):
    print(f"{video_name}已完成下载")


# if __name__ == '__main__':
#     pool = Pool(3)
#     lists = [f"权利的游戏,第{i}集" for i in range(1,9)]
#     for video_name in lists:
#         pool.apply_async(download,args=(video_name,),callback=alert)
#
#     pool.close()
#     pool.join()


# 5.使用进程池完成一个文件夹中多个文件的复制，复制出来的文件名为旧文件名-复件.后缀
import os

# 传入文件名，复制新文件  旧文件名-复件.后缀
def copy_dir(f):
    if os.path.isfile(f):
        with open(f, "rb") as f1:
            tu = f.rpartition(".")
            newname = tu[0] + "-副件" + tu[1] + tu[2]
            with open(newname, "wb") as f2:
                content = f1.read(1024)
                while content:
                    f2.write(content)
                    content = f1.read(1024)
    return f
def alert(file):
    print(f"{file}拷贝完成")

def find_file(dir):
    files = os.listdir(dir)
    for f in files:
        f = dir + "/" + f
        if os.path.isfile(f):
            pool.apply_async(copy_dir, args = (f,),callback = alert)
        else:
            find_file(f)
def delete_file(dir):
    file = os.listdir(dir)

    for f in file:
        f = dir + "\\" + f
        if os.path.isfile(f) and "副件" in f:

            os.remove(f)
        elif os.path.isdir(f):
            delete_file(f)

if __name__ == '__main__':
    dir = r"E:\怪奇物语\work\2"
    delete_file(dir)
    pool = Pool(3)
    # find_file(dir)
    # pool.close()
    # pool.join()

# 6.使用多线程完成售票的模拟案例(注意线程锁的使用)
# from threading import Lock,Thread
# import time
# tickets = 100
#
# lock = Lock()
# def sale(name):
#     global tickets
#     while tickets > 0:
#         if lock.acquire():
#             if tickets:
#                 tickets -= 1
#                 print(f"{name}卖出一张票,还有{tickets}张票")
#                 time.sleep(0.1)
#             lock.release()
#
#
# t1 = Thread(target=sale,args=("客服1",))
# t2 = Thread(target=sale,args=("客服2",))
#
# t1.start()
# t2.start()