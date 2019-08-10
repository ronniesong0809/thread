import threading
import time

class myThread (threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter

    def run(self):
        threadLock = threading.Lock()

        print ("Starting " + self.name)

        threadLock.acquire()
        print_time(self.name, self.counter, 5)
        threadLock.release()

        print ("Exiting " + self.name)

def print_time(threadName, delay, counter):
    while counter:
        time.sleep(delay)
        print (threadName +': ' + time.ctime())
        counter -= 1

def main():
    threads = []

    thread1 = myThread(1, "Thread-1", 1)
    thread2 = myThread(2, "Thread-2", 2)

    thread1.start()
    thread2.start()

    threads.append(thread1)
    threads.append(thread2)

    for t in threads:
        t.join()

    print ("Exiting Main Thread")

if __name__=='__main__':
    main()