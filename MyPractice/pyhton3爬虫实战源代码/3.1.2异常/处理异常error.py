from urllib import request, error

try:
    # https://cuiqingcai.com  成功
    response = request.urlopen("https://cuiqingcai.com//index.html")
except error.HTTPError as e:
    print(e.reason, e.code, e.headers, sep="\n")
except error.URLError as e:
    print(e.reason)
else:
    print("Request Successfully")