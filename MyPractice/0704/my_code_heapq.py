import heapq

nums = [1,24,5,6,7,8,20,304,50]
largenum = heapq.nlargest(3,nums)
print(largenum)
smallnum = heapq.nsmallest(4,nums)
print(smallnum)


portfolio = [
    {'name': 'IBM', 'shares': 100, 'price': 91.1},
    {'name': 'AAPL', 'shares': 50, 'price': 543.22},
    {'name': 'FB', 'shares': 200, 'price': 21.09},
    {'name': 'HPQ', 'shares': 35, 'price': 31.75},
    {'name': 'YHOO', 'shares': 45, 'price': 16.35},
    {'name': 'ACME', 'shares': 75, 'price': 115.65}
]

shares = heapq.nsmallest(3,portfolio,key=lambda s:s['shares'])

print(shares)
heap = list(nums)
heapq.heapify(heap)
print(heap)

print(heapq.heappop(heap))
print(heapq.heappop(heap))


# 优先队列
class PriorityQueue:
    def __init__(self):
        self._queue = []
        self._index = 0

    def push(self, item, priority):
        heapq.heappush(self._queue, (priority, self._index, item))
        self._index += 1

    def pop(self):
        return heapq.heappop(self._queue)[-1]

class Item:
    def __init__(self, name):
        self.name = name
    def __repr__(self):
         return 'Item({!r})'.format(self.name)

q = PriorityQueue()
q.push(Item("张三"),1)
q.push(Item("李四"),5)
q.push(Item("王五"),3)
q.push(Item("赵柳"),2)
q.push(Item("金器"),1)
print(q.pop())
print(q.pop())
print(q.pop())
print(q.pop())
print(q.pop())

# 一个键对应多个值
from collections import  defaultdict
d = defaultdict(list)
d['a'].append(1)
d['a'].append(1)
d['a'].append(2)

d['b'].append(2)

for li in d:
    print(li)
    print(d[li])
# set 没有重复
d = defaultdict(set)
d['a'].add(1)
d['a'].add(2)
d['b'].add(4)
d['a'].add(1)
pairs=[("name","张三"),("age",17)]
for k,v in pairs:
    if k not in d:
        d[k]=[]
    d[k].append(v)
print(d)

from collections import OrderedDict

d = OrderedDict()
d['foo'] = 5
d['bar'] = 2
d['spam'] = 3
d['grok'] = 4
d
# Outputs "foo 1", "bar 2", "spam 3", "grok 4"
for key in d:
    print(key, d[key])


prices = {
    'ACME': 45.23,
    'AAPL': 612.78,
    'IBM': 205.55,
    'HPQ': 37.20,
    'FB': 10.75
}
# 在一个字典上执行普通的数学运算，你会发现它们仅仅作用于键，而不是值
min(prices) # Returns 'AAPL'
max(prices) # Returns 'IBM'

min(prices.values()) # Returns 10.75
max(prices.values()) # Returns 612.78

min(prices, key=lambda k: prices[k]) # Returns 'FB'
max(prices, key=lambda k: prices[k]) # Returns 'AAPL'


min_price = min(zip(prices.values(), prices.keys()))
# min_price is (10.75, 'FB')
print("min_price",min_price)
max_price = max(zip(prices.values(), prices.keys()))
# max_price is (612.78, 'AAPL')
print("max_price",max_price)

#值由大到小排序
prices_sorted = sorted(zip(prices.values(), prices.keys()),reverse=True)
# prices_sorted is [(10.75, 'FB'), (37.2, 'HPQ'),
#                   (45.23, 'ACME'), (205.55, 'IBM'),
#                   (612.78, 'AAPL')]
print(prices_sorted)

print("*"*20)
a = {
    'x' : 1,
    'y' : 2,
    'z' : 14
}
b = {
    'w':3,
    'x':11,
    'z':14
}

print(a.keys() & b.keys())
print(a.keys() - b.keys())
print(a.keys() | b.keys())
c = {key:a[key] for key in a.keys() - {'z', 'w'}}
print(c)

print(a.items() & b.items())


def dedupe(items, key=None):
    seen = set()

    for item in items:
        print(item)
        val = item if key is None else key(item)
        if val not in seen:
            yield item
            seen.add(val)


a = [ {'x':1, 'y':2}, {'x':1, 'y':3}, {'x':1, 'y':2}, {'x':2, 'y':4}]
res = list(dedupe(a, key=lambda d: (d['x'],d['y'])))
print(res)

words = [
    'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
    'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the',
    'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into',
    'my', 'eyes', "you're", 'under'
]
word2=[
    'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
    'the', 'eyes', 'the','from','collections','import','counter',
    'from','collections','import','counter',
    'from','collections','import','counter'

]

from collections import Counter

c = Counter(words)
res = c.most_common(3)
print(res)
print(c['eyes'])

c1 = Counter(word2)
print(c1)
print(c1+c)

print(c-c1)
c1.update(c)
print(c1)

rows = [
    {'fname': 'Brian', 'lname': 'Jones', 'uid': 1003},
    {'fname': 'David', 'lname': 'Beazley', 'uid': 1002},
    {'fname': 'John', 'lname': 'Cleese', 'uid': 1001},
    {'fname': 'Big', 'lname': 'Jones', 'uid': 1004}
]

from operator import itemgetter

res = sorted(rows,key = itemgetter('fname'))
res = sorted(rows,key = itemgetter("uid"))
# print(res)
students = {'1002': {'name': '张三', 'age': 12, 'height': 189, 'sex': '男'},
            '1001': {'name': '李四', 'age': 19, 'height': 176, 'sex': '女'},
            '1003': {'name': '王武', 'age': 20, 'height': 176, 'sex': '女'}
            }
students.update({"1004":{"name":"zhansgan"}})
students["1004"]={}
# print(students)

liss = []

for chunk in list(range(10)):
    liss.extend([chunk])
print(liss)