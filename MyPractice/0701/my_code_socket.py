import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
hosts = socket.gethostname()

port = 1234
s.bind((hosts, port))
# listen 代表连接的最大次数
s.listen(5)

while True:

    c,addr = s.accept()
    print("Got connection from",addr)
    c.send('Thank you for connecting'.encode())
    c.close()