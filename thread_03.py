import threading


g_num = 0

mutex  = threading.Lock()

def test1(times):
    global g_num
    for i in range(times):
        mutex.acquire()
        g_num += 1
        mutex.release()

def test2(times):
    global g_num
    for i in range(times):
        mutex.acquire()
        g_num += 1
        mutex.release()

def main():
    t1 = threading.Thread(target=test1, args=(1000000, ))
    t2 = threading.Thread(target=test2, args=(1000000, ))
    t1.start()
    t2.start()
    while True:
        thread_num = len(threading.enumerate())
        if thread_num <= 1:
            break
    print(g_num)


if __name__ == "__main__":
    main()