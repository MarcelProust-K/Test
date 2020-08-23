import threading
import time

def test01(times):
    for i in range(times):
        print(i)
        print("start test01")
        time.sleep(2)


def test02(times):
    for i in range(times):
        print(i)
        print("start test02")
        time.sleep(1)


class MyThread(threading.Thread):

    def __init__(self, times, fun):
        super(MyThread, self).__init__()
        self.times = times
        self.fun = fun

    def run(self):
        self.fun(self.times)


def main():
    times = 3
    t1 = MyThread(times, test01)
    t2 = MyThread(times, test02)
    t1.start()
    t2.start()

if __name__ == "__main__":
    main()