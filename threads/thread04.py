#!/usr/bin/env python3
import threading
from time import sleep
def do_this():
    global x,lock
    print("This is do_this thread!") 
    lock.acquire()
    try:
        while x < 300:
            x +=1
        print(x)
    finally:
        lock.release()
def do_after():
    global x,lock
    print("This is do_after thread!")
    lock.acquire()
    try:
        x = 450
        while x < 600:
            x +=1
        print(x)
    finally:
        lock.release()

def main():
    global x,lock
    x = 0
    lock = threading.Lock()
    our_thread = threading.Thread(target=do_this)
    our_thread.start()
    #our_thread.join() #will make sure do_this thread finished before do_after thread starts
    our_next_thread = threading.Thread(target=do_after)
    our_next_thread.start() 


if __name__ == "__main__":
    main()