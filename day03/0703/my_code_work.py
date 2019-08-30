# for i in range(1, 11):
#
#     for j in range(10, i - 1, -1):
#         print(" . ", end="")
#     print(" * " * i, end="")
#     print()
#
#
# iyear = int(input("请输入年：\n"))
# imonth = int(input("请输入月：\n"))
# iday = int(input("请输入日：\n"))
# lis = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#
#
# def checkYear(iyear):
#     return ((iyear % 4 == 0 and iyear % 100 != 0) or iyear % 400 == 0)
#
#
# tol_day = 0
#
# for i in range(1, imonth):
#     # tol_day+=lis[i]
#     if i in [1, 3, 5, 7, 8, 10, 12]:
#         tol_day += 31
#     elif i == 2:
#         tol_day += 28
#         if checkYear(iyear):
#             tol_day += 1
#     else:
#         tol_day += 30
# tol_day += iday
# print(tol_day)

#
# for i in range(9, 0, -1):
#     for k in range(0, 9 - i):
#         print("    ", end="\t")
#     for j in range(1, i + 1):
#         print("{}*{}={:02d}".format(i, j, i * j), end="\t")
#     print()
#
#
#
# for i in range(1, 11):
#     for j in range(1, 11):
#         print(" * ", end="")
#
#     print()
#
#
# print("---------------------------")
# for i in range(1, 11):
#     for j in range(1, 11):
#         if i == 1 or i == 10:
#             print(" *  *  *  *  *  *  *  *  *  * ", end="")
#             break
#         elif  j == 1 or j == 10 :
#             print(" * ", end="")
#         else:
#             print(" . ", end="")
#     print()
#
# print("---------------------")
#
# for i in range(1, 11):
#     for j in range(1, 11):
#         if i == 1 or i == 10:
#             print(" *  *  *  *  *  *  *  *  *  * ", end="")
#             break
#         elif i == j or j == 1 or j == 10 or (i + j == 11):
#             print(" * ", end="")
#         else:
#             print("   ", end="")
#     print()
#
#
# print("---------------------")
#
# for i in range(1, 11):
#     for j in range(1, 11):
#         if i == 1 or i == 10:
#             print(" *  *  *  *  *  *  *  *  *  * ", end="")
#             break
#         elif i == j or j == 1 or j == 10 or (i + j == 11):
#             print(" * ", end="")
#         elif i <= j and j + i >= 11:
#             print(" $ ", end="")
#         else:
#             print("   ", end="")
#     print()

from collections import deque


def search(lines, pattern, history=5):
    previous_lines = deque(maxlen=history)
    for line in lines:
        if pattern in line:
            yield line, previous_lines
        previous_lines.append(line)

# Example use on a file
if __name__ == '__main__':
    with open(r'./sonfile.txt') as f:
        for line, prevlines in search(f, 'python', 5):
            print(line.strip())
            print("&"*20)
            for pline in prevlines:
                print(pline, end='')

            print('-' * 20)