"""
进程之间的通信
队列：
    multiprocessing.Queue
工作机制：
    先进先出
创建：
    multiprocessing.Queue(maxsize = n)
入队：
    put()
        如果对满，会导致阻塞
出队：
    get()
        如果队空，会导致阻塞
    get_nowait()
        如果为空，抛出异常
是否队满：
    full()
是否队空：
    empty()
获取队长:
    qsize()

"""
import multiprocessing

#
# def task1(list1):
#     for i in range(3):
#         list1.append(i)
#     print(id(list1))
#     print(list1)
#
#
# def task2(list1):
#     for i in range(5, 8):
#         list1.append(i)
#     print(id(list1))
#     print(list1)
#
#
# if __name__ == '__main__':
#     list1 = []
#     print(id(list1))
#
#     p1 = multiprocessing.Process(target=task1, args=(list1,))
#     p2 = multiprocessing.Process(target=task2, args=(list1,))
#     p1.start()
#     p2.start()


def getData(q):
    for i in range(1000):
        q.put(i)
        print("put")
    print("爬取完毕")

def process_data(q):
    for i in range(1000):
        q.get()
        print("get")
    print("处理完毕")

if __name__ == '__main__':
    q = multiprocessing.Queue(2)
    p1 = multiprocessing.Process(target=getData,args=(q,))
    p2 = multiprocessing.Process(target=process_data,args=(q,))

    print(q.qsize())
    print(q._maxsize)

    p1.start()
    p2.start()
