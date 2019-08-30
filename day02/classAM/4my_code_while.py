count = 0
while count < 3:
    print("一首凉凉送给你")
    count += 1

# 1 2 3....10累加和
# count = 0
# sum = 0
# while count <= 10:
#     sum += count
#     count += 1
# print(sum)

# 1 2 3....10 偶数累加和
# count = 10
# sum = 0
# while count > 0:
#     sum += count
#     count -= 2
# print(sum)
#
# sum = 0
# count = 2
# while True:
#     sum += count
#     count += 2
#     if count > 10:
#         break
# print(sum)


# while .... else
# continue 跳出本次循环
# break 结束循环
# start = 10
# while start >= 0:
#     print(start)
#     start -= 1
# else:
#     print("循环结束")
# print("程序结束")
#
# start = 0
# while True:
#     print(start)
#     if start == 4:
#         break
#     start += 1

start = 0
while start < 10:
    start += 1
    if start == 4:
        continue
    print(start)
