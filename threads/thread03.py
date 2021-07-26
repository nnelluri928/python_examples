#!/usr/bin/env python3
import threading
from time import sleep
def do_this():
    global x
    print("This is do_this thread!") 
    while x < 300:
        x +=1
    print(x)
def do_after():
    global x
    print("This is do_after thread!")
    x = 450
    while x < 600:
        x +=1
    print(x)

def main():
    global x
    x = 0
    our_thread = threading.Thread(target=do_this)
    our_thread.start()
    our_thread.join() #will make sure do_this thread finished before do_after thread starts
    our_next_thread = threading.Thread(target=do_after)
    our_next_thread.start() 
    print("main function finished")
    print(our_thread.ident)
    print(our_next_thread.ident)

if __name__ == "__main__":
    main()