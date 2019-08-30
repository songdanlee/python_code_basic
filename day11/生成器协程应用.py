import time
def save():
    while True:
        print("保存")
        yield 1

def prin():
    while True:
        print("打印")
        yield 0


g=save()
g1=prin()
while True:
    g.send(None)
    time.sleep(1)
    g1.send(None)