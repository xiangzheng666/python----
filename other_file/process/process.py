import os
from multiprocessing import Process,Pool

# pid = os.getpid()
# print(pid)

def a(k):
    print('this is a process %d'%k)


p=Pool(2)
for i in range(2):
    p.apply_async(a,args=(i))
p.close()
p.join()