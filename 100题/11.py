#古典问题：有一对兔子，从出生后第3个月起每个月都生一对兔子，
# 小兔子长到第三个月后每个月又生一对兔子，
# 假如兔子都不死，问每个月的兔子总数为多少？
#1 1 2 3 5 8 13

def fs(m):
    if m <=2:
        return 1
    else:
        return fs(m-1)+fs(m-2)

for i in range(1,8):
    print(fs(i))

