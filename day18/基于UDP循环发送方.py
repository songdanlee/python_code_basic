"""
传输层传输协议：
    UDP

    TCP

套接字通信(socket)

UDP
1.发送方
    1.创建套接字(指定的用的传输协议)
    2.发送给谁
    3.关闭套接字


2.接收方

"""
import socket

# 创建套接字
# #socket.AF_INET :表示ipV4  socket.SOCK_DGRAM:表示使用UDP协议
socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
address = ("127.0.0.1",9999)

while True:
    data = input("输入要发送的信息：").encode("utf-8")
    # 发送
    socket.sendto(data,address)

    v = socket.recvfrom(4096)
    print(f"接收到{v[1][0]}回复的数据：{v[0].decode('utf-8')}")

socket.close()