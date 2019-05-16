import threading
import time

#方式一
# def print_time():
#     print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime()))
#
# t1 = threading.Thread(args=print_time())
# t2 = threading.Thread(args=print_time())
# t3 = threading.Thread(args=print_time())
# t4 = threading.Thread(args=print_time())
#
# t1.start()
# t2.start()
# t3.start()
# t4.start()
#
# for i in [t1,t2,t3,t4]:
#     i.start()

#方式二

class Therd_time(threading.Thread):
    def __init__(self,count):
        super().__init__()
        self.count = count

    def run(self):
        for i in range(50):
            time.sleep(5)
            print(self.count,time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))


t1 = Therd_time(1)
t2 = Therd_time(2)
t3 = Therd_time(3)
t4 = Therd_time(4)


for i in [t1,t2,t3,t4]:
    i.start()
    i.join()

