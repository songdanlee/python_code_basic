#
# count = 3
# while count > 0:
#     print("一首凉凉送给你")
#     count -= 1

'''
需求：计算1-10之间数值的累加和
1+2+3+4..+10
'''
#
# count = 1
# sum = 0
# while count <= 10 :
#     sum += count
#     count += 1
# print(sum)

'''
需求：计算1-10之间所有偶数的和
2+4+6+8+10
'''
#
# count = 0
# sum = 0
# while count <= 10:
#     sum += count
#     count += 2
# print(sum)


# 跳出当次循环 continue
# count = 1
# while count < 10:
#     count += 1
#     if count == 4:
#         continue
#     print(count)


# break 跳出循环
count = 1
while count < 10:
    count += 1
    if count == 4:
       break
    print(count)
