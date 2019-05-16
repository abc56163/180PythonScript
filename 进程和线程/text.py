from multiprocessing import Process,Lock
import os,time

def work():
    look = Lock()
    look.acquire()
    print('%s is running' %os.getpid())
    time.sleep(2)
    print('%s is done' %os.getpid())
    look.release()

if __name__ == '__main__':
    for i in range(3):
        p=Process(target=work)
        p.start()
