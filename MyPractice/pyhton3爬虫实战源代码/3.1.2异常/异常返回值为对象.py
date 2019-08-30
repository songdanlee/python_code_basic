import socket
import urllib.request
import urllib.error

try:
    response = urllib.request.urlopen("http://www.baidu.com",timeout=0.01)
except urllib.error.URLError as e:
    print(type(e))
    if isinstance(e.reason,socket.timeout):
        print("Time Out")
else:
    print("request successful")