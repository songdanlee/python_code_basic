n = 100
sum = 0
while n:
    sum += n
    n -= 1
print(sum)

n = 10
sum = 1
while n:
    sum *= n
    n -= 2
    if sum > 100:
        break
print(sum, n)
for i in range(1, 10, 2):
    print(i)
