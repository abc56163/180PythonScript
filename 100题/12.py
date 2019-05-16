#判断101-200之间有多少个素数，并输出所有素数。
from math import sqrt
l = 0
for i in range(101,200):
    for j in range(2,int(sqrt(i)+1)):
        if i%j != 0:
            l = 1

    if l == 1:
        print(i)


