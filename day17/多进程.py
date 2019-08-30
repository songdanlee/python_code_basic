"""
进程与线程
网络编程
数据结构与算法
周五：测试

多进程与多线程以及协程（实现多任务）

多任务：
    同时执行多个任务

同时：
    并行与并发（课下查询）
    并行：
        两个任务同时执行
        两个老师同时为两个学生解答问题
    并发：（高并发）
        两个任务交替执行
        一个老师同时为两个学生解答问题

多任务：
1.多进程
    进程？
        针对操作系统来讲的，
        运行中的程序程序(代码)，
        一个程序默认情况下，只有一个进程(主进程)

    进程，需要向系统申请单独的内存



    开启多任务：
        使用多进程
        创建子进程：
        multiprocessing.Process(group=None, target=None, name=None, args=(), kwargs={})
        target: 指定在子进程中执行的任务
        name:  为子进程创建的名字
        args: 为函数传递的参数

    注意：
        手动开启的子进程，会将主进程中所有的资源复制一份（更消耗内存）
        用空间换时间

    多进程可以充分发挥多核的优势,每个CPU中处理一个进程任务

2.多线程

3.协程

"""
import time
import multiprocessing


def download1(t1):
    for i in range(10):
        print(f"{t1}已完成{i * 10} %")
        time.sleep(1)
def download2():
    for i in range(10):
        print(f"任务二已完成{i * 10} %")
        time.sleep(1)
if __name__ == '__main__':

    p = multiprocessing.Process(target=download1,args=("任务一",))
    p1 = multiprocessing.Process(target=download2,name="task2")
    print(p1.name)

    p.start()
    p1.start()
