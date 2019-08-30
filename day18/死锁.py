"""
死锁产生
    1.多线程处理
    2.互斥锁的使用

解决方案
    if lock2.acquire(blocking = False)
    if lock2.acquire(timeout = 2)
"""
import threading
import time

# 获取全局锁对象
lock1 = threading.Lock()
lock2 = threading.Lock()

def taks1():
    print("task 1 开始执行")
    if lock1.acquire():
        print("task1-获取lock1成功")
        time.sleep(1)
        # 获取锁超时后，不再获取
        # if lock2.acquire(timeout=3):
        # 获取锁失败后，不再获取
        if lock2.acquire(blocking=False):
        # if lock2.acquire():
            print("task1-获取lock2成功")
            lock2.release()
            print("task1-释放lock2成功")
        lock1.release()

def taks2():
    print("task 2 开始执行")
    if lock2.acquire():
        print("task2-获取lock2成功")
        time.sleep(1)

        if lock1.acquire():
            print("task2-获取lock1成功")
            lock1.release()
            print("task2-释放lock1成功")
        lock2.release()

t1 = threading.Thread(target=taks1)
t2 = threading.Thread(target=taks2)
t1.start()
t2.start()
