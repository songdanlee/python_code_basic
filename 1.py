# https://chrome.google.com/webstore/category/extensions?hl=zh-CN
#
#
# https://pan.baidu.com/s/10s0Z0
#
# def count_code_nums(file):
#     """
#     :param file: 文件路径，.py文件
#     :rtype :int
#     """
#     with open(file,encoding='utf-8') as data:
#         count, flag = 0, 0
#         begin = ('"""', "'''")
#         for line in data:
#             line2 = line.strip()
#             print(line2)
#             if line2.startswith('#'):continue
#             elif line2.startswith(begin):
#
#                 if line2.endswith(begin) and len(line2) > 3:
#                     print(line2,"111")
#                     flag = 0
#                     continue
#                 elif flag == 0:
#                     print(line2, "222")
#                     flag = 1
#                 else:
#                     print(line2, "333")
#                     flag = 0
#                     continue
#             elif flag == 1 and line2.endswith(begin):
#                 print(line2, "4444")
#                 flag = 0
#                 continue
#             if flag == 0 and line2:
#                 print(line2, "5555")
#                 count += 1
#     return count
#
# def detect_rows(begin=0, root='.'):
#     """
#     统计指定文件夹内所有py文件代码量
#     :param begin: 起始，一般使用默认0即可
#     :param root: 需要统计的文件（文件夹）路径
#     :rtype :int
#     """
#     import os, glob
#     for file in glob.glob(os.path.join(root, '*')):
#         if os.path.isdir(file):
#             begin += detect_rows(0, file)
#         elif file.endswith('.py'):
#             begin += count_code_nums(file)
#     return begin
#
# if __name__ == '__main__':
#     print (count_code_nums(r"E:\python workspace\day13\test\songdan_1.py"))
#     # print (detect_rows())


print(sum([i for i in range(2, 102,2)]))
print(sum([  i for i in range(1,100)]))
def leapyear(y):
    return (y % 400 == 0 or (y % 4 ==0 and y % 100 ==0))
#定义一个数组，每个月的天数，由于python中的数组是从0开始，而月份是从1开始，所以数组第一个数为0
f = lambda x,y:x>y


for i in range(1,101):
    count = 1
    print(i,end="\t")
    while count**2 <= i:
        print(count,end="\t")
        count += 1
    print("")
"".lower()
"".upper()
"".startswith("a")
"".endswith("e")
"".isalpha()
"".isdigit()
"".isspace()
"".isnumeric()
"".isalnum()
"".find("a")
"".rfind("a")
"".partition('.')
"".split()
"".strip()
"".count(".")
print(" ".join(["abc","edf","jih"]))
print("a b c ".title())
print("e f g ".capitalize())

