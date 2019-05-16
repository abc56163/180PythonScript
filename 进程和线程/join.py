from multiprocessing import Process
import time
import random

def task(n):
    time.sleep((random.randrange(1,3)))
    print('-------->%s' % n)

if __name__ == '__main__':
    p1 = Process(target=task,args=(1,))
    p2 = Process(target=task,args=(2,))
    p3 = Process(target=task,args=(3,))

    ps = [p1,p2,p3]

    for p in ps:
        p.start()
        print(p.name,p.pid)
        p.join()
    print('-------->4')