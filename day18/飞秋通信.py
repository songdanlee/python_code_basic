"""
#飞秋发送消息，遵守飞秋自己的协议
#1：默认版本
#123456发送时间，可以任意写
#张无忌:能说的小牛 名称跟简称
#32:发送消息

"""
import socket
import time
# 创建套接字
udpSocket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
# 发送消息
for i in range(5):
    udpSocket.sendto("1:123456:张靓颖:仙女一枝花:32:在吗，我的小可爱？".encode('gbk'), ('10.10.116.151', 2425))
    time.sleep(1)
content = udpSocket.recvfrom(1024)
print(content[0].decode("utf-8"),content[1])
# 关闭套接字
udpSocket.close()