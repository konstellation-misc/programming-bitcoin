"""Writing function that accepts ONLY keyword arguments"""


# Simply place keyword arguments after * argument, or a single unnamed *
def receive_message(maxsize, *, block):
    """Receive message"""
    pass


def detail(*info, verified):
    print(info)
    print(verified)
    pass
    

if __name__ == "__main__":
    res = detail("Michael", "Jordan", verified=True)

