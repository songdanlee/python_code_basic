import os

Name = input('Name of the Receiver: ')
Name = '穆梓'
clientDict = {'lz':'513278236',
              '穆梓':'318750798'
              } # 人名 和对应的 qq号

os.system('start tencent://message/?uin=' + clientDict[Name])