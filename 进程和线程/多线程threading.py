import threading
import time

def one():
    for i in range(2):
        ti = time.strftime('%y%m%d %H:%M:%S')
        print('启动第一组第'+str(i)+'个程序时间:'+ti)
        time.sleep(2)

def two():
    for i in range(2):
        ti = time.strftime('%y%m%d %H:%M:%S')
        print('启动第二组第'+str(i)+'个程序时间:'+ti)
        time.sleep(2)


def three():
    for i in range(2):
        ti = time.strftime('%y%m%d %H:%M:%S')
        print('启动第三组第'+str(i)+'个程序时间:'+ti)
        time.sleep(2)

def thread():
    threads = []
    t1 = threading.Thread(target=one)
    threads.append(t1)
    t2 = threading.Thread(target=two)
    threads.append(t2)
    t3 = threading.Thread(target=three)
    threads.append(t3)
    for t in threads:
        t.setDaemon(True)
        t.start()
    t.join()
    print('主线程')

if __name__ == '__main__':
    # one()
    # two()
    # three()
    thread()