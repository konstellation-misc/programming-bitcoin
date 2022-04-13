

class SEC:
    def __init__(self, SEC256Point):
        self.x = SEC256Point.x
        self.y = SEC256Point.y
    def serialize(self):
        b'\x04' + self.x.num.to_bytes(32, 'big') \
                + self.y.num.to_bytes(32, 'big')
    def deserialize(self, stream):
        if stream[0] != b'\x04':
            return
        self.x = int.from_bytes(stream[1:33], 'big')
        self.y = int.from_bytes(stream[33:65], 'big')
