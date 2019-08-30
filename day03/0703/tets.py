#定义一个函数，判断是否为闰年
def leapyear(y):
    return (y % 400 == 0 or (y % 4 ==0 and y % 100 ==0))
#定义一个数组，每个月的天数，由于python中的数组是从0开始，而月份是从1开始，所以数组第一个数为0
days = [0,31,28,31,30,31,30,31,31,30,31,30]
#存储月份的天数
res = 0
#由用户输入年月日
year = int(input("请输入年份："))
month = int(input("请输入月份："))
day = int(input("请输入日期："))
#如果是闰年的话，2月份加一天
if leapyear(year):
    days[2] += 1
#遍历一次days，对应月份中的天数,把对应的天数传递给res存储
for i in range(month):
    res += days[i]
#打印出天数！
print(f"这是{year}年的第{res+day}天")



import datetime

def func():
    y = input("请输入年份")
    m = input("请输入月份")
    d = input("请输入日期")
    t1 = datetime.datetime.now()#获取当前时间
    t2 = datetime.datetime(int(y),int(m),int(d))#获取指定时间
    t3 = t2 - t1
    print("离%s-%s-%s还有%d天"%(y,m,d,t3.days))
func()