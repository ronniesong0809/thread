import threading
import time

list = [0,0,0,0,0,0,0,0,0,0,0,0]

class myThread(threading.Thread):
    def __init__(self,threadID,name,counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter

    def run(self):
        threadLock = threading.Lock()

        print ("Starting " + self.name)
        threadLock.acquire()
        print_time(self.name, self.counter, list.__len__())
        threadLock.release()

    def __del__(self):
        print ("Exiting " + self.name)

def print_time(threadName,delay,counter):
    while counter:
        time.sleep(delay)
        list[counter-1] += 1
        print (threadName +': ' + "list[" + str(counter) + "] is change to " + str(list[counter-1]) + ": " + time.ctime())
        print("\t  " + str(list))
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

if __name__ == "__main__":
    main()