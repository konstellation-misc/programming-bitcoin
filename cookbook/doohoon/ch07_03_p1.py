def add_int(x: int, y: int) -> int:
    try:
        assert type(x) == int
        assert type(y) == int
    except AssertionError:
        return 0
    return x + y

print(add_int(1, 0.1))
print(add_int(2, 2))
