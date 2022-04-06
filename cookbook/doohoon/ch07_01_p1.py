def add(one, *args) :
    sum_i = 0
    [sum_i := sum_i + i for i in args]
    return one + sum_i

print(add(1,2,3,4,5,6))