import random
import time
import datetime


def data_source():
    while True:
        yield random.randint(0, 100)
        time.sleep(0.1)


def top_k(k, time):
    lst = []
    ds = data_source()
    start_time = datetime.datetime.now()
    while True:
        lst.append(next(ds))
        stop_time = datetime.datetime.now()
        if (stop_time - start_time).total_seconds() >= (time - 0.1):
            break
    return lst


print(top_k(1, 1))
