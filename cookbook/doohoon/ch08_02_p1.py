some_format = {
    'abc': "{obj.a}, {obj.b}, {obj.c}",
    'bca': "{obj.b}, {obj.c}, {obj.a}",
    'cab': "{obj.c}, {obj.a}, {obj.b}",
}

class fmt_what:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def __format__(self, what):
        try:
            assert type(what) == str
            if what == "":
                what == "abc"

            fmt = some_format[what]
            return fmt.format(obj=self)
            
        except AssertionError:
            return "wrong"

a = fmt_what("this", "is", "format")
b = format(a, "abc")
print(b)

b = format(a, "bca")
print(b)

b = format(a, "cab")
print(b)
# format(a, 1)
