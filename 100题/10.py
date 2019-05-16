#暂停一秒输出，并格式化当前时间。
import time
print(time.localtime())
print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime()))
time.sleep(2)
print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime()))

