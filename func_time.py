from time import time
import random
from functools import wraps
max_data_len = 20000


def timing(func):
    def _wrapper(*arg, **kw):
        time_start = time()
        res = func(*arg, **kw)
        time_end = time()
        return (time_start, time_end,time_end - time_start), res, func.__name__
    return wrapper

def measure(func):
    @wraps(func)
    def _time_it(*args, **kwargs):
        start = int(round(time() * 1000))
        try:
            return func(*args, **kwargs)
        finally:
            end_ = int(round(time() * 1000)) - start
            print(f"Total execution time: {end_ if end_ > 0 else 0} ms")
    return _time_it
    
data = [random.randint(0,10) for each in range(0,max_data_len)]

@measure
def sorting_original(data):
    sorted_data = []
    while data:
       sorted_data.append(data.pop(random.randint(0,len(data) - 1)))
    return sorted_data

@measure
def sorting_fisher(data):
    for index in range(0,len(data),-1):
        index_change = random.randint(0,len(data) - 1)
        data[index_change], data[index] = data[index], data[index_change]
    return data
    
#print(sorting_fisher(data))
print(sorting_original(data)[0:3:2])