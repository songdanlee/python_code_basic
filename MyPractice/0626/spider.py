import requests


param = input("请输入要搜索的内容")
base_url = "http://www.baidu.com/s?wd="+param

response = requests.get(base_url)
html = response.content.decode("utf-8")

print(html)
