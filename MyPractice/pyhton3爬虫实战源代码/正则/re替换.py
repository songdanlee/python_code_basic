import re
import requests,time
import json
def reMethod():
    content = "awhdu4312iie2)_((**89"
    # sub 替换
    content = re.sub("\d", "", content)
    print(content)


# reMethod()

def get_one_page(url):
    headers = {
        'User-Agent':"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1"
    }

    response = requests.get(url,headers = headers)
    if response.status_code == 200:
        return response.text
    return None
def parse_one_page(html):
    pattern = re.compile('<dd>.*?board-index.*?>(.*?)</i>.*?data-src="(.*?)".*?>.*?name.*?a.*?>(.*?)</a>.*?star.*?>(.*?)</p>.*?releasetime.*?>(.*?)</p>.*?integer.*?>(.*?)</i>.*?fraction.*?>(.*?)</i>.*?</dd>',re.S)
    items = re.findall(pattern,html)
    for item in items:
        yield {
            "index": item[0],
            "image": item[1],
            "title": item[2],
            "actor": item[3].strip()[3:] if len(item[3]) > 3 else "",
            "time": item[4].strip()[5:] if len(item[4]) > 5 else "",
            "score":item[5].strip()+item[6].strip()
        }
def write_to_file(content):
   with open("result.txt","a",encoding="utf-8") as file:
            print(content)
            file.write(json.dumps(content, ensure_ascii=False) + "\n")

def main(offset):
        url = "https://maoyan.com/board/4?offset="+str(offset)
        html = get_one_page(url)
        g = parse_one_page(html)
        for i in g:
            write_to_file(i)
if __name__ == '__main__':
    for i in range(10):
        main(offset=i*10)
        time.sleep(1)
# print(type(json.dumps({1:2})))
# str = '{"accessToken": "521de21161b23988173e6f7f48f9ee96e28", "User-Agent": "Apache-HttpClient/4.5.2 (Java/1.8.0_131)"}'

# print((json.loads('{"123":"2"}')))