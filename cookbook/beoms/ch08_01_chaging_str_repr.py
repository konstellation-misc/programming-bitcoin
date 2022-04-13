class Pair:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'Pair({self.x!r}, {self.y!r})'

    def __str__(self):
        return f'Pair({self.x!r}, {self.y!r})'

    # def __eq__(self, other):
    #     return self.x == other.x and self.y == other.y

# Problem 1
# print("(1)", eval(repr(Pair(1, 2))) == Pair(1,2))


f = open('ch08_01_chaging_str_repr.py')
# Problem2
# print("(2)", eval(repr(f)) == f)