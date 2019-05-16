#模拟抢票练习，多个进程共享一个文件，这里用文件模拟数据库，db.txt内容{'count':1}表示只有一张票

import time,json
from multiprocessing import Process,Lock

with open('db.txt','w') as fp:
    data = {'count':1}
    da = json.dump(data,fp)



def search(name):
    dic = json.load(open('db.txt'))
    time.sleep(1)
    print('%s查到剩余票数%s' %(name,dic['count']))

def get(name):
    dic = json.load(open('db.txt'))
    time.sleep(1)
    if dic['count']>0:
        dic['count'] -=1
        time.sleep(1)
        json.dump(dic,open('db.txt','w'))
        print('%s购票成功' % name)
#互斥锁（join只能一个所有的进程都一个一个的执行，互斥锁将一个任务整体穿行）
def task(name,lock):
    search(name)
    with lock:
        get(name)



if __name__ == '__main__':
    lock = Lock()
    for i in range(10):
        name = '%s' % i
        p = Process(target=task,args=(name,lock,))
        p.start()