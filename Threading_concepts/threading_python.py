import threading
import time

def count1():
    for i in range(1, 10):
        time.sleep(2)
        print(i)

def count2():
    for i in range(1, 10, 3):
        print(i)

t1 = threading.Thread(target=count1, daemon=True)
t2 = threading.Thread(target=count2, daemon=True)

t1.start()
t2.start()

