import requests
import itchat
# pycharts 版本要为0.1.9.4，高版本无法导入Pie，pip install pyecharts==0.1.9.4
from pyecharts  import Pie
# # 向图灵机器人发送消息，得到图灵机器人的回复消息
# def get_response(msg):
#     apiUrl =  'http://openapi.tuling123.com/openapi/api'
#     # 接口请求数据
#     data = {
#             "info": str(msg),
#             "key": "7e9377d76fc7ee9499f6dec8eed37bbb",
#             "userId": "123"
#     }
#     try:
#         r = requests.post(apiUrl,data=data).json()
#         return r.get("text")
#     except:
#         return
# #注册方法
# @itchat.msg_register(itchat.content.TEXT)
# def tuling_replay(msg):
#     defaultReplay = "I received:" + msg["Text"]
#
#     replay = get_response(msg["Text"])
#
#     return replay or defaultReplay
#
itchat.auto_login(hotReload=True)
# result = itchat.search_friends()
# print(result)
# itchat.run()

# 获取好友列表
"""
好友的获取方法为get_friends，将会返回完整的好友列表。
其中每个好友为一个字典
列表的第一项为本人的账号信息
传入update键为True将可以更新好友列表并返回
"""
friends = itchat.get_friends(update=True)[0:]
def calc_sex(friends):
    # 初始化计数器，有男有女，性别不填为其他
    male = female = other = 0

    # 遍历列表，列表第一位是袭击，所以从自己之后计算
    # 1 男性   2 女性
    print(type(friends))
    print(type(friends[1]))
    for i in friends[1:]:
        # print(i)
        sex = i["Sex"]
        if sex == 1:
            male += 1
        elif sex == 2:
            female += 1
        else:
            other += 1
    # 总数
    total = len(friends[1:])
    #男性比率
    male_radio = (float(male) / total * 100)
    #女性比率
    female_radio = (float(female) / total * 100)
    # 其他
    other_radio = (float(other) / total * 100)
    # 打印结果
    print(u"男性朋友: %.2f%%" % male_radio)
    print(u"女性朋友: %.2f%%" % female_radio)
    print(u"其他: %.2f%%" % other_radio)
    return male,female,other,total
male,female,other,total = calc_sex(friends)

def draw_pie(male,female,other):
    attr = ['男性', '女性', '其他']
    v1 = [male, female, other]
    pie = Pie('%s的微信好友性别比例' % (friends[0]['NickName']))
    pie.add('', attr, v1, is_label_show=True)
    pie.render(path='snapshot.html')
try:

    draw_pie(male,female,other)
except Exception as e:
    print(e)
finally:
    itchat.logout()