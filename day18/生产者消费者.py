"""
生产者消费者模式：
进程队列：
    multiprocessing.Queue
线程队列：
    queue.Queue(先进先出队列)
    实现了锁的队列，线程安全的
    入队：
        put()
    出队:
        get()
    队长：
        qsize()

"""
from threading import Thread
from queue import Queue
import time

q = Queue(maxsize=10)


class Produce(Thread):
    count = 1

    def __init__(self, name):
        super(Produce, self).__init__()
        self.name = name

    def run(self):
        while True:
            result = f"{self.name}生产了第{Produce.count}个包子"
            q.put(result)
            print(result)
            Produce.count += 1
            time.sleep(1)


class Custom(Thread):
    def __init__(self, name):
        super(Custom, self).__init__()
        self.name = name

    def run(self) -> None:
        while True:
            if q.qsize() > 0:
                r = q.get()
                print(f"{self.name}吃了{r}")
            time.sleep(2)


if __name__ == '__main__':
    p1 = Produce("张三")
    t1 = Custom("李四")
    t2 = Custom("王无")

    p1.start()
    t1.start()
    t2.start()
