import time
import random
from multiprocessing import Process
#方式一
def piao(name):
    print('%s piaoing' % name)
    time.sleep(random.randrange(1,5))
    print('%s piao end' % name)


if __name__ == '__main__':
    p1=Process(target=piao,args=('alan',))
    p2=Process(target=piao,args=('hulk',))
    p3=Process(target=piao,args=('max',))
    p4=Process(target=piao,args=('hali',))
    p_list=[p1,p2,p3,p4]
    for p in p_list:
        p.start()
    print('主')

# 方法二
class Piao(Process):
    def __init__(self,name):
        super().__init__()
        self.name = name

    def run(name):
        print('%s piaoing' % name)
        time.sleep(random.randrange(1,5))
        print('%s piao end' % name)



if __name__ == '__main__':
    p1=Piao('alan')
    p2=Piao('hulk')
    p3=Piao('max')
    p4=Piao('hali')
    p_list = [p1, p2, p3, p4]
    for p in p_list:
        p.start()
    print('主')