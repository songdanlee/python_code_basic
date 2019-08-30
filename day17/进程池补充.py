import time
from multiprocessing import Pool
from multiprocessing import current_process
import random

def download(name):
    print(f"下载任务{current_process()}---pid：{current_process().pid}")
    for i  in range(1,11):
        print(f"{name}下载进行到{i * 10}%")
        time.sleep(random.random())
    return name

def alert(name):
    print(f"{name}下载完成")

lists = [f"西部世界第{i}集" for i  in range(1,13)]
if __name__ == '__main__':
    print(f"当前主进程:{current_process()}")
    pool = Pool(3)

    for s in lists:
        pool.apply_async(download,args=(s,),callback=alert)

    pool.close()
    pool.join()