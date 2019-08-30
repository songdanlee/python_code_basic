import requests
import time



while True:

    tname = input("请输入贴吧名,输入exit退出\n")
    if tname == 'exit':
        print("退出爬虫")
        break
    page =int(input("请输入页码\n"))


    #确定url
    #发送请求

    for i in range(0,page):
        base_url = "https://tieba.baidu.com/f?kw=%s&pn=%d"%(tname,i*50)

        response = requests.get(base_url)
        html = response.content.decode('utf-8')
        file = open('./teiba'+str(i)+'.html','w',encoding='utf-8')
        file.write(html)
        file.close()
        print("爬虫爬取第%s页"%(i+1))
        time.sleep(5)
    else:
        print("爬虫完毕")


