import datetime
import time

def run_fn():
    print("start", datetime.datetime.now())
    x = 0
    for i in range(200000000):
        x += 1
    print("stop", datetime.datetime.now())


if __name__ == '__main__':
    run_fn()