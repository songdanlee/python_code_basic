import requests


#确定url
base_url = "http://www.baidu.com"
#发送请求
response = requests.get(base_url)

# 读取相应内容
# decode 解码
# encode 编码
html = response.content.decode('utf-8')

print(html)

#  将源代码保存到本地
# 打开本地文件，执行w 写操作以encoding指定写入编码格式
file = open('./baidu.html', 'w', encoding='utf-8')
# 写入文件
file.write(html)
# 关闭文件
file.close()