a = []

def append_one(x: list, x_id: int) -> None:
    print(f"(1) {id(x) == x_id}")
    x.append(1)
    print(f"(2) {id(x) == x_id}")

append_one(a, id(a))
print(f"(3) {a == []}")


b = 0

def add_one(x: int, x_id: int) -> None:
    print(f"(4) {id(x) == x_id}")
    x = x + 1
    print(f"(5) {id(x) == x_id}")

add_one(b, id(b))
print(f"(6) {b == 0}")
