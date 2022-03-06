from ecc import Point


def main():
    prime = 223
    problems = [
        [(170, 142), (60, 139)], [(47, 71), (17, 56)], [(143, 98), (76, 66)]
    ]
    for p1, p2 in problems:
        p1 = Point(*p1, 0, 7, prime)
        p2 = Point(*p2, 0, 7, prime)
        print(f"{p1} + {p2} = {p1 + p2}")


if __name__ == '__main__':
    main()
