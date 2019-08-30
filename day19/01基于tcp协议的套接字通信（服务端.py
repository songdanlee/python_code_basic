
import socket
#创建socket对象
tcpsocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#给服务器端 绑定一个端口号
address = ("127.0.0.1",9999)
tcpsocket.bind(address)
#当服务器满载时，设置客户端最大的等待连接数为 5
tcpsocket.listen(5)
print('开启监听')
#等待着客户端 来跟服务器端建立连接 ：在此阻塞
newsocket,clientAddr = tcpsocket.accept()
print('有客户端接入')
print(clientAddr)
# 通过客户端的套接字进行接收

content = newsocket.recv(4096)
print("服务器端收到信息为：",content.decode('utf-8'))

# 关闭服务对象
newsocket.close()
tcpsocket.close()
