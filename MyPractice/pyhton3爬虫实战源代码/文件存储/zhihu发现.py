import requests
import time as t
from pyquery import PyQuery as pq


requests.packages.urllib3.disable_warnings()
requests.adapters.DEFAULT_RETRIES = 5
s = requests.session()
s.keep_alive = False

url = "https://www.zhihu.com/explore"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36"
}


def open_html(url):
    req = requests.get(url=url, headers=headers,verify=False)
    html = req.text
    req.close()
    doc = pq(html)

    return doc


doc = open_html(url=url)
items = doc.find(".ExploreSpecialCard-contentItem").items()


def find_question(url):
    doc = open_html(html)
    user = doc("a .UserLink-link").text()
    # print(user)
    content = doc("div .RichContent-inner span").text()
    # print(content)
    time = doc("div .ContentItem-time").text()
    time = time[-10:]
    # print(time[-10:])
    print("--" * 80)
    t.sleep(2)
    return user, time, content


def write_into_file(question, user, time, content):
    with open("explore.txt", "w", encoding="utf-8") as f:
        f.write("\n".join([question, user, time, content]))
        f.write("\n" + "=" * 50 + "\n")


for it in items:
    resu = it.find(".ExploreSpecialCard-contentTitle")
    html = resu.attr("href")
    requestion = resu.text()
    print(requestion)
    html = r"https://www.zhihu.com" + html
    user, time, content = find_question(html)
    write_into_file(question=requestion, user=user, content=content, time=time)
    t.sleep(3)
