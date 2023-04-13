import threading
import time


# 多线程
def sing(msg):
    while True:
        # print("我在唱歌...")
        print(msg)
        time.sleep(1)


def dance(msg):
    while True:
        # print("我在跳舞...")
        print(msg)
        time.sleep(1)


if __name__ == '__main__':
    # sing()
    # dance()
    # 多线程
    # 唱歌线程
    sing_thread = threading.Thread(target=sing, args=("我要唱歌～～",))
    # 跳舞线程
    dance_thread = threading.Thread(target=dance, kwargs={"msg": "我在跳舞!!"})

    # start
    sing_thread.start()
    dance_thread.start()
