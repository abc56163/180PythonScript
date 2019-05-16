#输入三个整数x,y,z，请把这三个数由小到大输出。

list = []

for i in  range(3):
    num = int(input('please input three int:'))
    list.append(num)
print(sorted(list))



