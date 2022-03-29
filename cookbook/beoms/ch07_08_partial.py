from functools import partial

def spam(a, b, c):
    print(f"{a=} {b=} {c=}")


p1 = partial(spam, 1)

# p1(5,5)

# Question: Make parital on your own!


# Application 1

def distance(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    # hypotenuse
    return math.hypot(x2 - x1, y2 - y1)

def application1():
    points = [ (1, 2), (3, 4), (5, 6), (7, 8) ]
    import math

    pt = (4, 3)
    # Question: points.sort(key=??) w.r.t. pt


# Application 2
import random

def output_result(result, log=None):
    if log is not None and random.random() < 0.3:
        log.debug(f"Got {result}")

def add(x, y):
    print(f"compute {x} + {y}. assume it takes 3 seconds")
    import time
    time.sleep(3)
    return x + y

def application2():
    import logging
    from multiprocessing import Pool
    from functools import partial

    logging.basicConfig(level=logging.DEBUG)
    log = logging.getLogger('test')

    # Question. What if we don't use a pool?

    p = Pool(processes=10)
    for _ in range(10):
        p.apply_async(add, (3,4), callback=output_result)  # How should we change this?
    p.close()
    p.join()


# Application 3  skip


# Application 4 (mine) bound method
