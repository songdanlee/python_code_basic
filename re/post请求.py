import urllib.request
import urllib.parse
posturl = "https://iqianyue.com/mypost/"
postdata = urllib.parse.urlencode({
    "name":"sto@com.cn",
    "pass":"kijsksdm"
}).encode("utf-8")
# post 请求，
req = urllib.request.Request(posturl,postdata)
res = urllib.request.urlopen(req).read().decode("utf-8")
print(res)
