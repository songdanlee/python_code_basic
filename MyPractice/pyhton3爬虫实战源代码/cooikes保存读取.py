from urllib.request import HTTPCookieProcessor,build_opener
from urllib.error import URLError
from http.cookiejar import MozillaCookieJar,LWPCookieJar

filename = 'cookies.txt'
cookie = LWPCookieJar(filename)
handler = HTTPCookieProcessor(cookie)
opener = build_opener(handler)
response = opener.open("http://ww.baidu.com")

cookie.save(ignore_discard=True,ignore_expires=True)

try:
    cookie = LWPCookieJar()
    cookie.load(filename, ignore_expires=True, ignore_discard=True)
    handler = HTTPCookieProcessor(cookie)
    opener = build_opener(handler)
    response = opener.open("http://www.baidu.com",timeout=1)
    print(response.read().decode("utf-8"))
except URLError as e:
    print(e.reason)



