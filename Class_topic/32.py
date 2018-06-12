# synchronoss threading : to arrange  the order of thread in  output format

import threading
import time

def workerone(name,delay):

    threading.current_thread().setName(name)
    print("started-" +threading.current_thread().getName())
    n = 0
    lock.acquire()
    while n < 5:
        time.sleep(delay)
        print(threading.current_thread().getName()+ '-'+str(n))
        n += 1

    if threading.current_thread().getName() == 'Thread-1':
        if threading.current_thread().is_alive():
            print("still alive")
    print("ended-" + threading.current_thread().getName())
    lock.release()

lock = threading.Lock()

t1 = threading.Thread(target=workerone,args=('Thread-1',2))
t2 = threading.Thread(target=workerone,args=('Thread-2',2))

t1.start()
t2.start()
t1.join() # wait the  thread to terminate
t2.join()
print("still executing bcz m in async process")