from urllib.robotparser import RobotFileParser
from urllib.request import urlopen

def rootFileParser():
    rp = RobotFileParser()
    rp.set_url("http://www.jianshu.com/robots.txt")
    rp.read()
    print(rp.can_fetch("*", "https://www.jianshu.com/p/b67554025d7d"))
    print(rp.can_fetch("*", "http://www.jianshu.com/search?q=python&page=1&type=collections"))


rootFileParser()

rp = RobotFileParser()
rp.parse(urlopen("http://www.jianshu.com/robots.txt").read().decode("utf-8").split("\n"))
print(rp.can_fetch("*","http://www.jianshu.com/p/b67554025d7d"))
print(rp.can_fetch("*","http://www.jianshu.com/search?q=python&page=1&type=collections"))

