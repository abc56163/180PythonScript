import time
times = []
b = time.strftime('%H:%M:%S',time.localtime())
for i in b.split(':'):
    times.append(i)

print(times)
h,m,s =times
M=int(h)*60+int(m)+int(s)/60
print(int(M))