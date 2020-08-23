import threading
import time

def test01(times):
    for i in range(times):
        print(i)
        print("start test01")
        time.sleep(1)


def test02(times):
    for i in range(times):
        print(i)
        print("start test02")
        time.sleep(1)

def test03(times):
    print("this is test fun:")
    time.sleep(3)


def test04(times):
    print("this is test fun:")
    time.sleep(3)


def main():
    t1 = threading.Thread(target=test01, args=(3, ))
    t2 = threading.Thread(target=test02, args=(3, ))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print("run end")
    # while True:
    #     thread_num = len(threading.enumerate())
    #     print("当前运行的线程个数：%d" %thread_num)
    #     print(threading.main_thread())
    #     if thread_num <= 1:
    #         break
    #     time.sleep(1)

if __name__ == "__main__":
    main()