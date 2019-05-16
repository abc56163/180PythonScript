a = '电话突然'
txts = []
fp = open('2.txt', 'r')
txt = fp.readlines()
print(txt)
for i in txt:
    if a in i:
        pass
    else:
        txts.append(i)
print(txts)
fp.close()

with open('2.txt', 'w+') as fp:
    for i in txts:
        fp.write(i)



