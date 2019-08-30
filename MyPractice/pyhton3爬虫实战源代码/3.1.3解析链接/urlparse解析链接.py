from urllib.parse import urlparse,urlunparse,urlsplit,urlunsplit,urljoin,urlencode
from urllib.parse import parse_qs,parse_qsl,quote,unquote

def test_urlparse():
    global result
    result = urlparse("http://www.baidu.com/index.html;user?id=5#comment")
    print(type(result), result, sep="\n")


def test_urlunparse():
    global data
    # 返回 scheme://netloc/path;params?query#fragment
    data = ["http", "www.baidu.com", "index.html", "user", "a=6", "comment"]
    data = urlunparse(data)
    print(data)


def test_split():
    global result
    # 不再单独解析param部分
    result = urlsplit(data)
    print(result)


def test_urlunsplit():
    global data
    # urlunsplit 将链接各个部分组合成完整url，传入参数为可迭代对象，如元组列表，长度必须为5
    data = ["http", "www.baidu.com", "index.html", "a=6", "comment"]
    print(urlunsplit(data))


# test_urlparse()
# test_urlunparse()
# test_split()
# test_urlunsplit()

def test_urljoin():
    # urljoin(旧链接,新链接) 如果新链接包括schem(协议),nrtloc(域名),path(路径)则使用新连接，否则将旧链接的补充到新连接
    print(urljoin("http://www.baidu.com","FAQ.html"))
    print(urljoin("http://www.baidu.com","https://cuiqingcai.com/FAQ.html"))
    print(urljoin("http://www.baidu.com/about.html","https://cuiqingcai.com/FAQ.html"))
    print(urljoin("http://www.baidu.com/about.html","https://cuiqingcai.com/FAQ.html?question=2"))
    print(urljoin("http://www.baidu.com?wd=abc","https://cuiqingcai.com/index.php"))
    print(urljoin("http://www.baidu.com","?category=2#comment"))
    print(urljoin("www.baidu.com","?category=2#comment"))
    print(urljoin("www.baidu.com#comment","?category=2"))

# test_urljoin()

def test_urlencode():
    params = {
        "name":"germey",
        "age":22
    }
    base_url = "http://www.baidu.com?"
    # 构造get请求
    url = base_url + urlencode(params)
    print(url)
# test_urlencode()
def test_parse_qs():
    # 将请求参数转为字典
    query = "name=getmey&age=22"
    print(parse_qs(query))
# test_parse_qs()
def test_parse_qsl():
    # 将请求参数转为字典,第一个为参数名，第二个是参数值
    query = "name=getmey&age=22"
    print(parse_qsl(query))
# test_parse_qsl()

def test_quote():
    keyword="壁纸"
    url = "http://www.baidu.com/s?wd=" + quote(keyword)
    print(url)
# test_quote()

def test_urlunquote():
    url = "http://www.baidu.com/s?wd=%E5%A3%81%E7%BA%B8"
    print(unquote(url))
test_urlunquote()