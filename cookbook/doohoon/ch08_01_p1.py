class something_do:
    def __init__(self, a, b):
        # for what?
        self.a = a
        self.b = b

    def __repr__(self):
        return f"what? {self.a}, {self.b}"

    def __str__(self):
        return f"{self.a}, {self.b}"

a = something_do(1, 2)
print(a.__str__())
print(type(a.__str__()))
print(a.__repr__())
print(type(a.__repr__()))

a # ignore
print(f"print {a}")

print(f"print {a!r}")