def apply_async(func, args, *, callback):
    result = func(*args)

    callback(result)


def add(x, y):
    return x + y


# Problem 1 finish defining the class below so that

# >>> r = ResultHandler()
# >>> apply_async(add, (2, 3), callback=r.handler)
# [1] Got: 5
# >>> apply_async(add, ('hello', 'world'), callback=r.handler) [2] Got: helloworld
# >>>

class ResultHandler:
    def __init__(self):
        self.sequence = 0


# Problem 2 closure

def make_handler():
    def handler(result):
        pass
    pass


# Problem 3 use coroutine

def make_handler():
    while True:
        pass
