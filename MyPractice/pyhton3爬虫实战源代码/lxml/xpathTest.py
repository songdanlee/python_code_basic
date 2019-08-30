from lxml import etree
from  bs4 import BeautifulSoup

text = """
<div>
<ul>
<li class ='item-0'><a href ='link1.html'><span>first  item</span></a></li>
<li class ='item-1'><a href ='link2.html'>second  item</a></li>
<li class ='item-inactive'><a href ='link3.html'>third  item</a></li>
<li class ='item-1'><a href ='link4.html'>fourth  item</a></li>
<li class ='item-0'><a href ='link5.html'>five  item</a></li>
</ul>
</div>
"""
# html =  etree.HTML(text)
# result  = html.xpath('//li[1]/ancestor::*')
# print(result)
# result  = html.xpath('//li[1]/ancestor::div')
# print(result)
# result  = html.xpath ('//li[1]/attribute::*')
# print(result)
# result=  html.xpath('//li[1]/child::a[@href ="linkl.html"]')
# print(result)
# result  = html.xpath ('//li[1]/descendant::span')
# print(result)
# result  = html.xpath('//li[1]/following::*')
# print(result)
# result  = html.xpath('//li[1]/following-sibling::*')
# print(result)

soup = BeautifulSoup(text,'lxml')
print(soup.prettify())
print(soup.li.string)