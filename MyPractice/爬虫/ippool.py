# IP地址取自国内髙匿代理IP网站：http://www.xicidaili.com/nn/
# 仅仅爬取首页IP地址就足够一般使用
import urllib

from bs4 import BeautifulSoup
import requests
import json
import random

headers = {'User-Agent': "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36"}
def getHTMLText(url,proxies):
    try:
        r = requests.get(url,proxies=proxies)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
    except:
        return 0
    else:
        return r.text

def get_ip_list(url):
    web_data = requests.get(url,headers)
    print(web_data)
    return 1
    soup = BeautifulSoup(web_data.text, 'html')
    ips = soup.find_all('tr')
    print(ips)
    ip_list = []
    for i in range(1, len(ips)):
        ip_info = ips[i]
        tds = ip_info.find_all('td')
        ip_list.append(tds[1].text + ':' + tds[2].text)
#检测ip可用性，移除不可用ip：（这里其实总会出问题，你移除的ip可能只是暂时不能用，剩下的ip使用一次后可能之后也未必能用）
    for ip in ip_list:
        try:
          proxy_host = "https://" + ip
          proxy_temp = {"https": proxy_host}
          res = urllib.urlopen(url, proxies=proxy_temp).read()
        except Exception as e:
          ip_list.remove(ip)
          continue
    return ip_list
def get_random_ip(ip_list):
    proxy_list = []
    for ip in ip_list:
        proxy_list.append('http://' + ip)
    proxy_ip = random.choice(proxy_list)
    proxies = {'http': proxy_ip}
    return proxies
def getIp():
    url = "https://raw.githubusercontent.com/fate0/proxylist/master/proxy.list"
    data = requests.get(url,headers=headers).text.split("\n")
    for line in data:
        proxy_json = json.loads(line)
        host = proxy_json['host']
        port = proxy_json['port']
        type = proxy_json['type']
        print(host)
        print(type)
        print(port)
        return
if __name__ == '__main__':
    getIp()
    # url = 'https://www.xicidaili.com/nn'
    # ip_list = get_ip_list(url)
    # print(ip_list)
    # proxies = get_random_ip(ip_list)
    # print(proxies)

    # # 访问网址
    # url = 'http://icanhazip.com/'
    # # 这是代理IP
    # proxy = {'https': '222.89.32.172:9999'}
    # # 创建ProxyHandler
    # proxy_support = request.ProxyHandler(proxy)
    # # 创建Opener
    # opener = request.build_opener(proxy_support)
    # # 添加User Angent
    # opener.addheaders = [('User-Agent',
    #                       'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36')]
    # # 安装OPener
    # request.install_opener(opener)
    # # 使用自己安装好的Opener
    # response = request.urlopen(url)
    # # 读取相应信息并解码
    # html = response.read().decode("utf-8")
    # # 打印信息
    # print(html)
