from threading import Thread
import time
def sayhi(name):
    print('%s say hello' % name)
    time.sleep(2)
    print('%s say bay' %name)

if __name__ == '__main__':
    t=Thread(target=sayhi,args=('egon',))
    t.setDaemon(True) #由于设置了守护进程，主进程结束后，子进程将不会继续运行
    t.start()

    print('主线程')
    print(t.is_alive())