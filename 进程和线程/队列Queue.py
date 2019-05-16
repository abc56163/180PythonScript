from multiprocessing import Process,Queue,JoinableQueue
import time,random,os

#生产者消费模型实现

def consumer(q,name):
    while True:
        res=q.get()
        time.sleep(random.randint(1,3))
        print('\033[43m%s 吃 %s\033[0m' %(name,res))
        q.task_done()

def producer(q,name,food):
    for i in range(3):
        time.sleep(random.randint(1,3))
        res='%s%s' %(food,i)
        q.put(res)
        print('\033[45m%s 生产了 %s\033[0m' %(name,res))
    q.join()

if __name__ == '__main__':
    q=JoinableQueue()
    #生产包子的厨师门
    p1=Process(target=producer,args=(q,'egon','包子'))
    #吃包子的人
    c1=Process(target=consumer,args=(q,'alex'))
    c1.daemon=True

    p1.start()
    c1.start()
    p1.join()
    print('主')