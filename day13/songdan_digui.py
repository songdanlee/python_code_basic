def digui(n):
    print(n)
    if n == 1:
        return
    digui(n - 1)


# digui(5)

def digui2(n, cur=1):
    print(cur)
    if cur == n:
        return
    digui2(n, cur + 1)


digui2(5)
