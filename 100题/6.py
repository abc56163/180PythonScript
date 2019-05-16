#斐波那契数列。




def fs(n):
    if n <= 2:
        return 1
    else:
        return fs(n-1)+fs(n-2)


for i in range(11):
    print(fs(i))

