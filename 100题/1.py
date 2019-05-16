# 有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？
num = {}
for x in range(1,5):
    for y in range(1,5):
        for z in range(1,5):
            if x != y and x != z and y !=z:
                a = '%d%d%d' %(x,y,z)
                # 统计个数
                if a in num.keys():
                    num[a] +=1
                else:
                    num[a] = 1

print(num)




