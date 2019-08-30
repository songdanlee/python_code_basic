from pyquery import PyQuery as pq
# doc  = pq(filename="./baidu.html").text()
# print(doc("title"))

# doc = pq(url="https://cuiqingcai.com")
# print(doc("li"))
# print(doc(".xoxo li a").text())
# item = doc(".li")
# item = doc.find(".sub-menu")
# lis = doc.find("li")
# lis = item.children(".menu-item")
# print(lis)
# container = item.parent()
# container = item.parents("html")
# li = doc(".sub-menu")
# print(type(li))
# print(li)
# print(li.siblings())
#
# lis = doc(".sub-menu").items()
# print(type(lis))
# for li in lis:
#     print(li,type(li))
#
# doc = pq(url="https://cuiqingcai.com")
#
# items = doc(".sub-menu a").items()
#
# for it in items:
#     it.addClass("aaa")
#     it.attr("name","jeck")
#     print(it.text(),it,it.html(),it.attr("href"))
#     print("--------------------------------------")
#     it.removeClass("aaa")
#     print(it.text(),it,it.html(),it.attr("href"))
# html = """
# <div class="wrap">
# Hello World
# <p>This is a paragraph.</p>
# </div>
# """
# doc = pq(html)
# wrap = doc(".wrap")
# # wrap.find("p").remove()
# wrap.remove("p")
# print(wrap.text())

html = """
<div class="wrap">
<div id="container">
    <ul class="list">   
    <li  class="item-0">first item</li>
    <li  class="item-1"><a href ="link2.html">second  item</a></li>
    <li  class="item-0 active"><a href ="link3.html"><span  class ="bold"> third  item</span></a></li>
    <li  class="item-1 active"><a href ="link4.html">fourth  item</a></li>
    <li  class="item-0"><a href ="link5.html">fifth  item</a></li>
    </ul>
</div>
</div>
"""
doc = pq(html)
doc("li:nth-child(2n)")
# li = doc("li:first-child")
# print(li)
# li = doc("li:last-child")
# print(li)
# li = doc("li:nth-child(2)")
# print(li)
# li = doc("li:gt(0)") # 大于索引0的，
# print(li)
li = doc("li:nth-child(2n+1)") # 奇数索引
print(li)
li = doc("li:contains(second)")
print(li)
