#join()

import threading
import time

def workerone(name,delay):

    threading.current_thread().setName(name)
    print("started-" +threading.current_thread().getName())
    n = 0
    while n < 5:
        time.sleep(delay)
        print(threading.current_thread().getName()+ '-'+str(n))
        n += 1
    print("ended-" + threading.current_thread().getName())

t1 = threading.Thread(target=workerone,args=('Thread-1',2))
t2 = threading.Thread(target=workerone,args=('Thread-2',2))

t1.start()
t2.start()
t1.join() # wait the  thread to terminate
t2.join()
print("still executing bcz m in async process")