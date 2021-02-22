# Make a class called Counter, and make it a subclass of the Thread class in the Threading module.
# Make the class have two global variables, one called counter set to 0,
# and another called rounds set to 100.000. Now implement the run() method,
# let it include a simple for-loop that iterates through rounds (e.i. 100.000 times)
# and for each time increments the value of the counter by 1. Create 2 instances of the thread and start them,
# then join them and check the result of the counter, it should be 200.000, right?
# Run it a couple of times and consider some different reasons why you get the answer that you get.

import threading
from threading import Thread


class Counter(Thread):
    COUNTER = 0
    ROUNDS = 100000
    lock = threading.Lock()

    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        for self.COUNTER in range(self.ROUNDS):
            with Counter.lock:
            #Counter.lock.acquire()
                Counter.COUNTER += 1
                print(self.name, Counter.COUNTER)
            #Counter.lock.release()


if __name__ == '__main__':
    thr1 = Counter('thr1')
    thr2 = Counter('thr2')
    thr1.start()
    print(thr1)
    thr2.start()
    print(thr2)
    thr1.join()
    thr2.join()


