html = """
<div  class ="panel">
<div  class="panel-heading">
<h4>Hello</h4>
</div>
<div  class ="panel-body">
<ul  class ="list" id="list-1">
<li  class ="element">Foo</li>
<li  class ="element">Bar</li>
<li  class="element">Jay</li>
</ul>
<ul  class="list  list-small"  id ="list-2">
<li  class ="element">Foo</li>
<li  class ="element">Bar</li>
</ul>
</div>
</div>
"""

from bs4 import BeautifulSoup
# soup = BeautifulSoup(html,"lxml")
# print(soup.select(".panel .panel-heading"))
# print(soup.select("ul li"))
# print(soup.select("#list-2 li"))


soup = BeautifulSoup(html,"lxml")
# for ul in soup.select("ul"):
#     print(ul.select("li"))
#     for li in ul.select("li"):
#         print(li)

# for ul in soup.select("ul"):
#     print(ul["id"],ul["class"])
#     print(ul.attrs["id"],ul.attrs["class"])


for ul in soup.select("ul"):
    for li in ul.select("li"):
        print(li.string,li.get_text())