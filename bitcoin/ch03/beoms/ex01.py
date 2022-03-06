from ecc import FieldElement


def check_if_on_curve(x, y, a, b):
    return y ** 2 == x ** 3 + x * a + b


def main():
    prime = 223
    a = FieldElement(0, prime)
    b = FieldElement(7, prime)
    tups = (192,105), (17,56), (200,119), (1,193), (42,99)
    for x, y in tups:
        x = FieldElement(x, prime)
        y = FieldElement(y, prime)
        is_on_curve = check_if_on_curve(x, y, a, b)
        print(f"{x}, {y} on curve {is_on_curve}")


if __name__ == '__main__':
    main()
